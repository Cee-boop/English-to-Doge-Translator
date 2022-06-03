import requests
from tkinter import *


def doge():
    """
    Grabs translated response from API
    """
    user_input = user_entry.get()
    parameters = {
         'text': user_input
     }

    response = requests.get("https://api.funtranslations.com/translate/doge.json", params=parameters)
    response.raise_for_status()
    data = response.json()
    translation = data['contents']['translated']
    translation_label.config(text=f"Translation: {translation}")


window = Tk()
window.title("English to Doge Translator")
window.config(padx=150, pady=150)

canvas = Canvas(width=400, height=400)
doge_img = PhotoImage(file="./doge.png")
doge_canvas = canvas.create_image(200, 203, image=doge_img)
canvas_title = canvas.create_text(260, 260, text="Doge\nTranslator", font=("Comic Sans", 30, "bold"), fill="black")
canvas.grid(row=0, column=0)

enter_text_label = Label(text="Enter text to translate: ", font=("Comic Sans", 14, "bold"))
enter_text_label.grid(row=1, column=0)
user_entry = Entry(width=30)
user_entry.focus()
user_entry.grid(row=2, column=0)

translate_button = Button(text="Translate!", command=doge, width=12, font=("Comic Sans", 14, "normal"))
translate_button.grid(row=3, column=0)

# shows translated text:
translation_label = Label(text="", font=("Comic Sans", 14, "normal"))
translation_label.grid(row=4, column=0)

window.mainloop()
