import subprocess
import sys
import os


def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_package_pip(package):
    subprocess.check_call([os.path.join(os.path.dirname(sys.executable), 'pip'), 'install', package])

def check():
    try:
        import questionary as inquirer
    except:
        valid = input("The package 'questionary' isn't installed, would you like to install it ? [y/n] >> ")
        if valid in ['y', 'yes', 'o', 'oui']:
            print('Installing package..')
            try:
                install_package('questionary')
            except:
                install_package_pip('questionary')
        else:
            sys.exit(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Package successfully installed !")