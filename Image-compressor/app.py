from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import io

# --- Global Variables ---
src_paths = []
dst_folder = ""
root = Tk()
root.title("Image Compressor")
root.geometry("500x550")
root.configure(bg="#1e1e2f")

quality = IntVar(value=70)
estimated_savings = StringVar(value="Estimated savings: -- MB")

# --- Functions ---
def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        global src_paths
        src_paths = [os.path.join(folder, f) for f in os.listdir(folder)
                    if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        label_selected.config(text=f"{len(src_paths)} images loaded from folder")
        status_label.config(text="Ready", fg="lightgreen")
        update_estimated_savings()  # Update estimates after selecting images

def choose_images():
    files = filedialog.askopenfilenames(filetypes=[("Images", "*.jpg *.jpeg *.png")])
    if files:
        global src_paths
        src_paths = list(files)
        label_selected.config(text=f"{len(src_paths)} images selected")
        status_label.config(text="Ready", fg="lightgreen")
        update_estimated_savings()  # Update estimates after selecting images

def choose_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        global dst_folder
        dst_folder = folder
        label_output.config(text=f"Output Folder: {folder}")
        status_label.config(text="Ready", fg="lightgreen")

def show_preview(original_path, compressed_path):
    preview_win = Toplevel(root)
    preview_win.title("Preview")
    preview_win.geometry("800x400")

    original_img = Image.open(original_path)
    compressed_img = Image.open(compressed_path)
    max_height = 350
    original_img.thumbnail((500, max_height))
    compressed_img.thumbnail((500, max_height))

    original_photo = ImageTk.PhotoImage(original_img)
    compressed_photo = ImageTk.PhotoImage(compressed_img)

    Label(preview_win, text="Original", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    Label(preview_win, text="Compressed", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

    original_label = Label(preview_win, image=original_photo)
    original_label.image = original_photo
    original_label.grid(row=1, column=0, padx=10, pady=5)

    compressed_label = Label(preview_win, image=compressed_photo)
    compressed_label.image = compressed_photo
    compressed_label.grid(row=1, column=1, padx=10, pady=5)

    original_size = os.path.getsize(original_path) / 1024  # KB
    compressed_size = os.path.getsize(compressed_path) / 1024  # KB
    saved = original_size - compressed_size

    Label(preview_win, text=f"Original: {original_size:.1f} KB", font=("Arial", 10)).grid(row=2, column=0)
    Label(preview_win, text=f"Compressed: {compressed_size:.1f} KB", font=("Arial", 10)).grid(row=2, column=1)
    Label(preview_win, text=f"Saved: {saved:.1f} KB ({saved / original_size * 100:.1f}%)",
          font=("Arial", 10, "bold"), fg="green").grid(row=3, columnspan=2, pady=10)

def update_estimated_savings():
    if not src_paths:
        estimated_savings.set("Estimated savings: -- MB")
        return

    total_saved = 0
    for path in src_paths:
        try:
            img = Image.open(path)
            buffer = io.BytesIO()
            img.convert("RGB").save(buffer, "JPEG", quality=quality.get())
            compressed_size = buffer.tell()
            original_size = os.path.getsize(path)
            total_saved += (original_size - compressed_size)
        except:
            continue

    mb_saved = total_saved / (1024 * 1024)
    estimated_savings.set(f"Estimated savings: {mb_saved:.2f} MB")

def start_compression():
    if not src_paths or not dst_folder:
        status_label.config(text="Select images and output folder first!", fg="red")
        return

    count = 0
    total_saved = 0
    preview_available = False

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
            preview_available = output_path
        except Exception as e:
            print(f"Error compressing {path}: {e}")

    mb_saved = total_saved / (1024 * 1024)
    status_label.config(text=f"Compressed {count} images. Saved {mb_saved:.2f} MB", fg="lightgreen")

    if preview_available:
        Button(root, text="Preview Last Image", command=lambda: show_preview(src_paths[-1], preview_available),
               bg="#ff9900", fg="black").pack(pady=5)

def reset_all():
    global src_paths, dst_folder
    src_paths = []
    dst_folder = ""
    label_selected.config(text="No images/folder selected")
    label_output.config(text="No output folder selected")
    quality.set(70)
    estimated_savings.set("Estimated savings: -- MB")
    status_label.config(text="Reset done.", fg="blue")

# --- GUI Setup ---
Label(root, text="Image Compressor", font=("Segoe UI", 20, "bold"), bg="#1e1e2f", fg="#00ffff").pack(pady=10)

label_selected = Label(root, text="No images/folder selected", bg="#1e1e2f", fg="white")
label_selected.pack(pady=5)

Button(root, text="Choose Folder", command=choose_folder, bg="#00aaaa", fg="white").pack(pady=2)
Button(root, text="Choose Images", command=choose_images, bg="#00aaaa", fg="white").pack(pady=2)

Label(root, text="Compression Quality", bg="#1e1e2f", fg="white").pack(pady=10)
Scale(root, from_=1, to=100, orient=HORIZONTAL, variable=quality, bg="#1e1e2f", fg="white").pack()

Label(root, textvariable=estimated_savings, bg="#1e1e2f", fg="#00ff00").pack(pady=5)

label_output = Label(root, text="No output folder selected", bg="#1e1e2f", fg="white")
label_output.pack(pady=5)
Button(root, text="Choose Output Folder", command=choose_output_folder, bg="#00aaaa", fg="white").pack(pady=2)

Button(root, text="Start Compression", command=start_compression, bg="#0099ff", fg="white").pack(pady=10)
status_label = Label(root, text="Ready", fg="lightgreen", bg="#1e1e2f")
status_label.pack(pady=5)

Button(root, text="Reset", command=reset_all, bg="#555", fg="white").pack(pady=5)

# Bind quality slider to update estimates
quality.trace_add("write", lambda *args: update_estimated_savings())

root.mainloop()                                                                                                       