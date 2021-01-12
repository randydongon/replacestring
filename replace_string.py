from os import listdir
from os.path import isfile, join
import sys
import os
import magic

# pip install python-magic

sys.dont_write_bytecode = True

args = []
try:
    args = sys.argv[:]   
        
    
except Exception as e:
    print(e)
    exit()


p = "/"

def replacestring(main, source, dist):
    path = main+p
    # confirm = input(f"This will replace file content with word '{source}' to '{dist}':\npress y to proceed x to exit: ")
    # if confirm == 'y':
    
    if os.path.exists(main):
        fileonly = [f for f in listdir(path) if isfile(join(path, f))] #list files only from main directory
        if len(fileonly) > 0:
            
                executereplace(path, fileonly, source, dist)     
                
        
        listfolder = [f for f in listdir(path) if os.path.isdir(path+f)] # list all sub directories

        if len(listfolder) > 0:
            for item in listfolder:
                fileonly = [f for f in listdir(path+item) if isfile(join(path+item, f))]

                newpath = path+item+"/" 
                executereplace(newpath, fileonly, source, dist)      
        
    else:
        print("path doesn't exists ", path)


def executereplace(path, fileonly, source, dist):
    
    for txt in fileonly:
        ex = magic.from_file(path+txt, mime=True).split('/')
        x, y = ex
        if y == 'plain' or y == 'txt' or y == 'x-java':
            with open(path+txt, 'rt') as file:
                                
                data = file.read()
                # print(data)
                data = data.replace(source.encode('utf-8').decode('utf8'), dist.encode('utf-8').decode('utf8'))
                file.close()
                with open(path+txt, 'wt') as file:
                    file.write(data)
                    file.close()  
    

def checkarguments():
    if len(args) < 4 or len(args)> 4:
        print(f"Replace string takes 3 arguments, {len(args)-1} were given")
        print(args[1:])
        return
    
    m, s, d = args[1:]
    replacestring(m, s, d)


checkarguments()

