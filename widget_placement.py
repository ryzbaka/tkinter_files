import tkinter as tk
#tk geometry manager to place the widget in the best possible place.
#master widgets are reponsible for the grometric placement of their
#slave widgets and are organisational contatiners.

# the pack() geometry manager is used to specify 
# which edge of the parent a widget should stick to
root=tk.Tk()
label1=tk.Label(master=root,text='left')
label2=tk.Label(master=root,text='right')
label1.pack(side='left')
label2.pack(side='right')
# the grid geometry manager is used to split the master widget's area
# into a table and uses rows and columns to specify the slave widget's position.
#button.grid(row=0,column=1)
#the place geometry manager is for placing widgets using x y pixel coordinates.

#use the same geometry manager within a master widget.