'''A valid email address meets the following criteria:
It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is , , or  characters in length.
Given  pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
Hint: Try using Email.utils() to complete this challenge. For example, this code:
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
produces this output:
('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
Input Format
The first line contains a single integer, , denoting the number of email address. 
Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this format:
name <user@email.com>'''
import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m: print(x,y)
