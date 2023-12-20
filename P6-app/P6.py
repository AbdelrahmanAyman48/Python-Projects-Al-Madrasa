import tkinter as tk
from tkinter import *

# window = tk.Tk() #.mainloop() # Use 'Tk()' instead of 'TK()'
# window.title('gggggg')

# widget1 = tk.Label(text='start\nddff')
# widget = tk.Label(text='0')
# widget1.pack() # widget.grid(x,y) , widget.place()
# widget.pack() # widget.grid(x,y) , widget.place()
# def myfun():
#     widget['text']= 1+ int(widget['text'])
# button = tk.Button(text='here',command=myfun)
# button.pack()
# window.mainloop() 

#########################################
# root = tk.Tk()
# root.title("Home")
# # root.geometry(800,600)
# def btn_print():
#     name=txt1.get("1.0", "end")
#     lb1["text"]=name
#     lb1["bg"]="black"
# txt1= Text(root, width="50",height="5", bg="black", fg="white", font="40")
# btn1= Button(root, command=btn_print, text="Click Me", width="10",height="2", font="30", bg="black", fg="white")
# lb1= Label(root, width="50",height="5", bg="red", fg="white", font="40")
# lb1["text"]="Click Me"
# txt1.pack()
# btn1.pack()
# lb1.pack()
# root.mainloop()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# root = tk.Tk()
# root.title("Home")
# root.geometry('500x400')
# def btn_print():
#     name=txt1.get("1.0", "end")
#     lb1["text"]=name
#     lb1["bg"]="black"
# frame = Frame(root, bg='pink')
# txt1= Text(frame, width="50",height="5", bg="black", fg="white", font="40")
# btn1= Button(frame, command=btn_print, text="Click Me", width="10",height="2", font="30", bg="black", fg="white")
# lb1= Label(frame, width="50",height="5", bg="red", fg="white", font="40")
# lb1["text"]="Click Me"
# frame.pack()
# txt1.pack()
# btn1.pack()
# lb1.pack()
# root.mainloop()
####################################
# root = tk.Tk()
# root.title("Home")
# root.geometry('500x400')
# fr1=Frame (root)
# btn1=Button(fr1, text="Button1") 
# fr2=Frame (root)
# btn2=Button(fr2, text="Button2")
# fr3=Frame (root)
# btn3=Button(fr3, text="Button3")
# fr4=Frame (root)
# btn4=Button(fr4, text="Button4")
# btn5=Button(root, text="Button5")

# btn1.pack()
# btn2.pack()
# btn3.pack()
# btn4.pack()
# btn5.pack()
# fr1.pack(side=TOP)
# fr2.pack(side=BOTTOM)
# fr3.pack(side=LEFT)
# fr4.pack(side=RIGHT)
# £4444444444444444444444
# fr1.grid(row=0,column=0)
# fr2.grid(row=0,column=1)
# fr3.grid(row=1,column=0)
# fr4.grid(row=2,column=1)
# 3esrdtfghjhhggfv
# btn5.place(anchor=NW,width=200,height=200,bordermode=INSIDE)
# root.mainloop()
#5555555555555555555555

# root = tk.Tk()
# root.title("Home")
# root.geometry('800x600')
# Lbfr1=LabelFrame (root, text="This is a Label Frame")
# Lbfr1.pack(expand="yes", fill=BOTH)
# lb1=Label(Lbfr1, text="This is a Label")
# lb1.pack()
# root.mainloop()
##################################3
root = tk.Tk()
root.title("Home")
root.geometry('800x600')
def hello():
    print("Hello World")
checkbtn=Checkbutton(root, text="Auto Save", font="14", command=hello, state=DISABLED, onvalue='1')
checkbtn.pack()
rdbtn1=Radiobutton(root,text="Male", value=1)
rdbtn2=Radiobutton(root,text="FeMale", value=2)
rdbtn1.pack()
rdbtn2.pack()

root.mainloop()

#https://www.youtube.com/watch?v=Co8iA-wmOtw&list=PLhiFu-f80eo_JY4sO_XOB0khGVck2PUkJ&index=15&ab_channel=%D8%AA%D9%83%D9%86%D9%88U 