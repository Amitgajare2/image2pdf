import os
import img2pdf
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def dir_text_file(extension):
    img_ext = f".{extension.strip('.')}"
    webp_files = [x for x in dir_list if x.endswith(img_ext)]
    sort_files = sorted(webp_files, key=lambda x: int(x.split(".")[0]))  # Sort images by numbers

    # Store the list of image files in a text file
    with open("img_files.txt", "w") as file:
        for item in sort_files:
            file.write(item + "\n")

    messagebox.showinfo("Info", "Files stored in img_files.txt")

def img_to_pdf(dpi, img_extension):
    img_ext = f".{img_extension.strip('.')}"
    webp_files = [x for x in dir_list if x.endswith(img_ext)]
    sort_files = sorted(webp_files, key=lambda x: int(x.split(".")[0]))  # Sort images by numbers

    if not sort_files:
        messagebox.showwarning("Warning", "No images found with the provided extension.")
        return

    # Convert images to PDF with compression (adjust DPI)
    pdf_bytes = img2pdf.convert([os.path.join(path, img) for img in sort_files], dpi=dpi)

    # Save the PDF to a file
    pdf_file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="Save PDF File"
    )
    if pdf_file_path:
        with open(pdf_file_path, "wb") as pdf_file:
            pdf_file.write(pdf_bytes)
        messagebox.showinfo("Success", "Images converted to PDF successfully.")
    else:
        messagebox.showinfo("Info", "PDF conversion canceled.")

def natural_sort_key(s):
    # Custom sort key function for natural sorting
    return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', s)]

def normal_image_to_pdf(extension):
    img_ext = f".{extension.strip('.')}"
    webp_files = [x for x in sorted(dir_list, key=natural_sort_key) if x.endswith(img_ext)]

    if not webp_files:
        messagebox.showwarning("Warning", "No images found with the provided extension.")
        return

    pdf_bytes = img2pdf.convert([os.path.join(path, img) for img in webp_files], dpi=300)

    # Save the PDF to a file
    pdf_file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="Save PDF File"
    )
    if pdf_file_path:
        with open(pdf_file_path, "wb") as pdf_file:
            pdf_file.write(pdf_bytes)
        messagebox.showinfo("Success", "Images converted to PDF successfully.")
    else:
        messagebox.showinfo("Info", "PDF conversion canceled.")

def select_image_directory():
    global path, dir_list
    path = filedialog.askdirectory(title="Select Image Directory")
    if path:
        dir_list = os.listdir(path)
        directory_label.config(text=path)

def on_convert_click():
    selected_option = radio_var.get()
    extension = extension_entry.get()

    if not path:
        messagebox.showwarning("Warning", "Please select an image directory.")
        return

    if selected_option == 1:
        dir_text_file(extension)
    elif selected_option == 2:
        dpi_options = {
            1: 72,
            2: 150,
            3: 300,
        }
        selected_dpi = dpi_options.get(dpi_var.get())
        if not selected_dpi:
            messagebox.showwarning("Warning", "Please select a DPI option.")
            return
        img_to_pdf(selected_dpi, extension)
    elif selected_option == 3:
        normal_image_to_pdf(extension)

def show_credits():
    messagebox.showinfo("Credits", "Contributors:\n\nmortadapro#1127\npiratezoro#4189")

if __name__ == "__main__":
    path = ""
    dir_list = []

    root = tk.Tk()
    root.title("Image To PDF Maker")
    root.geometry("600x550")  # Increased window size to 600x550
    root.configure(bg="#222222")

    radio_var = tk.IntVar()
    radio_var.set(1)  # Set default option to 1

    dpi_var = tk.IntVar()
    dpi_var.set(1)  # Set default DPI option to 1

    title_label = tk.Label(root, text="Image To PDF Maker", font=("Helvetica", 18), bg="#222222", fg="#ffffff")
    title_label.pack(pady=15)

    extension_label = tk.Label(root, text="Enter Image Extension ex(.png):", font=("Helvetica", 12), bg="#222222", fg="#ffffff")
    extension_label.pack()

    extension_entry = tk.Entry(root, font=("Helvetica", 12), bg="#d3af37", fg="white")
    extension_entry.pack()

    conversion_frame = tk.Frame(root, bg="#222222")
    conversion_frame.pack(pady=10, padx=20)

    conversion_label = tk.Label(conversion_frame, text="Select Conversion Option:", font=("Helvetica", 12), bg="#222222", fg="#d3af37")
    conversion_label.pack(anchor="w")

    dir_radio = tk.Radiobutton(conversion_frame, text="Store in Text File", variable=radio_var, value=1, font=("Helvetica", 11), bg="#222222", fg="#ffffff", selectcolor="#d3af37")
    dir_radio.pack(anchor="w")

    pdf_radio = tk.Radiobutton(conversion_frame, text="Convert to PDF", variable=radio_var, value=2, font=("Helvetica", 11), bg="#222222", fg="#ffffff", selectcolor="#d3af37")
    pdf_radio.pack(anchor="w")

    dpi_frame = tk.Frame(root, bg="#222222")
    dpi_frame.pack(pady=10, padx=20)

    dpi_label = tk.Label(dpi_frame, text="Select DPI Option:", font=("Helvetica", 12), bg="#222222", fg="#d3af37")
    dpi_label.pack(anchor="w")

    screen_radio = tk.Radiobutton(dpi_frame, text="Screen (72 DPI)", variable=dpi_var, value=1, font=("Helvetica", 11), bg="#222222", fg="#ffffff", selectcolor="#d3af37")
    screen_radio.pack(anchor="w")

    ebook_radio = tk.Radiobutton(dpi_frame, text="Ebook (150 DPI)", variable=dpi_var, value=2, font=("Helvetica", 11), bg="#222222", fg="#ffffff", selectcolor="#d3af37")
    ebook_radio.pack(anchor="w")

    prepress_radio = tk.Radiobutton(dpi_frame, text="Prepress (300 DPI)", variable=dpi_var, value=3, font=("Helvetica", 11), bg="#222222", fg="#ffffff", selectcolor="#d3af37")
    prepress_radio.pack(anchor="w")

    normal_radio = tk.Radiobutton(dpi_frame, text="Normal Conversion", variable=radio_var, value=3, font=("Helvetica", 11), bg="#222222", fg="#ffffff", selectcolor="#d3af37")
    normal_radio.pack(anchor="w")

    select_dir_button = tk.Button(root, text="Select Image Directory", command=select_image_directory, font=("Helvetica", 12), bg="#d3af37")
    select_dir_button.pack(pady=10)

    directory_label = tk.Label(root, text="", font=("Helvetica", 11), bg="#222222", fg="#ffffff")
    directory_label.pack()

    convert_button = tk.Button(root, text="Convert", command=on_convert_click, font=("Helvetica", 12), bg="#d3af37")
    convert_button.pack(pady=15)

    credits_button = tk.Button(root, text="Credits (Contributors)", command=show_credits, font=("Helvetica", 10), bg="#d3af37", fg="#222222")
    credits_button.pack(pady=5)

    root.mainloop()
