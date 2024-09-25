poll_results = {}
polling_active = True

while polling_active:
    place = input("If you could visit one place in the world, where "
            "would you go?")
    time = input("When would you like to go there?")
    
    poll_results[place] = time 
    new_person = input("Are there any more respondents? (yes/no)")

    if new_person =='no':
        polling_active = False

print("---Places and dates down here: -----")
for place,time in poll_results.items():
    print(f"I see that you would like to {place} on {time}")


