#Code de Leo-Pol Brants
#17/10/18
def is_adn(s):
    """pre : s doit etre un string
       post: retourne si s est une sequence d'adn ou pas
"""
    if s == []:
        return False
    s = s.lower()
    a = ('a' in s)
    c = ('c' in s)
    g = ('g' in s)
    t = ('t' in s)

    for i in s:
        if i != 'a' and i != 'c' and i != 'g' and i != 't':
            return False
    return True

def positions(s, p):
    """ pre:s et p, des strings
        post: retourne la position de p dans s
    """
    s = s.upper()
    p = p.upper()
    pos = []
    l=len(p)
    for i in range (len(s)):
        if s[i:i+l] == p:
            pos.append(i)
    return pos

def distance_h(s, g):
    """pre: s et g, deux strings
       post: retourne la somme des lettres differentes entre s et g
    """
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
    """pre: s, string
       post: retourne le plus long palindrome contenu dans s
    """
    s = s.lower()
    pal = []
    for i in range(len(s)):
        a = i
        b = i+1
        while b<len(s) and s[a]==s[b] and a>=0:
            pal.append(s[a:b+1])
            a -= 1
            b += 1
    if pal == []:
        return s[0]
    long_pal=[len(i) for i in pal]
    for i in range(len(long_pal)):
        if long_pal[i] == max(long_pal):
            pos_pal=i
    return pal[pos_pal]
    
        

s = "aCgtcgtAccatg"
g = "actggtaccatga"
if is_adn(s):
    print (positions(s,'CG'))
    print(distance_h(s,g))
    print(len(s))
    print(plus_long_palindrome(s))
else :
    print(s,"n'est pas une sequence d'ADN")
