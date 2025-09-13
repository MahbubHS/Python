import random, time, os

for _ in range(60):
    stars = "".join(random.choice([" ","*"])
    for _ in range(60))
    print(stars) 
    time.sleep(0.2)
    os.system("cls" if os.name =="nt" else "clear")