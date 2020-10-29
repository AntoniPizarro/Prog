def anagrams(word, words):
    resultado = []
    for palabra in words:
        if len(palabra) == len(word):
            i = len(palabra)
            for caracter in palabra:
                if palabra.count(caracter) == word.count(caracter):
                    i -= 1
                if i <= 0:
                    resultado.append(palabra)
                    break
    return(resultado)

if __name__ == "__main__":
    assert(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
    assert(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])