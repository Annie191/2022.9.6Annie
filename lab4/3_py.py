length = 1
temp_length = 1
s = input()
s_length = len(s)
#print(s_length)
i = 1
temp = s[0]
#print(temp)
while i < s_length:
    if temp == s[i]:
        #print(temp)
        #print(s[i])
        #print()
        temp_length += 1
        i += 1
    elif temp != s[i]:
        if length < temp_length:
            length = temp_length
        temp_length = 1
        temp = s[i]
        i += 1
if length < temp_length:
    length = temp_length
print(length)        