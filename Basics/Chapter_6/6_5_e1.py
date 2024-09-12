rivers = {'Nile':'Egypt',
          'Amazon':'Brasil',
          'Rheine':'Germany'}

for river,country in rivers.items():
    print(f"The {river} flows through {country}")

for river in rivers:
    print(f"The {river}")

for river in rivers:
    print(f"{rivers[river].title()}")






