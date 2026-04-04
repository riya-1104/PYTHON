#Wap to accept a string and print the most occurring vowel and its frequency
s=input()
vowel="aeiouAEIOU"
freq={}
for ch in s:
    if ch in vowel:
        freq[ch]=freq.get(ch,0)+1
        
if freq:
    max_vowel=max(freq,key=freq.get)
    print(max_vowel,freq[max_vowel])
else:
    print("vowels doesnt exist in string")
