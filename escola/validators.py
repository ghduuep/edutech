from validate_docbr import CPF
import re

def cpf_invalido(numero_cpf):
    cpf = CPF()
    return not cpf.validate(numero_cpf)

def nome_invalido(nome):
    return not re.match(r'^[\sa-zA-ZÀ-ÿ]+$', nome)