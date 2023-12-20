from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from text_editor_style import Style

class Action:
    def __init__(self, root):
        self.root = root
        self.object_style = Style(self.root)
        self.txt_edit = self.object_style.txt_edit  # Access txt_edit from Style
        self.object_style.btn_open.config(command=self.open_file)
        self.object_style.btn_save.config(command=self.save_file)  # Bind save_file to the Save button

    def open_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not filepath:
            return
# This part utilizes the askopenfilename method from the filedialog module in tkinter. 
# It opens a file dialog box prompting the user to select a file to open.
# The file types available for selection are specified in the filetypes parameter. 
# In this case, it allows the user to choose text files (*.txt) or all files (*.*).
# If the user cancels the file dialog (by not selecting a file or clicking Cancel), the method returns, and nothing further happens.
        self.txt_edit.delete(1.0, tk.END)
# This line clears the content of the text editor (txt_edit) by deleting all the text content starting from the first character (1.0) to the end.
        with open(filepath, "r") as input_file:
            text = input_file.read()
# ..............................................................................................................................
            # with open("example.txt", "r") as file_object:
                # content = file_object.read()
    # Perform operations on the file content
    
# File is automatically closed after the block exits
# Code continues here without needing to explicitly close the file
# In summary, the with statement, when used in file handling, simplifies and ensures proper management of file 
# resources by automatically closing the file after its intended usage, making the code cleaner and more reliable.
# ...................................................................................................................................
            self.txt_edit.insert(tk.END, text)
# This part opens the selected file using the obtained file path (filepath). 
# It reads the content of the file (input_file.read()) and stores it in the variable text. 
# Then, it inserts the content (text) into the text editor (txt_edit) starting from the end (tk.END). 
# This means the content of the opened file will be displayed in the text editor.     
# with open(filepath, "r") as input_file:
# open(filepath, "r") is used to open a file in read mode ("r") specified by the file path filepath.
# as input_file assigns the file object returned by open() to the variable input_file.
# The with statement is used here to ensure that the file is properly closed after its suite finishes executing. It's a context manager that handles the opening and closing of files gracefully.
# text = input_file.read()
# input_file.read() reads the entire contents of the opened file and assigns it to the variable text. This method reads the file's content as a string.
# self.txt_edit.insert(tk.END, text)
# self.txt_edit refers to the text widget previously created in the Style class. It's an instance variable holding the text editor widget.
# insert(tk.END, text) is a method of the text widget (self.txt_edit). It is used to insert text at a specified position in the widget.
# tk.END represents the end of the text widget. So, the text obtained from the file is inserted at the end of the text editor.
        self.root.title(f'AlmdrasaTextEditor - {filepath}')
# Finally, it sets the title of the root window (self.root) to include the name of the opened file (filepath) as part of the title. 
# This way, the window title reflects the name of the file being edited.
# Overall, this open_file method allows the user to select a file to open, clears the existing content in the text editor, 
# loads the content of the selected file into the text editor, and updates the window title to reflect the opened file's name.
    def save_file(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not filepath:
            return

        with open(filepath, "w") as output_file:
            text = self.txt_edit.get(1.0, tk.END)
            output_file.write(text)
        
        self.root.title(f'AlmdrasaTextEditor - {filepath}')


        
if __name__ == '__main__':
    app = Tk()
    main_class = Action(app) 
    app.mainloop()
    