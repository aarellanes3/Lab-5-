from Heaps import Heaps


def read_file():
    h_a = open('test_file.txt')

    lines = h_a.readlines()
    for i in range(len(lines)):
        line = lines[i].replace("\n", "")
        tokens = line.split(',')
        he = Heaps()

        for j in range(len(tokens)):
            he.insert(int(tokens[j]))

        print(he.heap_array)
        r = []

        while not he.is_empty():
            r.append(he.extract_min())
            print(r)
            break


read_file()

