
import files
files.create_file("archivo.txt",{"carlos":"rivera"})
files.modify_file("archivo.txt",{"francisco":"castañeda", "otro":"dato"}, overwrite=True)
files.modify_file("archivo.txt",['pablo','pedro','paco'])