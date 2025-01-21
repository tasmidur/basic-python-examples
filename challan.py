import requests

# Define the URL for the API endpoint
url = "https://api.etaxnbr.gov.bd/ledgerservice/v3/api/other/save_tds"

# Set up the headers, including the Bearer token for authorization
headers = {
    "Authorization": "EwNCIsImlzcyI6Ik5CUiIsImNsYWltcyI6eyJ1c2VyUm9sZXMiOlsiVEFYUEFZRVIiXSwidXNlckZ1bGxOYW1lIjoiTUQuIFNBQkJJUlVMIElTTEFNIiwidXNlcklkZW50aXR5IjoiNzg3Mjk1NTUxMTA0IiwidXNlclR5cGUiOiJUQVhQQVlFUiJ9LCJleHAiOjE3Mzc3MTkzMzB9.Z7sV7tW6SqgLnsSz6zyQm40MX1aLcsnVOZuUsA86ejU",
    "Content-Type": "application/json"
}

challan_data = [
    {
        "tinNo": "787295551104",
        "assessmentYear": "",
        "section": "Salary [ Section-86]",
        "depositingAuthority": "BYSL Global Technology Group",
        "challanNo": "2324-0039091747",
        "challanDate": "2024-05-30",
        "referenceNo": "",
        "bank": "Sonali Bank PLC",
        "branchName": "Baridhara Branch",
        "challanAmount": "416",  # You can adjust the amount as needed
        "tdsClaim": "416",       # You can adjust the claim as needed
        "verificationStatus": "Pending",
        "referenceDate": ""
    },
    {
        "tinNo": "787295551104",
        "assessmentYear": "",
        "section": "Salary [ Section-86]",
        "depositingAuthority": "BYSL Global Technology Group",
        "challanNo": "2425-0003005564",
        "challanDate": "2024-07-31",
        "referenceNo": "",
        "bank": "Sonali Bank PLC",
        "branchName": "Baridhara Branch",
        "challanAmount": "416",  # You can adjust the amount as needed
        "tdsClaim": "416",       # You can adjust the claim as needed
        "verificationStatus": "Pending",
        "referenceDate": ""
    },
    {
        "tinNo": "787295551104",
        "assessmentYear": "",
        "section": "Salary [ Section-86]",
        "depositingAuthority": "BYSL Global Technology Group",
        "challanNo": "2425-0004744189",
        "challanDate": "2024-08-21",
        "referenceNo": "",
        "bank": "Sonali Bank PLC",
        "branchName": "Baridhara Branch",
        "challanAmount": "416",  # You can adjust the amount as needed
        "tdsClaim": "416",       # You can adjust the claim as needed
        "verificationStatus": "Pending",
        "referenceDate": ""
    },
    {
        "tinNo": "787295551104",
        "assessmentYear": "",
        "section": "Salary [ Section-86]",
        "depositingAuthority": "BYSL Global Technology Group",
        "challanNo": "2425-0004744507",
        "challanDate": "2024-08-21",
        "referenceNo": "",
        "bank": "Sonali Bank PLC",
        "branchName ": "Baridhara Branch",
        "challanAmount": "416",  # You can adjust the amount as needed
        "tdsClaim": "416",       # You can adjust the claim as needed
        "verificationStatus": "Pending",
        "referenceDate": ""
    }
]

# Example of how to use the data
for challan in challan_data:
    response = requests.post(url, headers=headers, json=challan)
    # Check the response status code and handle the response
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.text)