import questionary as inquirer

import sys

from . import validators

def prompt_continue():
    q = inquirer.confirm("Detected a cancellation, do you still want to continue?",
                         style= inquirer.Style([('question', 'bold fg:#fff bg:#de9c02')]),
                         default=False
    )
    r = q.ask()
    if r is None or not r:
        return False
    return True

def question_wrapper(q):
    r = q.ask()
    if r is None and not prompt_continue():
        sys.exit(1)
    elif r is None:
        return question_wrapper(q)
    else:
        return r

def prompt_input(message: str, validator=validators.NotNull, **kwargs):
    question = inquirer.text(
        message=message,
        validate=validator,
        **kwargs
    )
    return question_wrapper(question)

def prompt_password():
    return prompt_input("Enter password:")

def prompt_shift():
    shift = prompt_input("Enter shift (int):", validators.IntValidator)
    return int(shift or 0)

def prompt_string():
    return prompt_input("Enter string:", multiline=True)

def prompt_list(message: str, choices: [str]):
    select = inquirer.select(
        message=message,
        choices=choices
    )
    return question_wrapper(select)

def prompt_check_list(message: str, choices: [str]):
    select = inquirer.checkbox(
        message=message,
        choices=choices
    )
    return question_wrapper(select)
