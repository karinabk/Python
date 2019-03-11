#Solution for Task A
def myFun(num,string):
  mapa={}
  
  s=set()
  for word in string:
    vertex1 = ""
    vertex2 = ""

    for i in range(len(word)):
      vertex1=""
      if vertex2=="":
        if i+3<=len(word):
          for k in range(3):
            vertex1+=word[k+i]
      else:   
        vertex1=vertex2
      if i+4<=len(word):
        vertex2=""
        for j in range(3):
          vertex2+=word[j+i+1]
      else:
        break
    
      pair = (vertex1,vertex2)
      s.add(vertex1)
      s.add(vertex2)
      if vertex1 and vertex2:
        if pair not in mapa:
          mapa[pair]=1
        else:
          mapa[pair]+=1
  print(len(s))
  print(len(mapa))  
  for g in mapa:
    print("{} {} {}".format(g[0],g[1],mapa[g]))

if __name__ == '__main__':
  N = int(input())
  strings = []
  for _ in range(N):
    string = input()
    if len(string) < 3:
      continue
    strings.append(string)
  myFun(N,strings)
    

#Solution for task B


def myFun(nums,shab):
  d ={}
  s1 = ""
  s2=""

  for n in shab:
 
    chislo=""
    x =0
    for i in n:
      if i=='X':
        x+=1
      if i.isdigit():
        chislo+=i
    d[chislo]=(n,x)
  res1=[]
  for num in nums:
    chis1=""
    z=0
    for f in num:
      if f.isdigit():
        z+=1
    stri=""
    l=0
    for i in num:
      
      if i.isdigit():
        chis1+=i
        if chis1 in d:
          if d[chis1][1]+len(chis1)==z:
                
            l = len(chis1)
            stri=d[chis1][0]
      
    res =""
    ind = 0
    
    while stri[ind]!='X':
      res+=stri[ind] 
      ind+=1
    while stri[ind]=='X':
      res+=chis1[l]
      l+=1
      ind+=1
    while ind<len(stri):
      res+=stri[ind]
      ind+=1
    res1.append(res)
  for _ in res1:
    print(_)

if __name__ == '__main__':
  N = int(input())
  nums = []
  for _ in range(N):
    string = input()
    nums.append(string)
  N2=int(input())
  shab=[]
  for _ in range(N2):
    string=input()
    shab.append(string)
  #nums = ['28-49-5-123-45-67','87544456789','+28 (495) 123 45 56','875-(29)-123456']
  #shab = ['+875 (29) 1XXXXX - Atlantis MythCell','+875 (44) 4XXXXX - Atlantis MobTelecom','+28 (495) XXXXXXX - ElDorado GoldLine']
  myFun(nums,shab)

    
