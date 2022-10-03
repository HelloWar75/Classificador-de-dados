class RenavamValidator:

    def __init__(self, doc):
        self.renavam = str(doc).replace('.', '').replace('-', '').replace('/', '').zfill(11)
        if not self.correct_size():
            raise ValueError("RENAVAM Size Invalid!")

    def is_valid(self) -> bool:
        try:
            if self.correct_size():
                return True
            else:
                return False

            if self.validate_renavam():
                return True
            else:
                return False

        except ValueError:
            return False

    def correct_size(self) -> bool:
        if len(self.renavam) == 11:
            return True
        else:
            return False

    def validate_renavam(self) -> bool:
        renavam = self.renavam
        dv = 0
        num1 = int(renavam[0])
        num2 = int(renavam[1])
        num3 = int(renavam[2])
        num4 = int(renavam[3])
        num5 = int(renavam[4])
        num6 = int(renavam[5])
        num7 = int(renavam[6])
        num8 = int(renavam[7])
        num9 = int(renavam[8])
        num10 = int(renavam[9])
        num11 = int(renavam[10])  # DV

        sum1 = (sum([num1 * 3, num2 * 2, num3 * 9, num4 * 8, num5 * 7, num6 * 6, num7 * 5, num8 * 4, num9 * 3,
                     num10 * 2]) * 10) % 11

        if not (sum1 >= 10):
            dv = sum1

        if dv == num11:
            return True
        else:
            return False

    def format_renavam(self) -> str:
        return (
            "{}".format(
                self.renavam
            )
        )

    def __str__(self) -> str:
        return self.format_renavam()
