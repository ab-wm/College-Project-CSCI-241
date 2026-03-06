from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # Performance:
    # Linked_List: O(n^2). The str implementation operates in
    # quadratic time due to the combination of a current walk
    # and the repeated string catenations (linear time) at every
    # step.
    # Array: O(n^2). Same as Linked_list, current walk to the end
    # and string catenations lead to quadratic time
    
    # Orient your string from top (left) to bottom (right).
    return str(self.__dq)

  def __len__(self):
    # Performance:
    # Linked_List: O(1). Implementation simply returns a value,
    # which is constant time.
    # Array: O(1). Same as Linked_list, returns a value    
    
    return len(self.__dq)

  def push(self, val):
    # Performance:
    # Linked_List = O(1). By choosing the front, a
    # constant number of steps are required to return the first 
    # value, regardless of list length. This would have been O(n)
    # if the back was used due to the need of a current walk to the end.
    # Array: O(n): Simple index access and modification without
    # a current walk to the end would be O(1), but the occasional need to 
    # increase the size of the array leads to the O(n) time
    # complexity (__grow() is O(n))
    
    self.__dq.push_front(val)

  def pop(self):
    # Performance:
    # Linked_List = O(1). The front/head of the linked list allows 
    # constant time access, independent of the length of the list. 
    # Choosing the other end as the front would have led to O(n) 
    # due to the need of a current walk to the end.
    # Array = O(1). Front is always known and directly accessible , 
    # leading to constant time performance independendent of the 
    # length of the array.

    return self.__dq.pop_front()

  def peek(self):
    # Performance:
    # Linked_List = O(1). Using the front/head of the linked list 
    # avoids the need of a current walk to the end, allowing constant time 
    # access independent of the length of the list.
    # Array = O(1). Front is always known and accessible, constant
    # time access independent of length.

    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
