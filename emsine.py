import random

num_levels = 10
initial_resources = 100
resources_loss_percent = 0.1
min_resources_to_survive = 10

class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.resources = 0
        self.active = True
        
    def receive_resources(self, amount):
        self.resources += amount
        
    def transfer_resources(self, amount):
        loss = amount * resources_loss_percent
        transferred = amount - loss
        self.resources -= amount
        return transferred
    
    def is_alive(self):
        return self.resources >= min_resources_to_survive
        
def print_status(levels):
    print("\nУровни и ресурсы:")
    for level in levels:
        status = "активен" if level.active else "вышел"
        print(f"Уровень {level.level_number}: {level.resources:.1f} ресурсов ({status})")
    print("\n")

def main():
    levels = [Level(i + 1) for i in range(num_levels)]
    levels[0].receive_resources(initial_resources)
    
    for i in range(num_levels - 1):
        if not levels[i].active:
            continue
        
        print_status(levels)
        print(f"Ты на уровне {levels[i].level_number}.")
        print(f"Доступно ресурсов: {levels[i].resources:.1f}")
        
        while True:
            try:
                keep = float(input("Сколько ресурсов оставить себе? "))
                if keep < 0 or keep > levels[i].resources:
                    raise ValueError()
                break
            except ValueError:
                print("Неправильный ввод. Введи число от 0 до доступных ресурсов.")
        
        transfer = levels[i].resources - keep
        sent = levels[i].transfer_resources(transfer)
        levels[i + 1].receive_resources(sent)
        
        for level in levels:
            level.active = level.is_alive()
    
    print_status(levels)
    print("Игра закончена.")

if name == "__main__":
    main()
    
