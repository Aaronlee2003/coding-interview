class Solution:
    def isValid(self, s: str) -> bool:
    
        stack=[]
        for ch in s:
            if ch in '([{':
                stack.append(ch)
                
            if not stack:
                return False
            if ch==')' and stack.pop()!='(':
                return False
            
            if ch=='[' and stack.pop()!=']':
                return False
            if ch=="{" and stack.pop()!='}':
                return False    
            
        return True
                
                
                