input1 = input('Enter a phrase 1: ')  # отримуємо першу фразу від користувача
input2 = input('Enter a phrase 2: ')  # отримуємо другу фразу від користувача

phrase1 = input1.lower()  # перетворюємо першу фразу в нижній регістр
phrase2 = input2.lower()  # перетворюємо другу фразу в нижній регістр
set1 = set(symbol for symbol in phrase1 if symbol.isalpha())  # отримуємо множину унікальних літер з першої фрази
set2 = set(symbol for symbol in phrase2 if symbol.isalpha())  # отримуємо множину унікальних літер з другої фрази
print(set1)  # виводимо множину літер першої фрази
print(set2)  # виводимо множину літер другої фрази

if set2.issubset(set1):  # перевіряємо, чи множина літер другої фрази є підмножиною першої
    print('You can make the second phrase with the use of letters from the first phrase')  
else:
    print('You cannot make the second phrase with the use of letters from the first phrase') 
