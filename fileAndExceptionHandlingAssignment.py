with open("input.txt", "r") as file:
    text = file.read()
  
upper_text = text.upper()
output_content = f"{upper_text}"

with open("output.txt", "w") as file:
    file.write(output_content)

try:
    with open("data.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("data.txt not found. Please ensure the file exists.")


