import os

class node():
    def __init__(self, path, children):
        self.path = input("enter your path")
        self.children = os.listdir(self.path)
    
    def display

