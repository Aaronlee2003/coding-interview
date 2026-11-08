class TrieNode:
    def __init__(self):
     self.children = {}
     self.is_end_of_word = False

    class Trie:
       def __init__(self):
        # 트라이가 시작되는 빈 루트(Root) 노드를 생성합니다.
        self.root = TrieNode()
       def insert(self,word:str)->None:
         for char in word:
           #char이 현재 트라이 안에 없다면
           if char not in current.children:
              current.children[char]=TrieNode()
           current=current.children[char] #현재 글자 
         current.is_end_of_word = True

       def search(self,word:str)->None:
         current=self.root
         for char in word:
           if char not in current.child:
             return False
           current=current.children[char]
         return current.is_end_of_word
       def startswitch(self,prefix:str)->bool:
         current=self.root
         for char in prefix:
            if char not in current.children:
              return False
            current=current.children[char]
          return True
           
