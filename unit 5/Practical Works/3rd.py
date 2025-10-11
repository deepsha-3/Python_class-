# Write program to store output in file. 

output_text="Hello coders! You lost your life."

filename="output.txt"

with open(filename, "w") as file:
    file.write(output_text)

print(f"Ohh nice output written in {filename} file.")

