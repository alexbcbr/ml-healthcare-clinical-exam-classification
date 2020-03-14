#!/usr/bin/env python3

'''
MedicalApp: User Interface for Eletronic Medical Record
@author: Alex Coqueiro
@date: Feb, 2 2020
@see MedicalInvokeBreastCancerExam, MedicalInvokeDiabetesReadmission, MedicalDB, Translation.json
'''
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox

import PIL.Image 				 	#pip install pillow
import PIL.ImageTk

import MedicalDB as mdb
import MedicalInvokeBreastCancerExam as mlBreastCancer
#import MedicalInvokeDiabetesReadmission as mlDiabetes

from pyslate.pyslate import Pyslate  #pip install pyslate
from pyslate.backends.json_backend import JsonBackend

#======================
# functions
#======================
def btnCancerDiagnostic():
	img=mdb.patientData[int(patientSelected.get())]["exam_frame"]
	if (mlBreastCancer.predict_breast_cancer(img) == 0):
		tk.messagebox.showinfo(_.t('DIAGNOSTIC'),_.t('CANCER_NEGATIVE_DIANOSTIC'), icon = 'error')
	else:
		tk.messagebox.showinfo(_.t('DIAGNOSTIC'),_.t('CANCER_POSITIVE_DIANOSTIC'), icon = 'warning')
'''
def btnDiabetesDiagnostic():
	diabetes_data=mdb.patientData[int(patientSelected.get())]["patient_data"]
	if (mlDiabetes.predict_diabetes(diabetes_data) == 0):
		tk.messagebox.showinfo(_.t('DIAGNOSTIC'),_.t('DIABETES_NEGATIVE_READMISSION'), icon = 'error')
	else:
		tk.messagebox.showinfo(_.t('DIAGNOSTIC'),_.t('DIABETES_POSITIVE_READMISSION'), icon = 'warning')
'''

def cmbFindByPatientID(eventObject):
	nameEntryUI.configure(text = mdb.patientData[int(patientSelected.get())]["name"])
	insulinUI.configure(text = mdb.patientData[int(patientSelected.get())]["insulin_glyburide"])

	im = PIL.Image.open(mdb.patientData[int(patientSelected.get())]["photo"])
	photo = PIL.ImageTk.PhotoImage(im)
	photoPacientUI.configure(image=photo)
	photoPacientUI.image = photo

	imbreath = PIL.Image.open(mdb.patientData[int(patientSelected.get())]["exam_full"])
	photobreath = PIL.ImageTk.PhotoImage(imbreath)
	photobreathUI.configure(image=photobreath)
	photobreathUI.image = photobreath

def loadLogo():
	im = PIL.Image.open("logo.jpg")
	photo = PIL.ImageTk.PhotoImage(im)
	photoPacientUI.configure(image=photo)
	photoPacientUI.image = photo

def _quit():
    win.quit()      # win will exist when this function is called
    win.destroy()
    exit() 

def __init__(self):
	print("constructor")

#======================
# procedural code
#======================
_ = Pyslate("en", backend=JsonBackend("translation.json"))

win = tk.Tk()
win.title(_.t("APP_NAME"))
win.attributes("-fullscreen", True)

# ---------------------------------------------------------------
# Creating a Menu Bar
menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)   # command cmbFindByPatientID
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)
# ---------------------------------------------------------------
# Tab Control / Notebook introduced here ------------------------
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text=_.t('MENU_PATIENT'))      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text=_.t('MENU_STANDARD_PROCEDURE'))      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ---------------------------------------------------------------
    
# We are creating a container frame to hold all other widgets
patient_conditions_frame = ttk.LabelFrame(tab1)
patient_conditions_frame.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(patient_conditions_frame, text=_.t('PATIENT_ID')).grid(column=0, row=0, sticky='W')
patient = tk.StringVar()
patientSelected = ttk.Combobox(patient_conditions_frame, width=12, textvariable=patient)
patientSelected['values'] = ('10253', '8975')
patientSelected.grid(column=1, row=0, sticky='W')
        
# ---------------------------------------------------------------
# increase combobox width to longest patient
max_width  = max([len(x)for x in patientSelected['values']])
new_width = max_width
patientSelected.config(width=new_width)
patientSelected.bind("<<ComboboxSelected>>", cmbFindByPatientID)    
ENTRY_WIDTH = max_width + 3             # adjust per taste of alignment    
#==========================

#=============================================
# Adding Label & Textbox Entry widgets
#---------------------------------------------
photoPacientUI = ttk.Label(patient_conditions_frame)
photoPacientUI.grid(column=1, row=1, sticky='W')
loadLogo()
#---------------------------------------------
ttk.Label(patient_conditions_frame, text=_.t('NAME')).grid(column=0, row=2, sticky='W')
nameEntryUI = ttk.Label(patient_conditions_frame, font=("Arial", 18), foreground="blue")
nameEntryUI.grid(column=1, row=2, sticky='W')
#---------------------------------------------
ttk.Label(patient_conditions_frame, text=_.t('INSULIN')).grid(column=0, row=3, sticky='W')
insulinUI = ttk.Label(patient_conditions_frame, font=("Arial", 16), foreground="dark green")
insulinUI.grid(column=1, row=3, sticky='W')
#---------------------------------------------
#bDiabetesCheck = ttk.Button(patient_conditions_frame, text=_.t('BTN_DIABETES_CHECK_RESULT'), command=btnDiabetesDiagnostic).grid(row=3,column=1)
#---------------------------------------------
ttk.Label(patient_conditions_frame, text=_.t('MAMMOGRAPHY')).grid(column=0, row=4, sticky='W')
photobreathUI = ttk.Label(patient_conditions_frame)
photobreathUI.grid(column=1, row=4, sticky='W')
#---------------------------------------------
b = ttk.Button(patient_conditions_frame, text=_.t('BTN_CHECK_RESULT'), command=btnCancerDiagnostic).grid(column=1, row=5)
#---------------------------------------------

#======================
# Start GUI
#======================
win.mainloop()
