import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometers")
window.minsize(300, 200)
window.config(padx=50, pady=75)

input = tkinter.Entry()
input.config(width=10)
input.grid(column=1, row=0)

miles_text_label = tkinter.Label(text="Miles")
miles_text_label.grid(column=2, row=0)

conversion_text_label = tkinter.Label(text="is equal to ")
conversion_text_label.grid(column=0, row=1)

conversor_text_label = tkinter.Label(text="0")
conversor_text_label.grid(column=1, row=1)

km_text_label = tkinter.Label(text="Km")
km_text_label.grid(column=2, row=1)


def mile_to_km():
    mile = int(input.get())
    km = int(mile * 1.609)
    conversor_text_label.config(text=f"{km}")


button = tkinter.Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)


window.mainloop()
