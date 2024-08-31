from aes_decipher import aes_decipher
from aes_encipher import aes_encipher
from utils import bytes_to_hex, hex_to_bytes

if __name__ == "__main__":
    plaintext = hex_to_bytes('00112233445566778899aabbccddeeff')
    key = hex_to_bytes('000102030405060708090a0b0c0d0e0f')
    expected_ciphertext = hex_to_bytes('69c4e0d86a7b0430d8cdb78070b4c55a')
    
    enciphered = aes_encipher(plaintext, key)
    deciphered = aes_decipher(enciphered, key)
    
    print("Texto cifrado:", bytes_to_hex(enciphered))
    print("Texto decifrado:", bytes_to_hex(deciphered))
    print('Igual ao original?', bytes_to_hex(plaintext) == bytes_to_hex(deciphered))


    print('Cifração Correta?', bytes_to_hex(enciphered) == bytes_to_hex(expected_ciphertext))