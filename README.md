# Ciphers

A project implementing custom encryption algorithms, including ROTP, UnicodeShiftCipher, and other text transformation methods.

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Ciphers](#-ciphers)

---

## 🚀 About the Project

**Ciphers** is a Python-based project that provides a collection of custom encryption and decryption algorithms. It includes implementations of unique ciphers like **ROTP** (Rotation with Password) and **UnicodeShiftCipher**, which allow for dynamic and flexible text transformations.


## ✨ Features

- **ROTP Cipher**: A password-based rotation cipher that shifts characters dynamically based on a password.
- **Unicode Cipher**: A cipher that uses Unicode values and a shift to transform text, with support for hexadecimal output.
- **Hex Conversion**: Utilities to convert text to hexadecimal and vice versa.
- **Customizable**: Easily extendable to add new ciphers or modify existing ones.


## 🛠️ Installation

To use **Ciphers**, you need to have Python 3.7 or higher installed. Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/daisseur/Ciphers.git
   cd Ciphers
   ```
2. Install the package/cli
   - Using `pip`:
     ```bash
     pip install -e .
     ```
   - Using `pipx` to make the cli available everywhere:
     ```bash
     pipx install .
     ```
3. Use the cli
   ```bash
   ciphers -h
   ciphers -d "ŴƗƥƝƝśưƔƗƫƖ"  -p "ciphers" -c unicode_cipher -s 201  # Should output 'Hello there'
   ```

## 🎯 Usage

### There are different ways to encrypt/decrypt using this module
- __Using `to_encipher()` and `to_decipher()`__: 
  ```python
  from unicode_ciphers import to_encipher, to_decipher
  
  encrypted = to_encipher('caesar', "Veni vidi dici", shift=13)
  decrypted = to_decipher('caesar', encrypted, shift=13)
  ```
- __Using a `Cipher` class with direct methods__:
  ```python
  from unicode_ciphers import Caesar
  
  encrypted = Caesar("Veni vidi dici", shift=13).encrypt()
  # or 
  encrypted = Caesar().encrypt("Veni vici dici", shift=13)
  
  decrypted = Caesar(encrypted, shift=13).decrypt()
  # or 
  decrypted = encrypted.decrypt()
  ```
- __By instancing cipher class with password/shift arguments__:
  ```python
  from unicode_ciphers import Caesar
  
  cipher = Caesar(shift=13)

  encrypted = cipher.encrypt("Veni vidi dici")
  decrypted = cipher.decrypt(encrypted)
  ```
  
## 🔐 Ciphers

### ROTP Cipher (Rotation with Password)

```python
from unicode_ciphers.ciphers import ROTP

# Initialize the cipher with a password
rotp = ROTP(password="secret")

# Encrypt the string
encrypted = rotp.encrypt("Hello World !")
print(f"Encrypted: {encrypted}")

# Decrypt the string
decrypted = rotp.decipher(encrypted)
print(f"Decrypted: {decrypted}")
```

### Unicode Cipher

```python
from unicode_ciphers.ciphers import UnicodeCipher

# Initialize the cipher with a password and shift
cipher = UnicodeCipher(password="key", shift=5)

# Encrypt the string
encrypted = cipher.encrypt("Hello World !")
print(f"Encrypted: {encrypted}")

# Decrypt the string
decrypted = cipher.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
```

### Vigenère Cipher

```python
from unicode_ciphers.ciphers import Vigenere

# Initialize the cipher with a password and shift
cipher = Vigenere(password="key")

# Encrypt the string
encrypted = cipher.encrypt("Hello World !")
print(f"Encrypted: {encrypted}")

# Decrypt the string
decrypted = cipher.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
```

### Caesar Cipher

```python
from unicode_ciphers.ciphers import Caesar

# Initialize the cipher with a password and shift
cipher = Caesar(shift=13)

# Encrypt the string
encrypted = cipher.encrypt("Hello World !")
print(f"Encrypted: {encrypted}")

# Decrypt the string
decrypted = cipher.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
```

### Hex Conversion

```python
from unicode_ciphers.ciphers import to_hexa, from_hexa

# Convert text to hexadecimal
hex_string = to_hexa("Hello", separator=" ")
print(f"Hex: {hex_string}")

# Convert hexadecimal back to text
original_string = from_hexa(hex_string, separator=" ")
print(f"Original: {original_string}")
```

---
