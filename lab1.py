import tkinter as tk
from tkinter import colorchooser
from colormath.color_objects import LabColor, HSVColor, sRGBColor, CMYColor
from colormath.color_conversions import convert_color

# Флаги для предотвращения рекурсивного обновления
updating_cmyk = False
updating_lab = False
updating_hsv = False

def cmyk_to_rgb(c, m, y, k):
    r = int(255 * (1 - c) * (1 - k))
    g = int(255 * (1 - m) * (1 - k))
    b = int(255 * (1 - y) * (1 - k))
    return r, g, b

def rgb_to_cmyk(r, g, b):
    c = 1 - (r / 255.0)
    m = 1 - (g / 255.0)
    y = 1 - (b / 255.0)
    k = min(c, m, y)
    c = (c - k) / (1 - k) if (1 - k) != 0 else 0
    m = (m - k) / (1 - k) if (1 - k) != 0 else 0
    y = (y - k) / (1 - k) if (1 - k) != 0 else 0
    return c * 100, m * 100, y * 100, k * 100

def update_preview(r, g, b):
    color_preview.config(bg=f"#{r:02x}{g:02x}{b:02x}")

def update_colors_from_cmyk(c, m, y, k):
    global updating_cmyk, updating_lab, updating_hsv
    if updating_cmyk:
        return
    updating_cmyk = True
    try:
        r, g, b = cmyk_to_rgb(c, m, y, k)
        srgb_color = sRGBColor(r / 255.0, g / 255.0, b / 255.0)
        lab_color = convert_color(srgb_color, LabColor)
        hsv_color = convert_color(srgb_color, HSVColor)

        lab_l.set(int(lab_color.lab_l))
        lab_a.set(int(lab_color.lab_a))
        lab_b.set(int(lab_color.lab_b))

        hsv_h.set(int(hsv_color.hsv_h))
        hsv_s.set(int(hsv_color.hsv_s * 100))
        hsv_v.set(int(hsv_color.hsv_v * 100))

        update_preview(r, g, b)

    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        updating_cmyk = False

def update_from_cmyk(*args):
    c = cmyk_c.get() / 100.0
    m = cmyk_m.get() / 100.0
    y = cmyk_y.get() / 100.0
    k = cmyk_k.get() / 100.0
    update_colors_from_cmyk(c, m, y, k)

def update_from_lab(*args):
    global updating_lab, updating_cmyk, updating_hsv
    if updating_lab:
        return
    updating_lab = True
    try:
        l = lab_l.get()
        a = lab_a.get()
        b = lab_b.get()
        lab_color = LabColor(l, a, b)
        rgb_color = convert_color(lab_color, sRGBColor)
        r = int(rgb_color.clamped_rgb_r * 255)
        g = int(rgb_color.clamped_rgb_g * 255)
        b = int(rgb_color.clamped_rgb_b * 255)
        c, m, y, k = rgb_to_cmyk(r, g, b)

        if not updating_cmyk:
            cmyk_c.set(int(c))
            cmyk_m.set(int(m))
            cmyk_y.set(int(y))
            cmyk_k.set(int(k))
        
        if not updating_hsv:
            hsv_color = convert_color(rgb_color, HSVColor)
            hsv_h.set(int(hsv_color.hsv_h))
            hsv_s.set(int(hsv_color.hsv_s * 100))
            hsv_v.set(int(hsv_color.hsv_v * 100))
        
        update_preview(r, g, b)

    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        updating_lab = False

def update_from_hsv(*args):
    global updating_hsv, updating_cmyk, updating_lab
    if updating_hsv:
        return
    updating_hsv = True
    try:
        h = hsv_h.get()
        s = hsv_s.get() / 100.0
        v = hsv_v.get() / 100.0
        hsv_color = HSVColor(h, s, v)
        rgb_color = convert_color(hsv_color, sRGBColor)
        r = int(rgb_color.clamped_rgb_r * 255)
        g = int(rgb_color.clamped_rgb_g * 255)
        b = int(rgb_color.clamped_rgb_b * 255)
        c, m, y, k = rgb_to_cmyk(r, g, b)

        if not updating_cmyk:
            cmyk_c.set(int(c))
            cmyk_m.set(int(m))
            cmyk_y.set(int(y))
            cmyk_k.set(int(k))

        if not updating_lab:
            lab_color = convert_color(rgb_color, LabColor)
            lab_l.set(int(lab_color.lab_l))
            lab_a.set(int(lab_color.lab_a))
            lab_b.set(int(lab_color.lab_b))
        
        update_preview(r, g, b)

    except ValueError as e:
        print(f"Ошибка: {e}")
    finally:
        updating_hsv = False

