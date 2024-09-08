grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)

grades_SR = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),
             sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
print(grades_SR)

students_sort=sorted(students)
print(students_sort)

dict_cl=dict(zip(students_sort, grades_SR))
print(dict_cl)
