a=input('строка')
a=a.upper( )
a=a.split( )
for x in a :
   if x==x[::-1]:
       print('полиндром')
    else:
        print('не полиндром')
