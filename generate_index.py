import os

def list_json_files():
    db_dir = 'db'
    
    # Check if the db folder exists
    if not os.path.exists(db_dir):
        print(f"Error: The '{db_dir}' folder was not found in the current directory.")
        return
        
    # Get all .json files and sort them alphabetically
    json_files = [f for f in os.listdir(db_dir) if f.endswith('.json')]
    json_files.sort()
    
    if not json_files:
        print(f"No JSON files found in the '{db_dir}' folder.")
        return
        
    # Print the exact format needed for index.html
    print("\n✅ Success! Copy the code below and paste it into your index.html:\n")
    print("-" * 50)
    print("const DB_FILES = [")
    for i, f in enumerate(json_files):
        # Add a comma to all except the last one (optional, but cleaner)
        if i < len(json_files) - 1:
            print(f'    "{f}",')
        else:
            print(f'    "{f}"')
    print("];")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    list_json_files()