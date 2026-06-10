# task
# in this you are given dimission of a cubiod and a number n if the sum of dimission of cubiod match n number 
# then dont append the dimission in list other wise do

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    My_list=list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sub = [i,j,k]
                
                if sum(sub) != n:
                    My_list.append(sub)
    print(My_list)
