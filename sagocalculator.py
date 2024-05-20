import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import time

def draw_image(image, draw):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            draw.point((x, y), fill=pixel)
            window.update()
            time.sleep(0.0001)

def display_image(image_path):
    image = Image.open(image_path)
    image = image.resize((600, 600))  # Resize the image as needed
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

    # Draw the image progressively from top to bottom
    draw = ImageDraw.Draw(image)
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            draw.point((x, y), fill=pixel)
        photo = ImageTk.PhotoImage(image.crop((0, 0, width, y + 1)))
        image_label.config(image=photo)
        image_label.image = photo
        window.update()
        time.sleep(0.0001)

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="white")  # Set background color to white

# Label for instructions
instructions_label = tk.Label(window, text="This is a calculator. Please enter two numbers below and click 'Calculate'", anchor=tk.NW, justify=tk.LEFT)
instructions_label.pack(padx=10, pady=10)

# Calculator interface
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

calculate_button = tk.Button(window, text="Calculate", command=lambda: display_image("sagofinal.jpg"))
calculate_button.pack()

# Image display
image_label = tk.Label(window)
image_label.pack(pady=10)

window.mainloop()
