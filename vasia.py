import datetime
print(datetime.datetime.now())


def vasia():
    name = input("Sinu nimi: ")
    action = input("Tegevus: ")
    time = datetime.datetime.now()
    text = f"Date: {time} Nimi: {name}, Oli selline tegevus: {action}\n"
    file = open("vasia.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("Login oli salvestatu edukalt")
    