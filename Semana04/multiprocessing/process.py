import time  #importa a biblioteca time para determinar o tempo de execução
import concurrent.futures #importa biblioteca que permite o multiprocessing
from PIL import Image, ImageFilter # importa essa biblioteca para processar
# as imagens

img_names = [ #imagens no mesmo diretórios à serem borradas
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter() # Contador do tempo inicial

size = (1200, 1200) # Mudando o tamanho das imagens para 1200 por 1200


def process_image(img_name): # Cria uma função de processamento da imagem
    img = Image.open(img_name) # Abrindo as imagens no vetor
    # Aplica borrador Gaussiano na imagem
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size) # Cortando a imagem para o tamonho size
    img.save(f'processed/{img_name}') # Salva a imagem no diretório processed
    print(f'{img_name} was processed...') # Imprime que a imagem foi processada

# A linha abaixo permite o multiprocessamento
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)
# Usado para imprimir que o processamento foi feito em ordem


t2 = time.perf_counter() # Contador do tempo final

print(f'Finished in {t2-t1} seconds') # Imprime o tempo de execução