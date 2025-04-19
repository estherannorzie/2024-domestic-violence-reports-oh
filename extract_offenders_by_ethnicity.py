# Install and use pdfplumber for more accurate PDF text extraction
import pdfplumber, re, pandas as pd
from collections import defaultdict

# Redefine monthly totals using pdfplumber
monthly_totals = defaultdict(lambda: defaultdict(int))

months_pattern = r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b'

# Open and read the PDF with pdfplumber
with pdfplumber.open("2024-Ethnicity-of-Offenders.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()

        # Extract month lines
        for line in text.splitlines():
            if re.match(months_pattern, line):
                parts = line.split()
                month = parts[0]
                if len(parts) >= 7:
                    try:
                        monthly_totals[month]["Asian"] += int(parts[1])
                        monthly_totals[month]["Caucasian"] += int(parts[2])
                        monthly_totals[month]["African American"] += int(parts[3])
                        monthly_totals[month]["Native American"] += int(parts[4])
                        monthly_totals[month]["Hispanic"] += int(parts[5])
                        monthly_totals[month]["Other"] += int(parts[6])
                    except ValueError:
                        continue

# Build final DataFrame
ethnicity_categories = [
    "Asian",
    "Caucasian",
    "African American",
    "Native American",
    "Hispanic",
    "Other"
]

month_order = [
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December"
]

data = []
for month in month_order:
    row = [month]
    total = 0
    for category in ethnicity_categories:
        count = monthly_totals[month][category]
        row.append(count)
        total += count
    row.append(total)
    data.append(row)

print(data)
# df_final = pd.DataFrame(data, columns=['Month', 'A', 'CC', 'AA', 'NA', 'H', 'O', 'Totals'])

# print(df_final)
