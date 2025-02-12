#This python script automates the classification of student data based on Marks into Outstanding,Good and Poor classes

import pandas as pd

#Following function takes the input xlsx file and generates the output xlsx file 

def categorize_students(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)
    
    # Ensure the column names are correctly matched
    if 'Name' not in df.columns or 'Marks' not in df.columns:
        raise ValueError("Input file must contain 'Name' and 'Marks' columns")
    
    # Define categorization function
    def categorize(marks):
        if marks >= 10:
            return 'Outstanding'
        elif marks >= 7:
            return 'Good'
        else:
            return 'Poor'
    
    # Apply categorization
    df['Category'] = df['Marks'].apply(categorize)
    
    # Save to a new Excel file
    df.to_excel(output_file, index=False)
    print(f"Categorized student list saved to {output_file}")

# Classification usage
input_excel = "Slowlearner.xlsx"  # Input file with columns: Name, Marks
output_excel = "categorized_students.xlsx"
categorize_students(input_excel, output_excel)

