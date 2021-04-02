pokemon = ('picachu', 'charmander', 'bulbasaur')
print(pokemon[1])
starter1 = pokemon[0]
starter2 = pokemon[1]
starter3 = pokemon[2]

print(starter1, starter2, starter3)

str = 'Hannah'
my_tuple = tuple(str)
i = 0
while i < len(str):
    print(str[i])
    i += 1


x = range(2, 11)
for n in x:
    print(n)



x = 2
while x > 1 and x < 11:
    print(x)
    x = x + 1

str = ' This is a simple string'
for n in str:
    print(n)

my_tuple = ('this', 'is', 'a', 'simple', 'set')

for i in my_tuple:
    for j in range(4,7):
        print(f'i = {i}; j = {j}')

