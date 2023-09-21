try:
    import pycdlib
except ModuleNotFoundError:
    print("Please ensure Pycdlib is installed.")
    exit(1)
import os #Library for OS functions
import subprocess #Library for running commands

iso = pycdlib.PyCdlib() #Create the PyCdlib object
pwd = os.getcwd() #Get the current working directory
path_to_iso = f"{pwd}/Win11_22H2_English_x64v2.iso" #Hardcoded for now
usb_files = f"{pwd}/usb_files" #Requires folder to exist, currently

iso.open(path_to_iso) #Open the ISO file
print(path_to_iso) #A lil feedback to terminal

#walk the iso and get the files and directories
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
            print(f"{path_to_iso}{full_path}") #A lil feedback to terminal
            temp_wim_path = os.path.join(pwd, "the_curtain", "temp_install.wim")
            iso.get_file_from_iso(local_path = temp_wim_path, udf_path=full_path)

            output_swm_path = os.path.join(usb_files, "sources", "install.swm")
            #Splits install.wim into 3800MB chunks and moves to usb_files/sources
            command = ['wimlib-imagex', 'split', temp_wim_path, output_swm_path, str(3800)]
            subprocess.run(command, capture_output=True, text=True)
            os.remove(temp_wim_path)
        else:
            iso.get_file_from_iso(local_path=os.path.join(
                f"{usb_files}{path}", file), udf_path=full_path)
    
iso.close() #Close the ISO file
print("Copy complete. Your files are in the usb_files directory.")