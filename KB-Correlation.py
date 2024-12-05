from bs4 import BeautifulSoup
import requests
import re

def extract_cves(html_content):
    # Parse the HTML content
    doc = BeautifulSoup(html_content, "html.parser")
   
    # Find all table cell tags
    tags = doc.find_all("td")
   
    # List to store found CVEs
    cves = []
   
    # Regex pattern to match CVE format
    cve_pattern = re.compile(r'CVE-\d{4}-\d+')
   
    # Iterate through tags to find CVE matches
    for tag in tags:
        # Check if the tag contains text and matches CVE pattern
        if tag.text and cve_pattern.search(tag.text):
            cves.append(tag.text.strip())
   
    return cves

# Use the function
url = "https://nciipc.gov.in/advisories/CVE/CVE-KB/2024/Nov.html"
month = re.search(r'/(\w+)\.html$', url).group(1)
result = requests.get(url)
found_cves = extract_cves(result.text)  # Changed from result.txt to result.text

# Print CVEs on new lines
for cve in found_cves:
    with open(f"{month}.txt", "a") as f:
        #print(cve)
        print(cve, file=f)