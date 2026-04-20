import requests
import tkinter as tk

url = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")

data = url.json()

value_moeda = float(data["USDBRL"]['bid'])

windows = tk.Tk()


label_view_convert = tk.Label(windows, text="")

def view_convertor():
    

    
    try:
        coin = float(values.get())
        
        coin_convert = coin * value_moeda

        label_view_convert.config(
            text=f"YOUR VALUE IN USD: US${coin_convert:.2f}"
        )
    except:
        
        label_view_convert.config(
                text="ONLY NUMBERS PLS"
        )

banner_image = tk.PhotoImage(file="banner.png")
banner_image = banner_image.subsample(1)
banner = tk.Label(windows, image=banner_image)




tittle = tk.Label(windows, text="WELCOME TO THE BRL TO USD CONVERTER")

values = tk.Entry(windows)

button = tk.Button(windows, command= view_convertor)


banner.pack()
tittle.pack()
values.pack()
button.pack()
label_view_convert.pack()

windows.mainloop()

