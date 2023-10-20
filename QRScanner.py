import cv2
import tkinter as tk
from tkinter import filedialog
from pyzbar.pyzbar import decode

def read_qr_code_from_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if file_path:
        image = cv2.imread(file_path)
        decoded_objects = decode(image)

        if decoded_objects:
            result_label.config(text=f"QR Code Data: {decoded_objects[0].data.decode('utf-8')}")
        else:
            result_label.config(text="No QR code found in the selected image.")

def read_qr_code_from_webcam():
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()
        decoded_objects = decode(frame)

        if decoded_objects:
            result_label.config(text=f"QR Code Data: {decoded_objects[0].data.decode('utf-8')}")
            break

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == 27: 
            break

    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("QR")
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)
title_label = tk.Label(frame, text="QR Code Scanner", font=("Arial", 16))
title_label.pack(pady=10)

image_button = tk.Button(frame, text="Scan QR Code from Image", command=read_qr_code_from_image)
image_button.pack(pady=10)

webcam_button = tk.Button(frame, text="Scan QR Code from Webcam", command=read_qr_code_from_webcam)
webcam_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 12), wraplength=400)
result_label.pack()

root.mainloop()
