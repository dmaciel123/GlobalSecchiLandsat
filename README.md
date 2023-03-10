# Global Secchi Landsat
 
This code applies the Mixture Density Network (MDN) algorithm to Landsat atmospherically corrected or in situ measured Remote Sensing Reflectance to predict Secchi Disk Depth (Zsd). 

To run the code, clone the GitHub repository and install the required packages (requirements.txt) in a new Python (3.6 or 3.9) environment. 

Two examples are provided:

1) Running the MDN for TM, ETM+, and OLI simulated Rrs based on a subset of GLORIA (Lehmann et al. 2023) dataset

2) Running the MDN for OLI-2 Chesapeake Bay Rrs data to spatialize the Zsd.
 

## Instalation 

First, clone the repository using the following command 


```sh
git clone https://github.com/dmaciel123/GlobalSecchiLandsat
```

After that, cd to your MDN folder and install the requirements based on the requirements.txt file. 

``` sh
pip install -r .\requirements.txt
```

## Running the MDN algorithm for in situ data

Three Python scripts are provided to the user to run the MDN algorithm to Landsat-5/TM, Landsat-7/ETM+ and Landsat-8-9/OLI in situ simulated Remote Sensing Reflectance. To run these scripts, open the selected one (e.g., MDN Application TM.py) and change the input data to your dataset. See the examples provided for each sensor. 

## Running the MDN algorithm for Landsat satellite data.

An example is provided to run the MDN algorithm for Landsat-9/OLI data from Chesapeake Bay (Maryland, United States). Input data for this script is the .NETCDF file obtained from the ACOLITE atmospheric correction method, and the .TIF Rrs file obtained as output from ACOLITE. TIF file is used to convert the .NETCDF to a more GIS familar .TIF format. 



