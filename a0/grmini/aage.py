s1 = "listen"
s2 = "silent"
 
is_anagram = sorted(s1) == sorted(s2)

if is_anagram:
    print("anagram")
else:
    print("not_anagram")
