import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance  # Pillow for image processing
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

# Function to open file dialog
def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    entry_input_file.delete(0, tk.END)
    entry_input_file.insert(0, file_path)

# Function to start processing
def start_categorization():
    input_file = entry_input_file.get()
    output_file = "categorized_students.xlsx"
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
root.title("Student Data Classification By Dr KPG")
root.geometry("500x400")
root.resizable(False, False)

# Load background image and apply dark overlay
bg_image = Image.open("mmit-logo.jpg").resize((500, 400), Image.LANCZOS)
dark_overlay = Image.new("RGBA", (500, 400), (0, 0, 0, 100))  # Semi-transparent black overlay
bg_image = Image.alpha_composite(bg_image.convert("RGBA"), dark_overlay).convert("RGB")
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Styling
label_font = ("Arial", 11, "bold")
entry_bg = "#f0f0f0"  # Light background for better contrast
entry_fg = "#000000"  # Black text for readability
btn_bg = "#008000"  # Green button
btn_fg = "#ffffff"  # White text on button

# Labels and Entry Widgets
canvas.create_text(250, 30, text="Student Data Classification", font=("Arial", 14, "bold"), fill="white")

tk.Label(root, text="Select Input Excel File:", font=label_font, fg="white", bg="black").place(x=40, y=60)
entry_input_file = tk.Entry(root, width=40, bg=entry_bg, fg=entry_fg, relief="solid")
entry_input_file.place(x=40, y=85)
tk.Button(root, text="Browse", command=select_input_file, bg=btn_bg, fg=btn_fg).place(x=400, y=80)

tk.Label(root, text="Minimum Marks for Outstanding:", font=label_font, fg="white", bg="black").place(x=40, y=120)
entry_outstanding = tk.Entry(root, width=10, bg=entry_bg, fg=entry_fg, relief="solid")
entry_outstanding.place(x=320, y=120)

tk.Label(root, text="Minimum Marks for Good:", font=label_font, fg="white", bg="black").place(x=40, y=160)
entry_good = tk.Entry(root, width=10, bg=entry_bg, fg=entry_fg, relief="solid")
entry_good.place(x=320, y=160)

# Process Button
tk.Button(root, text="Categorize Students", command=start_categorization, bg=btn_bg, fg=btn_fg, font=("Arial", 12, "bold")).place(x=170, y=220)

# Run the GUI
root.mainloop()
