k=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'\0']
k[0]= int(input("Digite o valor inicial = "))

count = 0
while (count <20):
    print (' O valor atual é = [',count,']  ',k[count])
    k[count+1]=k[count]+2
    count=count+1

print("Good bye!")