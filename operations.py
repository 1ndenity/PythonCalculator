def dodawanie(liczby):
    result = liczby[0]
    for i in range(1, len(liczby)):
        result += liczby[i]
    return result, f"Wynik dodawania: {' + '.join([str(l) for l in liczby])} = {result}"

def odejmowanie(liczby):
    result = liczby[0]
    for i in range(1, len(liczby)):
        result -= liczby[i]
    return result, f"Wynik odejmowania: {' - '.join([str(l) for l in liczby])} = {result}"

def mnozenie(liczby):
    result = liczby[0]
    for i in range(1, len(liczby)):
        result *= liczby[i]
    return result, f"Wynik mnożenia: {' * '.join([str(l) for l in liczby])} = {result}"

def dzielenie(liczby):
    result = liczby[0]
    try:
        for i in range(1, len(liczby)):
            if liczby[i] == 0:
                raise ZeroDivisionError("Nie można dzielić przez zero!")
            result /= liczby[i]
        return result, f"Wynik dzielenia: {' / '.join([str(l) for l in liczby])} = {result}"
    except ZeroDivisionError as e:
        return None, f"Błąd: {e}"

def modulo(liczby):
    result = liczby[0]
    try:
        for i in range(1, len(liczby)):
            if liczby[i] == 0:
                raise ZeroDivisionError("Nie można wykonać operacji modulo przez zero!")
            result %= liczby[i]
        return result, f"Wynik modulo: {' % '.join([str(l) for l in liczby])} = {result}"
    except ZeroDivisionError as e:
        return None, f"Błąd: {e}"

def append_do_krotki(liczby):
    krotka = tuple(liczby)
    
    try:
        new_value = float(input("Podaj wartość do dodania do krotki: "))
        nowa_krotka = krotka + (new_value,)
        return nowa_krotka, f"Oryginalna krotka: {krotka}\nNowa krotka po dodaniu {new_value}: {nowa_krotka}"
    except ValueError:
        return krotka, "To nie jest poprawna liczba dla krotki"

def operacje_na_liscie(liczby):
    dlugosc = len(liczby)
    nowa_lista = [element * dlugosc for element in liczby]
    
    wynik = f"Oryginalna lista: {liczby}\n"
    wynik += f"Długość listy: {dlugosc}\n"
    wynik += f"Nowa lista po mnożeniu każdego elementu przez długość: {nowa_lista}\n"
    
    wynik += f"Suma elementów nowej listy: {sum(nowa_lista)}\n"
    wynik += f"Średnia wartość elementów nowej listy: {sum(nowa_lista) / len(nowa_lista)}"
    
    return nowa_lista, wynik