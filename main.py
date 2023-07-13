
import files
files.create_file("archivo.txt", "esta es la primer linea")
files.modify_file("archivo.txt","esta es una linea remplazada", overwrite=True)
files.modify_file("archivo.txt",'esta linea es adicionada')