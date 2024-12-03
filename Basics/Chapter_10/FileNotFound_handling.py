from pathlib import Path
filename = 'alice.txt'
path = Path(filename)
'''
try:
    alice_contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"There is no file called {path}")
'''


#Analyzing text

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"There is no file called {path}")
else:
    # Counting the number of words
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} contains approximately {num_words} words")
    