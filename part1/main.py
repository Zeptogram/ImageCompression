import numpy as np
import functions as dct

# Per testing
testing = False

if testing:
    test_vector = np.array([456, 332, 43, 56, 785, 23, 12, 309, 78])
    test_matrix = np.array([[456, 332, 43, 56, 785, 23, 12, 309, 78],
                            [  9, 372, 223,  84, 140, 272, 150, 253,  97],
                            [ 40, 387, 321, 299, 366, 226,  11, 142, 264],
                            [202,  77, 289, 144, 323,  94, 212, 183, 399],
                            [ 32, 145, 119, 138, 357, 212, 129,  47,  66],
                            [314, 285, 372, 102,  26, 131, 142, 204,  53],
                            [ 90, 186, 233, 150,  11, 105, 147,  53, 215],
                            [398, 359, 292, 310,  37, 184, 234,  88, 151],
                            [ 76, 111,  24, 372,  87, 271,  66, 158, 290]])
    # Salvo i risultati delle dct
    custom_dct_res =  dct.dct_custom(test_vector)
    custom_dct2_res = dct.dct2_custom(test_matrix)
    library_dct_res = dct.dct_library(test_vector)
    library_dct2_res = dct.dct2_library(test_matrix)
    # Scrittura su file delle dct
    dct.write_results_to_file("DCT CUSTOM", custom_dct_res)
    dct.write_results_to_file("DCT LIBRARY", library_dct_res)
    dct.write_results_to_file("DCT2 CUSTOM", custom_dct2_res)
    dct.write_results_to_file("DCT2 LIBRARY", library_dct2_res)
    # Test di equality
    dct_eq = np.allclose(custom_dct_res, library_dct_res, atol=1e-8)
    print("Le DCT sono uguali: ", dct_eq)
    dct2_eq = np.allclose(custom_dct2_res, library_dct2_res, atol=1e-8)
    print("Le DCT2 sono uguali: ", dct2_eq)
else:
    # Analisi sulle DCT2
    dct.dct2_analize_graph()
