def comer(comida,eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente só vive uma vez'

    return f'Estou comendo {comida} porque {final}'

def dormir(num_horas):
    if num_horas > 8:
        return f'Putz dormi muito, estou atrasado para o trabalho'
    else:
        return f'Continuo cansado apos dormir por {num_horas} horas'

def eh_engracada(pessoa):
    comediantes =['jim carrey','bozo','sergio malandro']
    if pessoa in comediantes:
        return True
    return False