import fitz
import re

# Open the PDF
pdf = fitz.open('UPDATED_CVE_LIST0512_0512.pdf')

# Regular expression to match CVE-<year>-<number>
cve_pattern = r'CVE-\d{4}\s*-\s*\d{4,5}'

# Set to store unique CVE IDs (using a set automatically removes duplicates)
unique_cves = set()

# Loop through all the pages in the PDF
for page_num in range(pdf.page_count):
    page = pdf.load_page(page_num)  # Load each page
    text = page.get_text("text")  # Extract text from the page
    
    # Normalize the text by removing newlines and extra spaces
    normalized_text = ' '.join(text.splitlines())
    normalized_text = re.sub(r'\s+', '', normalized_text)
    
    # Find all CVE matches on this page
    matches = re.findall(cve_pattern, normalized_text)
    
    # Add matches to the set of unique CVEs
    unique_cves.update(matches)

# Save unique CVEs to a file
if unique_cves:
    with open('unique_cves_parsed_from_pdf.txt', 'w') as f:
        f.write(f"Total unique CVEs found: {len(unique_cves)}\n")
        for cve in sorted(unique_cves):
            f.write(f"{cve}\n")
else:
    print("No CVE IDs found.")

# Close the PDF
pdf.close()