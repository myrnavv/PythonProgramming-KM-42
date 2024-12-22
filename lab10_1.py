salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
indexation_list = []
def calculate_indexation(salary):
    '''
    the function calculates the indexation for a given salary
    '''
    return round(salary * 0.3, 2)
        
def generate_salary(salary_list, calculate_indexation):
    '''
    the function generates a new list of salaries after applying indexation.
    It takes in a list of salaries and a function to calculate indexation.
    '''
    salary_list2 = []  
    global indexation_list 
    indexation_list = []  # clear the global indexation_list to avoid duplications on multiple calls of function
    for salary in salary_list:
        new_salary = round(salary + calculate_indexation(salary), 2) # calculate new salary
        indexation_list.append(calculate_indexation(salary))
        salary_list2.append(new_salary)
    return salary_list2
new_salary_list = generate_salary(salary_list, calculate_indexation)
print("Salary table:") # print the table of original salaries, new salaries and indexations for each item
for i in range(len(salary_list)):
    print(salary_list[i], new_salary_list[i], indexation_list[i])