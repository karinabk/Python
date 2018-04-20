'''You are given a text of N lines. The text contains && and || symbols. 
Your task is to modify those symbols to the following:
&& → and
|| → or
Both && and || should have a space " " on both sides.'''
for _ in range(int(input())):
    input_ = input()
    while ' && ' in input_ or ' || ' in input_:
        input_ = input_.replace(" && ", " and ").replace(" || ", " or ")
    print(input_)
    
    
