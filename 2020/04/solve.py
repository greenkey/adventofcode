import re

file_name = 'input'

mask = re.compile(r'([a-z]+):([^ ]+)')

documents = []
with open(file_name, 'r') as f:
    data = []
    for line in f:
        line = line.strip()
        if line:
            data.append(line)
        else:
            documents.append({k: v for k, v in mask.findall(' '.join(data))})
            data = []
    documents.append({k: v for k, v in mask.findall(' '.join(data))})

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

print(sum(required_fields.issubset(doc.keys()) for doc in documents))
