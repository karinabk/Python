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
    listValues= list(student.values()) # creating list of points only
    minV = listValues[0]
    
    for i in range(len(listValues)): # finding minimum
        if minV>listValues[i]:
            minV=listValues[i]
    
    listValues=set(listValues) # getting rid of duplicate numbers
    listValues.remove(minV)  # get rif of min value
    listValues=list(listValues)
    
    secMin=listValues[0]
    for k in range(len(listValues)): # finding second minimum value
        if secMin>listValues[k]:
            secMin=listValues[k]
    
    resultList=[]
    for k,v in student.items():
        if secMin== v:
            resultList.append(k) # creating list with names of students with these points
    resultList.sort()
    string = '\n'.join(resultList)
    print(string)
            
            #it works now
