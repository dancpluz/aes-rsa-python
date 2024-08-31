# Transforma hexadecimal em bytes
def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

# Transforma bytes em hexadecimal
def bytes_to_hex(byte_str):
    return byte_str.hex()

# Converte o estado de 16 bytes em uma matriz 4x4
def state_to_matrix(state):
    return [[state[r + 4 * c] for c in range(4)] for r in range(4)]

# Converte uma matriz 4x4 em um estado linear de 16 bytes
def matrix_to_state(matrix):
    return bytes(matrix[r][c] for c in range(4) for r in range(4))

# Lê um arquivo e retorna os dados binários
def read_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Escreve dados binários em um arquivo
def write_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)