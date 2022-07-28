#Utilizar la opcion run an debug
#Puntos de interrupcion o brake point



try:
    pass
except:
    pass
finally:
    pass

#RAISE, reportar error


def palindromo(palabra):
    try:
        if(type(palabra)==str):
            print("es una palabra")
        else:
            raise ValueError('!Error!, solo ingresar números')
    except ValueError as e:
        print('Error:',e)

#palindromo(1)

#Afirmaciones o assert

def pal(palabra):
    assert type(palabra)==str,"!solo texto!"
    print(palabra)

pal(1)