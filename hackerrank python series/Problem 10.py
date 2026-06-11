# Task
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    records=list()
    second_lowest_list=list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
    records.sort(key=lambda x: x[1])
    
    i=1
    while i < len(records):
        if records[0][1]!=records[i][1]:
            second_lowest=records[i][1]
            break
        else:
            i +=1
                
    for i in range (len(records)):       
        if second_lowest == records[i][1]:
            second_lowest_list.append(records[i][0])
            
    second_lowest_list.sort()
    
    for i in second_lowest_list:
        print(i)
        
        