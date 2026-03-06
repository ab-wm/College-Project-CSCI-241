from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__front = 0 # Tracks indices
    self.__back = 0 # Not None, as self.__size = 0 will prevent access
    self.__size = 0 # 0 Prevents operations on empty arrays

  def __str__(self):
    # Performance: O(n^2). The while loop needs to loop through n elements of the
    # array to return the appropriate string. The use of fstrings increase the
    # time complexity to quadratic time due to linear time nature of fstrings
    # and the need to repeadtely call it.
    # Otherwise all other steps operate in constant time.

    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    list_string = '[ ' # Start of the string
    current = self.__front
    if self.__size == 0: # Empty
      list_string += ']'
      return list_string
    elif self.__size == 1: # Single element
      list_string = f'{list_string}{self.__contents[current]} ]'
      return list_string
    else:
      list_string = f'{list_string}{self.__contents[current]}'
      while current != self.__back: # Continue till the end
        current = (current + 1) % self.__capacity
        list_string += f', {self.__contents[current]}'
      list_string += ' ]'
      return list_string

  def __len__(self):
    # Performance: O(1). Simply returns a variable value, hence, needing
    # a constant number of steps regardless of the length of the list.

    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # Performance: O(n). The creation of the new array and other steps like assignments
    # all operate in constant time. The number of times the while loop runs is linearly
    # dependent on the number of elements in the previous array. Assuming the worst-case
    # scenario, there will be n loops to copy the original array (accessing the indexes
    # themselves are constant time)     

    # Replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    # Create new array of double size
    self.__capacity *= 2
    new_array = [None] * self.__capacity
    current = self.__front

    if self.__size == 1: # If only one element
      new_array[0] = self.__contents[current]
      self.__contents = new_array
      self.__front = 0
      self.__back = 0
    else:
      new_array[0] = self.__contents[current]
      pos = 1 # Counter to track the indices of the new array
      while current != self.__back: # Read till the end of the present array
        current = (current + 1) % self.__size
        new_array[pos] = self.__contents[current]
        pos += 1
      self.__contents = new_array
      self.__front = 0 # Reset positions of front to 0, and back accordingly
      self.__back = self.__size - 1
    
  def push_front(self, val):
    # Performance: O(n). While accessing and changing the value
    # at an index is constant time (front is always tracked),
    # the need to call __grow() method if the array runs out 
    # of space leads to the O(n) time complexity.    
    
    # Replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity: # Max capacity reached
      self.__grow()
    if self.__size == 0: #If empty. Front and back not changed due to already at 0
      self.__contents[0] = val
      self.__size += 1
    else:
      self.__front = (self.__front - 1) % self.__capacity
      self.__contents[self.__front] = val
      self.__size += 1
    
  def pop_front(self):
    # Performance: O(1). The number of steps remain constant, regardless of the size 
    # of the list (front index is always known). Since the array does not need to shrink if 
    # values decreases, there is never the need to call the slower __grow() method that 
    # runs in O(n).   
    
    # Replace pass with your implementation. Do not reduce the capacity.

    popped = None # If empty, return None, otherwise store and return popped val
    if self.__size == 0: # Empty if size is 0
      return popped
    elif self.__size == 1: # 1 element to empty, reset front, back and size to 0
      popped = self.__contents[self.__front]
      self.__front = 0
      self.__back = 0
      self.__size = 0
      return popped
    else:
      popped = self.__contents[self.__front]
      self.__front = (self.__front + 1) % self.__capacity
      self.__size -= 1
      return popped
    
  def peek_front(self):
    # Performance: O(1). Accessing any index of an array takes a constant number
    # of steps; there is no need for a current walk like linked lists as the
    # front index is always tracked. "Any" here is important, as the __front 
    # can be anywhere.    
    
    # Replace pass with your implementation.
    if self.__size == 0: # Empty array
      return None
    else:
      return self.__contents[self.__front]
    
  def push_back(self, val):
    # Performance: O(n). While mostly needing a constant number of steps (accessing
    # indexes are constant time, and back index is always known), the occasional call to __grow means the worst case
    # performance is O(n), instead of the more ideal O(1) performance.    
    
    # Replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity: # Max capacity
      self.__grow()
    if self.__size == 0: #If empty. Front and back not changed due to already at 0
      self.__contents[0] = val
      self.__size += 1
    else:
      self.__back = (self.__back + 1) % self.__capacity
      self.__contents[self.__back] = val
      self.__size += 1
  
  def pop_back(self):
    # Performance: O(1). Just like pop_front(), accessing and removing a value
    # at an index operates in constant time, and the lack of a current walk 
    # by tracking front and back means this method takes a constant number of
    # steps regardless of the length of the array. The array also does not need
    # to be shrunk, avoiding the need to call __grow().
    
    # Replace pass with your implementation. Do not reduce the capacity.
    popped = None # Return None when empty, otherwise store and return popped val
    if self.__size == 0: # Empty
      return popped
    elif self.__size == 1: # Reset size, front and back to 0 if it is last element
      popped = self.__contents[self.__back]
      self.__front = 0
      self.__back = 0
      self.__size = 0
      return popped
    else:
      popped = self.__contents[self.__back]
      self.__back = (self.__back - 1) % self.__capacity
      self.__size -= 1
      return popped

  def peek_back(self):
    # Performance: O(1). Accessing any index operate in constant time, and tracking
    # the back index avoids the need of a current walk. Hence, this method operates
    # in constant time, regardless of the legth of the array.    
    
    # Pass with your implementation.
    if self.__size == 0: # If empty
      return None
    else:
      return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
