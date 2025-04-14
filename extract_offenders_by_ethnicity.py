from PyPDF2 import PdfReader
from collections import defaultdict
import matplotlib.pyplot as plt


# I want to gather the number of offenders by race each month of 2024
# The output should look like this
Example_list = [
    {"Asian": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
        {"Caucasian": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"African American": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"Native American": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"Hispanic": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"Other": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }}
]

# Load the PDF
reader = PdfReader("2024-Ethnicity-of-Offenders.pdf")

# Initialize a dictionary to store ethnicity offender counts by month
Example_list = [
    {"Asian": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
        {"Caucasian": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"African American": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"Native American": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"Hispanic": 
     {
        "January": 18, 
        "February": 16, 
        "March": 16, 
        "April": 16, 
        "May": 16, 
        "June": 16, 
        "July": 16, 
        "August": 16, 
        "September": 16, 
        "October": 16, 
        "November": 16, 
        "December": 16
    }},
    {"Other": 
     {
        "January": 0, 
        "February": 0, 
        "March": 0, 
        "April": 0, 
        "May": 0, 
        "June": 0, 
        "July": 0, 
        "August": 0, 
        "September": 0, 
        "October": 0, 
        "November": 0, 
        "December": 0
    }}
]

# monthly_asian_counts = defaultdict(int)

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

ethnicities = [
    "Asian", 
    "Caucasian", 
    "African American", 
    "Hispanic", 
    "Other"
]

# Go through each page and extract each Race / Ethnicity offender data
pages = reader.pages

for page in pages: # go through each page
    # print(page)
    text = page.extract_text() # extract the text
