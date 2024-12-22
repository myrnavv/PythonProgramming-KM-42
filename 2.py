import fileinput

years = [year for year in range(1880, 2020)]

male_top_names = {}
female_top_names = {}

with fileinput.input(files=(f'yob{year}.txt' for year in years)) as file:
    male_names = {}
    female_names = {}

    for line in file:
        name, sex, count = line.strip().split(',')
        count = int(count)

        if sex == 'M':
            male_names[name] = male_names.get(name, 0) + count
        elif sex == 'F':
            female_names[name] = female_names.get(name, 0) + count

        if file.isfirstline() or file.filename() != fileinput.filename():
            if male_names:
                top_male_name = max(male_names, key=male_names.get)
                male_top_names[top_male_name] = male_top_names.get(top_male_name, 0) + 1

            if female_names:
                top_female_name = max(female_names, key=female_names.get)
                female_top_names[top_female_name] = female_top_names.get(top_female_name, 0) + 1

            male_names = {}
            female_names = {}

sorted_male_names = sorted(male_top_names.items(), key=lambda x: -x[1])
sorted_female_names = sorted(female_top_names.items(), key=lambda x: -x[1])

for name, count in sorted_male_names:
    print(f"{name} {count}")

for name, count in sorted_female_names:
    print(f"{name} {count}")
