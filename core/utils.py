from random import randint
from datetime import date


def prepare_cpf(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    return cpf

def prepare_cnpj(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace(' ', '')
    cnpj = cnpj.replace('/', '')
    return cnpj

def prepare_phone(phone):
    phone = phone.replace('(', '')
    phone = phone.replace(')', '')
    phone = phone.replace(' ', '')
    phone = phone.replace('-', '')
    check = phone[:2]
    if check == '55':
        return phone
    return '55{0}'.format(phone)

def listing_months(year):
    months = []
    for i in range(1, 13):
        months.append((i, date(year, i, 1).strftime('%B')))
    return months

def truncate_float(value, n):
    try:
        s = u'{0:.{1}f}'.format(value, n)
    except Exception:
        s = u'0.0'
    result = s.split('.')
    return result[0]

def str_to_bool(s):
    if s.lower() in ['1', 'sim', 'yes', 'on', 'true']:
        return True
    return False


class CPF:
    """
    Classe to work with brazilian CPF
    """

    def format(self, cpf):
        """
        Method that formats a brazilian CPF

        Tests:
        >>> print CPF().format('91289037736')
        912.890.377-36
        """
        return "%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

    def validate(self, cpf):
        """
        Method to validate a brazilian CPF number.

        Tests:
        >>> print CPF().validate('91289037736')
        True
        >>> print CPF().validate('91289037731')
        False
        """
        if not cpf.isdigit():
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")

        cpf_invalidos = [11*str(i) for i in range(10)]
        if cpf in cpf_invalidos:
            return False

        if len(cpf) < 11:
            return False

        if len(cpf) > 11:
            return False

        selfcpf = [int(x) for x in cpf]
        cpf = selfcpf[:9]

        while len(cpf) < 11:
            list_1 = []
            list_2 = []
            for x in range(len(cpf)):
                list_1.append((x, cpf[x]))
            for i, v in list_1:
                list_2.append((len(cpf)+1-i)*v)

            r = sum(list_2) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            cpf.append(f)

        return bool(cpf == selfcpf)

    def generate(self, formatar=False):
        # 9 random numbers
        arNumeros = []
        for i in range(9):
            arNumeros.append(randint(0, 9))

        # Calculating the first DV
        somaJ = (arNumeros[0] * 10) + (arNumeros[1] * 9) + (arNumeros[2] * 8) + (arNumeros[3] * 7) + (arNumeros[4] * 6) + (arNumeros[5] * 5) + (arNumeros[6] * 4) + (arNumeros[7] * 3) + (arNumeros[8] * 2)

        restoJ = somaJ % 11

        if (restoJ == 0 or restoJ == 1):
            j = 0
        else:
            j = 11 - restoJ

        arNumeros.append(j)

        # Calculating the second DV
        somaK = (arNumeros[0] * 11) + (arNumeros[1] * 10) + (arNumeros[2] * 9) + (arNumeros[3] * 8) + (arNumeros[4] * 7) + (arNumeros[5] * 6) + (arNumeros[6] * 5) + (arNumeros[7] * 4) + (arNumeros[8] * 3) + (j * 2)

        restoK = somaK % 11

        if (restoK == 0 or restoK == 1):
            k = 0
        else:
            k = 11 - restoK

        arNumeros.append(k)

        cpf = ''.join(str(x) for x in arNumeros)

        if formatar:
            return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        else:
            return cpf

    def unformat(self, cpf):
        """
        Method to remove formatting of CPF numbers.
        Tests:

        >>> print CPF().unformat('036.166.833-35')
        03616683335
        """
        return prepare_cpf(cpf)


class Phone:
    """
    Class to work with mobile numbers.
    """
    list_mobile = ['6', '7', '8', '9']
    list_landline = ['1', '2', '3', '4', '5']

    def mask(self, number):
        n = self.format(number)
        n = n[2:]
        ddd, col1, col2 = n[:2], n[2:7], n[7:]
        return n if len(n) < 10 else u'(%s) %s-%s' % (ddd, col1, col2)

    def format(self, number):
        n = number.replace('_', '')
        n = number.replace('(', '').replace(')', '')
        n = n.replace(' ', '').replace('-', '')
        check = n[:2]
        return n if check == '55' else u'55{0}'.format(n)

    def valid(self, number):
        n = self.format(number)
        if len(n) < 13:
            return 'incomplete'
        n = n[4:]
        digit_checker = n[0]
        return 'mobile' if digit_checker in self.list_mobile else 'landline'
