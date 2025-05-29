import random
from collections import Counter
import time

class CrewMember:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.vote = None

    def __str__(self):
        status = "Жив" if self.alive else "Мёртв"
        return f"{self.name} ({status})"

def create_crew(num_players=6):
    names = [f"Игрок {i+1}" for i in range(num_players)]
    crew = [CrewMember(name) for name in names]
    return crew

def choose_impostor(crew):
    return random.choice(crew)

def get_alive_players(crew):
    return [member for member in crew if member.alive]

def kill_player(impostor, crew):
    alive = get_alive_players(crew)
    targets = [p for p in alive if p != impostor]
    if not targets:
        return None
    victim = random.choice(targets)
    victim.alive = False
    print(f"\n{victim.name} был убит.")
    return victim

def voting_round(crew):
    alive = get_alive_players(crew)
    print("\nГолосование началось...")
    time.sleep(1)
    
    votes = []
    for voter in alive:
        choices = [p for p in alive if p != voter]
        if not choices:
            print(f"{voter.name} не может голосовать (нет доступных кандидатов).")
            continue
        vote = random.choice(choices)
        voter.vote = vote
        votes.append(vote.name)
        print(f"{voter.name} голосует за {vote.name}")
        time.sleep(0.5)

    if not votes:
        print("Голосов нет, никто не изгнан.")
        return None

    count = Counter(votes)
    most_common = count.most_common(1)[0]
    ejected_name = most_common[0]
    
    for member in crew:
        if member.name == ejected_name and member.alive:
            member.alive = False
            print(f"\n{member.name} был изгнан с корабля.")
            return member
    return None

def check_victory(crew, impostor):
    alive = get_alive_players(crew)
    if impostor not in alive:
        print("\nЭкипаж победил. Предатель был изгнан.")
        return True
    if len(alive) == 1 and impostor in alive:
        print(f"\nПобеда предателя. {impostor.name} остался один.")
        return True
    return False

def print_status(crew):
    print("\nТекущий статус:")
    for member in crew:
        print("-", member)

def play_game():
    print("Начинается игра 'Among Us-lite'")
    crew = create_crew()
    impostor = choose_impostor(crew)
    print("Предатель выбран тайно.\n")

    round_num = 1
    while True:
        print(f"\nРаунд {round_num}")
        time.sleep(1)
        
        kill_player(impostor, crew)
        time.sleep(1)

    
        if check_victory(crew, impostor):
            break

        voting_round(crew)
        time.sleep(1)
        print_status(crew)

        if check_victory(crew, impostor):
            break

        round_num += 1

if __name__ == "__main__":
    play_game()

