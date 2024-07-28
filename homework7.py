grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = list(students)
a.sort()
b = list(grades)
c = {}
c.update({a[0]: sum(b[0])/len(b[0])})
c.update({a[1]: sum(b[1])/len(b[1])})
c.update({a[2]: sum(b[2])/len(b[2])})
c.update({a[3]: sum(b[3])/len(b[3])})
c.update({a[4]: sum(b[4])/len(b[4])})
print(c)

