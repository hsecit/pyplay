from tkinter import *
from Solution import HashTag

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hashtags = HashTag()
        self.trend = LabelFrame(self,text="trend",padx=20,pady=20)
        self.trend.pack()
        for element in self.hashtags.topten_tags():
            Label(self.trend,text=element,pady=10).pack()
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    # def post_widget(self):
    #     listbox = Listbox(self,
    #               activestyle = 'dotbox', 
    #               font = "Helvetica")
    #     for post in self.hashtags.show_bytag('#follow4follow'):
                                              


    def say_hi(self):
        print("hi there, everyone!")

root = Tk()
app = Application(master=root)
app.mainloop()