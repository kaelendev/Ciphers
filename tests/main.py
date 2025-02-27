import unittest
from unicode_ciphers import registry
import random
from unidecode import unidecode

class TestCiphers(unittest.TestCase):
    def test_encode_encrypt_cycle(self):
        test_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'"
        for cipher_info in registry.list_ciphers():
            with self.subTest(cipher_name=cipher_info["name"]):
                cipher_class = cipher_info["class"]
                print(f"Testing cipher: {cipher_info['name']}")
                password = "§/${*[!('pass0256')!]*}$\\§"

                match cipher_info["name"].lower():
                    case "caesar":
                        cipher_instance = cipher_class(shift=random.randint(-26, 26), string=test_string)
                        test_string = unidecode(test_string)  # because Caesar cipher will always convert the string with unidecode
                    case "rotp":
                        cipher_instance = cipher_class(password=password, string=test_string)
                        test_string = unidecode(test_string)  # because ROTP cipher will always convert the string with unidecode
                    case "vigenere":
                        cipher_instance = cipher_class(password=password, string=test_string)
                        test_string = unidecode(test_string)  # because Vigenere cipher will always convert the string with unidecode
                    case "unicode_cipher":
                        cipher_instance = cipher_class(password=password, string=test_string, shift=random.randint(-1114111, 1114111))
                    case _:
                        cipher_instance = cipher_class(string=test_string, password=password)

                try:
                    encrypted = cipher_instance.encipher().string
                    self.assertIsNotNone(encrypted, f"Encrypting failed for {cipher_info['name']}")
                except Exception as e:
                    self.fail(f"Encrypting raised an exception for {cipher_info['name']}: {e}")

                try:
                    decrypted = cipher_instance.decrypt(string=encrypted).string
                    self.assertIsNotNone(decrypted, f"Decrypting failed for {cipher_info['name']}")
                except Exception as e:
                    self.fail(f"Decrypting raised an exception for {cipher_info['name']}: {e}")


                self.assertEqual(decrypted, test_string, f"Decrypted result does not match input for {cipher_info['name']}")


if __name__ == "__main__":
    unittest.main()