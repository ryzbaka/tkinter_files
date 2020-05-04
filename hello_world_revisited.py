import tkinter as tk

class HelloWorld:
    def __init__(self,master):
        self.label=tk.Label(master=master,text='Hello Tkinter')
        self.label.grid(row=0,column=0,columnspan=2)#columnspan denotes the number of columns this widget will take up.

        self.texas_button=tk.Button(master=master,text="Texas",command=self.texas_hello).grid(row=1,column=0)
        self.hawaii_button=tk.Button(master=master,text='Hawaii',command=self.hawaii_hello).grid(row=1,column=1)

    def texas_hello(self):
        self.label.config(text="Howdy, Tkinter")
    
    def hawaii_hello(self):
        self.label.config(text="Hola, Tkinter")

def main():
    root=tk.Tk()
    app=HelloWorld(root)
    root.mainloop()

if __name__=='__main__':
    main()