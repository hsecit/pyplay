#!/usr/bin/python

from termcolor import colored
import operator
import itertools
# ui
from tkinter import *

#ui
def init_desktop (top_ten):
    win = Tk()
    # some logic
    l = LabelFrame(win, text="->Trend hashtags<-", padx=20, pady=20)
    l.pack(fill="both", expand="yes")
    for el in top_ten:
        lab = Label(l,text=el)
        lab.pack()
    tag_lab = Label(win,text="select posts by tag :")
    tag_id = Entry(win)
    tag_lab.pack()
    tag_id.pack()

    query = Button(win,text="query")
    query.pack()


    win.mainloop()

# filter hashes => return list that contains only hashtags
def filter_hashtags(_list):
    hash_tags = []
    for el in _list:
        if el != '':
            if str(el)[0] == '#':
                hash_tags.append(el)
    return hash_tags


def count_hashtag_occurrence(_list):
    _list = filter_hashtags(_list)
    # store element that already counted
    counted = []
    # {element : number_occurrence}
    tag_count = {}
    for el in _list:
        count = 0
        if el not in counted :
            for x in _list :
                if x == el :
                    count+=1
            counted.append(el)
            tag_count[el] = count
    return tag_count


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def _max(_dict):
    max_key = ""
    m = 0
    for key in _dict:
        if int(_dict[key]) > m :
            m = int(_dict[key])
            max_key = key
    return max_key,m
# return the top ten hahstags in tweets
def top_ten(_dict):
    sort_ = sorted(_dict.items(),key=operator.itemgetter(1))
    return sort_[-10:]

def show_post_bytag(posts,tag) :
    posts_contains_tag = []
    for post in posts:
        if tag in post.split(" "):
            post = highlight_tag(post,tag)
            posts_contains_tag.append(post)
    return posts_contains_tag

def highlight_tag(post,tag):
    htag = colored(tag,'green','on_red')
    post_s = post.split(" ")
    for i,el in enumerate(post_s):
        if el == tag :
            post_s[i] = htag
    return "".join(post_s)

with open("data",'r') as f :
       lines = f.readlines()
       l = lines[1].split(" ")
       text = ""
       for el in lines:
           if el != "\n" and is_number(el) == False:
               text += el
       count_dict = count_hashtag_occurrence(text.split(" "))

       mx = _max(count_dict)
       top = top_ten(count_dict)
       top = top[::-1]

       # call ui components
       init_desktop(top)

       print(colored(mx,'red'))
       print(colored("\t -> top hashtags <- \n",'green'))
       tmp = 0
       for el in top :
           tmp+=1
           print (colored(f"\t{tmp}- {el}","blue"))

       # show posts by tag
       id_tag = int(input("choose hashtag: "))
       tag = top[id_tag-1][0]
       posts_bytag = show_post_bytag(lines,tag)
       for p in posts_bytag:
           print(colored(f"\n{p}",'white'))




		
