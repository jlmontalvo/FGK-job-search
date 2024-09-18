import json
import re

# Define the categories
career_mapping = {
    "tecnico en sistemas": [
        r'técnico en sistemas', r'técnico en informática', r'técnico en computación', r'técnico en redes'
    ],
    "ingeniero en sistemas": [
        r'ingeniero en sistemas', r'ingeniero en informática', r'ingeniero de software'
    ],
    "tecnico en mercadeo": [
        r'técnico en mercadeo', r'técnico en marketing'
    ],
    "licenciado en mercadeo": [
        r'licenciado en mercadeo', r'licenciado en marketing'
    ],
    "licenciado en finanzas y/o economia": [
        r'licenciado en finanzas', r'licenciado en economía', r'maestría en finanzas'
    ],
    "tecnico en contabilidad": [
        r'técnico en contabilidad', r'técnico en contaduría'
    ],
    "licenciado en contabilidad": [
        r'licenciado en contabilidad', r'licenciado en contaduría'
    ],
    "administrador de empresas": [
        r'administrador de empresas', r'licenciado en administración'
    ],
    "tecnico en diseno": [
        r'técnico en diseño', r'técnico en multimedia', r'técnico en diseño gráfico'
    ],
    "licenciado en diseno": [
        r'licenciado en diseño', r'licenciado en diseño gráfico'
    ],
    "licenciado en comunicaciones": [
        r'licenciado en comunicaciones', r'licenciado en ciencias de la comunicación'
    ],
    "multimedia": [
        r'técnico en multimedia', r'técnico en comunicación audiovisual'
    ],
    "tecnico mecatronica": [
        r'técnico en mecatrónica'
    ],
    "ingeniero industrial": [
        r'ingeniero industrial', r'técnico en ingeniería industrial'
    ],
    "tecnico civil": [
        r'técnico en ingeniería civil'
    ],
    "agronomia": [
        r'técnico en agronomía', r'ingeniero agrónomo'
    ]
}

# Load JSON data
with open('jobs_data_updated.json', 'r', encoding='utf-8') as file:
    jobs_data = json.load(file)

# Helper function to categorize careers
def categorize_carrera(carrera):
    carrera = carrera.lower()
    for category, patterns in career_mapping.items():
        for pattern in patterns:
            if re.search(pattern, carrera, re.IGNORECASE):
                return category
    return "other"

# Process each job to map and categorize the career fields
for job in jobs_data:
    carreras = job.get("Carreras", [])
    categorized_carreras = []

    for carrera in carreras:
        categorized_carreras.append(categorize_carrera(carrera))

    # Replace the Carreras with the categorized ones
    job["Carreras"] = categorized_carreras if categorized_carreras else ["sin especificar"]

# Save the updated data back to the JSON file
with open('jobs_data_categorized.json', 'w', encoding='utf-8') as outfile:
    json.dump(jobs_data, outfile, ensure_ascii=False, indent=4)

print("Updated job data has been saved to 'jobs_data_categorized.json'")
