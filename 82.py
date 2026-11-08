from multiprocessing import dummy


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next










class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
       dummy = ListNode(0, head)
       prev = dummy
       
       while head:
           
           if head.nex and head.val== head.next.val:
               while head.next and head.val == head.next.val:
                   head = head.next
                   prev.next=head.next
                   
               else:
                   prev=prev.next
                   head=head.next
                   
               return dummy.next
                   
                
        
        
        #if we use dummy origin linkedist head dummy.next will be the new head after removing duplicates