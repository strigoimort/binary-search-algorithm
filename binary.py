import pandas as pd

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_id, _ = arr[mid]  # Extract ID from the tuple
        
        if mid_id == target:
            return arr[mid]  # Target found, return the tuple
        elif mid_id < target:
            left = mid + 1  # Continue search in the right half
        else:
            right = mid - 1  # Continue search in the left half
    
    return None  # Target not found

# Read data from Excel file
excel_file = "data.xlsx"  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Convert ID column to integers
df['ID'] = df['ID'].astype(int)

# Sort the data by ID
df = df.sort_values(by='ID')

# Convert DataFrame to list of tuples
data = [tuple(row) for row in df.to_numpy()]

# Example usage:
target_id = 25  # Replace with the ID you want to search for
result = binary_search(data, target_id)
if result is not None:
    found_id, found_name = result
    print(f"ID: {found_id}, Name: {found_name}")
else:
    print(f"ID {target_id} not found in the Excel file.")
