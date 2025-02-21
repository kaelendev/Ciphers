import subprocess
import sys


def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check():
    try:
        import questionary as inquirer
    except:
        valid = input("The package 'questionary' isn't installed, would you like to install it ? [y/n] >> ")
        if valid in ['y', 'yes', 'o', 'oui']:
            print('Installing package..')
            install_package('questionary')
        else:
            sys.exit(1)