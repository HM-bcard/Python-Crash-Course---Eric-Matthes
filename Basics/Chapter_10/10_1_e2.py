from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

def bday_in_pi():
    n = '920407'

    if n in contents:
        print('yes')
    else:
        print('no')


bday_in_pi()

