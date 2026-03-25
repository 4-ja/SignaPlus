import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil

class HelpGUI(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("AutoSignatory - How To & FAQ")
        self.geometry("450x500")
        self.configure(bg="white")
        
        # Icon/Header
        tk.Label(self, text="📖 User Guide", font=("Segoe UI", 16, "bold"), bg="white", pady=20).pack()

        # Instructions Text
        instructions = [
            ("1. Automation Folder", "Place any file in the 'To_Be_Signed' folder.\nThe app signs and moves it automatically."),
            ("2. Drag & Drop", "You can also drag files directly onto the\nDashboard to sign them instantly."),
            ("3. Signature Setup", "Go to Settings (⚙) to set your name.\nThe app looks for this name in PDFs to place your sig."),
            ("4. Daily Folders", "Signed files are saved in 'Signed_Documents'\norganized by the current date."),
            ("5. Reveal File", "Double-click any row in the list to open\nFile Explorer and highlight that file.")
        ]

        for title, desc in instructions:
            frame = tk.Frame(self, bg="white", pady=5)
            frame.pack(fill="x", padx=30)
            tk.Label(frame, text=title, font=("Segoe UI", 10, "bold"), bg="white", fg="#0078d4").pack(anchor="w")
            tk.Label(frame, text=desc, font=("Segoe UI", 9), bg="white", justify="left").pack(anchor="w")

        ttk.Button(self, text="Got it!", command=self.destroy).pack(pady=20)

class SettingsGUI(tk.Toplevel):
    def __init__(self, parent, current_name, save_callback):
        super().__init__(parent)
        self.title("AutoSignatory Settings")
        self.geometry("400x320")
        self.configure(bg="white")
        self.save_callback = save_callback
        
        tk.Label(self, text="Configuration", font=("Segoe UI", 12, "bold"), bg="white").pack(pady=15)
        tk.Label(self, text="Signatory Name (Text to find):", bg="white").pack(anchor="w", padx=40)
        self.name_entry = tk.Entry(self, font=("Segoe UI", 10), width=30)
        self.name_entry.insert(0, current_name)
        self.name_entry.pack(pady=5, padx=40)

        tk.Label(self, text="Signature Image:", bg="white").pack(anchor="w", padx=40, pady=(10,0))
        ttk.Button(self, text="Select Signature Image...", command=self.pick_signature).pack(pady=5, padx=40, fill="x")
        ttk.Button(self, text="Save Settings", command=self.save).pack(pady=30, padx=40, fill="x")

    def pick_signature(self):
        file = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file:
            if not os.path.exists("Signature"): os.makedirs("Signature")
            shutil.copy(file, "Signature/signature.png")
            messagebox.showinfo("Success", "Signature image updated!")

    def save(self):
        self.save_callback(self.name_entry.get())
        self.destroy()

class DownloadStyleGUI(tk.Toplevel):
    def __init__(self, parent, open_settings_callback, open_help_callback):
        super().__init__(parent)
        self.title("AutoSignatory - Dashboard")
        self.geometry("650x500")
        self.configure(bg="#f5f5f7")
        
        header_frame = tk.Frame(self, bg="#f5f5f7")
        header_frame.pack(fill="x")
        
        tk.Label(header_frame, text="Recent Signatures", font=("Segoe UI", 14, "bold"), 
                 bg="#f5f5f7", fg="#1d1d1f", padx=20, pady=15).pack(side="left")
        
        # Buttons for Settings and Help
        btn_frame = tk.Frame(header_frame, bg="#f5f5f7")
        btn_frame.pack(side="right", padx=10)
        
        ttk.Button(btn_frame, text="❓ Help", command=open_help_callback).pack(side="right", padx=5)
        ttk.Button(btn_frame, text="⚙ Settings", command=open_settings_callback).pack(side="right", padx=5)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=35, font=("Segoe UI", 10))
        
        self.tree = ttk.Treeview(self, columns=("filename", "date", "status"), show="headings")
        self.tree.heading("filename", text="Filename")
        self.tree.heading("date", text="Date Modified")
        self.tree.heading("status", text="Status")
        self.tree.column("filename", width=250)
        self.tree.column("date", width=150)
        self.tree.column("status", width=100)
        self.tree.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def add_task_row(self, filename, date_mod, status):
        self.tree.insert('', 0, values=(filename, date_mod, status))