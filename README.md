# Ciphers

A project implementing custom encryption algorithms, including ROTP, UnicodeShiftCipher, and other text transformation methods.

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)

---

## 🚀 About the Project

**Ciphers** is a Python-based project that provides a collection of custom encryption and decryption algorithms. It includes implementations of unique ciphers like **ROTP** (Rotation with Password) and **UnicodeShiftCipher**, which allow for dynamic and flexible text transformations.

---

## ✨ Features

- **ROTP Cipher**: A password-based rotation cipher that shifts characters dynamically based on a password.
- **Unicode Cipher**: A cipher that uses Unicode values and a shift to transform text, with support for hexadecimal output.
- **Hex Conversion**: Utilities to convert text to hexadecimal and vice versa.
- **Customizable**: Easily extendable to add new ciphers or modify existing ones.
- **Error Handling**: Robust input validation and error handling for reliable usage.

---

## 🛠️ Installation

To use **Ciphers**, you need to have Python 3.7 or higher installed. Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/daisseur/Ciphers.git
   cd Ciphers
   ```

2. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. You're ready to go! Import the ciphers into your Python scripts and start using them.

4. You can also try the cli/tui:
   ```bash
   python3 -m unicode_ciphers  # start the interactive tui
   python3 -m unicode_ciphers -h  # for the cli
   ```
---

## 🎯 Usage

### ROTP Cipher

```python
from unicode_ciphers.ciphers import ROTP

# Initialize the cipher with a password
rotp = ROTP(password="secret", string="Hello, World!")

# encrypte the string
decrypted = rotp.encrypt()
print(f"encrypted: {decrypted}")

# Decode the string
decoded = rotp.decode(string=decrypted.result)
print(f"Decoded: {decoded}")
```

### Unicode Cipher

```python
from unicode_ciphers.ciphers import UnicodeCipher

# Initialize the cipher with a password and shift
cipher = UnicodeCipher(password="key", string="Hello", shift=5, hexa=True)

# encrypte the string
decrypted = cipher.encrypt()
print(f"encrypted (Hex): {decrypted.result}")

# Decode the string
decoded = cipher.decode(string=decrypted.result)
print(f"Decoded: {decoded}")
```

### Hex Conversion

```python
from unicode_ciphers.ciphers import to_hexa, from_hexa

# Convert text to hexadecimal
hex_string = to_hexa("Hello", separator="-")
print(f"Hex: {hex_string}")

# Convert hexadecimal back to text
original_string = from_hexa(hex_string, separator="-")
print(f"Original: {original_string}")
```

---

## 📚 Examples

### Example 1: Using ROTP Cipher
```python
from unicode_ciphers.ciphers import ROTP

rotp = ROTP(password="myPassword", string="Encrypt this message!")
decrypted = rotp.encrypt()
print(f"encrypted: {decrypted.result}")  # Output: encrypted text
decoded = rotp.decode(string=decrypted.result)
print(f"Decoded: {decoded.result}")  # Output: "Encrypt this message!"
```

### Example 2: Using UnicodeShiftCipher
```python
from unicode_ciphers.ciphers import UnicodeCipher
cipher = UnicodeCipher(password="key", string="Hello", shift=10, hexa=False)
decrypted = cipher.encrypt()
print(f"encrypted: {decrypted.result}")  # Output: Transformed text
decoded = cipher.decode(string=decrypted.result)
print(f"Decoded: {decoded.result}")  # Output: "Hello"
```

> Absolument pas fait avec chatGPT en fait... mensonges !