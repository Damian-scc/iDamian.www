from time import sleep

def printLyrics():
    lines = [
        ("I wanna da-", 0.06), #1
        ("I wanna dance in the lights", 0.1),#2
        ("I wanna ro-", 0.08),#3
        ("I wanna rock your body", 0.09),#4
        ("I wanna go", 0.1),#5
        ("I wanna go for a ride", 0.08), #6
        ("Hop in the music and", 0.09),#7
        ("Rock your body", 0.08),#8
        ("Rock your body", 0.08),#9
        ("come on, come on", 0.07),#10
        ("Rock your body", 0.06),#11
        ("(Rock your body)", 0.06),#12
         ("Rock your body ", 0.05),#13
        ("come on, come on", 0.06),#14
        ("Rock your body", 0.9),#15
    ]

    for line, delay in lines:
        for char in line:
            print(char, end="", flush=True)
            sleep(delay)
        print()

# uruchamiamy!
printLyrics()
