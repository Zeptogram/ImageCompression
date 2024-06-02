from scipy.fft import dctn, idctn
import numpy as np


matrix = [
    [231, 32, 233, 161, 24, 71, 140, 245],
    [247, 40, 248, 245, 124, 204, 36, 107],
    [234, 202, 245, 167, 9, 217, 239, 173],
    [193, 190, 100, 167, 43, 180, 8, 70],
    [11, 24, 210, 177, 81, 243, 8, 112],
    [97, 195, 203, 47, 125, 114, 165, 181],
    [193, 70, 174, 167, 41, 30, 127, 245],
    [87, 149, 57, 192, 65, 129, 178, 228]
]


print(dctn(matrix, 2, norm="ortho"))

def divide_in_blocks(image_matrix, F):
    image_height, image_width = image_matrix.shape
    blocks = []
    num_blocks_vert = image_height // F
    num_blocks_horiz = image_width // F
    
    for i in range(num_blocks_vert):
        for j in range(num_blocks_horiz):
            block = image_matrix[i*F:(i+1)*F, j*F:(j+1)*F]
            blocks.append(block)
    
    return blocks

def compress_block(c, d, F):
    compressed_block = np.zeros_like(c, dtype=np.uint8)
    for k in range(F):
        for l in range(F):
            soglia = k + l
            if soglia < d:
                compressed_block[k][l] = c[k][l]

    return compressed_block

def compress_block2(c, d, F):
    compressed_block = c * (np.abs(np.add.outer(range(F), range(F))) < d)
    return compressed_block


# Genera una matrice 24x24 con valori casuali compresi tra 0 e 255
image_matrix = np.random.randint(0, 256, size=(10, 10))
print(image_matrix)

# Applica la funzione divide_in_blocks alla matrice
blocks = divide_in_blocks(image_matrix, 10)

# Stampare un esempio di blocco
print("Esempio di blocco:")
#print(blocks[0])

print(compress_block(blocks[0], 3, 10))
print(compress_block2(blocks[0], 3, 10))