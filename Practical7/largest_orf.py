import re

seq = "AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG"

pattern = r"(AUG)(?:.{3})*?(UAA|UAG|UGA)"

result = re.search(pattern, seq)

orf = result.group(1) + result.group(0)[3:-3]

print("Longest ORF:", orf)
print("Length:", len(orf))