import requests
from bs4 import BeautifulSoup
import csv
import json

# Step 1: Get the total number of pages
def get_total_pages(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        pagination = soup.find_all('li')
        last_page = 1
        for page in pagination:
            page_link = page.find('a', href=True)
            if page_link and 'Page=' in page_link['href']:
                try:
                    page_number = int(page_link.text)
                    if page_number > last_page:
                        last_page = page_number
                except ValueError:
                    pass  # In case it's not a valid number
        return last_page
    else:
        print("Failed to retrieve the page count")
        return 1  # Default to 1 if the request fails

# Step 2: Scrape job details from the href
def get_job_details(job_url):
    response = requests.get(job_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extraer Nombre de la Posición
    try:
        job_title = soup.find('h1').text.strip()
    except AttributeError:
        job_title = 'N/A'

    # Extraer Tipo de Contratación
    try:
        tipo_contratacion = soup.find('td', text='Tipo de Contratación').find_next_sibling('td').text.strip()
    except AttributeError:
        tipo_contratacion = 'N/A'

    # Extraer Nivel de Experiencia
    try:
        nivel_experiencia = soup.find('td', text='Nivel de Experiencia').find_next_sibling('td').text.strip()
    except AttributeError:
        nivel_experiencia = 'N/A'

    # Extraer Salario Máximo y Mínimo
    try:
        salario_max = soup.find('td', text='Salario máximo (USD)').find_next_sibling('td').text.strip()
    except AttributeError:
        salario_max = 'N/A'
    
    try:
        salario_min = soup.find('td', text='Salario minimo (USD)').find_next_sibling('td').text.strip()
    except AttributeError:
        salario_min = 'N/A'

    # Extraer Departamento
    try:
        departamento = soup.find('td', text='Departamento').find_next_sibling('td').text.strip()
    except AttributeError:
        departamento = 'N/A'

    # Extraer Descripción
    try:
        descripcion = soup.find('meta', attrs={'name': 'description'})['content'].strip()
    except AttributeError:
        descripcion = 'N/A'

    # Devolver los detalles en un diccionario
    return {
        'URL': job_url,
        'Title': job_title,
        'Tipo de Contratación': tipo_contratacion,
        'Nivel de Experiencia': nivel_experiencia,
        'Salario Mínimo (USD)': salario_min,
        'Salario Máximo (USD)': salario_max,
        'Departamento': departamento,
        'Descripción': descripcion
    }

def scrape_jobs(total_pages):
    base_url = "https://www.tecoloco.com.sv/empleos"
    params = {
        "Keywords": "",
        "autosuggestEndpoint": "/autosuggest",
        "Categoria": "1",
        "PaisId": "21",
        "btnSubmit": " ",
        "Page": 1
    }

    job_details_list = []
    visited_urls = set()  # Set to store unique URLs

    for page in range(1, total_pages + 1):
        params['Page'] = page
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all job entries that have both 'jobid' and 'href'
            job_entries = soup.find_all('a', {'jobid': True, 'href': True})

            for job in job_entries:
                href = "https://www.tecoloco.com.sv" + job['href']  # Construir la URL completa del trabajo

                if href not in visited_urls:
                    visited_urls.add(href)  # Add to set to avoid duplicate processing
                    print(f"Scraping job at: {href}")

                    # Obtener detalles del trabajo
                    job_details = get_job_details(href)
                    job_details_list.append(job_details)
        else:
            print(f"Failed to retrieve page {page}")

    # Guardar los detalles de los trabajos en un archivo JSON
    with open('job_details.json', 'w', encoding='utf-8') as f:
        json.dump(job_details_list, f, indent=4, ensure_ascii=False)

# Main execution
start_url = "https://www.tecoloco.com.sv/empleos?Keywords=&autosuggestEndpoint=%2fautosuggest&Categoria=1&PaisId=21&btnSubmit=%20"

total_pages = get_total_pages(start_url)
print(f"Total pages found: {total_pages}")

# Step 4: Start scraping the job data based on the total pages
scrape_jobs(total_pages)
