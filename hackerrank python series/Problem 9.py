# Task
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score(second highest that must not be same as first highest).
# You are given n scores(total number of scores). 
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = (list(map(int, input().split())))
    
    arr.sort()
    
    for i in range(1,n):
        if arr[n-1]!=arr[n-i-1]:
            print(arr[n-i-1])
            break

