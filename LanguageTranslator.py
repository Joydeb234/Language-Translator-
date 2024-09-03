from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

root = Tk()
root.geometry("500x400")
root['bg'] = 'Sky blue'
root.title("TRANSLATOR language")

Label(root, text="Language Translator", font="Arial 20 bold").pack()
Label(root, text="Enter Text", font='Arial 20 bold', bg='White').place(x=165, y=100)

Input_text = Entry(root, width=60)
Input_text.place(x=40, y=130)

Label(root, text="Final Results", font='Arial 20 bold', bg='White').place(x=120, y=240)
Output_text = Text(root, font='Arial 13 bold', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=40, y=280)

language = ['english', 'french', 'spanish', 'german', 'hindi', 'italian', 'russian', 'bengali',
             'japanese', 'korean', 'arabic', 'portuguese', 'dutch', 'turkish', 'tamil', 'telugu']

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130, y=160)
dest_lang.set('choose language')

def translate():
    translator = GoogleTranslator(source='auto', target=dest_lang.get())
    translated_text = translator.translate(Input_text.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated_text)

trans_btn = Button(root, text="Translate", font='Arial 12 bold', pady=5, command=translate, bg='Orange', activebackground='Green')
trans_btn.place(x=200, y=180)

root.mainloop()
