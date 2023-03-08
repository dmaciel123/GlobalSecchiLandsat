import os

os.chdir('/Users/danielmaciel/Library/CloudStorage/OneDrive-inpe.br/Doutorado/Artigos/Global Secchi')


from MDN import image_estimates, get_tile_data, get_sensor_bands
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from osgeo import gdal 
import numpy as np
import pandas as pd
import numpy as np
from image_application_function import image_MDN_application
import glob 


#IMAGE_PATH_NC = '/Users/danielmaciel/Library/CloudStorage/OneDrive-Personal/R_Projects/Time_Series_Secchi_Global_secchi/Data/Taihu/LT05_L1TP_119038_19850111_20200918_02_T1/Outputs/L5_TM_1985_01_11_02_01_29_119038_L2W.nc'
#IMAGE_PATH_TIF_REF = '/Users/danielmaciel/Library/CloudStorage/OneDrive-Personal/R_Projects/Time_Series_Secchi_Global_secchi/Data/Taihu/LT05_L1TP_119038_19850111_20200918_02_T1/Outputs/L5_TM_1985_01_11_02_01_29_119038_L2W_Rrs_486.tif'
#SAVE_PATH = '/Users/danielmaciel/Library/CloudStorage/OneDrive-Personal/R_Projects/Time_Series_Secchi_Global_secchi/Data/Taihu/LT05_L1TP_119038_19850111_20200918_02_T1/Outputs/L5_TM_1985_01_11_02_01_29_119038_L2W_secchi.tif'



res = glob.glob('/Volumes/Crucial X8/Projects/Secchi Maps/Data/SecchiApplication/LakeVictoria/*/Processed/*.nc', recursive = True)
path_ref = glob.glob('/Volumes/Crucial X8/Projects/Secchi Maps/Data/SecchiApplication/LakeVictoria/*/Processed/*Rrs_561.tif', recursive = True)
path_ref_TM = glob.glob('/Volumes/Crucial X8/Projects/Secchi Maps/Data/SecchiApplication/LakeVictoria/*/Processed/*Rrs_571.tif', recursive = True)

path_ref = path_ref+path_ref_TM
save_path = glob.glob('/Volumes/Crucial X8/Projects/Secchi Maps/Data/SecchiApplication/LakeVictoria/*/Processed/', recursive = True)

print(res)
print('           ')

print(path_ref)

print('           ')
print(save_path)

num_images = (len(save_path))

print(len(res))
print(len(path_ref))
print(num_images)

## Aplicação única

image_MDN_application('/Users/danielmaciel/Library/CloudStorage/OneDrive-Personal/R_Projects/Time_Series_Secchi_Global_secchi/Data/Cheseapeake/LC09_L1TP_014034_20230213_20230214_02_T1/L9_OLI_2023_02_13_15_41_09_014034_L2W.nc', 
                        '/Users/danielmaciel/Library/CloudStorage/OneDrive-Personal/R_Projects/Time_Series_Secchi_Global_secchi/Data/Cheseapeake/LC09_L1TP_014034_20230213_20230214_02_T1/L9_OLI_2023_02_13_15_41_09_014034_L2W_Rrs_561.tif', 
                        '/Users/danielmaciel/Library/CloudStorage/OneDrive-Personal/R_Projects/Time_Series_Secchi_Global_secchi/Data/Cheseapeake/LC09_L1TP_014034_20230213_20230214_02_T1', 'OLI-NoCoastal', False)

 

# for i in range(1):

    
#     IMAGE_PATH_NC = res[i]
#     print(IMAGE_PATH_NC)

#     IMAGE_PATH_TIF_REF = path_ref[i]
#     print(IMAGE_PATH_TIF_REF)

#     SAVE_PATH = save_path[i]
#     print(SAVE_PATH)

#     sensor = SAVE_PATH.split('/')[-3].split('_')[0]
#     print(sensor)
#     print(i)

#     if sensor == 'LT05':
#         image_MDN_application(IMAGE_PATH_NC, IMAGE_PATH_TIF_REF, SAVE_PATH, 'TM', False)

#     if sensor == 'LE07':
#         image_MDN_application(IMAGE_PATH_NC, IMAGE_PATH_TIF_REF, SAVE_PATH, 'ETM', False)

#     if sensor == 'LC08':
#         image_MDN_application(IMAGE_PATH_NC, IMAGE_PATH_TIF_REF, SAVE_PATH, 'OLI-NoCoastal', False)

#     if sensor == 'LC09':
#         image_MDN_application(IMAGE_PATH_NC, IMAGE_PATH_TIF_REF, SAVE_PATH, 'OLI-NoCoastal', False)   

