from tkinter import *
import tkinter as tk
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename


# .......................style..................
class Style:
        def __init__(self, master): #window
                self.master = master
                self.master.title("Almdrasa Text Editor")
                self.master.rowconfigure(0, minsize=600)
                self.master.columnconfigure(1, minsize=800)
        # ........................Text box...........
                self.txt_edit = tk.Text(self.master)
                self.txt_edit.grid(column=1, row=0, sticky="nsew")
        # ........................Frame for button...........
                self.frame_buttons = tk.Frame(self.master, relief=tk.RAISED)
                self.frame_buttons.grid(column=0, row=0, sticky="ns")
        # ........................button box...........................
                self.btn_open = tk.Button(
                        self.frame_buttons, text="Open", borderwidth=0, bg='#006585'
                        )#,command=self.open_file)
                self.btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)

                self.btn_save = tk.Button(
                        self.frame_buttons, text="Save", borderwidth=0, bg='#006525'
                        )# ,command=self.save_file)
                self.btn_save.grid(column=0, row=1, sticky="ew", padx=5)
        #................wrong way of writting............
        # self.btn_open  = Button(
        #         self.frame_buttons, borderwidth=0, bg='#252525').grid(column=0, row=0, sticky="ew", padx=5, pady=5)
        # self.btn_save  = Button(
        #         self.master, borderwidth=0, bg='#252525').grid(column=0, row=1, sticky="ew", padx=5)

#..................could be used if you dont want to use "action" file /// if you want all in one file
    # def open_file(self):
    #     filepath = tk.filedialog.askopenfilename(
    #         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    #     )

    #     if not filepath:
    #         return

    #     self.txt_edit.delete(1.0, tk.END)
    #     with open(filepath, "r") as input_file:
    #         text = input_file.read()
    #         self.txt_edit.insert(tk.END, text)
        
    #     self.master.title(f'AlmdrasaTextEditor - {filepath}')
    # def save_file():
    #         filepath = tk.filedialog.asksaveasfilename(
    #             defaultextension="txt",
    #             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    #         )

    #         if not filepath:
    #             return

    #         with open(filepath, "w") as output_file:
    #             text = self.txt_edit.get(1.0, tk.END)
    #             output_file.write(text)

    #         self.master.title(f'AlmdrasaTextEditor - {filepath}')
if __name__ == "__main__":
        root = tk.Tk()
        style = Style(root)
        root.mainloop()

# .................code of the course.................
# def open_file():
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )

#     if not filepath:
#         return

#     txt_edit.delete(1.0, tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)

#     window.title(f'AlmdrasaTextEditor - {filepath}')

# def save_file():
#         filepath = asksaveasfilename(
#             defaultextension="txt",
#             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#         )

#         if not filepath:
#             return

#         with open(filepath, "w") as output_file:
#             text = txt_edit.get(1.0, tk.END)
#             output_file.write(text)
        
#         window.title(f'AlmdrasaTextEditor - {filepath}')



# btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
# btn_save = tk.Button(frame_buttons, text="Save As", command=save_file)
