import pycdlib
import os # Library for OS functions

iso = pycdlib.PyCdlib() # Create a PyCdlib object

path_to_iso = input("Enter the absolute path to the ISO file: ")

pwd = os.getcwd() # Get the current working directory
path_to_write = f"{pwd}/install.wim" # Path to write the file to
file_on_iso = "/sources/install.wim" # File to get from the ISO

iso.open(path_to_iso) # Open the ISO file
iso.get_file_from_iso(path_to_write, udf_path = file_on_iso) # Get the file from the ISO
iso.close() # Close the ISO file
print(f"{file_on_iso} has been extracted to {pwd}.")
