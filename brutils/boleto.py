from random import randint

# FORMATTING
############


def remove_symbols_boleto(boleto: str) -> str:

    return "".join(filter(str.isdigit, boleto))


def modulo10(numero: str) -> int:
   
    total = 0
    peso = 2
    for n in reversed(numero):
        mult = int(n) * peso
        total += mult // 10 + mult % 10
        peso = 3 - peso
    resto = total % 10
    return 0 if resto == 0 else 10 - resto


def modulo11(numero: str) -> int:
    
    total = 0
    peso = 2
    for n in reversed(numero):
        total += int(n) * peso
        peso += 1
        if peso > 9:
            peso = 2
    resto = total % 11
    if resto == 0 or resto == 1:
        return 0
    if resto == 10:
        return 1
    return 11 - resto



def display(boleto: str) -> str:
    boleto = remove_symbols_boleto(boleto)
    if not is_valid_boleto(boleto):
        return None
    return "{}.{} {}.{} {}.{} {} {}".format(boleto[:5], boleto[5:10], boleto[10:15], boleto[15:21], boleto[21:26], boleto[26:32], boleto[32:33], boleto[33:])


def format_boleto(boleto: str) -> str:

    if not is_valid_boleto(boleto):
        return None

    return "{}.{} {}.{} {}.{} {} {}".format(boleto[:5], boleto[5:10], boleto[10:15], boleto[15:21], boleto[21:26], boleto[26:32], boleto[32:33], boleto[33:])


# OPERATIONS
############


def is_valid_boleto(boleto: str) -> bool:

    boleto = remove_symbols_boleto(boleto)

    if not boleto.isdigit() or len(boleto) != 47 or len(set(boleto)) == 1:
        return False

    blocos = [
        (boleto[0:9], int(boleto[9])),
        (boleto[10:20], int(boleto[20])),
        (boleto[21:31], int(boleto[31])),
    ]

    if not all(modulo10(nums) == dv for nums, dv in blocos):
        return False

    dv_geral = int(boleto[32])
    resto_num = boleto[0:4] + boleto[32:47]
    if modulo11(resto_num) != dv_geral:
        return False

    return True



def generate_boleto() -> str:
    
    bloco1_base = "".join(str(randint(0, 9)) for _ in range(9))
    dv1 = modulo10(bloco1_base)

    
    bloco2_base = "".join(str(randint(0, 9)) for _ in range(10))
    dv2 = modulo10(bloco2_base)

    
    bloco3_base = "".join(str(randint(0, 9)) for _ in range(10))
    dv3 = modulo10(bloco3_base)

    
    resto_num = bloco1_base[:4] + bloco3_base + bloco2_base[:3]  
    dv_geral = modulo11(resto_num)

    
    fator_valor = "".join(str(randint(0, 9)) for _ in range(14))

    
    boleto = f"{bloco1_base}{dv1}{bloco2_base}{dv2}{bloco3_base}{dv3}{dv_geral}{fator_valor}"
    return boleto
