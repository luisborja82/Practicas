#1
def Sumar(a,b):
    return a+b
pass

# a=Sumar(5,5)
# print(a)

def Cant(a:str):
    return len(a)
pass

# nombre= input("Ingrese tu nombre ")

# print(" Tu nombre tiene "+ str(Cant(nombre))+" letras")

#5
def Mayu(a:str):
    return a.upper()
pass

# nombre= input("Ingrese tu nombre ")
# a=Mayu(nombre)
# print(a)

def Mayu(a:str):

    return a.upper()
pass

def minu(b:str):
    return b.lower()
pass


# nombre= input("Ingrese tu nombre ")
# a=minu(nombre)
# b=Mayu(nombre)
# print(a)
# print(b)
def cant(nom1: str,nomb2:str):
    if len(nom1)>len(nomb2):
        return True
    else:
        return False
pass

# nom1=input("Ingrese un nombre ")
# nom2=input("Ingrese otro nombre ")

# print(str(cant(nom1,nom2)))

import cadena as a

print(a.leer_cadena())


def expo(base,expon):
    return pow(base,expon)
pass

assert expo(2,5)== 32
assert expo(8,8)== 16777216
assert expo(1,9)== 1

print("Paso")



