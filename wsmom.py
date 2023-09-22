try:
    import pycdlib
except ModuleNotFoundError:
    print("Please ensure Pycdlib is installed.")
    exit(1)
import os #Library for OS functions
import subprocess #Library for running commands

pwd = os.getcwd() #Get the present working directory

#Create needed folders if they don't exist, I can probably simplify this later, but it works for now
for required_folders in ["usb_files", ".the_curtain"]:
    if not os.path.exists(os.path.join(pwd, required_folders)):
        os.makedirs(os.path.join(pwd, required_folders))
usb_files = f"{pwd}/usb_files"

#List what ISO files are in pwd and ask user to select one
print("\nISO images found:")
for iso_file in os.listdir(os.path.join(pwd)):
    if iso_file.endswith(".iso"):
        print(iso_file)
print("\n")
#Ask user to select an iso file
path_to_iso = os.path.join(pwd, input("Enter the name of the ISO file you want to use: \n"))

iso = pycdlib.PyCdlib() #Create the PyCdlib object
iso.open(path_to_iso) #Open the ISO file
print(f"\nContinuing with: {path_to_iso}") #A lil feedback to terminal

#Walk the iso and get the files and directories
for path, dirlist, files in iso.walk(udf_path = '/'): 
    
    #Create the directories
    for directory in dirlist:
        local_dir_path = os.path.join(f"{usb_files}{path}", directory)
        if not os.path.exists(local_dir_path):
            os.mkdir(local_dir_path)
    
    #Copy the files
    for file in files:
        full_path = os.path.join(path, file)
        if file.endswith("install.wim"): #passes the cmd to use wimlib on the .wim files
            
            print(f"Reticulating splines: {path_to_iso}{full_path}") #A lil feedback to terminal
            temp_wim_path = os.path.join(pwd, ".the_curtain", "temp_install.wim")
            iso.get_file_from_iso(local_path = temp_wim_path, udf_path=full_path)
            
            #Splits install.wim into 3800MB chunks and moves to usb_files/sources
            output_swm_path = os.path.join(usb_files, "sources", "install.swm")
            command = ['wimlib-imagex', 'split', temp_wim_path, output_swm_path, str(3800)]
            subprocess.run(command, capture_output=True, text=True)
            os.remove(temp_wim_path)
        else:
            iso.get_file_from_iso(local_path=os.path.join(
                f"{usb_files}{path}", file), udf_path=full_path)
    
iso.close() #Close the ISO file
print("Copy complete. Your files are in the usb_files directory.")
