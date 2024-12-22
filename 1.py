import csv
import os

with open('Rammstein.csv', 'w', newline='') as csvfile:
    fieldnames = ['Song', 'Year']  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
    writer.writeheader() 
    writer.writerow({'Song': 'Mutter', 
                     'Year': 2001})
    writer.writerow({'Song': 'Sonne', 
                     'Year': 2001})
    writer.writerow({'Song': 'Ohne dich', 
                     'Year': 2004})
    writer.writerow({'Song': 'Deutchland', 
                     'Year': 2019})
    writer.writerow({'Song': 'Ich will', 
                     'Year': 2001})
    writer.writerow({'Song': 'Du hast', 
                     'Year': 1997})
    writer.writerow({'Song': 'Mein herz brennt', 
                     'Year': 2001})
    writer.writerow({'Song': 'Du riechst so gut', 
                     'Year': 1995})

with open('Rammstein.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  
    for heading in reader.fieldnames: 
        print(heading, end=' ')
    print('\n------------')
    for row in reader:  
        print(row['Song'], row['Year'])
        
print('--------------------------------\nDo you want to delete this file?\nIf you do, enter "1", if not, enter any other symbol:')    
del_file = input()   
if del_file == '1':
    os.remove('Rammstein.csv')
    print('File is succesfully deleted.')   
else:
    print('File is saved.')