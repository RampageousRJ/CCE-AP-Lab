from tkinter import *


class Application(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.count_val = 0
        self.placeholder = ""
        self.create_widgets()
        self.eq_pressed = False
        
    def create_widgets(self):
        self.text_label = Label(self, text=f"{self.count_val}")
        self.text_label.grid(row = 0,column = 0, columnspan = 5)
        self.button_0 = Button(self, text = "0", command=lambda: self.insertNumber(0), height = 3, width = 6).grid(row = 4, column = 1)
        self.button_1 = Button(self, text = "1", command=lambda: self.insertNumber(1), height = 3, width = 6).grid(row = 3, column = 0)
        self.button_2 = Button(self, text = "2", command=lambda: self.insertNumber(2), height = 3, width = 6).grid(row = 3, column = 1)
        self.button_3 = Button(self, text = "3", command=lambda: self.insertNumber(3), height = 3, width = 6).grid(row = 3, column = 2)
        self.button_4 = Button(self, text = "4", command=lambda: self.insertNumber(4), height = 3, width = 6).grid(row = 2, column = 0)
        self.button_5 = Button(self, text = "5", command=lambda: self.insertNumber(5), height = 3, width = 6).grid(row = 2, column = 1)        
        self.button_6 = Button(self, text = "6", command=lambda: self.insertNumber(6), height = 3, width = 6).grid(row = 2, column = 2)        
        self.button_7 = Button(self, text = "7", command=lambda: self.insertNumber(7), height = 3, width = 6).grid(row = 1, column = 0)        
        self.button_8 = Button(self, text = "8", command=lambda: self.insertNumber(8), height = 3, width = 6).grid(row = 1, column = 1)        
        self.button_9 = Button(self, text = "9", command=lambda: self.insertNumber(9), height = 3, width = 6).grid(row = 1, column = 2)        
        self.button_add = Button(self, text = "+", command =lambda: self.function("+"), height = 3, width= 6).grid(row = 1, column = 3)        
        self.button_sub = Button(self, text = "-", command =lambda: self.function("-"), height = 3, width= 6).grid(row = 2, column = 3)        
        self.button_mult = Button(self, text = "*", command =lambda: self.function("*"), height = 3, width= 6).grid(row = 3, column = 3)        
        self.button_div = Button(self, text = "/", command =lambda: self.function("/"), height = 3, width= 6).grid(row = 4, column = 3)        
        self.button_eq = Button(self, text = "=", command = self.equals, height = 9, width= 6).grid(row = 1, column = 4, rowspan = 3)        
        self.button_AC = Button(self, text = "AC", command = self.clear, height = 3, width= 6).grid(row = 4, column = 2)        
        self.button_del = Button(self, text = "Delete", command = self.delete, height = 3, width= 6).grid(row = 4, column = 0)
            
    def insertNumber(self, value):
        if self.eq_pressed:
            self.placeholder = ""
            self.clear()
            self.eq_pressed = False
        self.placeholder += f"{value}"
        self.text_label = Label(self, text=self.placeholder)
        self.text_label.grid(row = 0,column = 0, columnspan = 5)
        
    def function(self, operator):
        self.placeholder = self.placeholder+f"{operator}"
        self.text_label = Label(self, text=self.placeholder)
        self.text_label.grid(row = 0,column = 0, columnspan = 5)
        
    def equals(self):
        operator = ""
        for i in range(len(self.placeholder)):
            try:
                int(self.placeholder[i])
            except:
                operator = self.placeholder[i]
                mid = i
                
        if operator == "+":
            self.placeholder = str(int(self.placeholder[:mid]) + int(self.placeholder[mid+1:]))
            self.clear()
            self.text_label = Label(self, text=self.placeholder)
            self.text_label.grid(row = 0,column = 0, columnspan = 5)
        elif operator == "-":
            self.placeholder = str(int(self.placeholder[:mid]) - int(self.placeholder[mid+1:]))
            self.clear()
            self.text_label = Label(self, text=self.placeholder)
            self.text_label.grid(row = 0,column = 0, columnspan = 5)
        elif operator == "*":
            self.placeholder = str(int(self.placeholder[:mid]) * int(self.placeholder[mid+1:]))
            self.clear()
            self.text_label = Label(self, text=self.placeholder)
            self.text_label.grid(row = 0,column = 0, columnspan = 5)
        elif operator == "/":
            self.placeholder = str(int(self.placeholder[:mid]) / int(self.placeholder[mid+1:]))
            self.clear()
            self.text_label = Label(self, text=self.placeholder)
            self.text_label.grid(row = 0,column = 0, columnspan = 5)
        
        self.eq_pressed = True
            
    def clear(self):
        self.text_label = Label(self, text="                                                ")
        self.text_label.grid(row = 0,column = 0, columnspan = 5)
            
    def delete(self):
        self.placeholder = self.placeholder[:len(self.placeholder)-1]
        self.text_label = Label(self, text=self.placeholder)
        self.text_label.grid(row = 0,column = 0, columnspan = 5)

def main():     
    app = Application()
    app.mainloop()
    
if __name__ == '__main__':
    main()