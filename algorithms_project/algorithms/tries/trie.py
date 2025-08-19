class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        print(f"Inserindo a palavra: {word}")
        for i, char in enumerate(word):
            print(f"\nPasso {i + 1}: Inserindo '{char}'")
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
                print(f"  '{char}' não encontrado, criando novo nó.")
            else:
                print(f"  '{char}' já existe, seguindo para o próximo.")
            current_node = current_node.children[char]
            print(f"  children do nó atual: {list(current_node.children.keys())}")
        current_node.is_end_of_word = True
        print(f"\nFinal da palavra '{word}' marcado com is_end_of_word = True.\n")

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True


trie = Trie()

trie.insert("apple")

# trie.insert("banana")
# trie.insert("app")
# trie.insert("orange")

# print(trie.search("apple"))
