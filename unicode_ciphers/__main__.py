from .ciphers import *
from .menu.prompt import prompt_password, prompt_input, prompt_shift, prompt_list, prompt_check_list

classes = ["Caesar", "ROTP", "UnicodeCipher", "Vigenere"]

def main():
    encrypt_mode = prompt_list("Encrypt or Decrypt ?", ["Encrypt", "Decrypt"])
    cipher_class = prompt_list("What cipher are you using ?", classes)
    string = prompt_input('Enter string:')

    match cipher_class:
        case "Caesar":
            shift = prompt_shift()
            options = [
                {
                    'name': 'digits',
                    'checked': True
                },
                {
                    'name': 'specials'
                }
            ]
            prompt_check_list("Options to rotate", options)
            cipher = Caesar(string=string, shift=shift)
        case "Vigenere":
            password = prompt_password()
            cipher = Vigenere(string=string, password=password)
        case "ROTP":
            password = prompt_password()
            cipher = ROTP(string=string, password=password)
        case "UnicodeCipher":
            password = prompt_password()
            shift = prompt_shift()
            cipher = UnicodeCipher(string=string, password=password, shift=shift)
        case _:
            return 'ERROR'

    if encrypt_mode == 'Encrypt' and cipher:
        return cipher.encrypt()
    else:
        return cipher.decrypt()


if __name__ == '__main__':
    result = main()
    _repr = repr(result)
    _hexa = to_hexa(result)

    print(f"Result (string): {result}")
    print(f"Result (repr): {_repr}")
    print(f"Result (hexa): {_hexa}")


    # printc(f"[bold magenta]Result (string): [/magenta bold][green bold]{result}[/]")
    # printc(f"[bold magenta]Result (repr): [/][i]{_repr}[/]")
    # printc(f"[bold magenta]Result (hexa): [/magenta bold][bold]{_hexa}[/]")
