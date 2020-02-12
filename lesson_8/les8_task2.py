# 2) Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque
from operator import attrgetter


class Leaf:
    def __init__(self, item):
        self.symbol, self.data = item


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Huffman:
    def __init__(self):
        self.codes = {}

    def gen_codes(self, tree, code=''):
        if isinstance(tree, Node):
            self.gen_codes(tree.left, code=f'{code}0')
            self.gen_codes(tree.right, code=f'{code}1')
        elif isinstance(tree, Leaf):
            self.codes[tree.symbol] = code

    def coder(self, s):
        string = Counter(s).items()
        leaves = [Leaf(i) for i in string]
        while len(leaves) > 1:
            leaves = deque(sorted(leaves, key=attrgetter('data')))
            left, right = leaves.popleft(), leaves.popleft()
            node_weight = left.data + right.data
            leaves.append(Node(node_weight, left, right))
        tree = leaves.pop()
        self.gen_codes(tree)
        return ' '.join([self.codes[i] for i in s])


s1 = 'В лесу родилась елочка!'
s = 'beep boop beer!'
ss = Huffman()
print(f'Строка: < {s} > закодированная по алгоритму Хаффмана:\n{ss.coder(s)}')
