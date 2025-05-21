class MurderStatsManager:
    def __init__(self):
        self.data = {}

    def add_data(self, continent, country, city, count):
        if continent not in self.data:
            self.data[continent] = {}
        if country not in self.data[continent]:
            self.data[continent][country] = {}
        self.data[continent][country][city] = count

    def get_stats(self):
        return self.data

    def get_city_stats(self, continent, country, city):
        if continent in self.data:
            if country in self.data[continent]:
                if city in self.data[continent][country]:
                    return self.data[continent][country][city]
        return None

    def remove_city(self, continent, country, city):
        if continent in self.data:
            if country in self.data[continent]:
                if city in self.data[continent][country]:
                    self.data[continent][country].pop(city)
                    # Удалим страну, если в ней больше нет городов
                    if len(self.data[continent][country]) == 0:
                        self.data[continent].pop(country)
                    # Удалим континент, если в нём больше нет стран
                    if len(self.data[continent]) == 0:
                        self.data.pop(continent)

if __name__ == "__main__":
    manager = MurderStatsManager()

    # Данные по Европе и Азии
    manager.add_data("Europe", "Estonia", "Tallinn", 5)
    manager.add_data("Europe", "Finland", "Helsinki", 3)
    manager.add_data("Asia", "Japan", "Tokyo", 8)

    # Данные по Африке (для ученика B)
    manager.add_data("Africa", "Nigeria", "Lagos", 6)
    manager.add_data("Africa", "Egypt", "Cairo", 4)

    # Вывод всей статистики
    print("Статистика по всем городам:")
    print(manager.get_stats())

    # Проверка метода get_city_stats
    print("\nСтатистика по городу Tokyo:")
    print(manager.get_city_stats("Asia", "Japan", "Tokyo"))

    # Проверка метода remove_city
    manager.remove_city("Africa", "Egypt", "Cairo")
    print("\nПосле удаления города Cairo:")
    print(manager.get_stats())
