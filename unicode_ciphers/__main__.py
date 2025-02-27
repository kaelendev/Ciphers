from argparse import Namespace
import pathlib
from io import TextIOWrapper
from os.path import exists
from .ciphers import *
from .menu.check_install import check
import argparse
from .ciphers.registry import registry

ciphers = [ x['name'] for x in registry.list_ciphers()]
parser = argparse.ArgumentParser(prog='unicode_ciphers', description="Encrypt or decrypt a string using different ciphers.")

def parse_args():
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the given string or file")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the given string or file")
    parser.add_argument('string', nargs='?', default=None, help="String to encrypt/decrypt")
    parser.add_argument("-i", "--input", dest="input_file", type=argparse.FileType('r', encoding='UTF-8'),
                        help="Entry file to read the string to encrypt/decrypt")
    parser.add_argument("-o", "--output", dest="output_file", type=pathlib.Path,
                        help="Output file to write the result")
    parser.add_argument('-p', '--password', help="Password to use for encryption/decryption")
    parser.add_argument('-s', '--shift', type=int, help="Shift to use for encryption/decryption")
    parser.add_argument('-c', '--cipher', help="Cipher to use for encryption/decryption")
    parser.add_argument('--option', action='append', dest="options",
                        help="Option(s) for encryption/decryption")
    parser.add_argument('--hexa', action="store_true", help="The string will be decoded from hexa before being encrypted/decrypted")
    return parser.parse_args()


def handle_args(args: Namespace) -> Namespace:
    args.encrypt_mode = 'Encrypt' if args.encrypt else 'Decrypt' if args.decrypt else None

    if args.string and args.input_file:
        parser.error("You can't provide both 'string' and 'input_file' arguments")
    elif args.input_file:
        args.string = args.input_file.read()

    if args.cipher and args.cipher.lower() not in ciphers:
        parser.error(f"The cipher provided is not valid, please use one of these: {ciphers}")
    else:
        args.cipher = ciphers[ciphers.index(args.cipher.lower())] if args.cipher else None

    if args.hexa:
        separator = None
        half_string_length = int(len(args.string) / 2)
        if args.string.count("0x") < half_string_length:
            if args.string.count(",") >= half_string_length:
                separator = ','
            elif args.string.count(" ") >= half_string_length:
                separator = ' '
        try:
            args.string = from_hexa(args.string, separator)
        except ValueError:
            parser.error("The string provided is not in hexadecimal")

    return args


def handle_write_file(filename: str, result: str):
    open(filename, 'w', encoding='UTF-8').write(result)

def main(args: Namespace):
    check()
    from .menu.prompt import prompt_password, prompt_input, prompt_shift, prompt_list, prompt_check_list

    encrypt_mode: str = args.encrypt_mode or prompt_list("Encrypt or Decrypt ?", ["Encrypt", "Decrypt"])
    cipher_class: str = args.cipher or prompt_list("What cipher are you using ?", [f"{cipher.replace('_', ' ').capitalize()}({cipher})" for cipher in ciphers])
    string: str = args.string or prompt_input('Enter string:')

    if string.count("0x") >= len(string) / 2 and string.count(" ") == 0:
        string = from_hexa(string)

    match cipher_class.replace(" ", "_").split("(")[0].lower():
        case "caesar":
            shift = args.shift if args.shift is not None else prompt_shift()
            q_options = ['digits', 'specials']
            options = args.options or [] if args.shift is not None else prompt_check_list("Options to rotate", q_options)
            cipher = Caesar(string=string, shift=shift, options=options)
        case "vigenere":
            password = args.password or prompt_password()
            cipher = Vigenere(string=string, password=password)
        case "rotp":
            password = args.password or prompt_password()
            cipher = ROTP(string=string, password=password)
        case "unicode_cipher":
            password = args.password or prompt_password()
            shift = args.shift if args.shift is not None else prompt_shift()
            cipher = UnicodeCipher(string=string, password=password, shift=shift)
        case _:
            raise ValueError

    if encrypt_mode == 'Encrypt' and cipher:
        return cipher.encrypt()
    elif cipher:
        return cipher.decrypt()

if __name__ == '__main__':
    args = parse_args()
    args = handle_args(args)

    result: str = main(args).string

    if args.output_file:
        handle_write_file(args.output_file, result)

    _repr = repr(result)
    _hexa = to_hexa(result)

    print(f"Result (string): {result}")
    print(f"Result (repr): {_repr}")
    print(f"Result (hexa): {_hexa}")
