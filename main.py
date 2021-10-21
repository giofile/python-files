__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os 
#  info OS module  - The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality. ... path* modules include many functions to interact with the file system.

import shutil 
 # info shutil module  - The shutil module helps you automate copying files and directories. This saves the steps of opening, reading, writing and closing files when there is no actual processing. It is a utility module which can be used to accomplish tasks, such as: copying, moving, or removing directory trees

# import zipfile, achteraf niet nodig, maar kon wel
# info zipfile module -  This module provides tools to create, read, write, append, and list a ZIP file // achteraf niet nodig , maar kon wel
# naslag en voorbeeld --> https://www.geeksforgeeks.org/working-zip-files-python/

zip_files = 'data.zip'  
#  variabel declareerd voor het zoeken van juiste password in 'data.zip'


# opdracht 1 clean_cache
# python string join, voorbeelden --> https://www.w3schools.com/python/ref_string_join.asp
# info over __file__  --> https: // stackoverflow.com/questions/9271464/what-does-the-file-variable-mean-do
# B = os.path.dirname(os.path.realpath(__file__))
# B is the canonicalised (?) directory where the program resides.

basic_path = os.path.dirname(os.path.realpath(__file__))
cache_path = os.path.join(basic_path, 'cache')

# doel van 'clean_cache' functie, om te kijken of folder 'cache bestaat', als deze er is, dan gegevens uit cache folder legen/ als niet bestaat word een nieuwe lege cache folder aangemaakt
# https://stackoverflow.com/questions/10873364/shutil-rmtree-clarification
# shutil.rmtree --> removing directory path
# chdir = change directory / mkdir = make a new directory

def clean_cache():
    os.chdir(basic_path)
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir(cache_path)


# opdract 2 cache_zip
# hierbij de zipfile uitpakken en verplaatsen naar de nieuwe lege cache folder
# shutil.unpack_archive() method in Python is used to unpack an archive file.
# naslag--> https: // www.geeksforgeeks.org/working-zip-files-python/ 
# andere methode --> with ZipFile(file_name, 'r') as zip: zip.extractall(nieuw leeg locatie) /  "the 'r' stands for read-mode" 
# (zie ook --> https://www.geeksforgeeks.org/working-zip-files-python/)

def cache_zip(zip_files, cache_path):
    shutil.unpack_archive(zip_files, cache_path)


# opdracht 3 cache_files
# creëren van een list van files voor de cache_path
# The file paths should be specified in absolute terms ----> use "os.path.abspath()"
# os.scandir() --> The os.scandir() method in Python is used to get an iterator of os.DirEntry objects corresponding to the entries in the directory given by the specified path.
#  os.path.abspath() ---> returns the absolute pathname to the path passed as a parameter to this function.
# naslag : https://www.geeksforgeeks.org/python-os-scandir-method/
# abspath voorbeelden --> https://www.geeksforgeeks.org/python-os-path-abspath-method-with-example/

def cached_files():
    cached_list = []
    for query in os.scandir(cache_path):
        cached_list.append(os.path.abspath(query))
    return cached_list


# opdracht 4 find_password
# zoeken in de teksten van de cached_list naar juiste password
# with statement in Python--> https: // stackoverflow.com/questions/32375864/purpose-of-including-r-in-the-open-function
# naslag with open() statement --> https: // cmdlinetips.com/2016/01/opening-a-file-in-python-using-with-statement/
# The access modes available for the open() function are as follows: r : Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function. rb : Opens the file as read-only in binary format and starts reading from the beginning of the file
# naslag en voorbeelden .split method --> https://www.w3schools.com/python/ref_string_split.asp

def find_password(cached_list):
    for element in cached_list:
        with open(element,'r') as search_file:
            for line in search_file:
                if 'password' in line:
                    searched_password = line.split()[1]
    return searched_password


if __name__ == '__main__':
    clean_cache()
    cache_zip(zip_files, cache_path)
    # print(cached_files())
    cached_files = cached_files()
    print(find_password(cached_files))
