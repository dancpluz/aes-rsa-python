from aes_ctr_encipher_decipher import aes_ctr_decipher, aes_ctr_encipher
from utils import bytes_to_hex, hex_to_bytes


if __name__ == "__main__":
    # Chave de 128 bits (16 bytes)
    key = hex_to_bytes('000102030405060708090a0b0c0d0e0f')
    
    # Nonce (número arbitrário) - escolha 12 bytes e deixe 4 bytes para o contador
    nonce = hex_to_bytes('1234567890abcdef12345678')
    
    # Texto simples para cifração
    plaintext = "Este é um texto de teste para o modo CTR."
    
    # Cifrar o plaintext usando o modo CTR
    ciphertext = aes_ctr_encipher(plaintext, key, nonce)
    
    # Decifrar o ciphertext usando o modo CTR
    decrypted_text = aes_ctr_decipher(ciphertext, key, nonce)

    print("Texto cifrado:", bytes_to_hex(ciphertext))
    print("Texto decifrado:", decrypted_text.decode('utf-8'))
