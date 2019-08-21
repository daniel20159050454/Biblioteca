import pyrebase
import socket
import json
import os

firebaseConfig = {
            'apiKey': "AIzaSyD6NeWtwGK0yeDfG6C1W-ZesVnjNFlVnSw",
            'authDomain': "biblioteca-b2317.firebaseapp.com",
            'databaseURL': "https://biblioteca-b2317.firebaseio.com",
            'projectId': "biblioteca-b2317",
            'storageBucket': "",
            'messagingSenderId': "1080656799035",
            'appId': "1:1080656799035:web:0064e0d7e84c5e7d"}


class firebase:
    def __init__(self, config):
        self._firebase = pyrebase.initialize_app(config)
        self._db = self._firebase.database()
        self._auth = self._firebase.auth()
        self.books = []
    

    def addLivro(self, livro):
        try:
            self._db.child('livros/'+livro['isbn']).set(livro)
            return True
        except Exception as e:
            print(e)
            return False
    
    def remover_Livro(self, result):
        self._db.child('livros/'+str(result)).remove()

    def buscaFirebase(self):
        dados = self._db.child('livros/').push()


