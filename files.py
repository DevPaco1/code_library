import os
import json

def create_file(file_name: str, content: list | dict = None):

    mode = "w" if content else "x"

    try:
        file = open(file_name, mode)

    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        raise OSError(f"You do not hav permisson to create '{file_name}'") from error

    if content:
        content_json = json.dumps(content)
        file.write(content_json)

    file.close()


def modify_file(file_name: str, content: list | dict, overwrite: bool =False):

    if not isinstance(content, list|dict) or content == "":
        raise ValueError("'content' argument must be specified")
    
    content_json = json.dumps(content)

    if overwrite == True:
        file = open(file_name,"w")
        file.write(content_json)
        file.close()
    else:
        file = open(file_name,"a")
        file.write(content_json)
        file.close()

def read(file_name: str):
    if not os.path.exists(file_name):
        raise FileNotFoundError(F'File {file_name} was not found')
    
    file = open(file_name)
    content = json.load(file)
    file.close()
    return content
