# Python tem um modulo built-in (integrado) para trabalhar com data e hora chamado datetime
import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a hora/data de agora
print(datetime.datetime.now()) # 2021-08-01 16:18:11.785796

# datetime.datetime(year,month,day,hour,minite,second,microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)

# Alterar o horario para 16 horas,0 min,0 seg, 0 microsegundo
inicio = inicio.replace(hour=16,minute=0,second=0,microsecond=0)
print(inicio)

# aniversario = input('Informe sua data de aniversario (dd/mm/yy): ')
# aniversario = aniversario.split('/')
# aniversario = datetime.datetime(int(aniversario[2]),int(aniversario[1]),int(aniversario[0]))
# print(aniversario)

evento = datetime.datetime.now()
# Acesso individual dos elementos de data e hora
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(dir(evento))