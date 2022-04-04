# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import filedialog, Tk, mainloop
from tkinter.ttk import *
import os
from VennDigram_on_Deseq2_result import *

def Simpletoggle():
    if verbosity_button.config('text')[-1] == 'UNIQUE':
        verbosity_button.config(text='CORE')
    else:
        verbosity_button.config(text='UNIQUE')

def get_names_inputs_and_start(path_list):
    names_files = name_input.get()
    names_files = names_files.split(",")

    my_text = verbosity_button.cget('text')
    if my_text == 'CORE':
        Run_Program(path_list, names_files, True)
    else:
        Run_Program(path_list, names_files, False)

def get_input(nb_DESeq2):
    path_list = []
    for i in range(int(nb_DESeq2)):

        filepath = filedialog.askopenfilename(initialdir=os.path.dirname(os.path.abspath(__file__)), title="Select file",
                                                   filetypes=(("tabular files", "*.tabular"), ("text files", "*.txt"), ("all files", "*.*")))

        path_list.append(str(filepath))
        Label(window, text="The File n°"+ str(i+1) +" is located at : " + str(filepath), font=('Aerial 11')).pack()
    btn1 = Button(window, text="Start Venn diagrams", command=lambda : get_names_inputs_and_start(path_list))
    btn1.pack()

def openNewWindow():
    nb_DESeq2 = float(nb_input.get())
    print(nb_DESeq2)
    if nb_DESeq2 > 0 & nb_DESeq2.is_integer():
        btn.destroy()
        get_input(nb_DESeq2)

# creates a Tk() object
window = Tk()

# sets the geometry of main
# root window
window.geometry("800x400")

#Label text
label = Label(window, text="This tool is used to create venn diagrams from DESeq2 outputs. \n"
                           "The outputs must be filtered beforehand on their p-values or p-values adjusted.\n \n"
                           "How many input do you have ?")
label.pack(padx=0, pady=14)

nb_input = Entry(window)
nb_input.pack()

Label(window, text="Enter names for this files: \n"
                   "like : file_name_1, file_name_2...", font=('Aerial 11')).pack(padx=0, pady=14)
name_input = Entry(window)
name_input.pack()

Label(window, text = "Write file for the unique-genome or core-genome").pack()
verbosity_button = Button(text="CORE", width=10, command=Simpletoggle)
verbosity_button.pack(pady=10)

Label(window, text = "Run, please input the files one by one !").pack()
btn = Button(window, text="Next step", command=openNewWindow)
btn.pack(padx=0, pady=14)

# mainloop, runs infinitely
mainloop()