import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk

import sys
from pathlib import Path
from ips_util import Patch
import ips
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
import sys

data_dir = "";
# 
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'): data_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))



def single(base_patch, Datts,out):
    # Get Offset And build ID
    build_id = Datts[:64]
    offset = int(Datts[64:-1] + Datts[-1])

    print(Datts)
    print(build_id)
    print(offset)
    
    tmp_p = ips.Patch()

    for r in base_patch.records:
        tmp_p.add_record(r.offset + offset, r.content, r.rle_size)
    if not os.path.exists(out): os.mkdir(Path(out))
    # Build the patch
    patch_path = Path(out, f"{build_id}.ips")
    # Save the patch
    with patch_path.open("w+b") as f:
        f.write(bytes(tmp_p))


def multiple(base_patch, Datts,out):
    print(base_patch)
    print(Datts)

    for line in Datts:
        print(Datts[line])
        single(base_patch, Datts[line],out)


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logo para Switch -.- v3.4")
        self.geometry("425x170")
        self.configure(background="#60b6eb")
        file_path = os.path.join(data_dir, 'icon.ico')
        self.iconbitmap(file_path) 
        # Evitar que la ventana se pueda redimensionar
        self.resizable(False, False)
        # Evitar que la ventana se pueda maximizar

        # Diccionario para las opciones
        self.list = {}
        
        # Combobox (menú desplegable)
        self.myselect = ttk.Combobox(self, state="readonly",width=7)
        self.myselect.place(x=330, y=120)
        self.myselect.bind("<<ComboboxSelected>>", self.on_select)
        self.load_data()#Cargar data.txt
        latest = self.myselect['values'][-1]

        # Etiqueta de información
        self.label = tk.Label(self, text=f"PNG To IPS Logo Creator 1.0.0 -.- {latest}\n  \"PNG\" \"308x350\" \"RGBA\"",
                              font=("Times New Roman", 10), bg="#a5cbf0")
        ToolTip(self.label, "Esta es una Herramienta para cambiar el logo a la Nintendo Switch")
        self.label.place(x=10, y=10)

        # Campo de registro
        self.logs = tk.Label(self, bg="#60b6eb")
        self.logs.place(x=10, y=65)
        self.logs.config(text="")

        # Botón de conversión
        self.convert_button = tk.Button(self, text="Convertir", bg="#056aab", fg="white", width=15, height=2, command=self.process, bd=2,highlightcolor="white", highlightbackground="white", relief=tk.FLAT)
        self.convert_button.place(x=10, y=100)
        self.add_hover_effect(self.convert_button, "#056aab", "#035a91")

        # Botón de Abrir
        self.open_button  = tk.Button(self, text="Abrir", bg="#0994ed", fg="white", width=5, height=2, command=self.openFolder, bd=2,highlightcolor="white", highlightbackground="white", relief=tk.FLAT)
        self.open_button .place(x=145, y=100)
        self.add_hover_effect(self.open_button, "#0994ed", "#077acc")

        # Imagen de vista previa
        self.prev = tk.Label(self, bg="#fff", width=105, height=105)
        self.prev.place(x=305, y=10)
        self.prev.bind("<Button-1>", self.select_file)
        self.add_hover_effect(self.prev, "#fff", "#077acc")

        # Ruta inicial de la imagen
        self.default_img()

        # Etiqueta de créditos
        self.credit = tk.Label(self, text="By D3fau4 & Kronos2308", font=("Times New Roman", 10), bg="#60b6eb")
        ToolTip(self.credit, "Los Culpables")
        self.credit.place(x=230, y=145)

    
    def add_hover_effect(self,widget, normal_color, hover_color):
            widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
            widget.bind("<Leave>", lambda e: widget.config(bg=normal_color))


    def load_image(self):
        try:
            img = Image.open(self.file_path)
            
            # Verificar dimensiones
            if img.size != (308, 350):
                self.logs.config(text="La imagen debe ser de 308x350 píxeles.")
                #messagebox.showerror("Tamaño incorrecto", "La imagen debe ser de 308x350 píxeles.")
                self.default_img()
                return  # o raise Exception o lo que quieras hacer en caso de error

            img = img.resize((105, 105), Image.LANCZOS)
            self.img = ImageTk.PhotoImage(img)
            self.prev.config(image=self.img, text="")  # Limpia el texto y muestra la imagen
            
        except Exception as e:
            print(f"Error loading image: {e}")

    def load_data(self):
        options = ["Todos"]
        try:
            file_path = os.path.join(data_dir, 'data.txt')
            with open(file_path, "r") as f:
                for line in f:
                    text, value1, value2 = line.strip().split(",")
                    self.list[text] = value1 + value2
                    options.append(text)
            self.myselect['values'] = options
            self.myselect.current(0)  # Set default value to "Todos"
        except Exception as e:
            print(f"Error loading data: {e}")

    def select_file(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            self.load_image()
    def default_img(self):
        self.file_path = os.path.join(data_dir, 'temp.png')
        self.load_image()

    def openFolder(self):
        os.startfile("ips")
        self.logs.config(text="")
    def process(self):
        try:
            file = self.file_path.replace("file:///", "").replace("%20", " ")
            datas = self.myselect.get()
            print(self.list)

            self.logs.config(text="Creando ips Espere...")
            
            # Load the new Image 
            new_logo = Image.open(file)
            new_logo = new_logo.convert("RGBA")

            # Load the base image
            file_path = os.path.join(data_dir, 'logo.png')
            old_logo = Image.open(file_path)
            old_logo = old_logo.convert("RGBA")
            
            base_patch = ips.Patch.create(old_logo.tobytes(), new_logo.tobytes())
            
            out="ips\\atmosphere\\exefs_patches\\logo"
            os.makedirs(out, exist_ok=True)
            if datas == "Todos":
                multiple(base_patch, self.list,out)
            else:
                single(base_patch, self.list[datas],out)
            
            if not os.listdir(out):
                messagebox.showerror("Fallido", f"Ha habido un error convirtiendo:\n{file}")
            else:
                self.logs.config(text="Terminado, Usa Abrir 🔽🔽")

        except Exception as e:
            messagebox.showerror("Error", f"Error durante el proceso: {e}")

    def on_select(self, event):
        selected = self.myselect.get()
        print(f"Seleccionado: {selected}")

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Sin bordes ni título
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("Times New Roman", 9))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()



if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
