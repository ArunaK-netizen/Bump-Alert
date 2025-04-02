import customtkinter as ctk
import torch
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import shutil

# Load the trained YOLOv5 model directly
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt')  # Load your custom-trained model
    return model

# Function to run inference on the uploaded image
def run_inference(image_path, model):
    # Load and process the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    img_resized = img.resize((640, 640))  # Resize to match YOLOv5 input size
    img_tensor = np.array(img_resized)  # Convert to numpy array

    # Run inference
    results = model(img_tensor)

    # Save the output image with bounding boxes
    results.save()  # Saves the output image with bounding boxes in the 'runs/detect/exp' folder

    # Get the output image path
    output_image_path = 'runs/detect/exp/image0.jpg'  # This is the default output image path
    return output_image_path

# Function to load and display the output image
def load_and_display_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return

    # Load the model
    model = load_model()

    # Run inference on the uploaded image
    output_image_path = run_inference(file_path, model)

    # Load the output image
    img = Image.open(output_image_path)
    img = img.resize((640, 640))  # Resize to fit the display window

    # Convert the image to a Tkinter-compatible format
    img_tk = ImageTk.PhotoImage(img)

    # Display the image in the label
    output_label.configure(image=img_tk)
    output_label.image = img_tk  # Keep a reference to the image

    # Display success message
    messagebox.showinfo("Detection Complete", "Detection is complete, and the image is displayed.")

    folder_path = 'runs'
    shutil.rmtree(folder_path)

# Create the Tkinter UI
root = ctk.CTk()
root.title("YOLOv5 Object Detection")
root.geometry("800x600")

# Create a button to upload the image
upload_button = ctk.CTkButton(root, text="Upload Image", command=load_and_display_image)
upload_button.pack(pady=20)

# Create a label to display the output image, initially empty
output_label = ctk.CTkLabel(root)
output_label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
