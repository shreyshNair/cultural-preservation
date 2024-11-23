import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for handling images

# Function to set background image
def set_background(image_path, root):
    # Get the window size after the window is created
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Open the image using Pillow
    background_image = Image.open(image_path)
    background_image = background_image.resize((window_width, window_height))  # Resize image to fit window
    photo = ImageTk.PhotoImage(background_image)

    # Create Label widget to display the image
    label = tk.Label(root, image=photo)
    label.place(relheight=1, relwidth=1)  # Fill the entire window with the image

    # Keep a reference to the image to prevent it from being garbage collected
    label.image = photo

# Create the main window
root = tk.Tk()
root.geometry("600x700")  # Set window size

# Update the window size and configure the background after the window is created
root.update()

# Path to the local image file
image_path = "C:/Users/shrey/OneDrive/Desktop/Shrey/project/cultural tradition.png"  # Replace with your image path

# Set the background image
set_background(image_path, root)

# Add a text label on top of the background image
text_label = tk.Label(root, text="Welcome to your Cultural collage", font=("Arial", 16), fg="black", bg="white")
text_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

