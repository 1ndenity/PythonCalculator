import operations

def pobierz_dane():
    liczby = []

    first = input("Podaj pierwszą liczbę: ")

    try:
        liczby.append(float(first))
    except ValueError:
        print("To nie jest liczba")
        return None
    
    i = 2
    while True:
        next = input(f"Podaj {i}-ą liczbę (lub n jak nie chcesz): ")
        if next.lower() == 'n':
            break

        try:
            liczby.append(float(next))
            i += 1
        except ValueError:
            print("To nie jest liczba")
            continue
    
    if len(liczby) < 2:
        print("Musisz wprowadzić przynajmniej 2 liczby")
        return None
    
    return liczby

def wyswietl_menu():
    print("\nWybierz działanie:")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnożenie (*)")
    print("4. Dzielenie (/)")
    print("5. Modulo (%)")
    print("6. Append do krotki (Tuple)")
    print("7. Append do listy + iteracja i mnożenie")

def main():
    print("Witaj w kalkulatorze!")
    
    liczby = pobierz_dane()
    if liczby is None:
        return
    
    wyswietl_menu()
    
    operation = input("Jakie działanie chcesz używać? (wybierz 1-7): ")

    if operation == '1' or operation == '+':
        _, wynik = operations.dodawanie(liczby)
        print(wynik)
    
    elif operation == '2' or operation == '-':
        _, wynik = operations.odejmowanie(liczby)
        print(wynik)
    
    elif operation == '3' or operation == '*':
        _, wynik = operations.mnozenie(liczby)
        print(wynik)
    
    elif operation == '4' or operation == '/':
        _, wynik = operations.dzielenie(liczby)
        print(wynik)
    
    elif operation == '5' or operation == '%':
        _, wynik = operations.modulo(liczby)
        print(wynik)
    
    elif operation == '6':
        _, wynik = operations.append_do_krotki(liczby)
        print(wynik)
    
    elif operation == '7':
        _, wynik = operations.operacje_na_liscie(liczby)
        print(wynik)
    
    else:
        print(f"Nieznana operacja: {operation}. Wybierz opcję od 1 do 7.")

if __name__ == "__main__":
    main()