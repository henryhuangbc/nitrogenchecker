import random, string

print('Made by @GXGalaxy (Henry H)')
amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[H_GEN] {code}')
    value += 1
