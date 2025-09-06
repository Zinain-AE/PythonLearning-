name= input('Enter your name?')

match name:
    case "Wednesday" | "Modrica" | "Gomez" :
        print("Addams")
    case "Siren":
        print("Nevermore")
    case _:
        print("Nope")