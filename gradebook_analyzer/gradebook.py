# Vedansh Rawat 11/11/2025 Analyzing and reporting student grades
def calculate_average(marks):#function to calculate average marks
    total=sum(marks.values())
    average=total/len(marks)
    return average
def calculate_median(marks):#function to calculate median marks
    sorted_marks=sorted(marks.values())
    n=len(sorted_marks)
    if n%2==0:
        median=(sorted_marks[n//2-1]+sorted_marks[n//2])/2
    else:
        median=sorted_marks[n//2]
    return median
def find_max_score(marks):#function to find the maximum score
    max_student=max(marks,key=marks.get)
    max_score=marks[max_student]
    return max_student,max_score
def find_min_score(marks):#function to find the minimum score
    min_student=min(marks,key=marks.get)
    min_score=marks[min_student]
    return min_student,min_score
print('Welcome to the Gradebook Program !! it helps you to analyze and report student grades')
marks={}#dictionary to store student names and their marks
grades={}#dictionary to store student names and their grades
countA,countB,countC,countD,countF=0,0,0,0,0#counters for each grade
n=int(input('Enter the number of students: '))
for i in range(n):
    name=input('enter the name of the student :')
    mrks=float(input(f'enter the marks of {name}:'))
    marks[name]=mrks#storing name and marks in dictionary
    if mrks>=90:#assigning grades based on marks
        grades[name]='A'
        countA+=1
    elif mrks>=80:
        grades[name]='B'
        countB+=1
    elif mrks>=70:
        grades[name]='C'
        countC+=1
    elif mrks>=60:
        grades[name]='D'
        countD+=1
    else:
        grades[name]='F'
        countF+=1
print('------student report------')#printing the report
print(f"{'Name':<25} {'Marks':>8} {'Grade':>6}")
print('-' * 41)
for student in marks:
    print(f"{student:<25} {marks[student]:8.2f} {grades[student]:>6}")
print(f'the number of students who got A grade is {countA} and the number of students who got B grade is {countB}')#printing grade counts
print(f'the number of students who got C grade is {countC} and the number of students who got D grade is {countD}')
print(f'the number of students who got F grade is {countF}')
print(f'the average is {calculate_average(marks)}')#printing average marks
print(f'the median is {calculate_median(marks)}')#printing median marks
max_student,max_score=find_max_score(marks)#printing maximum score
print(f'the highest score is {max_score} obtained by {max_student}')
min_student,min_score=find_min_score(marks)#printing minimum score
print(f'the lowest score is {min_score} obtained by {min_student}')     




        
