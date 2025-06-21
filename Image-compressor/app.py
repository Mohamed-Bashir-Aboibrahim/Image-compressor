from tkinter import *
from tkinter import filedialog
import os
from PIL import Image
src_paths = []
dst_folder = ""
root = Tk()
root.title("Image Compressor")
root.geometry("400x450")
root.configure(bg="#1e1e2f")
quality = IntVar(value=70)
def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        global src_paths
        src_paths = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        label_selected.config(text=f"{len(src_paths)} images loaded from folder")
        status_label.config(text="Ready", fg="lightgreen")
def choose_images():
    files = filedialog.askopenfilenames(filetypes=[("Images", "*.jpg *.jpeg *.png")])
    if files:
        global src_paths
        src_paths = list(files)
        label_selected.config(text=f"{len(src_paths)} images selected")
        status_label.config(text="Ready", fg="lightgreen")
def choose_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        global dst_folder
        dst_folder = folder
        label_output.config(text=f"Output Folder: {folder}")
        status_label.config(text="Ready", fg="lightgreen")
def start_compression():
    if not src_paths or not dst_folder:
        status_label.config(text="Select images and output folder first!", fg="red")
        return
    count = 0
    total_saved = 0
    for path in src_paths:
        try:
            before = os.path.getsize(path)
            img = Image.open(path)
            img = img.convert("RGB")
            filename = os.path.basename(path)
            output_path = os.path.join(dst_folder, filename)
            img.save(output_path, "JPEG", quality=quality.get())
            after = os.path.getsize(output_path)
            saved = before - after
            total_saved += saved
            count += 1
        except:
            continue
    mb = total_saved / (1024 * 1024)
    status_label.config(text=f"Compressed {count} images. Saved {mb:.2f} MB", fg="lightgreen")
def reset_all():
    global src_paths, dst_folder
    src_paths = []
    dst_folder = ""
    label_selected.config(text="No images/folder selected")
    label_output.config(text="No output folder selected")
    quality.set(70)
    status_label.config(text="Reset done.", fg="blue")
Label(root, text="Image Compressor", font=("Segoe UI", 20, "bold"), bg="#1e1e2f", fg="#00ffff").pack(pady=10)
label_selected = Label(root, text="No images/folder selected", bg="#1e1e2f", fg="white", font=("Segoe UI", 10))
label_selected.pack(pady=5)
Button(root, text="Choose Folder", command=choose_folder, bg="#00aaaa", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=2)
Button(root, text="Choose Images", command=choose_images, bg="#00aaaa", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=2)
Label(root, text="Compression Quality", bg="#1e1e2f", fg="white", font=("Segoe UI", 10)).pack(pady=10)
Scale(root, from_=1, to=100, orient=HORIZONTAL, variable=quality,
      bg="#1e1e2f", fg="white", highlightbackground="#1e1e2f", troughcolor="#00ffff").pack()
label_output = Label(root, text="No output folder selected", bg="#1e1e2f", fg="white", font=("Segoe UI", 10))
label_output.pack(pady=5)
Button(root, text="Choose Output Folder", command=choose_output_folder, bg="#00aaaa", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=2)
Button(root, text="Start Compression", command=start_compression, bg="#0099ff", fg="white", font=("Segoe UI", 12, "bold")).pack(pady=10)
status_label = Label(root, text="Ready", fg="lightgreen", bg="#1e1e2f", font=("Segoe UI", 10))
status_label.pack(pady=5)
Button(root, text="Reset", command=reset_all, bg="#555", fg="white", font=("Segoe UI", 10)).pack(pady=5)
root.mainloop()