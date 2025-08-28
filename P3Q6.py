# File Handling : File Handling - Write a program that reads a text file and counts the number of lines, words, and characters.

#  Theory: File handling allows reading/writing files. We can count lines, words, characters.

def analyze_file(filename):
    with open(filename, "r") as f:
        text = f.read()
    lines = text.split("\n")
    words = text.split()
    chars = len(text)
    return len(lines), len(words), chars

# Example: create a file first
with open("sample.txt", "w") as f:
    f.write("Hello World\nMy name is nauman \nAI is powerful")

print(analyze_file("sample.txt"))