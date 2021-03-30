import requests # importa a biblioteca necessária para acessar os urls
import time     # importa time para calcular o tempo de execução do programa
import concurrent.futures # importa a biblioteca necessária para as Threads

img_urls = [ 
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
] #  Cria uma lista de urls contendo imagens para serem baixadas com
  # o uso de Threads


#  Recebe o tempo em que o programa iniciou
t1 = time.perf_counter()

#  Cria uma função chamada download_image recebendo uma url
#    Recebe o valor do vetor
#    Armazena o valor após a barra
#    O valor armazenado recebe a extensão jpg 
#    Cria uma variável que vai receber os bytes da imagem da url
#      Escreve em img_file img_bytes
#      Imprime na tela que a imagem foi baixada e seu nome
   
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3] 
    img_name = f'{img_name}.jpg' 
    with open(img_name, 'wb') as img_file: 
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...') 

#  Chama a função ThreadPoolExecutor como executor

#  Mapeia a função para garantir que seja impresso
# em ordem o download dos arquivos, já que os
# downloads são feitos paralelamente e o primeiro
# a ser baixado seria impresso primeiro na tela
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

#  Recebe o tempo no momento do fim da execução
t2 = time.perf_counter()

#  Imprime na tela o tempo de execução do programa
# subtraindo o tempo final menos o inicial
print(f'Finished in {t2-t1} seconds') 