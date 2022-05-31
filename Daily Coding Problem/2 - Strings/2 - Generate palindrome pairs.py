
def isPalindrome(x: str) -> bool:
    return x == x[::-1]
        

isPalindrome('ciao')

def palindromePairs(words: list):

    results = []

    for i, el1 in enumerate(words):
        for j, el2 in enumerate(words):
            if j==i:
                pass
            else:
                if isPalindrome(el1 + el2):
                    results.append((i, j))
    
    return results


palindromePairs(['ciao', 'oaic', 'da', 'di', 'd'])