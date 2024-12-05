from pathlib import Path

def read_text(text_file):
    print(Path.read_text(text_file))



text_files = ['cats.txt','dogs.txt','birds.txt']

for text_file in text_files:
    try:
        path = Path(text_file)
        read_text(path)
    except FileNotFoundError:
        '''
        log_path = Path('log.txt')
        with log_path.open(mode='a') as log_file:
            log_file.write(f"Sorry the file {text_file} has not been found")
        #path.write_text('log.txt',f"Sorry the file {text_file} has not been found")
        '''
        pass
    else:
        continue

