#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#You are given n scores.
#Store them in a list and find the score of the runner-up. 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    secMax=0
    maxV=0
    for i in arr:
        if maxV<arr:
            maxV=arr
            if secMax<arr and secMax!=max:
                secMax=arr
    print(secMax)

# it is working yet. just draft
