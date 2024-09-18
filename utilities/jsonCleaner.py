import json

# Load JSON data from a file
def load_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Save JSON data to a file
def save_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Function to remove duplicates from JSON data
def remove_duplicates(data):
    unique_items = []
    seen = set()

    for item in data:
        # Convert the item to a tuple of key-value pairs, then to a hashable form (tuple)
        item_tuple = tuple(sorted(item.items()))
        
        # Add unique items to the list
        if item_tuple not in seen:
            seen.add(item_tuple)
            unique_items.append(item)
    
    return unique_items

# Main function to load, process, and save JSON data
def main(input_file, output_file):
    # Load JSON data
    data = load_json(input_file)

    # Remove duplicates
    unique_data = remove_duplicates(data)

    # Save the cleaned JSON data
    save_json(unique_data, output_file)
    print(f"Removed duplicates. Cleaned data saved to {output_file}.")

# Run the script
if __name__ == "__main__":
    input_file = "job_details.json"  # Input file containing the JSON data
    output_file = "cleaned_output.json"  # Output file to save the cleaned JSON data

    main(input_file, output_file)
