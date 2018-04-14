
'''Task
Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing the size of each shoe he has in his shop. 
There are N number of customers who are willing to pay x
amount of money only if they get the shoe of their desired size.
Your task is to compute how much money 
Raghu earned.
Input Format
The first line contains X, the number of shoes. 
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers. 
The next N lines contain the space separated values of the Shoe size
desired by the customer and x, the price of the shoe.'''


from collections import Counter
N = int(input())
S =list(map(int,input().split()))
shoes =dict(Counter(S))
Cus=int(input())
price = []
for _ in range(Cus):
    price.append(list(map(int,input().split())))
for i in price:
    if price[i][0] in shoes.keys():
        summ+=price[i][1]
        
        
        # DOES NOT WORK YET
