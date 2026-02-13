import math
import tkinter as tk





window = tk.Tk()
window.configure(background="white")



DEFAULT_STYLE = {"outline": "green", "fill": "yellow", "width": 3}


def createAxis():
    canvas.create_polygon([1000, 0, 1000, 10000], **DEFAULT_STYLE)
    canvas.create_polygon([0, 700, 10000, 700], **DEFAULT_STYLE)


def lines():
    for i in range(100):
        canvas.create_polygon([i * 30, 720, i * 30, 680], **DEFAULT_STYLE)
        canvas.create_polygon([1020, i * 30, 980, i * 30], **DEFAULT_STYLE)










tk.Label(window, text="Your function:").pack(padx=10, pady=(10, 0))
name_entry = tk.Entry(window, width=300)  # input box
name_entry.pack(padx=10, pady=10)
name_entry.focus()

def function():
    points = []
    if name_entry.get()[:2] != "y =":
        print("wrong input")
        return
    else:
        pass

    for i in range(-500, 500):
        x_px = i*3+1000



function_confirm_button = tk.Button(window, text="Confirm Function", command=function)
function_confirm_button.pack(pady=10)

canvas = tk.Canvas(window, width=2000, height=2000)
canvas.pack()



def yequalsx():
    points = []
    for i in range(-500, 500):

        x_px = i * 3 + 1000
        y_px = math.cos(i / 20) * 200 + 700
        points.extend([x_px, y_px])  # flatten into [x1, y1, x2, y2, ...]

    canvas.create_line(*points, fill="green", width=3, smooth=True)






createAxis()
lines()
yequalsx()

window.mainloop()
