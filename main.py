import numpy as np
import functions as dct

# Per testing
testing = False


if testing:
    test_vector = np.array([456, 332, 43, 56, 785, 23, 12, 309, 78])
    test_matrix = np.array([[231, 32, 233, 161, 24, 71, 140, 245], 
                [247, 40, 248, 245, 124, 204, 36, 107], 
                [234, 202, 245, 167, 9, 217, 239, 173],
                [193, 190, 100, 167, 43, 180, 8, 70],
                [11, 24, 210, 177, 81, 243, 8, 112],
                [97, 195, 203, 47, 125, 114, 165, 181],
                [193, 70, 174, 167, 41, 30, 127, 245],
                [87, 149, 57, 192, 65, 129, 178, 228]])

    dct.write_results_to_file("DCT CUSTOM", dct.dct_custom(test_vector))
    dct.write_results_to_file("DCT LIBRARY", dct.dct_library(test_vector))
    dct.write_results_to_file("DCT2 CUSTOM", dct.dct2_custom(test_matrix))
    dct.write_results_to_file("DCT2 LIBRARY", dct.dct2_library(test_matrix))

# Analisi sulle DCT2
dct.dct2_analize_graph()
