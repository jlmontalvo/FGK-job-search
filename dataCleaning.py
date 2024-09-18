import json
import re

# Function to extract "carrera" from the job description
def extract_carrera(description):
    # Clean up the description by removing unnecessary escape characters
    description = description.replace('\r\n', ' ').replace('\t', ' ')
    
    # Regular expression to capture common academic degree mentions
    carrera_patterns = [
        r'(Ingeniero[a]?\s[\w\s]+)',
        r'(Maestría en[\w\s,]+)',
        r'(Bachiller[a]?)',
        r'(Licenciad[o|a]\s[\w\s]+)',
        r'(Certificación en[\w\s]+)',
        r'(Técnico en[\w\s]+)',
        r'(Doctor[a]?\s[\w\s]+)',
    ]
    
    carrera = []

    # Check for academic keywords
    for pattern in carrera_patterns:
        matches = re.findall(pattern, description, re.IGNORECASE)
        if matches:
            carrera.extend([match.strip() for match in matches])

    return carrera

spanish_numbers = {
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
}

# Function to convert Spanish words to numbers
def word_to_number(word):
    return spanish_numbers.get(word.lower())

# Function to extract the lowest number of years from "Nivel de Experiencia"
def extract_experience_level(experience_str):
    # If the experience mentions "Sin experiencia", set it to 0
    if "sin experiencia" in experience_str.lower() or "menos de un año" in experience_str.lower():
        return 0
    
    # Print for debugging purposes
    print("with experiencia")
    print(experience_str)

    # Use regex to specifically look for ranges like "De uno a tres años" or similar
    match_range = re.findall(r'de\s+(\w+)\s+a\s+(\w+)\s+años?', experience_str, re.IGNORECASE)
    
    # Debugging output to see matched ranges
    print(match_range)

    # If we find a range with word-based numbers, convert them to digits
    if match_range:
        lower_bound_word = match_range[0][0]
        upper_bound_word = match_range[0][1]
        
        lower_bound = word_to_number(lower_bound_word) or int(lower_bound_word)
        upper_bound = word_to_number(upper_bound_word) or int(upper_bound_word)
        
        return lower_bound

    # If no range, check for any individual years mentioned as words or digits
    match_single = re.findall(r'(\d+|uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez)\s+años?', experience_str, re.IGNORECASE)

    # If we find any single years mentioned, return the smallest one
    if match_single:
        # Convert any word-based numbers to digits
        numbers = [word_to_number(word) if word.isalpha() else int(word) for word in match_single]
        return min(numbers)
    
    # If no years found, return None
    return None
# Load jobs from a JSON file
def load_jobs_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        jobs = json.load(file)
    return jobs

# Save the updated jobs back to a JSON file
def save_jobs_to_json(jobs, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(jobs, file, ensure_ascii=False, indent=4)

# Function to process all jobs and update both carreras and experience level
def process_jobs(jobs):
    for job in jobs:
        # Process and add carreras
        description = job.get("Descripción", "")
        carrera = extract_carrera(description)
        job["Carreras"] = carrera  # Add the extracted carreras to the job object

        # Process and update experience level
        experience_str = job.get("Nivel de Experiencia", "")
        experience_level = extract_experience_level(experience_str)
        
        # Update the experience level if we successfully extracted a number
        if experience_level is not None:
            job["Nivel de Experiencia"] = experience_level

# Main execution
json_file_path = 'job_details.json'  # Path to your input JSON file
output_file_path = 'jobs_data_updated.json'  # Path to your output JSON file

# Load jobs from JSON
jobs_data = load_jobs_from_json(json_file_path)

# Process each job to extract and add "Carreras" and update "Nivel de Experiencia"
process_jobs(jobs_data)

# Save the updated jobs back to a new JSON file
save_jobs_to_json(jobs_data, output_file_path)

print(f"Updated jobs saved to {output_file_path}")
