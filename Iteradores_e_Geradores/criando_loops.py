for num in [1,2,3,4,5]:
    print(num)

iter([1,2,3,4,5])

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
meu_for('Caio abreu')
numeros = ['caio',2,3,4,5]
meu_for(numeros)