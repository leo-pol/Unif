#Code de Leo-Pol Brants
#17/10/18
def is_adn(s):
    if s == []:
        return False
    s = s.lower()
    a = ('a' in s)
    c = ('c' in s)
    g = ('g' in s)
    t = ('t' in s)

    if a and c and g and t :
        return True
    else:
        return False

def positions(s, p):
    s = s.upper()
    p = p.upper()
    pos = []
    l=len(p)
    for i in range (len(s)):
        if s[i:i+l] == p:
            pos.append(i)
    return pos

def distance_h(s, g):
    distance = 0
    s = s.lower()
    g = g.lower()
    if len(s) != len(g):
        return None
    for i in range (len(s)):
        if s[i] != g[i]:
            distance += 1
    return distance

def plus_long_palindrome(s):
    s = s.lower()
    pal = []
    for i in len(s):
        a = i
        b = i+1
        while s[a]==s[b] and a>=0:
            pal.append(s[a:b+1])#ajouter le pal de plus en plus grand dans la liste puis trouver le plus grand et le return
            a -= 1
            b += 1
        

s = "aCgtcgtAccatg"
g = "actggtaccatga"
print(is_adn(s))
print (positions(s,'CG'))
print(distance_h(s,g))
