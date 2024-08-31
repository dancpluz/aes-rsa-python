from aes_ctr_encipher_decipher import aes_ctr_decipher, aes_ctr_encipher
from aes_encipher import aes_encipher

# Multiplica dois números no campo de Galois GF(2^128).
def galois_multiply(x, y):
    result = 0
    for i in range(128):
        if y & 1:
            result ^= x
        carry = x & (1 << 127)
        x <<= 1
        if carry:
            x ^= 0xE1000000000000000000000000000000  # Polinômio irreduzível
        x &= (1 << 128) - 1  # Garantir que x tenha 128 bits
        y >>= 1
    return result & ((1 << 128) - 1)  # Garantir que o resultado tenha 128 bits

# Calcula o GHASH para a autenticação GCM.
def ghash(h, data):
    y = 0 
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        if len(block) < 16:
            block = block.ljust(16, b'\x00')  # Preencher com zeros
        y ^= int.from_bytes(block, byteorder='big')
        y = galois_multiply(y, int.from_bytes(h, byteorder='big'))
    return y.to_bytes(16, byteorder='big')

def aes_gcm_encipher(plaintext, key, nonce, num_rounds=10):
    # Cifra o texto
    ciphertext = aes_ctr_encipher(plaintext, key, nonce, num_rounds)

    # Autenticação
    h = aes_encipher(b'\x00' * 16, key, num_rounds) 
    len_c = len(ciphertext) * 8

    # Calcular GHASH apenas com ciphertext e seu comprimento
    ghash_input = ciphertext + len_c.to_bytes(8, byteorder='big')
    auth_tag = ghash(h, ghash_input)

    # Geração da tag de autenticidade (somar com o nonce)
    tag = aes_ctr_encipher(auth_tag, key, nonce, num_rounds)

    return ciphertext, tag

def aes_gcm_decipher(ciphertext, key, nonce, tag, num_rounds=10):
    # Decifrando o texto
    plaintext = aes_ctr_decipher(ciphertext, key, nonce, num_rounds)

    # Recalcular a tag de autenticidade
    h = aes_encipher(b'\x00' * 16, key, num_rounds)
    len_c = len(ciphertext) * 8

    # Calcular GHASH apenas com ciphertext e seu comprimento
    ghash_input = ciphertext + len_c.to_bytes(8, byteorder='big')
    auth_tag = ghash(h, ghash_input)
    expected_tag = aes_ctr_encipher(auth_tag, key, nonce, num_rounds)

    # Verificar a tag de autenticidade
    if expected_tag != tag:
        raise ValueError("Tag de autenticidade não confere, os dados podem ter sido corrompidos!")

    return plaintext