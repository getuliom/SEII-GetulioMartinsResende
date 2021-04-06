import socket # importa a biblioteca socket
import time 
import pickle # importa pickle para serializar o documento e transmitir na rede

HEADERSIZE=10 # tamanho arbitrário de cabeçalho

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # abre um socket tcp ipv4
s.bind((socket.gethostname(),1241)) # liga o socket criado com o host na porta 1243
s.listen(5)
f=open("Moonbounce_at_Arecibo.pdf","rb") # arquivo base para ser duplicado (pdf sobre o radio-observatório de arrecibo)
# leitura binaria
content=f.read() # a variavel content receve o conteudo do arquivo
while True:
    clientsocket, address=s.accept()
    print(f"Connection from {address} has been established.")

    msg=pickle.dumps(content) # transforma o arquivo em formato pickle
    msg=bytes(f"{len(msg):<{HEADERSIZE}}",'utf-8')+msg
    #print(msg)
    clientsocket.send(msg) # manda o arquiv serializado pelo pickle para o cliente

f.close() # fecha o arquivo em questão