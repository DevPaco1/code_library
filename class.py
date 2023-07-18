import files
import json

class User:

    def __init__(self, first_name,last_name,username='',password='',email=''):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.dict = {}

    def save(self):
        self.dict.update({"first_name":self.first_name,
                       "last_name":self.last_name,
                       "username":self.username,
                       "password":self.password,
                       "email":self.email})
        files.create('users.json',self.dict)


class Article:

    def __init__(self,title, content, status= '', image='', created_by=''):
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by
        self.dict ={}

    def save(self):
        self.dict.update({"title":self.title,
                       "content":self.content,
                       "status":self.status,
                       "image":self.image,
                       "created_by":self.created_by})
        files.create('posts.json',self.dict)

class Comments:

    def __init__(self,content,created_by='',article=''):
        self.content = content
        self.created_by = created_by
        self.article = article
        self.dict ={}

    def save(self):
        self.dict.update({"content":self.content,
                       "created_by":self.created_by,
                       "article":self.article})
        files.create('articles.json',self.dict)


user1 = User('zoe', 'rivera')
user1.save()
print(user1.__dict__)

article1 = Article('El principito', 'En un lugar muy lejano...')
article1.save()
print(article1.__dict__)

coment1 = Comments('JAJAJA')
coment1.save()
print(coment1.__dict__)