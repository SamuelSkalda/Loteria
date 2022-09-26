from random import*

cisla_p = input('Zadaj 6 tipov medzi 1 a 49 a oddel ich medzerou: ')
cisla_p = cisla_p.split()
print(cisla_p)
vyzrebovane = [0]*6
uhadnute = ''
v = ''
pocet_u = 0
subor = open('loteria_1.txt', 'r')
poc_uhadnute=[0]*6

for i in range(6):
    loteria = randrange(1,49)
    if loteria not in vyzrebovane:
        vyzrebovane[i] = loteria
        v += str(loteria)+' '
print('Vyzrebovane cisla: ',v)        

for cislo in vyzrebovane:
    if str(cislo) in cisla_p:
        uhadnute += str(cislo)+' '
        pocet_u += 1
print('Uhadnute cislo: ',uhadnute)
print('Pocet uhadnutych cisel: ',pocet_u)
    
for riadok in subor:
    u = 0
    riadok = riadok.strip()
    riadok = riadok.split()
    for cislo in riadok:
        if int(cislo) in vyzrebovane:
            u += 1
    if u > 0:
        poc_uhadnute[u-1] += 1

for i in range(len(poc_uhadnute)):
    print('{} ucastnikov tiplo spravne {} cisel.'.format(poc_uhadnute[i],i+1))