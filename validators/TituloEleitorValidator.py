class TituloEleitorValidator:

    def __init__(self, doc):
        self.titulo_eleitor = str(doc)
        if not self.correct_size():
            raise ValueError("Titulo Eleitor Size Invalid!")

    def is_valid(self) -> bool:
        try:
            if self.correct_size() and self.validate_titulo_eleitor():
                return True
            else:
                return False
        except ValueError:
            return False

    def correct_size(self) -> bool:
        if len(self.titulo_eleitor) == 12:
            return True
        else:
            return False

    def validate_titulo_eleitor(self) -> bool:
        titulo_eleitor = self.titulo_eleitor
        dv1 = 0
        dv2 = 0

        num1 = int(titulo_eleitor[0])
        num2 = int(titulo_eleitor[1])
        num3 = int(titulo_eleitor[2])
        num4 = int(titulo_eleitor[3])
        num5 = int(titulo_eleitor[4])
        num6 = int(titulo_eleitor[5])
        num7 = int(titulo_eleitor[6])
        num8 = int(titulo_eleitor[7])
        num9 = int(titulo_eleitor[8])
        num10 = int(titulo_eleitor[9])
        num11 = int(titulo_eleitor[10])
        num12 = int(titulo_eleitor[11])

        sum1 = sum([num1 * 2, num2 * 3, num3 * 4, num4 * 5, num5 * 6, num6 * 7, num7 * 8, num8 * 9]) % 11
        sum2 = sum([num9 * 7, num10 * 8, num11 * 9]) % 11

        if sum1 < 10:
            dv1 = sum1

        if sum2 < 10:
            dv2 = sum2

        if (dv1 == num11) and (dv2 == num12):
            return True
        else:
            return False

    def format_titulo_eleitor(self) -> str:
        return (
            "{}".format(
                self.titulo_eleitor
            )
        )

    def __str__(self) -> str:
        return self.format_titulo_eleitor()
