#Regular Expression Operations

#re findall
import re
text = "The quick brown fox"
pattern = r"fox"

search = re.search(pattern, text)
if search :
    print("Patternn found:", search.group())
else:
    print("Pattern not found")


#re Match   
matchtext = "The quick brown bread"
pattern = r"bread"

match = re.match(pattern, matchtext)
if match:
    print("Match found:", match.group())
else:
    print("No match")


#RegExp Replace
replacetext = "The quick brown bread fills the stomach"
pattern = r"brown"

replacement = "White"
new_text = re.sub(pattern, replacement, replacetext)
print("Modified text:", new_text)


#RegExp Search
searchtext = "The quick brown bread"
pattern = r"brown"

search = re.search(pattern, searchtext)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


#RegExp Split
splittext = "Apple,Banana,Cherries,Dragon"
pattern = r","

split_result = re.split(pattern, splittext)
print("Split result:", split_result)