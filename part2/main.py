import tkinter as tk
from tkinter import filedialog
from PIL import Image

def browse_image():
    filename = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if filename:
        img = Image.open(filename)
        img_label.config(text="Immagine selezionata: " + filename)
        enable_process_button()

def enable_process_button():
    if all((F_entry.get(), d_entry.get())):
        process_button.config(state=tk.NORMAL)
    else:
        process_button.config(state=tk.DISABLED)

def process_image():
    F = int(F_entry.get())
    d = int(d_entry.get())
    # Qui inserisci la logica per elaborare l'immagine con F e d

# Creazione della finestra principale
root = tk.Tk()
root.title("Selezione Immagine e Parametri DCT2")

# Dimensioni della finestra
window_width = 500
window_height = 200

# Posizionamento della finestra al centro dello schermo
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Spazio tra le componenti e il bordo della finestra
root.configure(padx=10, pady=10)

# Etichetta per visualizzare il percorso dell'immagine selezionata
img_label = tk.Label(root, text="Nessuna immagine selezionata")
img_label.pack()

# Pulsante per selezionare un'immagine
browse_button = tk.Button(root, text="Scegli Immagine", command=browse_image)
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
process_button = tk.Button(root, text="Elabora Immagine", command=process_image, state=tk.DISABLED)
process_button.pack()

# Aggiungi funzione di abilitazione del pulsante di elaborazione
F_entry.bind("<KeyRelease>", lambda event: enable_process_button())
d_entry.bind("<KeyRelease>", lambda event: enable_process_button())

# Avvio del loop principale della finestra
root.mainloop()
