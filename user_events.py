#tkinter uses event handling to deal with events.
# every event has to be binded to a handler function to repond to that event.
#the root.mainloop() function causes the program to enter an event loop where the program
#waits for an event to execute the appropriate handler function.

#interactive widgets that produce events(like buttons) 
# are handled using command callbacks.

#widgets that dont have command callbacks can still binded to and handler using the bind() method.
# the event loop cannot handle multiple events at the same time
import tkinter as tk

root=tk.Tk()
label=tk.Label(master=root,text="Button not clicked")
label.grid(row=0,column=0,columnspan=2)
button=tk.Button(master=root,text="Click me!",command=lambda : label.config(text="Button clicked")).grid(row=1,column=0)
root.mainloop()