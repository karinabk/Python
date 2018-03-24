NOT WORKING YET#You are given an integer,N.
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
    
    charinc=0
    chardec=0
    char_='a'
    string = ""
    first=chr(ord(char_)+size-1)
    for line in range(size):
        chardec=0
        for i in range(line+1):
            # print(string)
            string+=chr(ord(char_)+size-1-chardec)
            string+="-"
            if (ord(char_)+size-1-chardec)-ord(char_)==line+1:
                print("FREE")
                break
            chardec+=1
        # for k in range(line):
        #     string+=chr(ord(char_)+size-1+charinc)
        #     string+="-"
        #     charinc+=1
        
        print(string.center(4*size-3,"-"))
    
    
    
    
    
#     line=0
#     chardec=0
#     levaya=1
#     for i in range(size):
#         for k in range((size+size-1+(size+size-2))//2-line):
#             print("-", end="")
#         for l in range(levaya):
#             print(chr(ord(char_)+size-1-chardec), end="")
            
#             print(chr(ord(char_)+size-1-chardec), end="")
#             print("-")
#         for z in range(levaya-1):
            
#         for m in range((size+size-1+(size+size-2))//2-line):
#             print("-")
#         print("")
#         levaya+=1
#         line +=2
#         chardec+=1
    
 #  TRIED FOR PLENTY IF TIMES 
 #IS NOT WORKIN YET
