import sys, os
from datetime import datetime
f = open("template.typst", "r")
content = f.read()
f.close()

content = content.replace("DATE", str(datetime.now()))

def help():
    print("Usage: python generate.py <FOLDER> <MISSION_NAME> <AUTHOR>")
    print("Be sure there is a feedback.md in <FOLDER>")

student_line = """(name: "$NAME", symbol: $SYMBOL),\n"""

try:
    dir = sys.argv[1]
    name = sys.argv[2]
    author = sys.argv[3]
    if not os.path.isdir(dir):
        raise Exception("Unknown directory "+dir)
except Exception as e:
    print(e)
    help()
    sys.exit(1)

content = content.replace("NAME", name)
content = content.replace("AUTHOR", author)


symbols = {
    "1": "symbol_not_submitted",
    "2": "symbol_what",
    "3": "symbol_good",
    "4": "symbol_perfect",
}

students = ""

for f in os.listdir(dir):
    if os.path.isdir(dir+"/"+f):
        name, score = f.split("_")[-2:]
        students += (student_line.replace("$NAME", name).replace("$SYMBOL", symbols[score]))
        
content = content.replace("//ADD_STUDENTS_HERE", students)

codes_content = ""

if os.path.isfile(dir+"/feedback.md"):
    codes = open(dir+"/feedback.md").read().split("---")
    global_f = codes[-1]
    codes = codes[:-1]
    for c in codes:
        codes_content += f"""
```python
{c.strip()}
```
        """
else:
    help()
    sys.exit(1)
    
content = content.replace("// ADD_CODES_HERE", codes_content)
content = content.replace("//FEEDBACK", global_f.strip())

u = open(dir+"/output.typst", "w")
u.write(content)
u.close()

os.system(f"typst compile {dir}/output.typst")
