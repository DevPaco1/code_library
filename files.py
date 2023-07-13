def create_file(file_name, content = None):
    if content != None:
        file = open(file_name,"w")
        file.write(content)
        file.close()
    else:
        file = open(file_name,"x")
        file.close()



def modify_file(file_name, content, overwrite=False):
    if overwrite == True:
        file = open(file_name,"w")
        file.write(content)
        file.close()
    else:
        file = open(file_name,"a")
        file.write(content)
        file.close()