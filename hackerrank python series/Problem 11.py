# Task

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example
# marks key:value pairs are
# alpha:[20,30,40]
# beta: [30,50,70]
# query_name = 'beta'
# then we have to find the percentage of query_name
# and the average percentage must contain the 2 decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

    if query_name in student_marks:
        marks = sum(student_marks[query_name])
        length = len(student_marks[query_name])
        average = (marks/length)
        print(f"{average:.2f}")        