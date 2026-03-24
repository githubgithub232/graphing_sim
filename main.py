import math
import tkinter as tk
from sympy import sympify, symbols, lambdify

window = tk.Tk()
window.title("Graph with slider")

WIDTH = 1200
HEIGHT = 800
origin_x = WIDTH // 2
origin_y = HEIGHT // 2
scale = 40

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

tk.Label(window, text="Your function:").pack(pady=(10, 0))
name_entry = tk.Entry(window, width=50)
name_entry.pack(pady=5)
name_entry.insert(0, "a*x")

# slider for parameter a
a_slider = tk.Scale(
    window,
    from_=-100,
    to=100,
    orient="horizontal",
    resolution=1,
    label="a",
    length=400
)
a_slider.set(1)
a_slider.pack(pady=10)


def to_canvas(x, y):
    cx = origin_x + x * scale
    cy = origin_y - y * scale
    return cx, cy


def draw_axes():
    canvas.create_line(0, origin_y, WIDTH, origin_y, fill="black", width=2)
    canvas.create_line(origin_x, 0, origin_x, HEIGHT, fill="black", width=2)

    for x_tick in range(-WIDTH // (2 * scale), WIDTH // (2 * scale) + 1):
        cx, _ = to_canvas(x_tick, 0)
        canvas.create_line(cx, origin_y - 5, cx, origin_y + 5, fill="black")

    for y_tick in range(-HEIGHT // (2 * scale), HEIGHT // (2 * scale) + 1):
        _, cy = to_canvas(0, y_tick)
        canvas.create_line(origin_x - 5, cy, origin_x + 5, cy, fill="black")


def plot_function(*args):
    canvas.delete("graph")

    x, a = symbols("x a")

    try:
        expr = sympify(name_entry.get())
        func = lambdify((x, a), expr, "math")
        a_value = a_slider.get()
    except Exception as e:
        print("Parse error:", e)
        return

    points = []
    prev_cy = None

    for px in range(WIDTH):
        x_val = (px - origin_x) / scale

        try:
            y_val = func(x_val, a_value)

            if not math.isfinite(y_val) or abs(y_val) > 100:
                if len(points) >= 4:
                    canvas.create_line(*points, fill="green", width=2, tags="graph")
                points = []
                prev_cy = None
                continue

            cx, cy = to_canvas(x_val, y_val)

            # break line if jump is too large, helps for tan(x) etc.
            if prev_cy is not None and abs(cy - prev_cy) > 100:
                if len(points) >= 4:
                    canvas.create_line(*points, fill="green", width=2, tags="graph")
                points = []

            points.extend([cx, cy])
            prev_cy = cy

        except Exception:
            if len(points) >= 4:
                canvas.create_line(*points, fill="green", width=2, tags="graph")
            points = []
            prev_cy = None

    if len(points) >= 4:
        canvas.create_line(*points, fill="green", width=2, tags="graph")


tk.Button(window, text="Plot", command=plot_function).pack(pady=5)

# redraw automatically when slider moves
a_slider.config(command=plot_function)

draw_axes()
plot_function()
window.mainloop()