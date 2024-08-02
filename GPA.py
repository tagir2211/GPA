grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# создаем лист средних оценок
GPA = []
summ = []
#передираем все значения grades
for i in range(len(grades)):
    summ.append(0)
    #перебираем все значеия grades[i]
    for j in range(len(grades[i])):
        summ[i] =summ[i] + grades[i][j]
    GPA.append(round(summ[i]/len(grades[i]), 2))
#создаем список из можества students и сортрируем его
sort_student = list(students)
sort_student.sort()
#Преобразуем сортированый список и средний бал в словарь и выводим
print(dict(zip(sort_student, GPA)))