def choose_color():
    rgb, _ = colorchooser.askcolor()
    if rgb:
        r = int(rgb[0])
        g = int(rgb[1])
        b = int(rgb[2])
        srgb_color = sRGBColor(r / 255.0, g / 255.0, b / 255.0)
        lab_color = convert_color(srgb_color, LabColor)
        hsv_color = convert_color(srgb_color, HSVColor)

        lab_l.set(int(lab_color.lab_l))
        lab_a.set(int(lab_color.lab_a))
        lab_b.set(int(lab_color.lab_b))

        hsv_h.set(int(hsv_color.hsv_h))
        hsv_s.set(int(hsv_color.hsv_s * 100))
        hsv_v.set(int(hsv_color.hsv_v * 100))

        c, m, y, k = rgb_to_cmyk(r, g, b)
        cmyk_c.set(int(c))
        cmyk_m.set(int(m))
        cmyk_y.set(int(y))
        cmyk_k.set(int(k))

        update_preview(r, g, b)

root = tk.Tk()
root.title("Цветовой Конвертер CMYK ↔️ LAB ↔️ HSV")

color_preview = tk.Label(root, text="Your color:", bg="#000000", width=20, height=5)
color_preview.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tk.Label(root, text="CMYK").grid(row=1, column=0)
cmyk_c = tk.IntVar()
cmyk_m = tk.IntVar()
cmyk_y = tk.IntVar()
cmyk_k = tk.IntVar()

# CMYK Sliders and Entry
for i, (text, var) in enumerate([("C", cmyk_c), ("M", cmyk_m), ("Y", cmyk_y), ("K", cmyk_k)]):
    tk.Label(root, text=text).grid(row=2 + i, column=0)
    tk.Scale(root, from_=0, to=100, orient="horizontal", variable=var, command=lambda val, v=var: update_from_cmyk()).grid(row=2 + i, column=1)
    entry = tk.Entry(root, textvariable=var)
    entry.grid(row=2 + i, column=2)
    entry.bind("<Return>", update_from_cmyk)  # Bind Enter key to update

tk.Label(root, text="LAB").grid(row=1, column=3)
lab_l = tk.IntVar()
lab_a = tk.IntVar()
lab_b = tk.IntVar()

# LAB Sliders and Entry
for i, (text, var, from_, to_) in enumerate([("L", lab_l, 0, 100), ("A", lab_a, -128, 127), ("B", lab_b, -128, 127)]):
    tk.Label(root, text=text).grid(row=2 + i, column=3)
    tk.Scale(root, from_=from_, to=to_, orient="horizontal", variable=var, command=lambda val, v=var: update_from_lab()).grid(row=2 + i, column=4)
    entry = tk.Entry(root, textvariable=var)
    entry.grid(row=2 + i, column=5)
    entry.bind("<Return>", update_from_lab)  # Bind Enter key to update

tk.Label(root, text="HSV").grid(row=1, column=6)
hsv_h = tk.IntVar()
hsv_s = tk.IntVar()
hsv_v = tk.IntVar()

# HSV Sliders and Entry
for i, (text, var, from_, to_) in enumerate([("H", hsv_h, 0, 360), ("S", hsv_s, 0, 100), ("V", hsv_v, 0, 100)]):
    tk.Label(root, text=text).grid(row=2 + i, column=6)
    tk.Scale(root, from_=from_, to=to_, orient="horizontal", variable=var, command=lambda val, v=var: update_from_hsv()).grid(row=2 + i, column=7)
    entry = tk.Entry(root, textvariable=var)
    entry.grid(row=2 + i, column=8)
    entry.bind("<Return>", update_from_hsv)  # Bind Enter key to update

tk.Button(root, text="Choose color", command=choose_color).grid(row=6, column=0, columnspan=9, pady=10)

root.mainloop()
