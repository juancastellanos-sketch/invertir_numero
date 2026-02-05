# programma para invertir un numero de 4 dijitos

#input
n=input("digite un numero de 4 digitos: ")
n=int(n)

# processig
r4=n%10
r3=(n//10)%10
r2=(n//100)%10
r1=(n//1000)%10

ni= r4*1000+r3*100+r2*10+r1

# output
print("---------resultado--------")
print("numero original:"+ str(n))
print("ultimo dijito:"+ str(r4))
print("tercer dijito:"+ str(r3))
print("segundo dijito:"+ str(r2))
print("primer dijito:"+ str(r1))
print("el numero invertido es :"+ str(ni))

