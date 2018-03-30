#Given the names and grades for each student in a Physics class of N
#students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Output Format
#Print the name(s) of any student(s) having the second lowest grade in Physics; 
#if there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    student=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    student = dict(student)
    listValues= list(student.values())
    minV = listValues[0]
    secMin=0.0
    for i in range(len(listValues)):
        if minV>listValues[i]:
            if secMin!=minV: # in case if there are several minimum values
                secMin=minV  # for saving second minimum value
            minV=listValues[i]
    resultList=[]
    for k,v in student.items():
        if secMin== v:
            resultList.append(k)
    resultList.sort()
    string = '\n'.join(resultList)
    print(string)
            
            #it works now
