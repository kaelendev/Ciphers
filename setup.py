from setuptools import setup, find_packages
setup(
    name='Ciphers',
    version='0.1.0',
    author='daisseur',
    author_email='daisseur@gmail.com',
    packages=['unicode_ciphers'],

    url='https://github.com/daisseur/unicode_ciphers',
    description="A project implementing custom encryption algorithms, including ROTP, UnicodeShiftCipher, and other text transformation methods.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license=open('LICENSE', 'r').read(),
    keywords=['python', 'deltacode', 'cipher', 'encipher', 'encrypt', 'ROTP', 'Caesar', 'UnicodeCipher', 'Vigenere'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)