def arryastack(self,capacity=10):
        self.capacity=capacity
        self.stack=[0]*capacity
        self.top=-1#current index of the top element
        
        
        
        def push(self,element):
            #edge case
            if self.top==self.capacity-1:
                print("stack is full")
                return
            self.top+=1
            self.stack[self.top]=element
            
            
            
            
        def pop(self):
            #edge case
            if self.top==-1:
                print("stack is empty")
                return
            element=self.stack[self.top]
            self.top-=1
            return element
        
        
        def peek (self):
            if self.empty():
                print("stack is empty")
                return
            return self.stack[self.top]
        
        
        def empty(self):
            return self.top==-1
        
        
        def size(self):
            return self.top+1
        
        
        
class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
class linkedliststack:
    def __init__(self):
        self.head=None
        self.size=0
    
    def push(self,data):
        new_node=node(data,next=self.head)
        self.head=new_node
        self.size+=1
        
    def pop(self):
        if self.empty():
            print("stack is empty")
            return
        data=self.head.data
        self.head=self.head.next
        self.size-=1
        return data
        
    def peek(self):
        if self.empty():
            print("stack is empty")
            return
        return self.head.data
    
    def empty(self):
        return self.head is None

    def size(self):
        return self.size
    
class maxheap:
    def __init__(self,array=None):
        if array is not None:
            self.heap=array
            self.size=len(array)
            self.buildheap()
            
            
        else:
            self.heap=[]
            self.size=0
            
            
    def parent(self,index):
        return (index-1)//2
    
    def rightchild(self,index):
        return 2*index+2
    def leftchild(self,index):
        return 2*index+1
    
    def push(self,value):
        self.heap.append(value)
        self.size+=1
        self.heapifyup(self.size-1)#push at th last index and heapify up
        
        
    def shiftup(self,index:int):
        while index>0:
            parent=self.parent(index)
            if self.heap[parent]<self.heap[index]:
                self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
                index=parent
            else:
                break
    def pop(self):
        if  self.empty():
            print("heap is empty")
            return
        max_value=self.heap[0]
        last_value=self.heap.pop()
        if not self.empty():
            self.heap[0]=last_value
            self.heapifydown(0)
        self.size-=1
        return max_value
    
    
    #why pop self.heap[0] aand then heapify down from. if we remove pop[0] then we have to shift all the elements to left which is O(n) time complexity. so we replace the root with the last element and then heapify down from root which is O(log n)
    #heap is completley binary tree so we can represent it as an array. so we can use the last element to replace the root and then heapify down from root to maintain the heap property.
    
    def heapifydown(self,index:int):
        n=len(self.heap)
        
        while True:
            left=2*index+1
            right=2*index+2
            largest=index

            
            
            if left<n and self.heap[left]>self.heap[largest]:
              largest=left
            if right<n and self.heap[right]>self.heap[largest]:
               largest=right
        #if largest same index largest dont move else swap and heapify down
            if largest!=index:
               self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
               index=largest
            else:
                break
    def buildheap(self):
        for i in range((self.size//2)-1,-1,-1):
            self.heapifydown(i)
            #why we star n//1 completley binarry tree has property n/2 node we dont need to heapify down leaf nodes so we start from n//2-1 to 0 and heapify down each node to maintain the heap property.          
    def empty(self):
        return self.size==0
    
    def peek(self):
        if self.empty():
            print("heap is empty")
            return
        return self.heap[0]
    
    
    def len (self):
        return self.size