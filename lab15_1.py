def koef_binom(n):
    row = [1]
    for _ in range(n): 
        yield row       
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
            
for row in koef_binom(int(input('Enter a degree: '))):
    print(' '.join(map(str, row)))