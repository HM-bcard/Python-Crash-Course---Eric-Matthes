def mobys_and_dicks(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {path} hasn't been found")
    else:
        words = contents.split()
        moby = 0
        dick = 0
        for word in words:
            if word.lower() == 'moby':
                moby += 1
            elif word.lower() == 'dick':
                dick += 1
            else:
                continue
    print(f"The book {path} contains the word 'moby' {moby} times")
    print(f"The book contains the word 'dick' {dick} times")