import re

class file:
    name=''
    content=''
    owner=''

    def __init__(self,name,content,owner):
        self.name=name
        self.content=content
        self.owner=owner

class dir:
    path=''
    name=''
    subdirs=[]
    files=[]

    def __init__(self,path,name,subdirs,files):
        self.name=name
        self.path=path
        self.subdirs=subdirs
        self.files=files
        


