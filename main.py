import numpy as np
import functions as lib



a = np.array([456, 332, 43, 56, 785, 23, 12, 309, 78])
m = np.array([[231, 32, 233, 161, 24, 71, 140, 245], 
            [247, 40, 248, 245, 124, 204, 36, 107], 
            [234, 202, 245, 167, 9, 217, 239, 173],
            [193, 190, 100, 167, 43, 180, 8, 70],
            [11, 24, 210, 177, 81, 243, 8, 112],
            [97, 195, 203, 47, 125, 114, 165, 181],
            [193, 70, 174, 167, 41, 30, 127, 245],
            [87, 149, 57, 192, 65, 129, 178, 228]])

lib.write_results_to_file("DCT CUSTOM", lib.dct_custom(a))
lib.write_results_to_file("DCT LIBRARY", lib.dct_library(a))
lib.write_results_to_file("DCT2 CUSTOM", lib.dct2_custom(m))
lib.write_results_to_file("DCT2 LIBRARY", lib.dct2_library(m))

print("========================================================================================================")
print("DCT CUSTOM")
print("========================================================================================================")
print(lib.dct_custom(a))
print("========================================================================================================")
print("DCT LIBRARY")
print("========================================================================================================")
print(lib.dct_library(a))
print("========================================================================================================")
print("DCT2 CUSTOM")
print("========================================================================================================")
print(lib.dct2_custom(m))
print("========================================================================================================")
print("DCT2 LIBRARY")
print("========================================================================================================")
print(lib.dct2_library(m))