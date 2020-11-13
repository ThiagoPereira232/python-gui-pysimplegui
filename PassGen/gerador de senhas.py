import random
print("\n--------- PASSWORD GENERATOR ---------\n")
num = int(input("Digite a quantidade de caracteres: "))
def passGen(num):
    c=0
    i = ''
    lista = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    while c<num:
        i+=random.choice(lista)
        c+=1
    print(f"\nPassword: {i}\n\n--------------------------------------")
passGen(num)
