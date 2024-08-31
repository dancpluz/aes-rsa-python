import random
from hashlib import sha3_256
import base64

# Verifica se um número é primo usando o Teste de Miller-Rabin.
def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Teste de Miller-Rabin
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Gera um número primo aleatório com o número de bits especificado.
def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

# Gera um par de chaves RSA (pública e privada).
def generate_keys(bits=1024):

    # Geração de dois números primos grandes p e q
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Escolha de e (padrão é 65537, um valor comum)
    e = 65537
    # Cálculo da chave privada d
    d = pow(e, -1, phi)
    
    return ((n, e), (n, d))

# Converte um número inteiro para bytes.
def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, byteorder='big')

# Converte bytes para um número inteiro.
def bytes_to_int(xbytes):
    return int.from_bytes(xbytes, byteorder='big')

# Assina uma mensagem usando a chave privada RSA.
def sign_message(message, private_key):
    n, d = private_key
    # Gera o hash da mensagem usando SHA3-256
    hash_value = int.from_bytes(sha3_256(message).digest(), byteorder='big')
    # Assina o hash com a chave privada
    signature = pow(hash_value, d, n)
    # Converte a assinatura para bytes e codifica em base64
    signature_bytes = int_to_bytes(signature)
    return base64.b64encode(signature_bytes).decode()

# Verifica uma assinatura digital usando a chave pública RSA.
def verify_signature(message, signature, public_key):
    n, e = public_key
    # Decodifica a assinatura de base64 para bytes
    signature_bytes = base64.b64decode(signature)
    # Converte a assinatura de bytes para inteiro
    signature_int = bytes_to_int(signature_bytes)
    # Decifra o hash assinado usando a chave pública
    hash_value = pow(signature_int, e, n)
    
    # Gera o hash da mensagem original para comparação
    calculated_hash = int.from_bytes(sha3_256(message).digest(), byteorder='big')
    return hash_value == calculated_hash