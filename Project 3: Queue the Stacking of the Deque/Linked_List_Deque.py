from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    # Performance: O(1). Constant number of steps, regardless 
    # of list length. While insert_element_at is O(n) in the worst
    # case, insert element will never go past the first element,
    # eliminating the need of a current walk.

    # Use the head position for the front.
    if len(self) == 0:
      self.__list.append_element(val) #insert_element_at does not work on empty
    else:
      self.__list.insert_element_at(val, 0)
  
  def pop_front(self):
    # Performance: O(1). Constant number of steps. remove_element_at
    # is O(n) in the worst case, but as it never goes past the
    # first element, the current walk never happens.

    # Use the head position for the front.
    if len(self) == 0: # If empty return None and prevent modification
      return None
    else:
      return self.__list.remove_element_at(0)

  def peek_front(self):
    # Performance: O(1). Constant number of steps. get_element_at
    # is O(n), but never needs to walk across n elements as it always
    # targets the very first element, making it O(1).

    # Use the head position for the front.
    if len(self) == 0: # If empty return None
      return None
    else:
      return self.__list.get_element_at(0)

  def push_back(self, val):
    # Performance: O(1). Fortunately, the append_element() functions
    # in constant time by directly accessing the trailer. As the trailer
    # never changes regardless of list size, the addition of a new node 
    # requires a constant number of steps.

    # Use the tail position for the back.
    self.__list.append_element(val)
  
  def pop_back(self):
    # Performance: O(n). As there is no way to directly access the trailer,
    # the method remove_element_at must be used, which has a O(n) time
    # complexity. This is beacuse it must do the current walk to the end
    # of the list to get to the last node, hence the number of steps 
    # increasing with length of list (linearly). As a matter of fact,
    # it is always the worst case scenario.

    # Use the tail position for the back.
    if len(self) == 0: # If empty return None and prevent modification
      return None
    else:
      return self.__list.remove_element_at(len(self)-1)

  def peek_back(self):
    # Performance: O(n). The same situation as pop_back, with no access to trailer,
    # get_element_at needing to do a current walk (which increases the number of 
    # steps linearly with the number of elements n), and always the worst case
    # scenario as the method always needs to access the last element of the list
    
    # Use the tail position for the back.
    if len(self) == 0: # If empty return none
      return None
    else:
      return self.__list.get_element_at(len(self)-1)

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
