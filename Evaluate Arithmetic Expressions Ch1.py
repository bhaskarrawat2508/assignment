import os
import math
import re

#a = r"D:\\Doc\\input.txt"
#b = r"D:\\Doc\\output.txt"

with open(a, 'r') as infile, open(b, 'w') as outfile:
    for line in infile:
        line = line.strip()
        if "=" in line:
            expr = line.split("=")[0].strip()
            expr = expr.replace("^", "**")
            expr = re.sub(r'(\d|\))\s*\(', r'\1*(', expr)
            result = eval(expr, {"__builtins__": None}, {"math": math})
            outfile.write(f"{expr} = {result}\n")
        else:
            outfile.write(f"{line} = Error: No '=' found in line\n")
print(f"Output file generated at: {b}")
