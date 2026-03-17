import re

text = "Price is 100 and discount 20"

print(re.findall(r"\d+", text))