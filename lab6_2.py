provinces = {'A': 'Newfoundland', # словник для провінцій Канади
             'B': 'Nova Scotia',
             'C': 'Prince Edward Island',
             'E': 'New Brunswick',
             'G': 'Quebec',
             'H': 'Quebec',
             'J': 'Quebec',
             'K': 'Ontario',
             'L': 'Ontario',
             'M': 'Ontario',
             'N': 'Ontario',
             'P': 'Ontario',
             'R': 'Manitoba',
             'S': 'Saskatchewan',
             'T': 'Alberta',
             'V': 'British Columbia',
             'X': 'Nunavut or Northwest Territories',
             'Y': 'Yukon'}
while True:
    # введення поштового індексу користувачем
    postal_code = input("Enter a postal code: ").upper()  # переводимо літери у верхній регістр
    
    # перевіряємо на правильність поштового індексу
    if len(postal_code) == 3 and postal_code[0].isalpha() and postal_code[1].isdigit() and postal_code[2].isalpha():
        symbol1 = postal_code[0]
        symbol2 = postal_code[1]            
        if symbol1 in provinces: # перевіряємо, чи є перша літера серед провінцій Канади
            if symbol2 == '0':   # міська чи сільська місцевість
                location_type = "a rural area"
            else:
                location_type = "an urban area"  
            # виводимо кінцеву інформацію     
            print("The addressee is located in", location_type, "of the", provinces[symbol1], "province.")
            break 
        else:
            print("This is not a canadian postal code.")
            continue
    else:
        print("Incorrect postal code.")
        continue

