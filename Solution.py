import operator
from tkinter import *
class HashTag:
    """docstring for HashTag"""
    def __init__(self):
        self.file = open('data','r')
        self.lines = self.file.readlines()
        self.posts = self.build()
        self.hashtags = self._filter()

    def topten_tags(self):
        occurence_dict = self.occurence()
        sort =  sorted(occurence_dict.items(),key=operator.itemgetter(1))
        ten = sort[-10          :]
        return ten[::-1]

    def show_bytag(self,tag):
        posts_with_tag = []
        for p in self.lines:
            if tag in p.split(" "):
                posts_with_tag.append(p)
        return posts_with_tag

    def occurence(self):
        counted = []
        tag_count = {}
        for el in self.hashtags :
            count = 0
            if el not in counted:
                for tag in self.hashtags:
                    if tag == el :
                        count+=1
                counted.append(el)
                tag_count[el] = count
        return tag_count



    def _filter(self):
        hashtag_list = []
        for el in self.posts.split(" "):
            if el != '':
                if el[0] == '#':
                    hashtag_list.append(el)
        return hashtag_list

    def is_number(self,el):
        try:
            int(el)
            return True
        except ValueError:
            return False 

    def build(self):
        text = ""
        lines = self.file.readlines()
        for el in lines:
            if el != "\n" and self.is_number(el) == False:
                text += el
        return text

class Application():
    """docstring for Application"""
    def __init__(self):
        pass
        
# Test

# t = HashTag()

# print(len(t.show_bytag('#follow4follow')))
# # print(t.lines)
