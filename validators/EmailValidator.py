import re


class EmailValidator:

    def __init__(self, doc):
        self.email = str(doc)

    def is_valid(self) -> bool:
        try:
            if self.validate_email():
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_email(self) -> bool:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex, self.email):
            return True
        else:
            return False

    def format_email(self) -> str:
        return (
            "{}".format(
                self.email
            )
        )

    def __str__(self) -> str:
        return self.format_email()
