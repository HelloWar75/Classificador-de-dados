class CnpjValidator:

    def __init__(self, doc):
        self.cnpj = str(doc).replace('.', '').replace('/', '').replace('-', '')
        if not self.correct_size():
            raise ValueError("CPF Size Invalid!")

    def is_valid(self) -> bool:
        try:
            if self.correct_size():
                return True
            else:
                return False

            if self.validate_cnpj():
                return True
            else:
                return False

        except ValueError:
            return False

    def correct_size(self) -> bool:
        if len(self.cnpj) == 14:
            return True
        else:
            return False

    def validate_cnpj(self) -> bool:
        cnpj = self.cnpj

        dv1 = 0
        dv2 = 0

        num1 = int(cnpj[0])
        num2 = int(cnpj[1])
        num3 = int(cnpj[2])
        num4 = int(cnpj[3])
        num5 = int(cnpj[4])
        num6 = int(cnpj[5])
        num7 = int(cnpj[6])
        num8 = int(cnpj[7])
        num9 = int(cnpj[8])
        num10 = int(cnpj[9])
        num11 = int(cnpj[10])
        num12 = int(cnpj[11])
        num13 = int(cnpj[12])
        num14 = int(cnpj[13])

        sum1 = (num1 * 5) + (num2 * 4) + (num3 * 3) + (num4 * 2) + (num5 * 9) + (num6 * 8) + (num7 * 7) + (num8 * 6) + (
                    num9 * 5) + (num10 * 4) + (num11 * 3) + (num12 * 2)

        if sum1 % 11 > 2:
            dv1 = 11 - (sum1 % 11)

        sum2 = (num1 * 6) + (num2 * 5) + (num3 * 4) + (num4 * 3) + (num5 * 2) + (num6 * 9) + (num7 * 8) + (num8 * 7) + (
                    num9 * 6) + (num10 * 5) + (num11 * 4) + (num12 * 3) + (dv1 * 2)

        if sum2 % 11 > 2:
            dv2 = 11 - (sum2 % 11)

        if (num13 == dv1) and (num14 == dv2):
            return True
        else:
            return False

    def format_cnpj(self) -> str:
        return (
            "{}.{}.{}/{}-{}".format(
                self.cnpj[:2],
                self.cnpj[2:5],
                self.cnpj[5:8],
                self.cnpj[8:12],
                self.cnpj[12:],
            )
        )

    def __str__(self) -> str:
        return self.format_cnpj()
