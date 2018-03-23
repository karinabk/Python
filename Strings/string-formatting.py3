#Given an integer, n , print the following values for each integer i from 1 to n
#Each value should be space-padded to match the width of the binary value of:
#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary
#The four values must be printed on a single line in the order specified above for each i from 1 to n. 
#Each value should be space-padded to match the width of the binary value of n.

def print_formatted(number):                                        
    string = "{:>" + str(len(str(bin(number)))-2) + "}"
    for k in range(1, number+1):                                    
        print(string.format(k), end = " ")
        print(string.format(str(oct(k))[2:len(str(oct(k)))]), end = " ")
        print(string.format((str(hex(k))[2:len(str(hex(k)))].upper())), end = " ")   
        print(string.format(str(bin(k))[2:len(str(bin(k)))]))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
