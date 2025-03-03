# def read_notes(filename="notes.txt"):
#     """Loeb kõik märkmed failist ja tagastab need nimekirjana."""
#     notes = []
#     try:
#         with open(filename, "r") as file:
#             content = file.read().strip().split("---")
#             for note in content:
#                 if note.strip():  
#                     title, text = note.strip().split("\n", 1)
#                     notes.append({"title": title.split(":")[1].strip(), "text": text.split(":")[1].strip()})
#     except FileNotFoundError:
#         return notes
#     return notes
# 
# def write_note(title, text, filename="notes.txt"):
#     """Kirjutab uue märkme faili."""
#     with open(filename, "a") as file:
#         file.write(f"Pealkiri: {title}\nTekst: {text}\n---\n")
# 
# def delete_note_by_title(title, filename="notes.txt"):
#     """Kustutab märkme, mille pealkiri vastab antud pealkirjale."""
#     notes = read_notes(filename)
#     remaining_notes = [note for note in notes if note["title"] != title]
#     
#     with open(filename, "w") as file:
#         for note in remaining_notes:
#             file.write(f"Pealkiri: {note['title']}\nTekst: {note['text']}\n---\n")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
       


def read_grades(filename="grades.txt"):
    """Loeb kõik õpilased ja nende hinded failist."""
    students = []
    try:
        with open(filename, "r") as file:
            content = file.read().strip().split("---")
            for student in content:
                if student.strip():
                    name, grades = student.split("\n", 1)
                    name = name.split(":")[1].strip()
                    grades = list(map(int, grades.split(":")[1].strip().split(", ")))
                    students.append({"name": name, "grades": grades})
    except FileNotFoundError:
        return students
    return students

def write_grade(name, grades, filename="grades.txt"):
    """Lisab õpilase ja tema hinded faili."""
    with open(filename, "a") as file:
        file.write(f"Nimi: {name}\nHinded: {', '.join(map(str, grades))}\n---\n")

