import random # технические переменые
q=0
a=('аденин гуанин цитозин тимин хемосинтез фотосинтез сахороза полисахариды углеводы транскрипция лактоза мальтоза') # мне было лень придуиывать слова, поэтому я взял их из учебника по биологии
a=a.split( )        
s=random.choice(a)
f=len(s)
s=str(s)
h=s
s=list(s)           
for e in s :
    e=('*')
    print(e)        # кодирование слова
while q==1
    print('угадай слово по буквам')
    print(f,'букв в слове')
    d=input('напиши букву или слово')
    z=len(d)
    if z==f:
        if d==h:
            print('победа')
            q=1
        else:
            print('порожение')  # сравнения слова
            q=1
 
    else:
        
        for y in s :
            print('напиши букву')
            e=e+1
            print(e)
            if d==y:
                e=d
                q=10
                q=q-1
                if q==1 :
                    print('победа')
            else:
                e=e
                q=10
                q=q-1
                if q==1 :
                    print('поражение')# сравнения букв
        
