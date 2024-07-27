import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://farhatlectures.com/exam-performance/cpa-exam-pass-rates-by-university/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table
table = soup.find('table')

# Extract table headers
headers = [th.text.strip() for th in table.find('thead').find_all('th')]

# Extract table rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    cells = [td.text.strip() for td in tr.find_all('td')]
    rows.append(cells)

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save to CSV
df.to_csv('data/CPA_Exam_Pass_Rates_by_University.csv', index=False)

print("Data saved to data/CPA_Exam_Pass_Rates_by_University.csv")
