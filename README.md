# 🔐 BTC Password Vault

![Stars](https://img.shields.io/github/stars/myexistences/btc-password-vault?style=flat-square)
![Forks](https://img.shields.io/github/forks/myexistences/btc-password-vault?style=flat-square)
![Issues](https://img.shields.io/github/issues/myexistences/btc-password-vault?style=flat-square)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=myexistences.btc-password-vault)

> AES-256 encrypted password & seed storage built for Bitcoin holders, privacy-focused users, and crypto devs. 100% offline. Fully secure. No internet required.

---

## 🔒 Features

- AES-256-GCM encryption with PBKDF2 (390,000 iterations)
- Encrypt and decrypt any secret: BTC seed, private keys, notes
- Zero external files, runs completely offline
- Clean CLI interface with professional UX
- Secure password input with `getpass()`
- Cross-platform (Windows, Linux, macOS)

---

## 🧠 How It Works

- You choose a **master password** to encrypt your data
- Output is a secure Base64 string you can store anywhere (USB, text file, even on paper)
- Use the same master password to decrypt it any time

---

## 📦 Installation

```bash
git clone https://github.com/myexistences/btc-password-vault.git
cd btc-password-vault
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python pass.py
```

### 🔐 Encryption Example

```plaintext
1. Encrypt a password or seed
Enter your secret: my super bitcoin seed
Enter encryption password: ********

✅ Encrypted Output:
Afj4JsdN3aK4j... (save this!)
```

### 🔓 Decryption Example

```plaintext
2. Decrypt from saved data
Paste encrypted data: Afj4JsdN3aK4j...
Enter encryption password: ********

✅ Decrypted Result:
my super bitcoin seed
```

---

## 📁 Project Structure

```
btc-password-vault/
├── pass.py               # Main script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 🛡️ Security Note

This script uses `cryptography`’s AES-GCM mode with strong key derivation (`PBKDF2HMAC`) and a unique salt/nonce per encryption. You must **remember your encryption password** — it cannot be recovered if lost.

---

## ✅ Requirements

- Python 3.6+
- `pip install -r requirements.txt`

---

## 📜 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Contributing

Pull requests are welcome! Feel free to open issues or suggest features.

---

## ⭐ Show some love

If this helped secure your crypto vault, star the repo 🌟 and share with others!
