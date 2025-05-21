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
                    
                    self.data[continent][country][city] = None

                
                all_empty = True
                for name in self.data[continent][country]:
                    if self.data[continent][country][name] is not None:
                        all_empty = False

                if all_empty:
                    self.data[continent][country] = None

                
                all_countries_empty = True
                for country_name in self.data[continent]:
                    if self.data[continent][country_name] is not None:
                        all_countries_empty = False

                if all_countries_empty:
                    self.data[continent] = None

if __name__ == "__main__":
    manager = MurderStatsManager()
    manager.add_data("Europe", "Estonia", "Tallinn", 5)
    manager.add_data("Europe", "Finland", "Helsinki", 3)
    manager.add_data("Asia", "Japan", "Tokyo", 8)
    manager.add_data("Africa", "Nigeria", "Lagos", 6)
    manager.add_data("Africa", "South Africa", "Cape Town", 4)
    
    
    
    
    
    
    

    
    
from grades_manager import add_grade, view_grades, search_student
def main1():
    while True:
        print("\nÕpilaste hinnete haldusprogramm:")
        print("1. Lisa õpilase hinded")
        print("2. Vaata kõiki õpilasi ja nende hindeid")
        print("3. Otsi õpilast nime järgi")
        print("4. Välju")

        choice = input("Vali tegevus (1-4): ")

        if choice == "1":
            add_grade()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Programmist väljumine.")
            break
        else:
            print("Vale valik, proovi uuesti.")

if __name__ == "__main__":
    main1()

