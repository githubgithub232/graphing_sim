# Graph with Slider

A simple Python Tkinter app for plotting mathematical functions with a slider controlled parameter.

## What it does

This program lets you:

- enter a mathematical expression such as `a*x`, `sin(a*x)`, `x**2 + a`, or `tan(x)`
- move a slider to change the value of parameter `a`
- draw the graph on a Tkinter canvas
- automatically redraw the graph when the slider changes
- display discontinuous functions more cleanly by breaking lines at large jumps

## Requirements

You need Python 3 and the following modules:

- `tkinter`
- `sympy`
- `math`

`math` is part of the Python standard library.

To install SymPy:

```bash
pip install sympy
```

## How to run

Save the program as something like `graph_slider.py`, then run:

```bash
python graph_slider.py
```

## How to use

1. Start the program.
2. Type a function into the input box.
3. Use `x` as the variable.
4. Use `a` as the slider controlled parameter.
5. Click **Plot** to draw the graph.
6. Move the slider to update the graph instantly.

## Example functions

You can try:

```text
a*x
x**2 + a
sin(a*x)
cos(x) + a
x**3 - a*x
tan(x)
```

## Notes about function input

The program uses SymPy to parse expressions, so use Python style math syntax:

- multiplication: `a*x`
- powers: `x**2`
- trig: `sin(x)`, `cos(x)`, `tan(x)`

Do not write:

```text
ax
x^2
```

Instead write:

```text
a*x
x**2
```

## How it works

- The canvas origin is placed in the middle of the window.
- Mathematical coordinates are converted to canvas coordinates using a scale factor.
- The x axis and y axis are drawn once.
- The function is evaluated for each pixel across the width of the canvas.
- If the result is not finite, too large, or jumps suddenly, the line is broken to avoid ugly vertical connections.

This is especially useful for functions like `tan(x)`.

## Current settings

- Window size: `1200 x 800`
- Origin: center of the canvas
- Scale: `40` pixels per unit
- Slider range for `a`: `-100` to `100`

## Possible improvements

You could extend the program by adding:

- axis number labels
- grid lines
- zoom in and zoom out buttons
- support for more parameters like `b` and `c`
- better error messages inside the window instead of printing to console
- custom graph colors
- mouse panning

## File overview

Main parts of the code:

- `to_canvas(x, y)` converts math coordinates into screen coordinates
- `draw_axes()` draws axes and tick marks
- `plot_function()` parses the expression and draws the graph
- `a_slider` controls the value of parameter `a`

## Author note

This is a nice beginner to intermediate project for learning:

- Tkinter GUI programming
- graph plotting
- coordinate systems
- symbolic parsing with SymPy
- handling difficult graphs such as discontinuities
