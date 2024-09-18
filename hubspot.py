# import requests
# import json

# # HubSpot API key or token
# HUBSPOT_API_KEY = 'Bearer pat-na1-f50ca258-982b-4272-9015-23b6bb46810f'  # Replace with your actual API key/token

# headers = {
#     'Authorization': HUBSPOT_API_KEY,
#     'Content-Type': 'application/json'
# }

# # Function to search for contact in HubSpot by email
# def search_contact_by_email(email):
#     url = 'https://api.hubapi.com/crm/v3/objects/contacts/search'
#     payload = {
#         "filterGroups": [
#             {
#                 "filters": [
#                     {
#                         "propertyName": "email",
#                         "operator": "EQ",
#                         "value": email
#                     }
#                 ]
#             }
#         ]
#     }

#     response = requests.post(url, headers=headers, json=payload)

#     if response.status_code == 200:
#         results = response.json().get('results', [])
#         if results:
#             return results[0].get('id')  # Return contact ID
#     else:
#         print(f"Failed to search for contact {email}. Status Code: {response.status_code}, Response: {response.text}")
#     return None

# # Function to search for deals associated with a contact
# def search_deal_by_contact(contact_id):
#     url = 'https://api.hubapi.com/crm/v3/objects/deals/search'
#     payload = {
#         "filterGroups": [
#             {
#                 "filters": [
#                     {
#                         "propertyName": "associations.contact",
#                         "operator": "EQ",
#                         "value": contact_id
#                     }
#                 ]
#             }
#         ]
#     }

#     response = requests.post(url, headers=headers, json=payload)

#     if response.status_code == 200:
#         results = response.json().get('results', [])
#         if results:
#             return results[0].get('id')  # Return the first deal ID associated with the contact
#     else:
#         print(f"Failed to search for deal associated with contact {contact_id}. Status Code: {response.status_code}, Response: {response.text}")
#     return None

# # Function to update the deal with the new date
# def update_deal(deal_id):
#     url = f'https://api.hubapi.com/crm/v3/objects/deals/{deal_id}'
#     payload = {
#         "properties": {
#             "fecha_de_inicio_del_proceso": "2024-09-13"  # 10 Sept 2024 at noon in ISO format
#         }
#     }

#     response = requests.patch(url, headers=headers, json=payload)

#     if response.status_code == 200:
#         print(f"Successfully updated deal {deal_id}.")
#     else:
#         print(f"Failed to update deal {deal_id}. Status Code: {response.status_code}, Response: {response.text}")

# # Function to process each applicant's email
# def process_applicant(email):
#     contact_id = search_contact_by_email(email)
#     if contact_id:
#         deal_id = search_deal_by_contact(contact_id)
#         if deal_id:
#             update_deal(deal_id)
#         else:
#             print(f"No deal found for contact {contact_id}.")
#     else:
#         print(f"No contact found for email {email}.")

# # Step 1: Call GET endpoint to retrieve applicant data from your local API
# local_api_headers = {
#     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikh0YmdMbFgxUng4WFUwT2tzSUlpQSJ9.eyJodHRwczovL2xvY2FsaG9zdDozMDAwL3JvbGVzIjpbIlJvbGVfc3R1ZGVudCJdLCJodHRwczovL2xvY2FsaG9zdDozMDAwL2VtYWlsIjoiaXNoQGlzaC5jb20iLCJpc3MiOiJodHRwczovL2Rldi03a2plMHZubDgyYmVlandxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NmQ3NGQwYjM1NzUxM2Q5ODRlMDk3ZWMiLCJhdWQiOlsidGVzdGVyIiwiaHR0cHM6Ly9kZXYtN2tqZTB2bmw4MmJlZWp3cS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzI2MTk3MDIwLCJleHAiOjE3MjYyODM0MjAsInNjb3BlIjoib3BlbmlkIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgY3JlYXRlOmN1cnJlbnRfdXNlciIsImF6cCI6IkxQbjVZcG84OThkZENLSHJPcjdKamFVZDhWY1VjSlp4IiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmN1cnJlbnRfdXNlciIsInJlYWQ6Y3VycmVudF91c2VyIiwidXBkYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSJdfQ.L2EGrNaswGZxNc4-Ulawg7bnqgaovGC7ZKsJr33z4lY3oBdc9HQy1GN_enbE3vbK_52oh7mU2kAICLUpmFnXhftSR7bYpR73ZYFcM9JZHzw7rXI0oyDSz2AXyEzv-82epMv_yutafPcqZ_Bf5rWedb4W8Cdn2r6EYSo7ZkStq9tJ4hVaURpXUQmiCra8jV806k0IbMfbVRZqujhgcUFuFDz36dKOQx5Vd0Nub-t-ZfygNs8mcGJdasoVgHABwa9fZDNUgOuEz7d5eahbWSYGS_gToruTIF-UMfP_fnZyx_nKHErj7ZsIY-wnt4e88-slY2DxoeuaeaAypMCGXmD8Rw',  # Replace with your local API token if needed
#     'Content-Type': 'application/json'
# }

# get_url = "http://localhost:3000/api/applicants"
# response = requests.get(get_url, headers=local_api_headers)

# if response.status_code == 200:
#     applicants = response.json()

