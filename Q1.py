import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import json

def clean_data(value):
    """Clean up extra quote characters from the data."""
    return value.replace('"', '').strip()

def convert_csv_to_json():
    filename = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV Files", "*.csv")])
    if not filename:
        messagebox.showerror("Error", "You didn't select a file.")
        return
    
    sales_data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cleaned_row = {key: clean_data(value) for key, value in row.items()}
                sales_data.append(cleaned_row)
        
        save_filename = filedialog.asksaveasfilename(title="Save JSON File", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
        if not save_filename:
            messagebox.showerror("Error", "You didn't specify a file to save.")
            return
        
        with open(save_filename, 'w', encoding='utf-8') as json_file:
            json.dump(sales_data, json_file, indent=4)

        messagebox.showinfo("Success", "Data successfully converted and saved.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def open_conversion_window():
    conversion_window = tk.Toplevel(root)
    conversion_window.title("Convert CSV to JSON")
    conversion_window.geometry("300x100")
    conversion_window.configure(bg="#005A4E")  # Slightly dark green background

    convert_button = tk.Button(conversion_window, text="Convert", command=convert_csv_to_json, bg="#007B6E", fg="white")
    convert_button.pack(pady=20)

def quit_program():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Sales Data Converter")
root.geometry("400x200")
root.configure(bg="#005A4E")  # Slightly dark green background

convert_window_button = tk.Button(root, text="Open Converter", command=open_conversion_window, bg="#007B6E", fg="white")
convert_window_button.pack(pady=20)

quit_button = tk.Button(root, text="QUIT", command=quit_program, bg="#007B6E", fg="white")
quit_button.pack(pady=20)

root.mainloop()
