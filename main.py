import time
import random

def give_vbuck(username, amount):
    print(f"Giving my boy {username} {amount} vbucks.")

    time.sleep(5)

    success = random.choice([True, False])

    if success:
        print("Success! Now you can buy floss emote and renegade raider!")
    else:
        print("Invalid username lmao")

give_vbuck(
    input( godkiller132968 ),
    int(input(1,000,000))
)
