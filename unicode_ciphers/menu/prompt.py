from PyInquirer import prompt
from . import validators

def prompt_input(message: str, validator=validators.NotNull):
    res = prompt([{
        'name': 'res',
        'type': 'input',
        'message': message,
        'validate': validator,
        }])
    return res.get('res')

def prompt_password():
    return prompt_input("Enter password:")

def prompt_shift():
    shift = prompt_input("Enter shift (int):", validators.IntValidator)
    return int(shift or 0)

def prompt_string():
    return prompt_input("Enter string:")

def prompt_list(message: str, choices: [str]):
    res = prompt([{
        'name': 'res',
        'type': 'list',
        'message': message,
        'choices': choices
    }])
    return res.get('res')

def prompt_check_list(message: str, choices: [str]):
    res = prompt([{
        'name': 'res',
        'type': 'checkbox',
        'message': message,
        'choices': choices
    }])
    return res.get('res')