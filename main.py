
import files
files.create_file("archivo.txt",{"carlos":"rivera"})
files.update("archivo.txt",{"francisco":"castañeda", "otro":"dato"}, overwrite=True)
files.update("archivo.txt",['pablo','pedro','paco'])
files.read("archivo.txt")