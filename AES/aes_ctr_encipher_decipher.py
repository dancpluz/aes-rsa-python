from aes_encipher import aes_encipher

def aes_ctr_encipher(plaintext, key, nonce, num_rounds=10):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')

    block_size = 16
    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        # Cria o bloco contador combinando o nonce com o contador
        counter = i // block_size
        counter_block = nonce + counter.to_bytes(block_size - len(nonce), byteorder='big')

        # Cifra o bloco contador para gerar o keystream
        keystream = aes_encipher(counter_block, key, num_rounds)

        # XOR keystream com o bloco de plaintext
        block = plaintext[i:i + block_size]
        ciphertext_block = bytes(a ^ b for a, b in zip(block, keystream[:len(block)]))
        ciphertext += ciphertext_block

    return ciphertext

def aes_ctr_decipher(ciphertext, key, nonce, num_rounds=10):
    return aes_ctr_encipher(ciphertext, key, nonce, num_rounds)