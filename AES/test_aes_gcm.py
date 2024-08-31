from os import path
from utils import hex_to_bytes, bytes_to_hex, read_file, write_file
from aes_gcm_encrypt_decrypt import aes_gcm_encipher, aes_gcm_decipher

# Define a pasta onde os arquivos serão salvos e lidos
base_folder = "arquivos"

def test_aes_gcm(plaintext, key, nonce, num_rounds=10):
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')

    # Cifração usando GCM
    ciphertext, tag = aes_gcm_encipher(plaintext, key, nonce, num_rounds)

    # Decifração usando GCM
    try:
        deciphered_plaintext = aes_gcm_decipher(ciphertext, key, nonce, tag, num_rounds)
        if deciphered_plaintext == plaintext:
            print("O modo GCM está funcionando corretamente!")
            print("Texto cifrado:", bytes_to_hex(ciphertext))
            print("Texto original:", deciphered_plaintext.decode('utf-8'))
        else:
            print("Erro: o texto decifrado não corresponde ao texto original.")
    except ValueError as e:
        print("Erro de autenticação:", str(e))

def test_aes_gcm_file(input_file, key, nonce, output_enciphered_file='enciphered', output_deciphered_name='deciphered', num_rounds=10):
    input_path = path.join(base_folder, input_file)
    output_enciphered_path = path.join(base_folder, output_enciphered_file)
    output_deciphered_path = path.join(base_folder, output_deciphered_name)

    plaintext = read_file(input_path)

    # Cifrar o arquivo
    ciphertext, tag = aes_gcm_encipher(plaintext, key, nonce, num_rounds)
    output_enciphered_name = path.splitext(output_enciphered_path)[0]

    write_file(output_enciphered_name + ".bin", ciphertext)
    write_file(output_enciphered_name + ".tag", tag)

    # Decifrar o arquivo
    enciphered_data = read_file(output_enciphered_name + ".bin")
    saved_tag = read_file(output_enciphered_name + ".tag")

    output_deciphered_name = path.splitext(output_deciphered_path)[0]
    input_file_ext = path.splitext(input_path)[1]

    try:
        deciphered_plaintext = aes_gcm_decipher(enciphered_data, key, nonce, saved_tag, num_rounds)
        write_file(output_deciphered_name + input_file_ext, deciphered_plaintext)
        print("O modo GCM para arquivo está funcionando!")
    except ValueError as e:
        print("Erro ao decifrar o arquivo: ", str(e))

if __name__ == "__main__":
    key = hex_to_bytes('000102030405060708090a0b0c0d0e0f')
    nonce = hex_to_bytes('000000000000000000000000')

    plaintext = "Este é um texto de teste para o modo GCM."

    test_aes_gcm(plaintext, key, nonce)

    test_aes_gcm_file("texto.txt", key, nonce, "texto_cifrado_gcm", "texto_decifrado_gcm")

    test_aes_gcm_file("selfie.jpg", key, nonce, "selfie_cifrado_gcm", "selfie_decifrado_gcm")

    # Testar decifração com texto cifrado pelo OpenSSL

    enciphered_data = read_file(path.join(base_folder, "selfie_cifrado_openssl.bin"))
    saved_tag = read_file(path.join(base_folder, "selfie_cifrado_gcm.tag"))

    try:
        deciphered_plaintext = aes_gcm_decipher(enciphered_data, key, nonce, saved_tag)
        write_file(path.join(base_folder, 'selfie_decifrado_openssl_gcm.jpg'), deciphered_plaintext)
        print("A decifração GCM para selfie cifrada em OpenSSL está funcionando!")
    except ValueError as e:
        print("Erro ao decifrar arquivo OpenSSL: ", str(e))

    # Testar cifração com texto cifrado pelo OpenSSL

    enciphered_data = read_file(path.join(base_folder, "texto_cifrado_openssl.bin"))
    saved_tag = read_file(path.join(base_folder, "texto_cifrado_gcm.tag"))

    try:
        deciphered_plaintext = aes_gcm_decipher(enciphered_data, key, nonce, saved_tag)
        write_file(path.join(base_folder, 'texto_decifrado_openssl_gcm.txt'), deciphered_plaintext)
        print("A decifração GCM para texto cifrado em OpenSSL está funcionando!")
    except ValueError as e:
        print("Erro ao decifrar arquivo OpenSSL: ", str(e))
