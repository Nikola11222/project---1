import tkinter as tk
import random

colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF"]  # List of colors

def change_color():
    color = random.choice(colors)  # Randomly select a color from the list
    app.configure(background=color)

def exit_app():
    app.destroy()

def special_effects():
    effect = random.randint(1, 4)  # Randomly select an effect

    if effect == 1:
        # Flash effect
        flash_effect()
    elif effect == 2:
        # Fade effect
        fade_effect()
    elif effect == 3:
        # Rainbow effect
        rainbow_effect()
    elif effect == 4:
        # Random colors effect
        random_colors_effect()

def flash_effect():
    # Flash effect for the color change
    for _ in range(5):  # Repeat the flash effect 5 times
        app.configure(background="white")
        app.update()
        app.after(200)
        change_color()
        app.update()
        app.after(200)

def fade_effect():
    # Fade effect for the color change
    current_color = app.cget("background")
    target_color = random.choice(colors)

    for i in range(10):  # Gradually transition the color over 10 steps
        r = int(current_color[1:3], 16)
        g = int(current_color[3:5], 16)
        b = int(current_color[5:7], 16)

        target_r = int(target_color[1:3], 16)
        target_g = int(target_color[3:5], 16)
        target_b = int(target_color[5:7], 16)

        new_r = int(r + (target_r - r) * (i / 10))
        new_g = int(g + (target_g - g) * (i / 10))
        new_b = int(b + (target_b - b) * (i / 10))

        new_color = f"#{new_r:02x}{new_g:02x}{new_b:02x}"

        app.configure(background=new_color)
        app.update()
        app.after(100)

    change_color()

def rainbow_effect():
    # Rainbow effect for the color change
    for color in colors:
        app.configure(background=color)
        app.update()
        app.after(500)

def random_colors_effect():
    # Random colors effect for the color change
    for _ in range(5):  # Repeat the random colors effect 5 times
        change_color()
        app.update()
        app.after(500)

# Create the main application window
app = tk.Tk()
app.title("Color Changing App")

# Configure app to open in full-screen mode
app.attributes("-fullscreen", True)



button_style = {'background': 'goldenrod', 'foreground': 'black'}

change_button = tk.Button(app, text="Change Color", command=change_color, **button_style)
change_button.pack(pady=5)

exit_button = tk.Button(app, text="Exit", command=exit_app, **button_style)
exit_button.pack(pady=5)

effects_button = tk.Button(app, text="Special Effects", command=special_effects, **button_style)
effects_button.pack(pady=5)

app.mainloop()