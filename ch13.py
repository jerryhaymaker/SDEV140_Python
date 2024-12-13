
import tkinter


def ConvertToFahrenheit():
    Celsius = float(InputBox.get())
    Fahrenheit = (Celsius * 9/5) + 32
    OutputLabel.config(text=round(Fahrenheit, 2))


Window = tkinter.Tk()
Window.title("Celsius to Fahrenheit Converter")
Window.minsize(width=250, height=50)

InputBox = tkinter.Entry(justify=tkinter.RIGHT)
OutputLabel = tkinter.Label(text="", justify=tkinter.RIGHT, width=8)
ActionButton = tkinter.Button(text='Convert', command=ConvertToFahrenheit)

InputBox.pack(padx=20, pady=20)
OutputLabel.pack(padx=20, pady=20, side=tkinter.RIGHT)
ActionButton.pack(padx=20, pady=20)


Window.mainloop() 
