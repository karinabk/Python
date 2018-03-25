#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications: 
#Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.
#Sample Designs
#    Size: 7 x 21 
#    ---------.|.---------
#    ------.|..|..|.------
#    ---.|..|..|..|..|.---
#    -------WELCOME-------
#    ---.|..|..|..|..|.---
#    ------.|..|..|.------
#    ---------.|.---------


def print_welcome(n,m):
    
    for line in range(n//2):
        string=".|."
        for _ in range(line):
            string+=".|..|."            
        print(string.center(m,"-"))
    welcome="WELCOME"
    print(welcome.center(m,"-"))
    print(string.center(m,"-"))
    for downline in range(n//2-1):
        list2=list(string)
        for i in range(6):
            list2.pop()
        string="".join(list2)
        print(string.center(m,"-"))

    

if __name__ == '__main__':
    list_ = input().split()
    list_=list(map(int,list_))
    print_welcome(list_[0],list_[1])
