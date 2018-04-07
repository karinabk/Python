def merge_the_tools(string, k):
    # your code goes here
    string=list(string)
    print(len(string))
    print(k)
    if len(string)>k:
        for i in range(0,len(string),len(string)//k):
            result=[]
            for j in range(len(string)//k):
                if string[i] not in result:
                    result.append(string[i])
                i+=1
            print("".join(result))
    if len(string)<=k:
        
        result=[]
        for q in range(len(string)):
            
            if string[q] not in result:
                result.append(string[q])
                
        print("".join(result))
        
        
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    #  DID NOT PASS ALL TESTS
