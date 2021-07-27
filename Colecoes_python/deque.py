from collections import deque

deq = deque('deek')
print(deq)

# Adicionando elementos no deque
deq.append('y') # Adiciona no final
print(deq)
deq.appendleft('k') # Adiciona no inicio
print(deq)
print('-----------------------------------')
# Remover elementos
print(deq.pop()) # Remove e retorna o ultimo elemento
print(deq)
print(deq.popleft())
print(deq)