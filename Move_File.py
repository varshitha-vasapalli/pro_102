import os 
import shutil
from_dir="C:/Users/SREE/Downloads/files"
to_dir="C:/Users/SREE/Desktop"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for i in list_of_files:
    name,ext=os.path.splitext(i)
    if ext == "":
        continue
    if ext in ['.txt', '.doc', '.docx','.pdf']:
        path1 = from_dir + '/' + i
        path2 =  to_dir + '/' + "Document_Files"
        path3 =  to_dir + '/' + "Document_Files" + '/' + i 
        if os.path.exists(path2):
            print("moving" + i + "......")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving" + i + "......")
            shutil.move(path1,path3) 
            #
       