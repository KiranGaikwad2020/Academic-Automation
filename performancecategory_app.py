import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# Function to categorize students
def categorize_students(input_file, output_file, outstanding_min, good_min):
    try:
        df = pd.read_excel(input_file)

        if 'Name' not in df.columns or 'Marks' not in df.columns:
            messagebox.showerror("Error", "Input file must contain 'Name' and 'Marks' columns.")
            return
        
        def categorize(marks):
            if marks >= outstanding_min:
                return 'Outstanding'
            elif marks >= good_min:
                return 'Good'
            else:
                return 'Poor'
        
        df['Category'] = df['Marks'].apply(categorize)
        df.to_excel(output_file, index=False)
        messagebox.showinfo("Success", f"Categorized student list saved to:\n{output_file}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    entry_input_file.delete(0, tk.END)
    entry_input_file.insert(0, file_path)

def start_categorization():
    input_file = entry_input_file.get()
    output_file = "/app/output/categorized_students.xlsx"  # Save in a fixed location inside container
    try:
        outstanding_min = int(entry_outstanding.get())
        good_min = int(entry_good.get())

        if not input_file:
            messagebox.showwarning("Warning", "Please select an input file.")
            return
        
        categorize_students(input_file, output_file, outstanding_min, good_min)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for marks.")

# Create GUI window
root = tk.Tk()
root.title("Student Data Classification")
root.geometry("400x300")

tk.Label(root, text="Select Input Excel File:").pack(pady=5)
entry_input_file = tk.Entry(root, width=40)
entry_input_file.pack()
tk.Button(root, text="Browse", command=select_input_file).pack(pady=5)

tk.Label(root, text="Minimum Marks for Outstanding:").pack(pady=5)
entry_outstanding = tk.Entry(root)
entry_outstanding.pack()

tk.Label(root, text="Minimum Marks for Good:").pack(pady=5)
entry_good = tk.Entry(root)
entry_good.pack()

tk.Button(root, text="Categorize Students", command=start_categorization, bg="green", fg="white").pack(pady=10)

root.mainloop()
