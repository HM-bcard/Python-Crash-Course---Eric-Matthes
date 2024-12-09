from pathlib import Path
path = Path('alice.txt')

try:
    text = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("This file doesn't exist")
else:
    
