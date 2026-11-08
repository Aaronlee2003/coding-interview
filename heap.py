
heap=[]
def up_heapify(index,heap):
    child_index=index
    while child_index!=0:
        parent_index=(child_index-1)//2
        if heap[child_index]>heap[parent_index]:
            heap[child_index],heap[parent_index]=heap[parent_index],heap[child_index]
            child_index=parent_index
        else:
            return 
        
def find_bigger_child_index(index, heap_size):
    parent=index
    left_child=(parent*2)-1
    right_child=(parent*2)+1

    if left_child<heap_size and heap[parent]<heap[left_child]:
         parent = left_child
    if right_child < heap_size and heap[parent] < heap[right_child]:
        parent = right_child
    return parent
def down_heapify(index, heap):
    parent_index = index
    find_bigger_child_index=find_bigger_child_index(parent_index,len(heap))


    while parent_index!=find_bigger_child_index:
        heap[parent_index],heap[find_bigger_child_index]=heap[find_bigger_child_index],heap[parent_index]
        parent_index=find_bigger_child_index
        bigger_child_index = find_bigger_child_index(parent_index, len(heap))


def make_heap(heap,index,heap_size):
    parent=index
    le1ft_child=parent*2-1
    right_child=parent*2+1

    if left_child<heap_size and heap[parent]<heap[left_child]:
         parent = left_child
    if right_child < heap_size and heap[parent] < heap[right_child]:
        parent = right_child
    #자식노다가 부모노드 보다 아직도 크면
    if parent != index:
            array[parent], array[index] = array[index], array[parent]
            make_heap(array, parent, heap_size)
	
    # 부모노드가 되는 노드들만을 골라서 뒤에서부터 heapify를 차례로 실행
    for i in range((N - 1) // 2, -1, -1):
        make_heap(array, i, heap_size)

                                                                                 