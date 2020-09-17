'''
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
'''

'''
适合场景：
自动补全
拼写检查
IP 路由 (最长前缀匹配)
T9 (九宫格)打字预测

还有其他的数据结构，如平衡树和哈希表，使我们能够在字符串数据集中搜索单词
为什么我们还需要 Trie 树呢？尽管哈希表可以在 O(1)O(1) 时间内寻找键值，却无法高效的完成以下操作：
找到具有同一前缀的全部键值。
按词典序枚举字符串的数据集。

Trie 树优于哈希表的另一个理由是，随着哈希表大小增加，会出现大量的冲突，时间复杂度可能增加到 O(n)O(n)
其中 nn 是插入的键的数量。与哈希表相比，Trie 树在存储多个具有相同前缀的键时可以使用较少的空间
此时 Trie 树只需要 O(m)O(m) 的时间复杂度，其中 mm 为键长。而在平衡树中查找键值需要 O(m log n)O(mlogn) 时间复杂度。

查找 Trie 树中的键前缀
时间复杂度 : O(m)O(m)。
空间复杂度 : O(1)O(1)。
'''

'''
思路:
TrieNode是一个节点，里面包含了一个长度26的数组，里面是初始数组都是None
利用字母的ascii码，将当前插入的字符放在数组的对应位置
对于下一个字符就将放置到上一个节点的数组对应位置
如果是最后一个字符，那么当前节点的isEnd为true，并且数组中没有一个节点
'''


class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False

    def containsKey(self, ch):
        # 转换为ASCII码进行计算
        if self.links[ord(ch) - ord('a')]:
            return True
        return False

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.isEnd = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        print("--------")
        for i in range(len(word)):
            ch = word[i]
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
            print(node.isEnd)
        node.setEnd()

    def searchPrefix(self, word):
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word):
        node = self.searchPrefix(word)
        return node and node.isEnd

    def startsWith(self, prefix):
        node = self.searchPrefix(prefix)
        return node


if __name__ == "__main__":
    t = Trie()
    t.insert('app')
    t.insert('apple')
    print(t.search('apple'))
