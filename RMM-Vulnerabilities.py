import os
import csv
from bs4 import BeautifulSoup

def parse_vulnerabilities(file_path):
    # Read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Find all vulnerability rows
    vulnerability_rows = soup.find_all('tr', class_='kt-datatable__row')
    
    # List to store parsed vulnerabilities
    vulnerabilities = []
    
    # Extract data from each row
    for row in vulnerability_rows:
        # Find all td elements in the row
        cells = row.find_all('td')
        
        # Check if we have enough cells
        if len(cells) >= 8:
            vulnerability = {
                'CVE': cells[1].text.strip(),
                'CVSS Score': cells[2].text.strip(),
                'CISA KEV': cells[3].text.strip(),
                'Published Date': cells[4].text.strip(),
                'Remediation Status': cells[5].text.strip(),
                'Vulnerable Software': cells[6].text.strip(),
                'Endpoints': cells[7].text.strip()
            }
            vulnerabilities.append(vulnerability)
    
    return vulnerabilities

def export_to_csv(vulnerabilities, output_file):
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Use the keys of the first vulnerability as fieldnames
        if vulnerabilities:
            fieldnames = vulnerabilities[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data
            for vulnerability in vulnerabilities:
                writer.writerow(vulnerability)
    
    print(f"Exported {len(vulnerabilities)} vulnerabilities to {output_file}")

def main():
    # Input and output file paths
    input_file = 'RMM-Vulnerabilities.html'
    output_file = 'cve_details.csv'
    
    try:
        # Parse vulnerabilities
        vulnerabilities = parse_vulnerabilities(input_file)
        
        # Export to CSV
        export_to_csv(vulnerabilities, output_file)
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found. Please check the filename and location.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()