import cv2
import tkinter as tk
from tkinter import filedialog
from pyzbar.pyzbar import decode

def read_qr_code():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if file_path:
        image = cv2.imread(file_path)
        decoded_objects = decode(image)

        if decoded_objects:
            result_label.config(text=f"QR Code Data: {decoded_objects[0].data.decode('utf-8')}")
        else:
            result_label.config(text="No QR code found in the selected image.")

root = tk.Tk()
root.title("QR")
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)
title_label = tk.Label(frame, text="QR Code Scanner", font=("Arial", 16))
title_label.pack(pady=10)

browse_button = tk.Button(frame, text="Browse for Image File", command=read_qr_code)
browse_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 12), wraplength=400)
result_label.pack()

root.mainloop()
