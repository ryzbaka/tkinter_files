#each widget is a class and is anything that is part of the GUI
#The widgets exist in a heirarchy with the root window at the top
#The parent widget acts as the geometry manager
import tkinter


root=tkinter.Tk()#parent
label=tkinter.Label(master=root,text="Example widget.")
button=tkinter.Button(master=root,text="Click me!")#master refers to the parent
#just creating the widget doesn't show it on the window.
# for displaying it on the window we have to do the following:
label.pack()
button.pack()
print(button['text'])
button.config(text="changed the original text")
print(button.config())# display all configurable options
root.mainloop()