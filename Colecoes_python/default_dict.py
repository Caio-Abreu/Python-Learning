from typing import DefaultDict
dicionario = DefaultDict(lambda:0)

dicionario['curso'] = 'Programação em python:Essencial'
print(dicionario)
print(dicionario['outro']) #KeyError no dicionario comum, diferente daqui