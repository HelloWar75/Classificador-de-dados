class ProcessoJudicialValidator:

    def __init__(self, doc):
        self.processo_judicial = str(doc).replace('-', '').replace('.', '')
        if not self.correct_size():
            raise ValueError("Processo Judicial Size Invalid!")

    def is_valid(self) -> bool:
        try:
            if self.correct_size() and self.validate_processo_judicial():
                return True
            else:
                return False
        except ValueError:
            return False

    def correct_size(self) -> bool:
        if len(self.processo_judicial) == 20:
            return True
        else:
            return False

    def validate_processo_judicial(self) -> bool:
        processo_judicial = self.processo_judicial
        processo_judicial_sem_dv = processo_judicial[0:7] + processo_judicial[9:] + '00'
        sum_part1 = int(processo_judicial[0:7]) % 97
        sum_part2 = int(str(sum_part1) + processo_judicial_sem_dv[7:14]) % 97
        sum_part3 = int(str(sum_part2) + processo_judicial_sem_dv[14:]) % 97
        sum_part4 = 98 - sum_part3

        if int(processo_judicial[7:9]) == sum_part4:
            return True
        else:
            return False

    def format_processo_judicial(self) -> str:
        return (
            "{}-{}.{}.{}.{}.{}".format(
                self.processo_judicial[:7],
                self.processo_judicial[7:9],
                self.processo_judicial[9:13],
                self.processo_judicial[13:14],
                self.processo_judicial[14:16],
                self.processo_judicial[16:]
            )
        )

    def __str__(self) -> str:
        return self.format_processo_judicial()
