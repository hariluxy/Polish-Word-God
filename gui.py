import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from save_operations import load_words_from_file, save_results_to_files
from word_analysis import analyze_words

def run_analysis(words, output_dir=None):
    print(f"Running analysis on: {words}")
    results = analyze_words(words)
    if output_dir:
        save_results_to_files(results, output_dir)
    update_table(results)
    messagebox.showinfo("Success", "Analysis complete. Results saved in the specified directory." if output_dir else "Analysis complete. Results displayed in the table.")

def update_table(results):
    # Clear the table
    for row in table.get_children():
        table.delete(row)
    # Insert new results
    for result in results:
        table.insert("", "end", values=result)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().strip()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, words)

def select_output_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        entry_output_directory.delete(0, tk.END)
        entry_output_directory.insert(0, directory_path)

def start_analysis():
    print("Start Analysis button clicked")
    word_file = entry_file_path.get()
    output_dir = entry_output_directory.get() if save_to_file_var.get() else None
    if save_to_file_var.get() and not output_dir:
        messagebox.showwarning("Input Error", "Please select an output directory.")
        return

    delimiter = delimiter_var.get()
    if word_file:
        words = load_words_from_file(word_file)
    else:
        words_text = text_box.get(1.0, tk.END).strip()
        if not words_text:
            messagebox.showwarning("Input Error", "Please enter words or select a file.")
            return
        # Split words based on the selected delimiter
        if delimiter == 'New line':
            words = [word.strip() for word in words_text.split('\n') if word.strip()]
        elif delimiter == 'Semicolon':
            words = [word.strip() for word in words_text.split(';') if word.strip()]
        elif delimiter == 'Regular speech':
            words = [word.strip() for word in words_text.split(' ') if word.strip()]

    run_analysis(words, output_dir)

def create_gui(root):
    global entry_file_path, entry_output_directory, save_to_file_var, text_box, delimiter_var, table

    # Create and place widgets
    label_file_path = tk.Label(root, text="Select Word List File (optional):")
    label_file_path.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_file_path = tk.Entry(root, width=50)
    entry_file_path.grid(row=0, column=1, padx=10, pady=5)
    button_browse_file = tk.Button(root, text="Browse", command=select_file)
    button_browse_file.grid(row=0, column=2, padx=10, pady=5)

    label_output_directory = tk.Label(root, text="Select Output Directory (optional):")
    label_output_directory.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_output_directory = tk.Entry(root, width=50)
    entry_output_directory.grid(row=1, column=1, padx=10, pady=5)
    button_browse_directory = tk.Button(root, text="Browse", command=select_output_directory)
    button_browse_directory.grid(row=1, column=2, padx=10, pady=5)

    save_to_file_var = tk.IntVar()
    checkbox_save_to_file = tk.Checkbutton(root, text="Save results to file", variable=save_to_file_var)
    checkbox_save_to_file.grid(row=1, column=3, padx=10, pady=5, sticky="w")

    label_text_box = tk.Label(root, text="You may also enter words directly:")
    label_text_box.grid(row=2, column=0, padx=10, pady=5, sticky="ne")
    text_box = tk.Text(root, width=50, height=10)
    text_box.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

    label_delimiter = tk.Label(root, text="Select delimiter:")
    label_delimiter.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    delimiter_var = tk.StringVar(value="New line")
    delimiter_options = ttk.Combobox(root, textvariable=delimiter_var, values=["New line", "Semicolon", "Regular speech"], state="readonly")
    delimiter_options.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    button_start = tk.Button(root, text="Start Analysis", command=start_analysis)
    button_start.grid(row=4, column=1, padx=10, pady=20)

    # Create and place the table for displaying results
    columns = ("Initial Word", "Base Form", "POS")
    table = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        table.heading(col, text=col)
    table.grid(row=5, column=0, columnspan=3, padx=10, pady=20)
