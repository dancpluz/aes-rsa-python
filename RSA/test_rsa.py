import os
from rsa import generate_keys, sign_message, verify_signature

# Define a pasta onde os arquivos serão salvos e lidos
base_folder = "arquivos"

# Lê um arquivo e retorna os dados binários
def read_file(file_path):
    with open(os.path.join(base_folder,file_path), 'rb') as file:
        return file.read()

# Salva a assinatura digital em um arquivo separado.
def save_signature(signature, file_path):
    signature_file = f"{file_path}.sig"
    with open(os.path.join(base_folder,signature_file), 'w') as file:
        file.write(signature)
    print(f"Assinatura salva em {signature_file}")

# Salva o arquivo original com a assinatura digital incorporada.
def save_file_with_signature(file_data, signature, file_path):
    signed_file_path = f"{file_path}.signed"
    with open(os.path.join(base_folder,signed_file_path), 'wb') as file:
        file.write(file_data)
        file.write(b'\n---SIGNATURE---\n')
        file.write(signature.encode())
    print(f"Arquivo com assinatura salvo em {signed_file_path}")

# Testa a assinatura e verificação de um arquivo.
def test_file_signature(file_path, private_key, public_key):
    print(f"Testando arquivo: {file_path}")
    file_data = read_file(file_path)
    
    signature = sign_message(file_data, private_key)
    print("Assinatura:")
    print(signature)
    
    save_signature(signature, file_path)
    save_file_with_signature(file_data, signature, file_path)
    
    is_valid = verify_signature(file_data, signature, public_key)
    print(f"Assinatura válida: {is_valid}")
    
    # Teste com chave pública diferente
    different_public_key, _ = generate_keys()
    is_valid_with_different_key = verify_signature(file_data, signature, different_public_key)
    print(f"Assinatura válida (chave pública diferente): {is_valid_with_different_key}")
    print("\n")

if __name__ == "__main__":
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)

    public_key, private_key = generate_keys()
    
    test_file_signature("selfie.jpg", private_key, public_key)
    test_file_signature("texto.txt", private_key, public_key)
    test_file_signature("doc.pdf", private_key, public_key)
