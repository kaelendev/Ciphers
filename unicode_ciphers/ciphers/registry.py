from .base import Cipher

class CipherRegistry:
    def __init__(self):
        self.ciphers = []

    def register(self, name: str, description: str, fullname: str):
        def decorator(cls: Cipher):
            self.ciphers.append({
                "name": name,
                "description": description,
                "fullname": fullname,
                "class": cls
            })
            return cls
        return decorator

    def list_ciphers(self):
        return self.ciphers

registry = CipherRegistry()