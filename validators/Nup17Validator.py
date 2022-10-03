class Nup17Validator:

    def __init__(self, doc):
        self.nup17 = str(doc).replace('.', '').replace('/', '').replace('-', '')
        if not self.correct_size():
            raise ValueError("NUP17 Size Invalid!")

    def is_valid(self) -> bool:
        try:
            if self.correct_size() and self.validate_nup17():
                return True
            else:
                return False
        except ValueError:
            return False

    def correct_size(self) -> bool:
        if len(self.nup17) == 17:
            return True
        else:
            return False

    def validate_nup17(self) -> bool:
        nup17 = self.nup17
        dv1 = 0
        dv2 = 0

        num1 = int(nup17[0])
        num2 = int(nup17[1])
        num3 = int(nup17[2])
        num4 = int(nup17[3])
        num5 = int(nup17[4])
        num6 = int(nup17[5])
        num7 = int(nup17[6])
        num8 = int(nup17[7])
        num9 = int(nup17[8])
        num10 = int(nup17[9])
        num11 = int(nup17[10])
        num12 = int(nup17[11])
        num13 = int(nup17[12])
        num14 = int(nup17[13])
        num15 = int(nup17[14])
        num16 = int(nup17[15])
        num17 = int(nup17[16])

        sum1 = sum(
            [num1 * 16, num2 * 15, num3 * 14, num4 * 13, num5 * 12, num6 * 11, num7 * 10, num8 * 9, num9 * 8, num10 * 7,
             num11 * 6, num12 * 5, num13 * 4, num14 * 3, num15 * 2]) % 11

        if (sum1 > 0) and (sum1 < 10):
            dv1 = 11 - sum1
        elif sum1 > 9:
            dv1 = int(str(sum1)[1])

        sum2 = sum([num1 * 17, num2 * 16, num3 * 15, num4 * 14, num5 * 13, num6 * 12, num7 * 11, num8 * 10, num9 * 9,
                    num10 * 8, num11 * 7, num12 * 6, num13 * 5, num14 * 4, num15 * 3, num16 * 2]) % 11

        if (sum2 > 0) and (sum2 < 10):
            dv2 = 11 - sum2
        elif sum2 > 9:
            dv2 = int(str(sum2)[1])

        if (dv1 == num16) and (dv2 == num17):
            return True
        else:
            return False

    def format_cnh(self) -> str:
        return (
            "{}.{}/{}-{}".format(
                self.nup17[:5],
                self.nup17[5:11],
                self.nup17[11:15],
                self.nup17[15:]
            )
        )

    def __str__(self) -> str:
        return self.format_cnh()
