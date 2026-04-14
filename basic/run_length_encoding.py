'''Given a string containing uppercase characters (A-Z), compress the string
using Run Length encoding. Repetition of character has to be replaced by storing
the length of that run.'''

def encoding(s):
    if not s:
        return ""
    ans=""
    c=1
    
    for i in range(1,len(s)):
         if s[i]==s[i-1]:
             c+=1
         
         else:
             ans+=str(c)+s[i-1]
             c=1
    ans+=str(c)+s[i-1]
    return ans  
    
s=input()
print(encoding(s))
