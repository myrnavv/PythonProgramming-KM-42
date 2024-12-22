with open('gadsby.txt', 'r') as file:
    lines = file.readlines()
letter_count = {}
total_letters = 0
for line in lines:
    for char in line.lower():
        if char.isalpha():  # check if the character is a letter
            if char not in letter_count:
                letter_count[char] = 0
            letter_count[char] += 1
            total_letters += 1  # calculate the total number of letters

letter_percentage = {}
for letter, count in letter_count.items():
    letter_percentage[letter] = (count / total_letters) * 100

# sort letters by percentage and round them
sorted_letters = sorted(((letter, round(percentage, 3)) for letter, percentage in letter_percentage.items()), key=lambda x: -x[1]) 

print("Top 5 letters:")  # print top 5 and bottom 5 letters
for char, percentage in sorted_letters[:5]:
    print(f"{char.upper()}: {percentage}%")

print("Bottom 5 letters:")
for char, percentage in sorted_letters[-5:]:
    print(f"{char.upper()}: {percentage}%")