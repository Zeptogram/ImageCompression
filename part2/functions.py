import numpy as np
from scipy.fft import dctn, idctn
from PIL import Image


# Effettuo tutte le operazioni per comprimere l'img
def compress_image(image, F, d):
    image_matrix = np.array(image)
    image_height, image_width = image_matrix.shape
    ff_blocks = []
    blocks = get_blocks(image_matrix, image_height, image_width, F)
    for f in blocks:
        f = np.array(f)
        c = dct2(f)
        c_compressed = compress_block(c, d, F)
        ff = idct_block(c_compressed)
        ff_blocks.append(ff)
    
    compressed_image = reconstruct_image(ff_blocks, image_width, image_height, F)
    return compressed_image

# Suddivido in blocchi FxF l'img, scartando gli avanzi
def get_blocks(matrix, image_height, image_width, F):
    blocks = []
    # // divisione intera, soggetta a scarti
    blocks_v= image_height // F
    blocks_h = image_width // F
    for i in range(blocks_v):
        for j in range(blocks_h):
            # Estrae il blocco F x F
            block = matrix[i*F:(i+1)*F, j*F:(j+1)*F]
            blocks.append(block)
    return blocks

# Elimino le componenti di un blocco ckl con k+l ≥ d
def compress_block(block, d, F):
    compressed_block = np.zeros_like(block)
    for k in range(F):
        for l in range(F):
            keep = k + l
            if keep < d:
                compressed_block[k][l] = block[k][l]
    return compressed_block

# Applico idct2 per tornare all'img, arrotondando le componenti
# con valori corretti per rgb a 1 byte
def idct_block(compressed_block):
    ff = idct2(compressed_block)
    ff_rounded = np.round(ff)
    ff_valid = np.clip(ff_rounded, 0, 255)
    ff_byte = ff_valid.astype(np.uint8)
    return ff_byte

def reconstruct_image(blocks, image_width, image_height, F):
    new_image_matrix = np.zeros((image_height, image_width), dtype=np.uint8)
    blocks_v = image_height // F
    blocks_h = image_width // F
    for i in range(blocks_v):
        for j in range(blocks_h):
            # Estrae il blocco F x F
            new_image_matrix[i*F:(i+1)*F, j*F:(j+1)*F] = blocks[i*blocks_h + j]

    return Image.fromarray(new_image_matrix)

# DCT2 della libreria
def dct2(matrix):
    return dctn(matrix, norm='ortho')

# IDCT2 della libreria
def idct2(matrix):
    return idctn(matrix, norm='ortho')

# Validazione input
def validate_data(d, F):
    # Controllo se la d è corretta
    if 0 <= d <= 2 * F - 2:
        # Controllo se F è positivo
        if F > 0:
            return True

    else:
        return False