oNOT WORKING YET#You are given an integer,N.
#Your task is to print an alphabet rangoli of size N. 
#(Rangoli is a form of Indian folk art based on creation of patterns.)
#Different sizes of alphabet rangoli are shown below:

#size 3

#----c----
#--c-b-c--
#c-b-a-b-c
#--c-b-c--
#----c----

#size 5

#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------
def print_rangoli(size):
    a='a'
    for line in range(size): #loop for line
        string1=""
        chardec=0
        for i in range(size): # putting letters in decreasing order
            string1+=chr(ord(a)+size-1+chardec)
            chardec-=1
            if i==line:
                break
        if line>=1: # increasing order starts from second line
            charinc=1
            for k in range(size-1): #putting letters in increasing order 
                string1+=chr(ord(a)+size+chardec+charinc)
                charinc+=1
                if k==line-1:
                    break
        string1=list(string1)
        string1=str("-".join(string1)) # putting - between letters
        print(string1.center(4*size-3,"-"))
    for line2 in range(size-1): # second half of the rangoli
        string2=""
        chardec=0
        for i in range(size-1): # putting letters in decreasing order
            string2+=chr(ord(a)+size-1-chardec)
            chardec+=1
            if i ==size-line2-2:
                break
        charinc=1
        if line2!=size-2: # excluding last line
            for j in range(size-2): # putting letters in increasing order
                string2+=chr(ord(a)+size-chardec+charinc)
                if j==size-3-line2:
                    break
                charinc+=1
                string1=list(string2)
        string2=str("-".join(string2))
        print(string2.center(4*size-3,"-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
        
        #IT WORKS NOW
