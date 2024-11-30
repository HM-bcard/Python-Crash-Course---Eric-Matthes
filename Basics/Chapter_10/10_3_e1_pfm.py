from pathlib import Path
path = Path('learning_python.txt')

file_contents = path.read_text()

for line in file_contents.splitlines():
    print(line.rstrip(),':3')
    

    
