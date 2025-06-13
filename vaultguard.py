import os, base64
from getpass import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from colorama import Fore, Style, init

init(autoreset=True)

def header():
    print("\n" + "="*50)
    print(Fore.CYAN + Style.BRIGHT + "         🔐 BTC PASSWORD VAULT 🔐")
    print("="*50 + "\n")

def menu():
    print(Fore.YELLOW + "1." + Style.BRIGHT + " Encrypt a password or seed")
    print(Fore.YELLOW + "2." + Style.BRIGHT + " Decrypt from saved data")
    print(Fore.YELLOW + "0." + Style.BRIGHT + " Exit")

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000
    )
    return kdf.derive(password.encode())

def encrypt_data(plain_text: str, password: str) -> str:
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = derive_key(password, salt)
    aes = AESGCM(key)
    encrypted = aes.encrypt(nonce, plain_text.encode(), None)
    return base64.b64encode(salt + nonce + encrypted).decode()

def decrypt_data(encrypted_text: str, password: str) -> str:
    try:
        decoded = base64.b64decode(encrypted_text)
        salt = decoded[:16]
        nonce = decoded[16:28]
        ct = decoded[28:]
        key = derive_key(password, salt)
        aes = AESGCM(key)
        decrypted = aes.decrypt(nonce, ct, None)
        return decrypted.decode()
    except Exception:
        return Fore.RED + "❌ Decryption failed: Invalid password or corrupted data."

def main():
    while True:
        header()
        menu()
        choice = input(Fore.GREEN + "\n➤ Enter your choice: ")

        if choice == '1':
            print(Fore.MAGENTA + "\n🔐 ENCRYPTION MODE")
            text = input(Fore.BLUE + "Enter your secret (password/seed): ")
            password = getpass(Fore.BLUE + "Set encryption password: ")
            encrypted = encrypt_data(text, password)
            print(Fore.GREEN + "\n✅ Encrypted Output:\n" + Style.RESET_ALL + encrypted)
            print(Fore.YELLOW + "\n⚠️ Save this encrypted string securely.")

        elif choice == '2':
            print(Fore.MAGENTA + "\n🔓 DECRYPTION MODE")
            encrypted = input(Fore.BLUE + "Paste encrypted data: ")
            password = getpass(Fore.BLUE + "Enter your encryption password: ")
            decrypted = decrypt_data(encrypted, password)
            print(Fore.GREEN + "\n✅ Decrypted Result:\n" + Style.RESET_ALL + decrypted)

        elif choice == '0':
            print(Fore.CYAN + "\n👋 Exiting... Stay safe!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

        input(Fore.YELLOW + "\n[Press Enter to continue...]")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
