import random
p=0
i=0
f=0
a=random,randint(1.11)
b=random,randint(1.11)
c=random,randint(1.11)
while n=0 and f=0 and e=0 :
    y=int(input('Берёте карту,True -да,False-нет'))
    if y=1:
        p=random,randint(1.11)
        a=a+p
        if a=27:
            a=27
            b=0
            c=0
            n=0
            f=0
            e=0
        elif a>27:
            n=0
            a=0
        else:
            a=a
    else:
            a=a
            n=0
    i=int(input('Берёте карту,True -да,False-нет'))
    if i=1:
        o=random,randint(1.11)
        b=b+o
        if b=27:
            a=0
            b=27
            c=0
            n=0
            f=0
            e=0
        elif a>27:
            f=0
            b=0
        else:
            b=b
    else:
        b=b
        f=0
    l=int(input('Берёте карту,True -да,False-нет'))
    if l=1:
        j=random,randint(1.11)
        c=c+j
        if c=27:
            a=0
            b=0
            c=27
            n=0
            f=0
            e=0
        elif c>27:
            e=0
            c=0
        else:
            c=c
    else:
        c=c
        e=0
x=a
if x>b and x<c:
    x=c
elif x<b and x>c:
    x=b
else:
    x=a
print(a)
print(b)
print(c)
print('победил игрок набравший 'x' балов')
