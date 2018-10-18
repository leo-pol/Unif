#Code de Leo-Pol Brants et Valérian Thiry, groupe 11.88
#17/10/18
import bioinfo

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_is_adn ():
    """ pre : 'is_adn(s)' une fonction importée du module bioinfo
        post : test si la fonction fait ce qu'on attend d'elle et donne la réussite ou non des tests
    """
    test(bioinfo.is_adn('atx')==False)
    test(bioinfo.is_adn('atg')==True )
    test(bioinfo.is_adn('bctg')==False)
    test(bioinfo.is_adn('aaaa')==True)
    test(bioinfo.is_adn('actg')==True)
  
def test_positions():
    """ pre : 'positions(s, p)' une fonction importée du module bioinfo
        post : test si la fonction fait ce qu'on attend d'elle et donne la réussite ou non des tests
    """
    test(bioinfo.positions("atagcttagctatcgactagcatcgcttacgactacga", "agc")==[2,7,18])
    test(bioinfo.positions("atgxyzjzzxyz", "xyz")==[3,9])
    test(bioinfo.positions("abc", "xyz")==[])
    test(bioinfo.positions("aaaz", "z")==[3])
    test(bioinfo.positions("atgvdzjzzvdz", "atg")==[0])
  
def test_distance_h():
    """ pre : 'distance_h(s, g)' une fonction importée du module bioinfo
        post : test si la fonction fait ce qu'on attend d'elle et donne la réussite ou non des tests
    """
    test(bioinfo.distance_h("chien", "niche")==5)
    test(bioinfo.distance_h("abcde", "abcdf")==1)
    test(bioinfo.distance_h("abcde", "abcd")==None)
    test(bioinfo.distance_h("abcde", "zbydx")==3)
    test(bioinfo.distance_h("jjjjj", "jjjjj")==0)
    test(bioinfo.distance_h("abcde", "abcde")==0)
    test(bioinfo.distance_h("", "")==0)
    
def test_plus_long_palindrome():
    """ pre : 'plus_long_palindrome(s)' une fonction importée du module bioinfo
        post : test si la fonction fait ce qu'on attend d'elle et donne la réussite ou non des tests
    """
    test(bioinfo.plus_long_palindrome("kayyak")=="kayyak")
    test(bioinfo.plus_long_palindrome("abcdefjijjijabcde")=="jijjij")
    test(bioinfo.plus_long_palindrome("kayak")=="k")
    test(bioinfo.plus_long_palindrome("abcdeff")=="ff")
    
test_is_adn ()
test_positions()
test_distance_h()
test_plus_long_palindrome()