from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()


    ### Front and backs of queues
    # Linked list:
    #   - Front is head and back is tail
    #   - Queue is built by pushing elements
    #     to the tail and elements removed
    #     from the front.
    #   - Head value returned for peeks, which is
    #     the front
    #   - No modification to str as it builds
    #     from head to tail
    # Queue:
    #   - Front is stored by self.__front and back
    #     is stored by self.__back
    #   - Queue is built by pushing to back and popping
    #     from front
    #   - self.__front value returned for peeks, which is
    #     the front
    #   - No modification of str as it builds by from
    #     self.__front to self.__back


  def __str__(self):
    # Performance:
    # Linked_List: O(n^2). The str implementation operates in
    # quadratic time due to the combination of a current walk
    # and the repeated string catenations (linear time) at every
    # step.
    # Array: O(n^2). Same as Linked_list, current walk to the end
    # and string catenations lead to quadratic time
    
    # TODO replace pass with your implementation.
    # Orient your string from front (left) to back (right).
    return str(self.__dq)

  def __len__(self):
    # Performance:
    # Linked_List: O(1). Implementation simply returns a value,
    # which is constant time.
    # Array: O(1). Same as Linked_list, returns a value

    # TODO replace pass with your implementation.
    return len(self.__dq)

  def enqueue(self, val):
    # Performance:
    # Linked_List: O(n). There is no direct access to the
    # end/tail of the list which serves as the back of the 
    # queue. This requires a current-walk to the end.
    # Array: O(n). Almost always O(1) due to index access, 
    # but the need to grow the array if it runs out of space
    # (worst case) leads to the O(n) time complexity

    self.__dq.push_back(val)

  def dequeue(self):
    # Performance:
    # Linked_List: O(1). Unlike enqueue, the front of the
    # queue is at the front/head of the list. Even though 
    # the implementation uses O(n) functions, the number
    # of steps taken by those functions are constant and
    # do not change with the number of elements in the
    # list
    # Array: O(1). The position of the front is always
    # known, eliminating the need of a current walk to the end.
    # Additionally, the size of the array never needs
    # to be decreased, which eliminates the need to call
    # __grow(), unlike enqueue.

    # TODO replace pass with your implementation.
    return self.__dq.pop_front()

  def peek(self):
    # Performance:
    # Linked_List: O(1). By choosing the front/head of the 
    # list as the front of the queue, the number of steps
    # taken do not change with the length of the list. The
    # functions used to implement it is O(n), but as it
    # never needs to perform a current walk to the end due it never
    # needing to go past the first element, those functions
    # operate in constant time.
    # Array: O(1). Just like enqueue and dequeue, front is 
    # known, and accessing it is in constant time. The number
    # of steps remaing constant, regardless of the length of the list.

    # TODO replace pass with your implementation.
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
