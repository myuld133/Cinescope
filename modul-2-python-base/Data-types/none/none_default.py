def greet(name=None):
    if name is None:
        print("Привет, гость!")
    else:
        print(f"Привет, {name}!")

greet()
greet("Анна")
