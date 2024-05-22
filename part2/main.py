import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from functions import validate_data, compress_image

selected_image = None
processed_image = None

def browse_image(img_label, enable_process_button):
    global selected_image
    filename = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if filename:
        selected_image = Image.open(filename).convert('L')  # Convert to grayscale for simplicity
        img_label.config(text="Immagine selezionata: " + filename)
        enable_process_button()

def enable_process_button(F_entry, d_entry, process_button):
    if all((F_entry.get(), d_entry.get(), selected_image)):
        process_button.config(state=tk.NORMAL)
    else:
        process_button.config(state=tk.DISABLED)

def process_image(F_entry, d_entry, img_label, proc_img_label):
    global processed_image
    try:
        F = int(F_entry.get())
        d = int(d_entry.get())
        is_valid = validate_data(d, F)
        if not is_valid:
            messagebox.showerror("Errore", "d non è compreso tra 0 e 2*f - 2")

        processed_image = compress_image(selected_image, F, d)
        
        original_image_tk = ImageTk.PhotoImage(selected_image)
        processed_image_tk = ImageTk.PhotoImage(processed_image)
        
        img_label.config(image=original_image_tk)
        img_label.image = original_image_tk
        
        proc_img_label.config(image=processed_image_tk)
        proc_img_label.image = processed_image_tk
    except:
            messagebox.showerror("Errore", "Impossibile Elaborare l'immagine")

# Creazione della finestra principale
root = tk.Tk()
root.title("Selezione Immagine e Parametri DCT2")

# Dimensioni della finestra
window_width = 1000
window_height = 500

# Posizionamento della finestra al centro dello schermo
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Spazio tra le componenti e il bordo della finestra
root.configure(padx=10, pady=10)

# Frame per contenere le immagini
frame = tk.Frame(root)
frame.pack()

# Etichetta per visualizzare l'immagine originale
img_label = tk.Label(frame)
img_label.grid(row=0, column=0, padx=5, pady=5)

# Etichetta per visualizzare l'immagine processata
proc_img_label = tk.Label(frame)
proc_img_label.grid(row=0, column=1, padx=5, pady=5)

# Pulsante per selezionare un'immagine
browse_button = tk.Button(root, text="Scegli Immagine", command=lambda: browse_image(img_label, lambda: enable_process_button(F_entry, d_entry, process_button)))
browse_button.pack()

# Etichetta e campo di inserimento per l'ampiezza delle finestrelle (F)
F_label = tk.Label(root, text="Ampiezza Finestrelle (F):")
F_label.pack()
F_entry = tk.Entry(root)
F_entry.pack()

# Etichetta e campo di inserimento per la soglia di taglio delle frequenze (d)
d_label = tk.Label(root, text="Soglia di Taglio Frequenze (d):")
d_label.pack()
d_entry = tk.Entry(root)
d_entry.pack()

# Pulsante per elaborare l'immagine con i parametri inseriti
process_button = tk.Button(root, text="Elabora Immagine", command=lambda: process_image(F_entry, d_entry, img_label, proc_img_label), state=tk.DISABLED)
process_button.pack()

# Aggiungi funzione di abilitazione del pulsante di elaborazione
F_entry.bind("<KeyRelease>", lambda event: enable_process_button(F_entry, d_entry, process_button))
d_entry.bind("<KeyRelease>", lambda event: enable_process_button(F_entry, d_entry, process_button))

# Avvio del loop principale della finestra
root.mainloop()
