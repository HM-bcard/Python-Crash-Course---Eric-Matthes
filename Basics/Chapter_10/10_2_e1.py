from pathlib import Path

path = Path('learning_python.txt')

file_contents = path.read_text()

print(file_contents.replace('Python','C'))


