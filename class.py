import files
import json
import os


class User:
    def __init__(self, first_name, last_name, username="", password="", email=""):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.dict = {}

 
    def save(self):
        self.dict.update(
            {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "username": self.username,
                "password": self.password,
                "email": self.email,
            }
        )

        if not os.path.exists("users.json"):
            files.create("users.json", self.dict)
        else:
            files.update("users.json", self.dict)


class Article:
    def __init__(self, title, content, status="", image="", created_by=""):
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by
        self.dict = {}

    def save(self):
        self.dict.update(
            {
                "title": self.title,
                "content": self.content,
                "status": self.status,
                "image": self.image,
                "created_by": self.created_by,
            }
        )

        if not os.path.exists("posts.json"):
            files.create("posts.json", self.dict)
        else:
            files.update("posts.json", self.dict)


class Comments:
    def __init__(self, content, created_by="", article=""):
        self.content = content
        self.created_by = created_by
        self.article = article
        self.dict = {}

    def save(self):
        self.dict.update(
            {
                "content": self.content,
                "created_by": self.created_by,
                "article": self.article,
            }
        )

        if not os.path.exists("articles.json"):
            files.create("articles.json", self.dict)
        else:
            files.update("articles.json", self.dict)


def get_all_users(lista_diccionario):
    pass

def constructor_json(archivo: str):
    content = files.read(archivo)
    for us in content:
        user = User(**us)
        print(user.__dict__)

def decorator1(func):
    def wrapper():
           func()
    if not os.path.exists("usuarios.log"):
         files.create("articles.json", "se ha creado el primer usuario nuevo")
    else:
        files.update("articles.json", "se agrego un nuevo usuario")
    return wrapper

def decorador2(func):
    def wrapper():
        func()
        print("se ha guardado una nueva entidad")
        
    return wrapper
    


user = User("paco", "castañeda")
@decorator1
@decorador2
user.save()


'''
user = User("isai", "rivera")
user.save()
user = User("rosa", "estrada")
user.save()
user = User("emanuel", "bustos")
user.save()'''
'''article1 = Article('El principito', 'En un lugar muy lejano...')
article1.save()
print(article1.__dict__)

coment1 = Comments('JAJAJA')
coment1.save()
print(coment1.__dict__)'''

constructor_json('users.json')