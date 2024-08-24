# versão do Python: 3.12.3

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _char_order_sum(self, word):
        return sum(ord(char) - ord('a') + 1 for char in word)

    def hash_function(self, word):
        return self._char_order_sum(word) % self.size

    def insert(self, word):
        index = self.hash_function(word)
        for item in self.table[index]:
            if item[0] == word:
                print(f"palavra ja existente: {word}")
                return
        self.table[index].append([word, 0])
        print(f"palavra inserida: {word}")

    def search(self, word):
        index = self.hash_function(word)
        for item in self.table[index]:
            if item[0] == word:
                item[1] += 1
                print(f"palavra existente: {word} {item[1]}")
                return
        print(f"palavra inexistente: {word}")

    def most_consulted(self):
        max_consultas = 0
        words = []
        for bucket in self.table:
            for item in bucket:
                if item[1] > max_consultas:
                    max_consultas = item[1]
                    words = [item[0]]
                elif item[1] == max_consultas:
                    words.append(item[0])

        if not words:
            print("tabela vazia")
        else:
            words.sort()
            print("palavras mais consultadas:")
            for word in words:
                print(word)
            print(f"numero de acessos: {max_consultas}")

    def ordered_list(self, l1, l2):
        words = []
        for bucket in self.table:
            for item in bucket:
                if l1 <= item[0][0] <= l2:
                    words.append(item[0])

        if not words:
            print("lista vazia")
        else:
            words.sort()
            print("palavras em ordem:")
            for word in words:
                print(word)

    def remove(self, word):
        index = self.hash_function(word)
        for item in self.table[index]:
            if item[0] == word:
                self.table[index].remove(item)
                print(f"palavra removida: {word}")
                return
        print(f"palavra inexistente: {word}")

    def words_in_index(self, n):
        if n < 0 or n >= self.size:
            print(f"nao ha palavras na lista de indice: {n}")
            return

        words = sorted([item[0] for item in self.table[n]])
        if not words:
            print(f"nao ha palavras na lista de indice: {n}")
        else:
            print(f"palavras na entrada: {n}")
            for word in words:
                print(word)

    def print_table(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                words = [f"{item[0]} {item[1]}" for item in sorted(bucket)]
                print(f"{i}: " + " ".join(words))
            else:
                print(f"{i}: ")


TAM_TABELA_HASH = 10
hash_table = HashTable(TAM_TABELA_HASH)

cmd = " "

while cmd != "e":
    cmd = str(input())

    match cmd:
        case "i":
            value = str(input())
            hash_table.insert(value)
        case "c":
            value = str(input())
            hash_table.search(value)

        case "f":
            hash_table.most_consulted()

        case "o":
            l1 = str(input())
            l2 = str(input())
            hash_table.ordered_list(l1, l2)

        case "r":
            value = str(input())
            hash_table.remove(value)

        case "n":
            index = int(input())
            hash_table.words_in_index(index)

        case "p":
            hash_table.print_table()
