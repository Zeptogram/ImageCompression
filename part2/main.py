import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from functions import validate_data, compress_image

selected_image = None
processed_image = None

# Selezione dell'immagine Bitmap
def browse_image(img_label, enable_process_button, size_label):
    global selected_image
    filename = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if filename:
        # Convertiamo a scale di grigi l'immagine per sicurezza
        selected_image = Image.open(filename).convert('L')  
        img_label.config(text="Immagine selezionata: " + filename)
        # Verifico se abilitare il bottone dell'elaborazione
        enable_process_button()
        # Mostro le dimensioni dell'immagine
        update_image_info(size_label)
        # Resize dell'immagine per mostrarla in finestra
        resize_and_display_image(img_label)

# Se è stato tutto inserito abilito il pulsante per l'elaborazione
def enable_process_button(F_entry, d_entry, process_button):
    if all((F_entry.get(), d_entry.get(), selected_image)):
        process_button.config(state=tk.NORMAL)
    else:
        process_button.config(state=tk.DISABLED)

# Aggiorno la label della size
def update_image_info(size_label):
    global selected_image
    # Se è selezionata
    if selected_image:
        width, height = selected_image.size
        size_label.config(text=f"Dimensione immagine: {width}x{height} pixel")

# Processa la vera e propria immagine
def process_image(F_entry, d_entry, img_label, proc_img_label):
    global processed_image
    try:
        # Converto ad int F e d inseriti
        F = int(F_entry.get())
        d = int(d_entry.get())
        # Valido d e F
        is_valid = validate_data(d, F)
        if not is_valid:
            messagebox.showerror("Errore", "d non è compreso tra 0 e 2*f - 2")

        # Ottengo l'immagine compressa
        processed_image = compress_image(selected_image, F, d)
        # Resize della immagine processata per mostrarla in finestra
        resize_processed_image = processed_image.resize(get_resized_dimensions(processed_image))
        processed_image_tk = ImageTk.PhotoImage(resize_processed_image)
        proc_img_label.config(image=processed_image_tk)
        proc_img_label.image = processed_image_tk
        # Abilito il pulsante per salvare l'immagine
        save_button.config(state=tk.NORMAL)
    except Exception as e:
            messagebox.showerror("Errore", f"Impossibile Elaborare l'immagine: {str(e)}")

# Resize di una immagine, mantenendo aspect ratio e occupando metà finestra
def get_resized_dimensions(image):
    window_height = root.winfo_height()
    window_width = root.winfo_width()
    max_height = window_height // 2  
    original_width, original_height = image.size
    ratio = min(max_height / original_height, window_width / original_width)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    return (new_width, new_height)

# Resize di una immagine selezionata
def resize_and_display_image(img_label):
    if selected_image:
        resized_image = selected_image.resize(get_resized_dimensions(selected_image), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)
        img_label.config(image=image_tk)
        img_label.image = image_tk
        
# Per salvare l'immagine processata
def save_image():
    if processed_image:
        save_filename = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("Bitmap files", "*.bmp")])
        if save_filename:
            processed_image.save(save_filename, "BMP")
            messagebox.showinfo("Successo", "Immagine salvata con successo.")

# Creazione della finestra principale
root = tk.Tk()
root.title("Selezione Immagine e Parametri DCT2")

# Dimensioni della finestra
window_width = 1000
window_height = 600

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
browse_button = tk.Button(root, text="Scegli Immagine", command=lambda: browse_image(img_label, lambda: enable_process_button(F_entry, d_entry, process_button), size_label))
browse_button.pack(pady=5)

# Etichetta per visualizzare la dimensione dell'immagine selezionata
size_label = tk.Label(root, text="")
size_label.pack(pady=5)

# Etichetta e campo di inserimento per l'ampiezza delle finestrelle (F)
F_label = tk.Label(root, text="Ampiezza Finestrelle (F):")
F_label.pack(pady=5)
F_entry = tk.Entry(root)
F_entry.pack(pady=5)

# Etichetta e campo di inserimento per la soglia di taglio delle frequenze (d)
d_label = tk.Label(root, text="Soglia di Taglio Frequenze (d):")
d_label.pack(pady=5)
d_entry = tk.Entry(root)
d_entry.pack(pady=5)

# Pulsante per elaborare l'immagine con i parametri inseriti
process_button = tk.Button(root, text="Elabora Immagine", command=lambda: process_image(F_entry, d_entry, img_label, proc_img_label), state=tk.DISABLED)
process_button.pack(pady=5)

# Pulsante per salvare l'immagine compressa
save_button = tk.Button(root, text="Salva Immagine Compressa", command=save_image, state=tk.DISABLED)
save_button.pack(pady=5)

# Aggiungi funzione di abilitazione del pulsante di elaborazione
F_entry.bind("<KeyRelease>", lambda event: enable_process_button(F_entry, d_entry, process_button))
d_entry.bind("<KeyRelease>", lambda event: enable_process_button(F_entry, d_entry, process_button))

# Bind del ridimensionamento della finestra per aggiornare l'immagine
root.bind("<Configure>", lambda event: resize_and_display_image(img_label))

# Avvio del loop principale della finestra
root.mainloop()
