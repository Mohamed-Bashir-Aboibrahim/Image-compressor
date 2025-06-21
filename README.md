#  Image-compressor

Do you have images that take up a big part of your disk? With this app, you can compress your images or entire folders of photos, choosing the quality you want for the output files. Reduce storage usage without sacrificing much photo quality! 😍

---

##  Features

- **Select Individual Images or Folders:** Easily choose single images or an entire folder of images to compress.
- **Adjustable Output Quality:** Set your preferred image quality from 1 to 100 using a slider.
- **Batch Processing:** Compress multiple images at once.
- **Progress and Status Updates:** See how many images were compressed and how much disk space you saved.
- **Simple GUI:** User-friendly interface made with Tkinter.
- **Supports JPG, JPEG, PNG:** Works with the most common image formats.

---

##  How to Use

>  You can add screenshots or GIFs below each step to visually explain the process.

### 1. Launch the App
Run `app.py` (requires Python and the Pillow library).

![image](https://github.com/user-attachments/assets/ede3d8c1-fde6-40f0-b505-0a2234c10f34)

---

### 2. Select Images or a Folder
- Click **"Choose Images"** to select specific image files, or  
- Click **"Choose Folder"** to select all images in a folder.
---

### 3. Set Compression Quality
- Use the slider to choose the quality (1 = lowest, 100 = highest, **70 is the default**).
---

### 4. Choose Output Folder
- Click **"Choose Output Folder"** and select where compressed images will be saved.


---

### 5. Start Compression
- Click **"Start Compression"** to begin. The app will show:
  - How many images were compressed
  - How much disk space was saved


---

### 6. Reset (Optional)
- Click **"Reset"** to clear all selections and start over.


---

## 📦 Requirements

- Python 3.x  
- Pillow (`pip install pillow`)

---

## 🔧 Installation

```bash
git clone https://github.com/Mohamed-Bashir-Aboibrahim/Image-compressor.git
cd Image-compressor
pip install pillow
python Image-compressor/app.py
