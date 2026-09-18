import pyttsx3
import PyPDF2
from tkinter.filedialog import *

f_Name = askopenfilename()
reader = PyPDF2.PdfReader(f_Name)
n_Pages = len(reader.pages)

for i in range(n_Pages):
    page = reader.pages[i]
    text = page.extract_text()
    init_Speech = pyttsx3.init()
    init_Speech.say(text)
    init_Speech.runAndwWait()