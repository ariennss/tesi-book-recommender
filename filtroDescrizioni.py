import pandas as pd
import sqlite3

# Step 1: Retrieve the list of book_ids where lcv = 0
db_path = "C:\\tesi\\bookRecommender.db"  # Replace with your actual database path
query = "SELECT book_id FROM Books WHERE lcv = 0"  # SQL query to get book_ids where lcv = 0

# Connect to your SQLite database
conn = sqlite3.connect(db_path)

# Execute the query and get the results
book_ids_from_db = pd.read_sql(query, conn)['book_id'].tolist()

# Step 2: Read the CSV file
csv_file_path = 'C:\\tesi\\inputforpython.csv'  # Replace with your actual CSV file path
df = pd.read_csv(csv_file_path)

# Filter rows where the book_id is in the list from the database
filtered_df = df[df['id'].isin(book_ids_from_db)]

# Step 3: Save the filtered data to a new CSV file
filtered_csv_file_path = 'C:\\Users\\arianna.franchetto\\source\\repos\\WebApplication1\\w2vdescriptions.csv'  # New file path
filtered_df.to_csv(filtered_csv_file_path, index=False)

print(f"Filtered data saved to {filtered_csv_file_path}")