class CnhValidator:

    def __init__(self, doc):
        self.cnh = str(doc).replace('.', '').replace('-', '').replace('/', '')
        if not self.correct_size():
            raise ValueError("CNH Size Invalid!")

    def is_valid(self) -> bool:
        try:
            if self.correct_size() and self.validate_cnh():
                return True
            else:
                return False
        except ValueError:
            return False

    def correct_size(self) -> bool:
        if len(self.cnh) == 11:
            return True
        else:
            return False

    def validate_cnh(self) -> bool:
        cnh = self.cnh
        dv1 = 0
        dv2 = 0
        num1 = int(cnh[0])
        num2 = int(cnh[1])
        num3 = int(cnh[2])
        num4 = int(cnh[3])
        num5 = int(cnh[4])
        num6 = int(cnh[5])
        num7 = int(cnh[6])
        num8 = int(cnh[7])
        num9 = int(cnh[8])
        num10 = int(cnh[9])
        num11 = int(cnh[10])

        sum1 = sum([num1 * 2, num2 * 3, num3 * 4, num4 * 5, num5 * 6, num6 * 7, num7 * 8, num8 * 9, num9 * 10]) % 11
        sum2 = sum([num1 * 3, num2 * 4, num3 * 5, num4 * 6, num5 * 7, num6 * 8, num7 * 9, num8 * 10, num9 * 11, num10 * 2]) % 11

        if (sum1 != 10) and (sum1 != 0):
            dv1 = 11 - sum1

        if (sum2 != 10) and (sum2 != 0):
            dv2 = 11 - sum2

        if (dv1 == num10) and (dv2 == num11):
            return True
        else:
            return False

    def format_cnh(self) -> str:
        return (
            "{}".format(
                self.cnh
            )
        )

    def __str__(self) -> str:
        return self.format_cnh()
