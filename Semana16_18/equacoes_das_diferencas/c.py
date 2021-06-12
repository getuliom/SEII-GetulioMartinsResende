k=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'\0']
k[0]= int(input("Digite o valor inicial = "))

count = 0
while (count <20):
    k[count+1]=(count+1)*(count+1)
    count=count+1
    print (' O valor atual é = [',count+1,']  ',k[count])

print("Good bye!")