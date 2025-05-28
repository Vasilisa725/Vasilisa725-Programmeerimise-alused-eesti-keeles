from rich.console import Console
from rich.table import Table
import random
import time

console = Console()

class CrewMember:
    def __init__(self, name, role):  
        self.name = name
        self.role = role
        self.hp = 100
        self.power = random.randint(15, 30)
        self.status = True
       
    def attack_alien(self, alien):
        if self.status:
            damage = self.power + random.randint(-5, 5)
            alien.hp -= damage
            if alien.hp < 0:
                alien.hp = 0
            console.print(f"[bold green]{self.name} attacks alien for {damage} damage!")
   
    def injure(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.status = False
            self.hp = 0
            console.print(f"[red]{self.name} the {self.role} was killed by the alien!")
        else:
            console.print(f"[yellow]{self.name} the {self.role} took {damage} damage! {self.hp} HP left.")
       

class Alien:
    def __init__(self):  
        self.aggression = random.randint(1, 10)
        self.hp = 120
       
    def attack(self, crew):
        damage = random.randint(15, 40) + self.aggression
        crew.injure(damage)
       
    def is_alive(self):
        return self.hp > 0


class Ship:
    def __init__(self):  
        self.rooms = ["engine room", "medical block", "warehouse", "rest room", "navigation center"]
        self.status = True

    def trigger_alarm(self, room):
        self.status = f"Alien presence detected in {room}"
        console.print(f"[bold red]{self.status}")
   
    def show_status(self):
        console.print(f"[blue]Ship status: {self.status}")


class Mission:
    def __init__(self, crewList):  
        self.crew = crewList
        self.alien = Alien()
        self.ship = Ship()

    def simulate(self):
        console.print("[bold green]The mission begins!")
        self.ship.show_status()
        time.sleep(1)

        for round_num in range(1, 10):
            if not self.alien.is_alive():
                console.print("[bold green]The crew defeated the alien!")
                break
            # Проверяем, жив ли кто-то из экипажа
            alive_crew = [member for member in self.crew if member.status]
            if len(alive_crew) == 0:
                console.print("[bold red]The entire crew was destroyed. The mission failed.")
                break

            console.print(f"[bold]Round {round_num}")
            room = random.choice(self.ship.rooms)
            console.print(f"[cyan]Scanning room: {room}")
            time.sleep(1)

            if random.random() < 0.7 and self.alien.is_alive():
                self.ship.trigger_alarm(room)
               
                # Чужой атакует случайного члена экипажа
                victim = random.choice(alive_crew)
                self.alien.attack(victim)

                # Оставшиеся члены экипажа атакуют чужого
                attackers = [member for member in alive_crew if member != victim]
                if attackers:
                    attacker = random.choice(attackers)
                    attacker.attack_alien(self.alien)
                    console.print(f"[bold cyan]Alien has {self.alien.hp} HP left")
                else:
                    console.print("[green]The scan is clear. The crew is breathing calmly.")
            else:
                console.print("[green]The scan is clear. No alien detected.")
           
            time.sleep(1)

        if self.alien.is_alive():
            console.print("[bold red]The alien survived. The mission is in jeopardy!")
        else:
            console.print("[bold green]The alien was defeated! Mission successful!")

        self.summary()

    def summary(self):
        table = Table(title="Ekipaaž")
        table.add_column("Name", style='yellow')
        table.add_column("Role", style='green')
        table.add_column("Health", style='red')
        table.add_column("Status", style='cyan')  

        for crewMember in self.crew:
            status = "Alive" if crewMember.status else "Died"
            table.add_row(crewMember.name, crewMember.role, str(crewMember.hp), status)

        console.print(table)


crew = [
    CrewMember("Ripli", "Captain"),
    CrewMember("Dallas", "Sailor"),
    CrewMember("Esh", "Science Officer"),
    CrewMember("Parker", "Engineer")
]

mission1 = Mission(crew)
mission1.simulate()
