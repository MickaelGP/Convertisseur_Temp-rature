def fahrenheit_vers_celcius(temperatures: float):
    temperature = (temperatures - 32) / 1.8
    return temperature


def fahrenheit_vers_kelvin(temperatures: float):
    temperature = (temperatures + 459.67) / 1.8
    return temperature


def celcius_vers_fahrenheit(temperatures: float):
    temperature = (temperatures * 1.8) + 32
    return temperature


def celcius_vers_kelvin(temperatures: float):
    temperature = (temperatures + 273.15)
    return temperature


def kelvin_vers_celcius(temperatures: float):
    temperature: float = (temperatures - 273.15)
    return temperature


def kelvin_vers_fahrenheit(temperatures: float):
    temperature = (temperatures * 1.8) - 459.67
    return temperature


def convertisseur_de_temperature():
    print("=== Bienvenue sur le convertisseur de temperature ===")
    print('Choix disponible:')
    print('1. De Fahrenheit vers Celsius')
    print('2. De Fahrenheit vers Kelvin')
    print('3. De Celsius vers Fahrenheit')
    print('4. De Celsius vers Kelvin')
    print('5. De Kelvin vers Celcius')
    print('6. De Kelvin vers Fahrenheit')
    print('0. Sortir')

    while True:
        choix = input('Indiquez votre choix de conversion (0-6) :')
        if choix == '0':
            print('Au revoir')
            break
        elif choix in ['1', '2', '3', '4', '5', '6']:
            temperature = float(input('Donnez la temperature a convertir :'))
            if choix == '1':
                resultat = fahrenheit_vers_celcius(temperature)
                print(f"{temperature} °F en Celcius est de :", resultat)
            elif choix == '2':
                resultat = fahrenheit_vers_kelvin(temperature)
                print(f"{temperature} °F en Kelvin est de :", temperature)
            elif choix == '3':
                resultat = celcius_vers_fahrenheit(temperature)
                print(f"{temperature} °C en Fahrenheit est de :", resultat)
            elif choix == '4':
                resultat = celcius_vers_kelvin(temperature)
                print(f"{temperature} °C en Kelvin est de :", resultat)
            elif choix == '5':
                resultat = kelvin_vers_celcius(temperature)
                print(f"{temperature} °K en Celcius est de :", resultat)
            elif choix == '6':
                resultat = kelvin_vers_fahrenheit(temperature)
                print(f"{temperature} °K en Fahrenheit est de :", resultat)
        else:
            print("Operation invalide try again !")


convertisseur_de_temperature()
