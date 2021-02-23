from random import choice
from string import ascii_letters, digits, punctuation
from typing import Optional


class PasswordGenerator:
    base: str = ascii_letters + digits + punctuation

    def __init__(self, size, randomize_pass_base: Optional[int] = 1):
        self.size = size
        self.randomize_pass_range = randomize_pass_base

    def _password_base(self):
        """
        Password base for generate password.

        Returns
        -------
        pass_base: str
            Password base to generate.
        """
        pass_base = ''
        for _ in range(self.randomize_pass_range):
            for _ in range(self.base.__len__()):
                char = choice(self.base)
                pass_base += char
                self.base.removeprefix(char)
        return pass_base

    def password_generate(self):
        """
        Generate password by size.

        Returns
        -------
        password: str
            Password generated.
        """
        password = ''
        password_base = self._password_base()
        for _ in range(self.size):
            password += choice(password_base)
        return password
