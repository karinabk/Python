#Ms. Gabriel Williams is a botany professor at District College. 
#One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
#Input Format
#The first line contains the integer,N, the total number of plants.
#The second line contains the N space separated heights of the plants.

def average(array):
    s=set()
    s.update(array)
    setSum=sum(s)
    
    return setSum/len(s)
    
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
