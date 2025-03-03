# from notes_manager import add_note, view_notes, delete_note
# 
# def main():
#     while True:
#         print("\nMärkmik programmi menüü:")
#         print("1. Lisa uus märkme")
#         print("2. Vaata kõiki märkmeid")
#         print("3. Kustuta märkme")
#         print("4. Välju")
# 
#         choice = input("Vali tegevus (1-4): ")
# 
#         if choice == "1":
#             add_note()
#         elif choice == "2":
#             view_notes()
#         elif choice == "3":
#             delete_note()
#         elif choice == "4":
#             print("Programmist väljumine.")
#             break
#         else:
#             print("Vale valik, proovi uuesti.")
# 
# if __name__ == "__main__":
#     main()
#     
    
    
    
    
    
    
    
    
    
    

    
    
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

