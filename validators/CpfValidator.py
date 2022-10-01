
class CpfValidator:

    def __init__(self, doc):
        self.cpf = str(doc).replace('.', '').replace('-', '')
        if not self.correct_size():
            raise ValueError("CPF Size Invalid!")
        if not self.validate_cpf():
            raise ValueError("CPF Are Invalid!")

    def is_valid(self):
        try:

            if self.correct_size():
                return True
            else:
                return False

            if self.validate_cpf():
                return True
            else:
                return False

        except ValueError:
            return False

    def correct_size(self):
        doc = self.cpf
        if len(doc) == 11:
            return True
        else:
            return False

    def validate_cpf(self):
        doc = self.cpf
        num1 = int(doc[0])
        num2 = int(doc[1])
        num3 = int(doc[2])
        num4 = int(doc[3])
        num5 = int(doc[4])
        num6 = int(doc[5])
        num7 = int(doc[6])
        num8 = int(doc[7])
        num9 = int(doc[8])
        num10 = int(doc[9])
        num11 = int(doc[10])

        sum1 = None
        sum2 = None

        if (num1 == num2) and (num3 == num4) and (num4 == num5) and (num6 == num7) and (num7 == num8) and (num8 == num9) and (num9 == num10) and (num10 == num11):
            raise ValueError("CPF Characters are equals!")
        else:
            sum1 = 0 if (((num1 * 10) + (num2 * 9) + (num3 * 8) + (num4 * 7) + (num5 * 6) + (num6 * 5) + (num7 * 4) + (
                    num8 * 3) + (num9 * 2)) * 10) % 11 == 10 else (((num1 * 10) + (num2 * 9) + (num3 * 8) + (
                    num4 * 7) + (num5 * 6) + (num6 * 5) + (num7 * 4) + (num8 * 3) + (num9 * 2)) * 10) % 11
            sum2 = 0 if (((num1 * 11) + (num2 * 10) + (num3 * 9) + (num4 * 8) + (num5 * 7) + (num6 * 6) + (num7 * 5) + (
                    num8 * 4) + (num9 * 3) + (num10 * 2)) * 10) % 11 == 10 else (((num1 * 11) + (num2 * 10) + (
                    num3 * 9) + (num4 * 8) + (num5 * 7) + (num6 * 6) + (num7 * 5) + (num8 * 4) + (num9 * 3) + (
                                                                                          num10 * 2)) * 10) % 11

        if (sum1 == num10) and (sum2 == num11):
            return True
        else:
            return False

    def format_cpf(self):
        first_group = self.cpf[:3]
        second_group = self.cpf[3:6]
        third_group = self.cpf[6:9]
        four_group = self.cpf[9:]
        return (
            "{}.{}.{}-{}".format(
                first_group,
                second_group,
                third_group,
                four_group
            )
        )

    def __str__(self):
        return self.format_cpf()
