import socket # biblioteca para transmissão de rede
import pickle # biblioteca de serialização de informação

HEADERSIZE = 10 # tamanho arbitrário de cabeçalho

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # cria um socket ipv4 tcp
s.connect((socket.gethostname(),1241)) # conecta o socket do host com a porta 1241
pat=socket.gethostname() # variável que recebe nome do host
f=open("file_client "+pat+" 1241 "+"newfile","wb") # função que cria um arquivo novo
while True: 
    full_msg = b''
    new_msg=True
    while True:
        msg=s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen=int(msg[:HEADERSIZE])
            new_msg=False
        print (f"full message lenght : {msglen}")

        full_msg+=msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE==msglen:
            print("full msg recvd") #  avisa quando toda a mensagem foi recebida
            print(full_msg[HEADERSIZE:]) # imprime na tela com o formato pickle
            print(pickle.loads(full_msg[HEADERSIZE:])) # imprime na tela no formato normal
            f.write(pickle.loads(full_msg[HEADERSIZE:])) # escreve no arquivo criado a informação do arquivo a ser copiado
            new_msg=True
            full_msg=b""

f.close() # função que fecha o arquivo criado