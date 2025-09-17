import hashlib
from urllib.request import urlopen
from tqdm import tqdm
import re

# Optional AI-like fallback suggestion (mocked)
def suggest_password(hash_value):
    print("\n[AI] Could not find password in the list.")
    print("[AI] Based on analysis, this may be a very strong or custom password.")
    print("[AI] Try checking passwords you've recently used or try a deeper brute-force tool.")
    # Placeholder for AI suggestions or API integration
    return None

def is_valid_sha1(s):
    return bool(re.fullmatch(r"[a-fA-F0-9]{40}", s))

def fetch_password_list(url):
    print("[*] Fetching password list...")
    try:
        response = urlopen(url)
        return response.read().decode('utf-8').splitlines()
    except Exception as e:
        print(f"[!] Failed to fetch password list: {e}")
        return []

def crack_sha1_hash(target_hash, passwords):
    print("[*] Starting SHA-1 hash cracking...\n")
    for password in tqdm(passwords, desc="Cracking", unit="attempt"):
        hash_attempt = hashlib.sha1(password.encode('utf-8')).hexdigest()
        if hash_attempt == target_hash:
            return password
    return None

def main():
    hash_input = input("[+] Enter SHA-1 hash value: ").strip().lower()

    if not is_valid_sha1(hash_input):
        print("[!] Invalid SHA-1 hash. It must be a 40-character hexadecimal string.")
        return

    password_url = "https://gist.githubusercontent.com/richardkundl/b68afdcf68240dcff50a/raw/9d3599897308553ba3fcd24baef5a4cb8f6f57b6/10k-common-passwords"
    passwords = fetch_password_list(password_url)

    if not passwords:
        print("[!] No passwords to try.")
        return

    found_password = crack_sha1_hash(hash_input, passwords)

    if found_password:
        print(f"\n[+] Password found: {found_password}")
    else:
        print("\n[-] Password not found in the list.")
        suggest_password(hash_input)

if __name__ == "__main__":
    main()
