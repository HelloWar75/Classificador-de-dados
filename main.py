from validators.CpfValidator import CpfValidator
from validators.CnpjValidator import CnpjValidator
def run():
    # cpf = '01386292001'
    # vCPF = CpfValidator(cpf)
    # print(vCPF.is_valid())

    cnpj = '47.661.114/0001-46'
    vCNPJ = CnpjValidator(cnpj)
    print(vCNPJ)


if __name__ == '__main__':
    run()
