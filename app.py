'''import json
with open('JSON10.json', 'r') as file:
    data = json.load(file)

filtered_data = [product for product in data if product.get('price', 0) >= 146.60]

sorted_data = sorted(filtered_data, key=lambda x: (x['category'], -x['price'], x['name']))
print(type(sorted_data))

with open('JSON10output.json', 'w') as f:
    json.dump(sorted_data, f, indent=1)

minified_json = json.dumps(sorted_data, separators=(',', ':'))
print(minified_json)'''

'''files = ['q-unicode-data/data1.csv', 'q-unicode-data/data2.csv', 'q-unicode-data/data3.txt']

symbols_to_match = {'š', 'Ÿ', '‰'}
total_sum = 0

with open('q-unicode-data/data1.csv', 'r', encoding='cp1252') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) >= 2 and parts[0] in symbols_to_match:
            try:
                total_sum += float(parts[1])
            except ValueError:
                pass

with open('q-unicode-data/data2.csv', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) >= 2 and parts[0] in symbols_to_match:
            try:
                total_sum += float(parts[1])
            except ValueError:
                pass

with open('q-unicode-data/data3.txt', 'r', encoding='utf-16') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) >= 2 and parts[0] in symbols_to_match:
            try:
                total_sum += float(parts[1])
            except ValueError:
                pass

print(f"Total sum of values for symbols š, Ÿ, ‰: {total_sum}")'''

'''import os, re

folder_path = 'q-replace-across-files'
pattern = re.compile(r'IITM', re.IGNORECASE)


for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        try:
            # Read file in binary mode to detect line endings
            with open(file_path, 'rb') as f:
                raw = f.read()

            # Detect line ending style
            if b'\r\n' in raw:
                newline = '\r\n'
            elif b'\r' in raw:
                newline = '\r'
            else:
                newline = '\n'

            # Try decoding with utf-8 first, then fallback
            try:
                text = raw.decode('utf-8')
                encoding = 'utf-8'
            except UnicodeDecodeError:
                text = raw.decode('cp1252')
                encoding = 'cp1252'

            # Replace "IITM" (in any case) with "IIT Madras"
            updated_text = pattern.sub("IIT Madras", text)

            # Write back with original line endings
            with open(file_path, 'w', encoding=encoding, newline=newline) as f:
                f.write(updated_text)

            print(f"✅ Updated: {filename}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")'''


'''import re

list=["test.email@university.edu",
"john.doe@company.com",
"user123@domain.org",
"notanemail",
"user@",
"@company.com"]

count = 0

pattern = re.compile(                                        # Start at word boundary
        r'[a-zA-Z0-9](?:[a-zA-Z0-9._%+-]*[a-zA-Z0-9])?'  # Local part: no leading/trailing dot
        r'@'
        r'(?:[a-zA-Z0-9-]+\.)+'                     # Domain: at least one dot
        r'[a-zA-Z]{2,}'                             # TLD: at least 2 letters
)

for email in list:
    if re.match(pattern, email):
        count+=1

print(count)'''

'''from itertools import zip_longest

count = 0

with open('q-compare-files/a.txt', 'r') as f1, open('q-compare-files/b.txt', 'r') as f2:
    for l1, l2 in zip_longest(f1, f2, fillvalue=''):
        if l1.strip() != l2.strip():
            count += 1

print(count)'''

'''import json, statistics

with open('q-calculate-variance.json', 'r') as f:
    data = json.load(f)

print(f"Variance: {statistics.variance(data=data)}")'''


import httpx
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def analyze_sentiment():
    url = BASE_URL
    headers = {
        "Authorization": API_KEY
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "Analyze the sentiment of the following text into one of the categories: GOOD, BAD, or NEUTRAL."
            },
            {
                "role": "user",
                "content": "PtU   i2OrNR jA i 1P1 5xtawRp8 9FGJ Cj   80 0jJS"
            }
        ]
    }

    response = httpx.post(url, json=data, headers=headers)
    response.raise_for_status()
    result = response.json()
    print(result)

if __name__ == "__main__":
    analyze_sentiment()
