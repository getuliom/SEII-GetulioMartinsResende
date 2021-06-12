k=[1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'\0']
k[0]= int(input("Digite o valor da posição 1 = "))
k[1]= int(input("Digite o valor da posição 2 = "))

print ('\n O valor atual é = [',1,']  ',k[0])

count = 1
while (count <20):
    print (' O valor atual é = [',count+1,']  ',k[count])
    k[count+1]=k[count]+(count+2)
    count=count+1

print(" Good bye!")