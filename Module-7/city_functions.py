#William Stearns
#4-20-25
#Module 7.2
#This function takes a city and country and returns a formatted string.

def city_function(city, country, population=None, language=None):
    if population is not None and language is not None:
       return (f"{city.title()}, {country.title()} - population {population}, {language.title()}.") 
    elif population is not None and language is None:
        return (f"{city.title()}, {country.title()} - population {population}.")
    elif population is None and language is not None:
         return (f"{city.title()}, {country.title()}, {language.title()}.")
    else:
        return (f"{city.title()}, {country.title()}")
def main():
    print(city_function("santiago" , "chile"))
    print(city_function("paris" , "france", 2000000))
    print(city_function("cardiff" , "wales", 300000, "Welsh"))

if __name__ == '__main__':
    main()