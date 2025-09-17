import hashlib
import re
from urllib.request import urlopen
from tqdm import tqdm
import os
import sys

# -----------------------------
# Config
PASSWORD_LIST_URL = "https://gist.githubusercontent.com/richardkundl/b68afdcf68240dcff50a/raw/9d3599897308553ba3fcd24baef5a4cb8f6f57b6/10k-common-passwords"

SUPPORTED_HASHES = {
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "md5": hashlib.md5
}

# -----------------------------
# Functions

def is_valid_hash(hash_str, hash_type):
    hash_lengths = {"sha1": 40, "sha256": 64, "md5": 32}
    return bool(re.fullmatch(r"[a-fA-F0-9]{%d}" % hash_lengths[hash_type], hash_str))

def fetch_password_list(url):
    try:
        print("[*] Downloading password list from web...")
        content = urlopen(url).read().decode('utf-8')
        return content.strip().splitlines()
    except Exception as e:
        print(f"[!] Failed to fetch password list: {e}")
        return []

def load_local_password_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read().strip().splitlines()
    except Exception as e:
        print(f"[!] Failed to read local password file: {e}")
        return []

def crack_hash(target_hash, password_list, hash_func):
    print("[*] Starting hash cracking...\n")
    for password in tqdm(password_list, desc="Trying", unit="password"):
        attempt_hash = hash_func(password.encode()).hexdigest()
        if attempt_hash == target_hash:
            return password
    return None

def suggest_password_variations():
    print("\n[AI] Generating common password variations to try:")
    suggestions = ['password123', 'admin', 'letmein', 'qwerty', '12345678', 'P@ssw0rd', 'welcome1']
    for suggestion in suggestions:
        print(f"   → {suggestion}")
    print("[AI] You can try cracking again using a custom dictionary with those ideas.")

# -----------------------------
# Main CLI Logic

def main():
    print("=== 🔓 Multi-Hash Password Cracker ===")

    # Hash Input
    hash_type = input("Choose hash type (sha1 / sha256 / md5): ").strip().lower()
    if hash_type not in SUPPORTED_HASHES:
        print("[!] Unsupported hash type.")
        sys.exit(1)

    target_hash = input(f"Enter the {hash_type.upper()} hash to crack: ").strip().lower()
    if not is_valid_hash(target_hash, hash_type):
        print(f"[!] Invalid {hash_type.upper()} hash format.")
        sys.exit(1)

    # Password Source
    use_local = input("Use local password file? (y/n): ").strip().lower() == 'y'
    if use_local:
        filepath = input("Enter local password file path: ").strip()
        if not os.path.isfile(filepath):
            print("[!] File does not exist.")
            sys.exit(1)
        passwords = load_local_password_file(filepath)
    else:
        passwords = fetch_password_list(PASSWORD_LIST_URL)

    if not passwords:
        print("[!] No passwords loaded.")
        sys.exit(1)

    # Crack Hash
    hash_func = SUPPORTED_HASHES[hash_type]
    result = crack_hash(target_hash, passwords, hash_func)

    if result:
        print(f"\n✅ Password found: **{result}**")
    else:
        print("\n❌ Password not found in the list.")
        suggest_password_variations()

if __name__ == "__main__":
    main()
