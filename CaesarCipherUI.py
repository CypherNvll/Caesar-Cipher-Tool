import CaesarCipher
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Tool")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # theme
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # tabs
        self.file_tab = ttk.Frame(self.notebook)
        self.string_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.file_tab, text="File Encryption")
        self.notebook.add(self.string_tab, text="String Encryption")
        
        # file tab
        self.setup_file_tab()
        
        # string tab
        self.setup_string_tab()
        
        # status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_file_tab(self):
        # file selection frame
        file_frame = ttk.LabelFrame(self.file_tab, text="File Selection", padding="10")
        file_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(file_frame, text="File/Folder Path:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.file_path_var = tk.StringVar()
        self.file_path_entry = ttk.Entry(file_frame, textvariable=self.file_path_var, width=50)
        self.file_path_entry.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)
        
        ttk.Button(file_frame, text="Browse...", command=self.browse_file).grid(row=0, column=2, padx=5, pady=5)
        
        # operation frame
        op_frame = ttk.LabelFrame(self.file_tab, text="Operation", padding="10")
        op_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.operation_var = tk.StringVar(value="encrypt")
        ttk.Radiobutton(op_frame, text="Encrypt", variable=self.operation_var, value="encrypt").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Radiobutton(op_frame, text="Decrypt", variable=self.operation_var, value="decrypt").grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # shift value frame
        shift_frame = ttk.LabelFrame(self.file_tab, text="Shift Value", padding="10")
        shift_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(shift_frame, text="Shift:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.shift_var = tk.StringVar(value="5")
        self.shift_entry = ttk.Entry(shift_frame, textvariable=self.shift_var, width=10)
        self.shift_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(shift_frame, text="(Default: 5)").grid(row=0, column=2, sticky=tk.W, pady=5)
        
        # action button
        ttk.Button(self.file_tab, text="Process File", command=self.process_file).pack(pady=20)
    
    def setup_string_tab(self):
        # Text areas frame
        text_frame = ttk.LabelFrame(self.string_tab, text="Text", padding="10")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create a frame for input and output areas
        io_frame = ttk.Frame(text_frame)
        io_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid weights for equal spacing
        io_frame.grid_columnconfigure(0, weight=1)
        io_frame.grid_columnconfigure(1, weight=1)
        
        # Input text frame (left side)
        input_frame = ttk.LabelFrame(io_frame, text="Input", padding="5")
        input_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        self.input_text = tk.Text(input_frame, height=10, wrap=tk.WORD)
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        # Output text frame (right side)
        output_frame = ttk.LabelFrame(io_frame, text="Output", padding="5")
        output_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        
        # Create read-only output text area
        self.output_text = tk.Text(output_frame, height=10, wrap=tk.WORD, bg='#f0f0f0')
        self.output_text.pack(fill=tk.BOTH, expand=True)
        self.output_text.config(state='disabled')  # Make it read-only
        
        # Controls frame
        controls_frame = ttk.Frame(self.string_tab)
        controls_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Operation frame (left side)
        op_frame = ttk.LabelFrame(controls_frame, text="Operation", padding="10")
        op_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        self.string_operation_var = tk.StringVar(value="encrypt")
        ttk.Radiobutton(op_frame, text="Encrypt", variable=self.string_operation_var, value="encrypt").grid(row=0, column=0, sticky=tk.W, pady=5, padx=20)
        ttk.Radiobutton(op_frame, text="Decrypt", variable=self.string_operation_var, value="decrypt").grid(row=0, column=1, sticky=tk.W, pady=5, padx=20)
        
        # Shift value frame (right side)
        shift_frame = ttk.LabelFrame(controls_frame, text="Shift Value", padding="10")
        shift_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        ttk.Label(shift_frame, text="Shift:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.string_shift_var = tk.StringVar(value="5")
        self.string_shift_entry = ttk.Entry(shift_frame, textvariable=self.string_shift_var, width=10)
        self.string_shift_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(shift_frame, text="(Default: 5)").grid(row=0, column=2, sticky=tk.W, pady=5)
        
        # Buttons frame
        button_frame = ttk.Frame(self.string_tab)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Center the buttons
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(3, weight=1)
        
        # Process button
        ttk.Button(button_frame, text="Process Text", command=self.process_string).grid(row=0, column=1, padx=10)
        
        # Copy button
        ttk.Button(button_frame, text="Copy Output", command=self.copy_to_clipboard).grid(row=0, column=2, padx=10)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select File")
        if file_path:
            self.file_path_var.set(file_path)
        else:
            folder_path = filedialog.askdirectory(title="Select Folder")
            if folder_path:
                self.file_path_var.set(folder_path)
    
    def process_file(self):
        file_path = self.file_path_var.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file or folder")
            return
        
        try:
            shift = int(self.shift_var.get())
        except ValueError:
            messagebox.showerror("Error", "Shift value must be an integer")
            return
        
        operation = self.operation_var.get()
        
        try:
            if operation == "encrypt":
                CaesarCipher.cipher(file_path, shift)
                self.status_var.set(f"File '{os.path.basename(file_path)}' encrypted successfully")
            else:
                CaesarCipher.decipher(file_path, shift)
                self.status_var.set(f"File '{os.path.basename(file_path)}' decrypted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Error occurred during processing")
    
    def process_string(self):
        input_text = self.input_text.get("1.0", tk.END)
        if not input_text:
            messagebox.showerror("Error", "Please enter some text")
            return
        
        try:
            shift = int(self.string_shift_var.get())
        except ValueError:
            messagebox.showerror("Error", "Shift value must be an integer")
            return
        
        operation = self.string_operation_var.get()
        
        try:
            if operation == "encrypt":
                result = CaesarCipher.str_cipher(input_text, shift)
            else:
                result = CaesarCipher.str_decipher(input_text, shift)
            
            self.output_text.config(state='normal')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", result)
            self.output_text.config(state='disabled')
            
            self.status_var.set("Text processed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Error occurred during processing")
    
    def copy_to_clipboard(self):
        output_text = self.output_text.get("1.0", tk.END).strip()
        if output_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(output_text)
            self.status_var.set("Text copied to clipboard")
        else:
            messagebox.showinfo("Info", "No text to copy")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()