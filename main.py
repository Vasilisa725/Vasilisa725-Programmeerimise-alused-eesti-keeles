"""
User managment System
Id: 1, Name: Thomas, 44
Id: 2, Name: Thomas, 44
Id: 3, Name: Thomas, 44
"""
import bookGreator as bookGreator
import vasia as vasia

def main():
    print("1 - külalisteraamat")
    print("2 - ")
    userInput = input("Sinu valik:")
    if userInput == "1":
        bookGreator.guestBook()
    elif userInput == "2":
        vasia.vasia()
    elif userInput == "3":
    userFile = input("Milline file sa tahad lugeda?")
    reader.readFile(userFile)
    else:
        print("vale valik")
        
main()