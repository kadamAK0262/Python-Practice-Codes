import pandas as pd

df = pd.read_csv('customer.csv')

# Export DataFrame to a CSV file
df.to_csv('output.csv', index=False)

# Export DataFrame to an Excel file
df.to_excel('output2.xlsx', index=False)

# Export DataFrame to a JSON file
df.to_json('output.json', orient='records')










# openpyxl is a Python library that allows you to read from and write to Excel files using Python. 
# It provides functionality to create, modify, and extract data from Excel files in the .xlsx format, 
# which is the default format used by Microsoft Excel since Excel 2007.

# Command
# pip install openpyxl

# Reading and Writing Excel Files: openpyxl allows you to read data from existing Excel files and 
# write new data to Excel files.

# Manipulating Worksheets and Cells: You can create, modify, and delete worksheets in Excel 
# files using openpyxl. Additionally, you can access and modify individual cells within a worksheet.

# Styling and Formatting: openpyxl provides functionality to apply styles and formatting to cells, 
# such as setting fonts, colors, borders, and alignment.

# Formula Support: You can define and manipulate formulas within cells using openpyxl, 
# allowing you to perform calculations and data analysis directly within Excel files.

# Chart Creation: openpyxl supports creating charts and graphs within Excel files, 
# allowing you to visualize data directly in Excel.