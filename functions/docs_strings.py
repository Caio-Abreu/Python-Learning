def diz_oi():
    """Uma função simples que retorna a string 'Oi!' """
    return 'Oi !'

print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' informada
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial.Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero * potencia

print(help(exponencial))