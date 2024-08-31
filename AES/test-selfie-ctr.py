import os
import math
from PIL import Image
from aes_ctr_encipher_decipher import aes_ctr_encipher
from utils import hex_to_bytes, read_file

def save_enciphered_image(ciphertext, num_rounds):
    # Calcular o tamanho necessário da imagem
    num_bytes = len(ciphertext)
    num_pixels = int((num_bytes + 2) / 3)
    W = H = int(math.ceil(num_pixels ** 0.5))

    # Preencher os dados da imagem com zeros, se necessário
    imagedata = ciphertext + b'\0' * (W * H * 3 - len(ciphertext))

    # Criar a imagem a partir dos dados
    image = Image.frombytes('RGB', (W, H), imagedata)

    # Garantir que a pasta "selfies" exista
    if not os.path.exists('selfies'):
        os.makedirs('selfies')

    # Salvar a imagem cifrada na pasta "selfies"
    image.save(f'selfies/selfie_{num_rounds}rodadas_cifrada.bmp')
    print(f'Imagem cifrada com {num_rounds} rodadas salva como "selfie_{num_rounds}rodadas_cifrada.bmp"')

def aes_ctr_encipher_image(image_file, key, nonce, num_rounds):
    plaintext = read_file(image_file)
    
    # Cifrar a imagem
    ciphertext = aes_ctr_encipher(plaintext, key, nonce, num_rounds)
    
    # Salvar o resultado cifrado como imagem
    save_enciphered_image(ciphertext, num_rounds)
    
    return ciphertext

if __name__ == "__main__":
    key = hex_to_bytes('000102030405060708090a0b0c0d0e0f')  # 128-bit key em hex
    nonce = hex_to_bytes('1234567890abcdef12345678')  # 96-bit nonce em hex

    image_file = 'arquivos/selfie.jpg'
    
    num_rounds_list = [1, 5, 9, 13]

    for num_rounds in num_rounds_list:
        aes_ctr_encipher_image(image_file, key, nonce, num_rounds)
