with open("input.txt", "r") as file:
    text = file.read()
  
upper_text = text.upper()
output_content = f"{upper_text}"

with open("output.txt", "w") as file:
    file.write(output_content)


