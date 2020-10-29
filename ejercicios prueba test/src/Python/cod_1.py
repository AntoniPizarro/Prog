def repeats(array):
        
    num_items_repetidos = 0
    suma = 0
    for item in array:
        if num_items_repetidos < 2 and array.count(item) == 1:
            suma += item
            num_items_repetidos += 1
        elif num_items_repetidos == 2:
            return suma
        else:
            continue
    return suma

if __name__ == "__main__":
    assert(repeats([4,5,7,5,4,8]),15)
    assert(repeats([9, 10, 19, 13, 19, 13]),19)
    assert(repeats([16, 0, 11, 4, 8, 16, 0, 11]),12)
    assert(repeats([5, 17, 18, 11, 13, 18, 11, 13]),22)
    assert(repeats([5, 10, 19, 13, 10, 13]),24)