#     # Step 2: Loop through applicants and process each email with HubSpot API
#     for applicant in applicants:
#         email = applicant.get('accountEmail', None)
#         if email:
#             process_applicant(email)
#         else:
#             print("Applicant missing email, skipping.")
# else:
#     print(f"Failed to retrieve applicants. Status code: {response.status_code}")


import requests
import json

# Step 1: Call GET endpoint to retrieve applicant data
headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikh0YmdMbFgxUng4WFUwT2tzSUlpQSJ9.eyJodHRwczovL2xvY2FsaG9zdDozMDAwL3JvbGVzIjpbIlJvbGVfc3R1ZGVudCJdLCJodHRwczovL2xvY2FsaG9zdDozMDAwL2VtYWlsIjoiaXNoQGlzaC5jb20iLCJpc3MiOiJodHRwczovL2Rldi03a2plMHZubDgyYmVlandxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NmQ3NGQwYjM1NzUxM2Q5ODRlMDk3ZWMiLCJhdWQiOlsidGVzdGVyIiwiaHR0cHM6Ly9kZXYtN2tqZTB2bmw4MmJlZWp3cS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzI2MTk3MDIwLCJleHAiOjE3MjYyODM0MjAsInNjb3BlIjoib3BlbmlkIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgY3JlYXRlOmN1cnJlbnRfdXNlciIsImF6cCI6IkxQbjVZcG84OThkZENLSHJPcjdKamFVZDhWY1VjSlp4IiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmN1cnJlbnRfdXNlciIsInJlYWQ6Y3VycmVudF91c2VyIiwidXBkYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSJdfQ.L2EGrNaswGZxNc4-Ulawg7bnqgaovGC7ZKsJr33z4lY3oBdc9HQy1GN_enbE3vbK_52oh7mU2kAICLUpmFnXhftSR7bYpR73ZYFcM9JZHzw7rXI0oyDSz2AXyEzv-82epMv_yutafPcqZ_Bf5rWedb4W8Cdn2r6EYSo7ZkStq9tJ4hVaURpXUQmiCra8jV806k0IbMfbVRZqujhgcUFuFDz36dKOQx5Vd0Nub-t-ZfygNs8mcGJdasoVgHABwa9fZDNUgOuEz7d5eahbWSYGS_gToruTIF-UMfP_fnZyx_nKHErj7ZsIY-wnt4e88-slY2DxoeuaeaAypMCGXmD8Rw',  # Replace with your local API token if needed
    'Content-Type': 'application/json'
}

get_url = "http://localhost:3000/api/applicants"
response = requests.get(get_url)

if response.status_code == 200:
    applicants = response.json()

    # Step 2: Loop through applicants and call the create user in HubSpot endpoint
    for applicant in applicants:
        email = applicant.get('accountEmail', None)

        # Create the payload for HubSpot create-user endpoint
        create_user_payload = {
            'email': email
        }
        create_user_url = "http://localhost:3000/api/create-user-in-hubspot"

        try:
            create_user_response = requests.post(create_user_url, json=create_user_payload, headers=headers)
            if create_user_response.status_code != 200:
                print(f"Failed to create user for email {email}. Response: {create_user_response.status_code}, {create_user_response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error creating user in HubSpot for email {email}: {e}")

        # Step 3: Update contact with additional information
        update_contact_payload = {
            "email": email,
            "firstname": applicant['datosPersonales'].get('nombres', '').strip() if applicant.get('datosPersonales') else None,
            "lastname": f"{applicant['datosPersonales'].get('primerApellido', '')} {applicant['datosPersonales'].get('segundoApellido', '')}".strip() if applicant.get('datosPersonales') else None,
            "apoyo_financiero_": "no" if not applicant.get('situacionDeDiscapacidad', {}).get('necesitaApoyoFinanciero', False) else "yes",
            "carrera_de_interes": applicant.get('carreraDeInteres', None),
            "company": "UpdatedCompany",
            "fecha_de_nacimiento_del_estudiante": applicant['datosPersonales'].get('fechaDeNacimiento', None) if applicant.get('datosPersonales') else None,
            "institucion_educativa_cursada": applicant['datosBachillerato'].get('nombreInstitucion', None) if applicant.get('datosBachillerato') else None,
            "nacionalidad": applicant['datosPersonales'].get('nacionalidad', None) if applicant.get('datosPersonales') else None,
            "phone": applicant['datosPersonales'].get('celular', None) if applicant.get('datosPersonales') else None,
            "tipo_de_institucion_educativa": applicant['datosBachillerato'].get('tipoBachillerato', None) if applicant.get('datosBachillerato') else None,
            "titulo_obtenido": applicant['datosBachillerato'].get('tituloObtenidoAObtener', None) if applicant.get('datosBachillerato') else None
        }
        update_contact_url = "http://localhost:3000/api/update-contact-by-email"

        try:
            update_contact_response = requests.post(update_contact_url, json=update_contact_payload, headers=headers)
            if update_contact_response.status_code != 200:
                print(f"Failed to update contact for email {email}. Response: {update_contact_response.status_code}, {update_contact_response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error updating contact for email {email}: {e}")
else:
    print(f"Failed to retrieve applicants. Status code: {response.status_code}")
