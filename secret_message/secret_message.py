import os


def rename_files():
     files_list = os.listdir('/Users/minageorge/workSpaces/python/udacity/secret_message/assets')
     os.chdir('/Users/minageorge/workSpaces/python/udacity/secret_message/assets')
     for file_name in files_list:
         os.rename(file_name,file_name.translate(None,"0123456789"))
     

rename_files()    