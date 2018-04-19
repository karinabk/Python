'''Dr. John Wesley has a spreadsheet containing a list of student's ID's, MARKS, CLASS and NAME.
Your task is to help Dr. Wesley calculate the average marks of the students.
AVERAGE = SUM_OF_ALL_MARKS/TOTAL_STUDENTS'''
from collections import namedtuple
N = int(input())
fields = input().split()
res = 0
for i in range(N):
    student = namedtuple('student',fields)
    f1, f2, f3,f4 = input().split()
    student = student(f1,f2,f3,f4)
    res += int(student.MARKS)
print('{:.2f}'.format(res/N))
