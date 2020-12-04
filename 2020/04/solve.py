import re
from functools import partial

file_name = 'input'

document_mask = re.compile(r'([a-z]+):([^ ]+)')

def is_int_between(lower, upper, x):
    try:
        num = int(x)
    except TypeError:
        return False
    return lower <= num <= upper

def matches_mask(mask, s):
    return mask.findall(s)

def validate_height(mask, hgt):
    try:
        height, mu = mask.findall(doc['hgt'])[0]
    except IndexError:
        return False

    if mu == 'cm':
        if not is_int_between(150, 193, height):
            return False
    elif mu == 'in':
        if not is_int_between(59, 76, height):
            return False

    return True

field_masks = {
    'byr': partial(is_int_between, 1920, 2002),
    'iyr': partial(is_int_between, 2010, 2020),
    'eyr': partial(is_int_between, 2020, 2030),
    'hgt': partial(validate_height, re.compile(r'([0-9]+)(cm|in)')),
    'hcl': partial(matches_mask, re.compile(r'\#[0-9a-f]{6}')),
    'ecl': partial(matches_mask, re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)')),
    'pid': partial(matches_mask, re.compile(r'^[0-9]{9}$')),
}

def validate(doc):
    for field, check in field_masks.items():
        if not check(doc[field]):
            return False
    return True


documents = []
with open(file_name, 'r') as f:
    data = []
    for line in f:
        line = line.strip()
        if line:
            data.append(line)
        else:
            documents.append({k: v for k, v in document_mask.findall(' '.join(data))})
            data = []
    documents.append({k: v for k, v in document_mask.findall(' '.join(data))})

valid_1 = 0
valid_2 = 0
for doc in documents:
    if set(field_masks.keys()).issubset(doc.keys()):
        valid_1 += 1
        valid_2 += validate(doc)

print(valid_1)
print(valid_2)
