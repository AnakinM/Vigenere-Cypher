f = open("output.txt", "r")
text = f.read()
f.close()

# Creates list of columns as lists. Basically, listo of lists
def divide_by_columns(n_cols, string):
    columns = []
    for i in range(n_cols):
        array = []
        for c in range(len(string)):
            if n_cols*c+i > len(string)-1: break
            array.append(string[n_cols*c+i])
        columns.append(array)
    return columns

def print_columns(array):
    for i in range(len(array)):
        row = ""
        for j in range(len(array[i])):
            row += array[i][j]
        print(row)

# Returns list of chars occurances. List has length of 26, with occurance of each letter at 
# given position in alphabet.
def count_char_occurances(string):
    alphabet_as_ascii = [_ for _ in range(ord('a'), ord('z')+1)]
    occurances = [0 for i in range(26)]
    for i in range(len(alphabet_as_ascii)):
        for c in string:
            if ord(c) == alphabet_as_ascii[i]:
                occurances[i] += 1
    return occurances

def calc_coincidence_index(l, occ):
    elems = [e*(e-1) for e in occ]
    summ = sum(elems)
    return summ/(l*(l-1))


def calc_mutual_concidence(n, lengths):
    products = []
    g=0
    for i in range(0, len(n)):
        for j in range(g, len(n)):
            products = [n[i][k]*n[j][k] for k in range(0, len(n[i]))]
            result = sum(products)/(lengths[i]*lengths[j])
            print("Mutual coincidence of ", i, " and ", j, " is ", result)
        g += 1

number_of_columns = int(input("Set number of columns: "))
divided = divide_by_columns(number_of_columns, text)
# n is list of lists of letter occurances
n = []
coincidence_indexes = []
for i in range(len(divided)):
    n.append(count_char_occurances(divided[i]))
    coincidence_indexes.append(calc_coincidence_index(len(divided[i]), n[i]))
    print("Coincidence index of column ", i, " is: ", coincidence_indexes[i])
lengths = [len(_) for _ in divided]
calc_mutual_concidence(n, lengths)
# 97 - a, 122 - z