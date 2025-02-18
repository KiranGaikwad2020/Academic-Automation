import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# Function to categorize students
def categorize_students(input_file, output_file, outstanding_min, good_min):
    try:
        # Read the Excel file
        df = pd.read_excel(input_file, engine='openpyxl')

        # Ensure the required columns are present
        if 'Name' not in df.columns or 'Marks' not in df.columns:
            messagebox.showerror("Error", "Input file must contain 'Name' and 'Marks' columns.")
            return
        
        # Define categorization function
        def categorize(marks):
            if marks >= outstanding_min:
                return 'Outstanding'
            elif marks >= good_min:
                return 'Good'
            else:
                return 'Poor'
        
        # Apply categorization
        df['Category'] = df['Marks'].apply(categorize)

        # Save to a new Excel file
        df.to_excel(output_file, index=False)
        messagebox.showinfo("Success", f"Categorized student list saved to:\n{output_file}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open file dialog and select input file
def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*")])
    entry_input_file.delete(0, tk.END)
    entry_input_file.insert(0, file_path)

# Function to start processing
def start_categorization():
    input_file = entry_input_file.get()
    output_file = "categorized_students.xlsx"  # Default output file
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

# Labels and Entry Widgets
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

# Process Button
tk.Button(root, text="Categorize Students", command=start_categorization, bg="green", fg="white").pack(pady=10)

# Run the GUI
root.mainloop()

