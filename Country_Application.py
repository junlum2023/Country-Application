def display_menu():
    print("Command Menu")
    print("view --> view country name")
    print("add --> Add a country")
    print("delete --> delete a country")
    print("exit --> Exit the program")
    print()
    
def display_codes(countries):
    code = list(countries.keys())
    code.sort()
    codes_line = "Country codes: "
    for code in code:
        codes_line += code + " "
    print(codes_line)
    
def view(countries):
    display_codes(countries)
    code = input("enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}. \n")
    else:
        print("There is no country with that code. \n")
        
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using that code")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added. \n")
        
def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted")
    else:
        print("There is no country with that code. \n")
        
def main():
    countries = {"CA": "Canada", "CN": "China", "CL": "Chile"}
    
    display_menu()
    while True:
        command = input("Command:  ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete(countries)
        elif command == "exit":
            print("Bye")
            break 
        else:
            print("Not a valid command, please try again. \n")
            
if __name__ == "__main__":
    main()
    
    
                     
          
          
