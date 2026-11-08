#how to solve hasing collsion
#seperate cahing  bucket consist with linkedlist it easy to erease and if table full  perfomance slope is gentle
#but pointer overhead  cache locality is uneffceintly


#open addressing 
#if collison  happen  find the anther empty bucket  so data is sequentaily so cache hit is hight if we need to delete  load factor is high clustering is ver slow
#this way is python diciotnary


#load factor  stored key / bucket if load factor over 0.7~0.75  expend bucket twice and present element recalating  hashing and reshasing then temporaly need o(n) time complexity amortize o(1)
# what is worst time complexity o(n) when happen
#this case is all data in one buckt this bucket like array so timecomplexity is o(n)
# so java 8 if chaing lenth is over 8 change way to store linkedlist to red-black tree


#leet code 706
class listnode:
    def __init__(self,key=1,val=-1,next=None):
        
        
        self.key=key
        self.val=val
        self.next=next
        
        
class myhashmap:
    def __init__(self):
        self.size=1000
        self.table=[listnode() for i in range(self.size)]# set dummy node head
        
        
    def __hash__(self,key:int)->int:
        return key%self.size
    
    
    
    def put(self,key:int,value:int)->None:
        idx=self.__hash__(key)
        curr=self.table[idx]
        
        while curr.next:
          if curr.next.key==key:
            curr.next.val=value
            return
        curr=curr.next
        
        
    def get(self,key:int)->int:
        idx=self.__hash__(key)#calculate bucket index
        cur=self.table[idx].next#find the real node
        
        while cur:
            if cur.key==key:
                return cur.val
            
            cur=cur.next
            
            
        return -1
    
    def remove(self,key:int)->None:
        idx=self.__hash__(key)
        prev=self.table[idx]
        
        curr=prev.next#finf the fist real data
        while curr:
            if curr.key==key:
                prev.next=curr.next\
                    
            prev=curr
            curr=curr.next
            
            
           
        
        
# leet code  146

        
    
        

    
        
        

        
        