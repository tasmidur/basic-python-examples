import requests

# Define the URL for the API endpoint
url = "https://api.etaxnbr.gov.bd/ledgerservice/v3/api/other/save_tds"

# Set up the headers, including the Bearer token for authorization
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJUQVhQQVlFUiIsInN1YiI6IjIxNTM2ODY5Nzk3MCIsImlzcyI6Ik5CUiIsImNsYWltcyI6eyJ1c2VyUm9sZXMiOlsiVEFYUEFZRVIiXSwidXNlckZ1bGxOYW1lIjoiTUFTVURVWlpBTUFOIiwidXNlcklkZW50aXR5IjoiMjE1MzY4Njk3OTcwIiwidXNlclR5cGUiOiJUQVhQQVlFUiJ9LCJleHAiOjE3Mzc4MDIyMTB9.auHERSBL1zulR2jLRFeCC3Q5Fz13dF1MBSttMdmwVrE",
    "Content-Type": "application/json"
}

challan_data = [
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-0010706996",
#     "challanDate": "2023-10-05",
#     "referenceNo": "",
#     "bank": "Somali Bank",
#     "branchName": "Baridhara Branch",
#     "challanAmount": "136332",
#     "tdsClaim": "416",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-0017157345",
#     "challanDate": "2023-11-15",
#     "referenceNo": "",
#     "bank": "Sonali Bank",
#     "branchName": "Baridhara Branch",
#     "challanAmount": "163307",
#     "tdsClaim": "416",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-00214/9527",
#     "challanDate": "2023-12-17",
#     "referenceNo": "",
#     "bank": "Sonali Bank",
#     "branchName": "Barichara Branch",
#     "challanAmount": "179368",
#     "tdsClaim": "416",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-0023763432",
#     "challanDate": "2024-01-14",
#     "referenceNo": "",
#     "bank": "Somali Bank",
#     "branchName": "Baridhara Branch",
#     "challanAmount": "187932",
#     "tdsClaim": "416",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-0027729938",
#     "challanDate": "2024-02-14",
#     "referenceNo": "",
#     "bank": "Sonali Bank",
#     "branchName": "Baridhara Branch",
#     "challanAmount": "204915",
#     "tdsClaim": "416",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-0031550444",
#     "challanDate": "2024-03-18",
#     "referenceNo": "",
#     "bank": "Somali Bank",
#     "branchName": "Baridhara Branch",
#     "challanAmount": "205748",
#     "tdsClaim": "416",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-0034068048",
#     "challanDate": "2024-04-15",
#     "referenceNo": "",
#     "bank": "Sonali Bank",
#     "branchName": "Baridhara Branch",
#     "challanAmount": "229672",
#     "tdsClaim": "438",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
#   {
#     "tinNo": "215368697970",
#     "assessmentYear": "",
#     "section": "Salary [ Section-86]",
#     "depositingAuthority": "BYSL Global Technology Group",
#     "challanNo": "2324-0039092747",
#     "challanDate": "2024-05-30",
#     "referenceNo": "",
#     "bank": "Somali Bank",
#     "branchName": "Baridhara Branch",
#     "challanAmount": "278557",
#     "tdsClaim": "558",
#     "verificationStatus": "Pending",
#     "referenceDate": ""
#   },
  {
    "tinNo": "215368697970",
    "assessmentYear": "",
    "section": "Salary [ Section-86]",
    "depositingAuthority": "BYSL Global Technology Group",
    "challanNo": "2425-0004744507",
    "challanDate": "2024-08-21",
    "referenceNo": "",
    "bank": "Sonali Bank",
    "branchName": "Baridhara Branch",
    "challanAmount": "298295",
    "tdsClaim": "558",
    "verificationStatus": "Pending",
    "referenceDate": ""
  },
  {
    "tinNo": "215368697970",
    "assessmentYear": "",
    "section": "Salary [ Section-86]",
    "depositingAuthority": "BYSL Global Technology Group",
    "challanNo": "2425-0004744805",
    "challanDate": "2024-08-21",
    "referenceNo": "",
    "bank": "Somali Bank",
    "branchName": "Baridhara Branch",
    "challanAmount": "295992",
    "tdsClaim": "567",
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