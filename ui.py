import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from ultralytics import YOLO
import os
import shutil

# Load your YOLOv11 model
def load_model():
    return YOLO("best.pt")  # Make sure best.pt is in the same folder

# Run inference and save result with the same name as the input image
def run_inference(image_path, model):
    # Clear temp directory (predictions/result)
    if os.path.exists("predictions/result"):
        shutil.rmtree("predictions/result")

    # Run prediction
    model.predict(
        source=image_path,
        save=True,
        imgsz=640,
        project="predictions",
        name="result",
        exist_ok=True
    )

    # Extract the filename from the input image path (without extension)
    input_image_name = os.path.basename(image_path)
    image_name_without_extension = os.path.splitext(input_image_name)[0]

    # Define output image path with the same name as the input image
    yolov_output = os.path.join("predictions", "result", f"{image_name_without_extension}.jpg")
    output_image_path = os.path.join("predictions\\result", f"{image_name_without_extension}.jpg")

    if not os.path.exists(yolov_output):
        raise FileNotFoundError("Prediction failed: output image not found.")

    # Rename and move the output image to match the input image name
    shutil.move(yolov_output, output_image_path)

    return output_image_path

# Triggered on image upload
def load_and_display_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not file_path:
        return

    try:
        model = load_model()
        output_image_path = run_inference(file_path, model)

        img = Image.open(output_image_path)
        img = img.resize((640, 640))
        img_tk = ImageTk.PhotoImage(img)

        output_label.configure(image=img_tk)
        output_label.image = img_tk

        messagebox.showinfo("Detection Complete", f"Detection complete. Output saved as {os.path.basename(output_image_path)}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter GUI
root = ctk.CTk()
root.title("YOLOv11 Object Detection")
root.geometry("800x600")

upload_button = ctk.CTkButton(root, text="Upload Image", command=load_and_display_image)
upload_button.pack(pady=20)

output_label = ctk.CTkLabel(root)
output_label.pack(pady=20)

root.mainloop()
