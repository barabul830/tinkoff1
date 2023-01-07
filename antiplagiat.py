import ast

class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.treelist = []

    def generic_visit(self, node):
        self.treelist.append(type(node))
        super().generic_visit(node)


# выбор первой программы для сравнения
first = (open('euclidean_distance.py', 'r', encoding='utf-8'))
text = first.read()
tree = ast.parse(text, mode='exec')
v = Visitor()
v.generic_visit(tree)
spisok1 = v.treelist

# выбор второй программы для сравнения
second = (open('euclidean_distance2.py', 'r', encoding='utf-8'))
text = second.read()
tree = ast.parse(text, mode='exec')
v = Visitor()
v.generic_visit(tree)
spisok2 = v.treelist
spisok = spisok1 + spisok2
s = set(spisok)
alph = list(s)
dicts = {alph[i]: i for i in range(len(alph))}
spisok1 = [dicts[spisok1[i]] for i in range(len(spisok1))]
spisok2 = [dicts[spisok2[i]] for i in range(len(spisok2))]


def levenshtein(word1, word2):
    n, m = len(word1), len(word2)
    if n > m:
        n, m = m, n
        word1, word2 = word2, word1

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous[j] + 1, current[j - 1] + 1, previous[j - 1]
            if word1[j - 1] != word2[i - 1]:
                change += 1
            current[j] = min(add, delete, change)

    return current[n]


score = 1 - levenshtein(spisok1, spisok2) / max(len(spisok1), len(spisok2))
print(score)
