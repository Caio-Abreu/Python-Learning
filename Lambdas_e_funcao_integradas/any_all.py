# all() -> retorna true se todos os elementos do interavel for verdadeiro ou vazio

print(all([0,1,2,3,4])) # False pois 0 = False
print(all([1,2,3,4])) # True

nomes = ['Caio','Carlos','Carla','Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print(all(letra for letra in 'iou' if letra in 'aeiou'))

print(all([num for num in [4,2,10,6,8] if num % 2 == 0]))

# any() -> se algum item for verdadeiro ele retorna True, só retorna False se o interavel estiver vazio

print(any([0,1,2,3,4])) # True
print(any([0,False,{},(),[]])) # False

nomes.append('Vanessa')
print(nomes)
print(any([nome[0]=='C' for nome in nomes]))

print(any([num for num in [4,2,10,6,8,9] if num % 2 == 0]))