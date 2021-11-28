import random
def shuffleString(x, n):
    y = []
    x = list(x)
    count =  0
    while count < n:
        random.shuffle(x)
        gabung = ''.join(x)
        count += 1
        if gabung not in y:
            y.append(gabung)
        else:
            count -= 1
    print(y)

shuffleString('aku', 3)
