class PisValidator:

    def __init__(self, doc):
        self.pis = str(doc).replace('.', '').replace('-', '')
        if not self.correct_size():
            raise ValueError("PIS Size Invalid!")

    def is_valid(self) -> bool:
        try:
            if self.correct_size() and self.validate_cnh():
                return True
            else:
                return False
        except ValueError:
            return False

    def correct_size(self) -> bool:
        if len(self.pis) == 11:
            return True
        else:
            return False

    def validate_pis(self) -> bool:
        pis = self.pis
        dv = 0

        num1 = int(pis[0])
        num2 = int(pis[1])
        num3 = int(pis[2])
        num4 = int(pis[3])
        num5 = int(pis[4])
        num6 = int(pis[5])
        num7 = int(pis[6])
        num8 = int(pis[7])
        num9 = int(pis[8])
        num10 = int(pis[9])
        num11 = int(pis[10])

        sum1 = (num1 * 3) + (num2 * 2) + (num3 * 9) + (num4 * 8) + (num5 * 7) + (num6 * 6) + (num7 * 5) + (num8 * 4) + (
                num9 * 3) + (num10 * 2)

        if ((11 - (sum1 % 11)) != 10) and ((11 - (sum1 % 11)) != 11):
            dv = 11 - (sum1 % 11)

        if dv == num11:
            return True
        else:
            return False

    def format_pis(self) -> str:
        return (
            "{}.{}.{}-{}".format(
                self.pis[:3],
                self.pis[3:8],
                self.pis[8:10],
                self.pis[10:]
            )
        )

    def __str__(self) -> str:
        return self.format_pis()
