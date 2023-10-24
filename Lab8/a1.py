from tkinter import *
import random


Questions = ["In a website browser address bar, what does “www” stand for?",
             "What is the atomic number of Hydrogen?",
             "Which African country was formerly known as Abyssinia?",
             "What is the largest internal organ in the human body?"]
options = [["wide world web", "world wide web", "world web wide"],
           ["1","2","3"],
           ["Kenya","Egypt","Ethiopia"],
           ["Lungs","Heart","Liver"]]
answer = ["world wide web","1","Ethiopia","Liver"]
num = random.randrange(0,len(Questions))

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master, height=300,width=600)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.text_Label = Label(self,text="Welcome to the Quiz!").grid()
        self.text_Label = Label(self,text=Questions[num]).grid()
        global var
        var = StringVar()
        self.R1 = Radiobutton(self, text=options[num][0], variable=var, value=options[num][0]).grid()
        self.R2 = Radiobutton(self, text=options[num][1], variable=var, value=options[num][1]).grid()
        self.R3 = Radiobutton(self, text=options[num][2], variable=var, value=options[num][2]).grid()
        var.set(1)
        self.submit = Button(self, text="Submit", command = self.submit).grid()
        
    def submit(self):
        opt = var.get()
        print(opt)
        if(opt == answer[num]):
            self.text_Label = Label(self,text="Correct Answer!").grid()
        else:
            self.text_Label = Label(self,text="Wrong Answer!").grid()
        
    
def main():
    app = Application()
    app.mainloop()
    
if __name__ == '__main__':
    main()