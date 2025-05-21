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
        return self.data.get(continent, {}).get(country, {}).get(city, None)

    def remove_city(self, continent, country, city):
        if continent in self.data and country in self.data[continent]:
            self.data[continent][country].pop(city, None)
            # Удалить страну, если в ней больше нет городов
            if not self.data[continent][country]:
                del self.data[continent][country]
            # Удалить континент, если в нём больше нет стран
            if not self.data[continent]:
                del self.data[continent]
if name == "__main__":
    manager = MurderStatsManager()
    manager.add_data("Europe", "Estonia", "Tallinn", 5)
    manager.add_data("Europe", "Finland", "Helsinki", 3)
    manager.add_data("Asia", "Japan", "Tokyo", 8)
    manager.add_data("Africa", "Nigeria", "Lagos", 6)
    manager.add_data("Africa", "South Africa", "Cape Town", 4)

    print(manager.get_stats())
    print("Tokyo stats:", manager.get_city_stats("Asia", "Japan", "Tokyo"))
    manager.remove_city("Europe", "Finland", "Helsinki")
    print("After removal:", manager.get_stats())
