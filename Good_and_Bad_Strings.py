# Jon is very fond of strings. (Or so he thinks!) But, he does not like strings which have same consecutive letters. No one has any idea why it is so. 
# He calls these strings as Bad strings. So, Good strings are the strings which do not have same consecutive letters. Now, the problem is quite simple. 
# Given a string S, you need to convert it into a Good String.

# You simply need to perform one operation - if there are two same consecutive letters, delete one of them.

def remove_duplicates(stng):
    new = stng[0]
    for i in range(1,len(stng)):
        if(stng[i-1] != stng[i]): new+= stng[i]
    return new    
    
for T in range(int(input())):
    print(remove_duplicates(input()))
