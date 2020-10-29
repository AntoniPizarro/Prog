def duplicate_encode(word):
    result = ""
    mayus = ""
    print(word)
    for c in word:
        mayus += c.upper()
    for c in mayus:
        if mayus[mayus.find(c)+1:].find(c) == -1:
            result += "("
        else:
            result += ")"
    return(result)




if __name__ == "__main_-":
    assert(duplicate_encode("din"),"(((")
    assert(duplicate_encode("recede"),"()()()")
    assert(duplicate_encode("Success"),")())())","should ignore case")
    assert(duplicate_encode("(( @"),"))((")