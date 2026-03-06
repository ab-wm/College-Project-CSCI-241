class Linked_List:
    
    class __Node:
        __slots__ = 'data', 'prev', 'next' 

        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. 
            # Performance: O(1), constant number of steps independent of n
            self.data = val
            self.prev = None
            self.next = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class
        # Performance: O(1), constant number of steps independent of n
        self.__size = 0 # Number of elements in list
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer # Link the guards
        self.__trailer.prev = self.__header

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        # Performance: O(1), returns a value with the same number of steps regardless
        # of n. Implementing size into the class itself avoids the need to
        # calculate the size everytime (which would be O(n))
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position.
        # Performance: O(1), the number of steps do not change, regardless of the list
        # length of n.
        new_node = self.__Node(val)
        self.__trailer.prev.next = new_node # Last element points at new
        new_node.prev = self.__trailer.prev # New points at previous last element
        new_node.next = self.__trailer # New points at trailer
        self.__trailer.prev = new_node # Trailer points at new last
        self.__size += 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position.
        # Performance: O(n), in the worst case scenario, the for loop will need
        # to transverse the entire list of n elements.
        if index < 0 or index >= self.__size:
            raise IndexError(f'IndexError: Index out of bounds')
        new_node = self.__Node(val)
        current = self.__header
        for _ in range(index):
            current = current.next
        current.next.prev = new_node
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
        self.__size += 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception.
        # Performance: O(n), in the worst case scenario, the for loop will need
        # to transverse the entire list of n elements.
        if index < 0 or index >= self.__size:
            raise IndexError(f'IndexError: Index out of bounds')
        current = self.__header
        for _ in range(index):
            current = current.next
        removed_node = current.next
        current.next = current.next.next
        current.next.prev = current
        self.__size -= 1
        return removed_node.data

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception.
        # Performance: O(n), in the worst case scenario, the for loop will need
        # to transverse the entire list of n elements.
        if index < 0 or index >= self.__size:
            raise IndexError(f'IndexError: Index out of bounds')
        current = self.__header.next
        for _ in range(index):
            current = current.next
        return current.data

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value.
        # Performance: O(1), regardless of the size of the list, the number
        # of steps required do not change. Only nodes near the header and trailer
        # are moved, and no steps are taken for nodes in the middle.
        if self.__size < 2 :
            return  
        temp_node_store = self.__header.next
        self.__header.next = self.__header.next.next # Join header with index 1
        self.__header.next.prev = self.__header
        self.__trailer.prev.next = temp_node_store
        temp_node_store.prev = self.__trailer.prev
        temp_node_store.next = self.__trailer
        self.__trailer.prev = temp_node_store

        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations.
        # Performance: O(n), the method must loop through all n elements of a 
        # list to function. It is linear as there are no nested loops, and all
        # other steps are O(1) (f-string specifically to avoid str() worst case).
        # Received help on performance considerations:
        # https://stackoverflow.com/questions/76298624/performance-of-f-string-vs-string-join
        list_string = '[ ' # Start of the string
        current = self.__header.next
        if current is self.__trailer:
            list_string += ']'
            return list_string
        else:  # Checks if atleast one node, and append element
            list_string = f'{list_string}{current.data}'
            current = current.next
            while current is not self.__trailer: # Starts from second node incase __size > 1
                list_string += f', {current.data}'
                current = current.next
        list_string += ' ]'
        return list_string

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        # Performance: O(1), constant number of steps, regardless of the size
        # of the list. Any performance cost would be due to the loop calling
        # the method.
        self.current = self.__header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        # Performance: O(1), similar to __iter__, constant number of steps.
        if self.current is self.__trailer:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
        return data

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        # Performance: O(n), the method must loop through all the elements of 
        # the original list of n elements. As append_element is O(1) and other
        # steps are simple/primitive in nature, the overall performance is O(n)
        new_list = Linked_List()        
        if self.__size == 0:
            return new_list
        current = self.__trailer.prev
        while current is not self.__header:
            new_list.append_element(current.data)
            current = current.prev
        return new_list

# Method to run test cases for get_element_at (g), insert_element_at(i), remove_element_at(r)
# __iter__ and __next__ (n), rotate_left (l), __reversed__ (o)
# Parameters -> (list, function (char), index (key), val (key))
def __function_test (test_list, func, index=0, val=0):
    match func:
        case 'g':
            try:
                print(f'  {str(test_list.get_element_at(index))}')
            except IndexError as err_msg:
                print(f'  {err_msg}')
        case 'i':
            try:
                test_list.insert_element_at(val,index)
            except IndexError as err_msg:
                print(f'  {err_msg}')
            print(f'  {str(test_list)}')
        case 'r':
            try:
                print(f"  Removed element value: {str(test_list.remove_element_at(index))}")
            except IndexError as err_msg:
                print(f'  {err_msg}')
            print(f'  {str(test_list)}')
        case 'n':
            print(f'      Printed via __str__: {str(test_list)}')
            print('      Printed via iterator: ', end='')
            for val in test_list:
                print(str(val), end=' ')
            print('')
        case 'l':
            print(f'      Before: {str(test_list)}')
            test_list.rotate_left()
            print(f'      After:  {str(test_list)}')  
        case 'o':
            print('      Reversed List: ',end='')
            new_list = reversed(test_list) # Garbage collection on reuse
            for val in new_list:
                print(val,end=' ')
            print(str(new_list))
            print('      Original list: ', end='')
            for val in test_list:
                print(val, end=' ')
            print(str(test_list))

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests

    val_list = Linked_List()
    empty_list = Linked_List()
    #####
    print('')
    print('*** Test Section 1\n*** Testing list initialization, append_element, __len__, and __str__')
    # Test: Printing a empty list, format, empty list length
    print('')
    print('* Test: Printing a empty list and format, empty list length')
    print(str(val_list))
    print(f'List length = {len(val_list)}')
    print('')

    # Test: Printing a singleton list, format, list length
    empty_list.append_element("Gamma")
    print('* Test: Printing a singleton list and format, list length (List value \'Gamma\')')
    print(str(empty_list))
    print(f'List length = {len(empty_list)}')
    print('')
    empty_list = Linked_List() #Restore the empty state by getting rid of old list

    # Test: Appending elements at tail, str format, list size
    #     : Three test values (different lengths)
    print('* Test: Appending elements at tail, str format, list size. \
Three test values - 13, Alpha, -136, 63, Beta, 1024 (in order)')
    val_list.append_element(13)
    val_list.append_element("Alpha")
    val_list.append_element(-136)
    val_list.append_element(63)
    val_list.append_element("Beta")
    val_list.append_element(1024)
    print(str(val_list))
    print(f'List length = {len(val_list)}')
    print('')
    print('')

    #####
    
    print('*** Test Section 2\n*** Testing get_element_at, insert_element_at, remove_element_at')
    # Test: get_element_at and out of bounds index, and empty list exceptions
    # Test Types: Out of Bounds (negative and large), at head, middle, and tail, and empty list
    print('')
    print('* Test: get_element_at and out of bounds index, and empty list exceptions')
    print(f'* List tested: {str(val_list)}')
    print('- Index value -1') # Negative index
    __function_test(val_list,'g',-1)
    print(f'- Index value {str(len(val_list)+3)}') # Too large index
    __function_test(val_list,'g',len(val_list)+3)
    print('- Index value 2') # Correct index (Arbitrary)
    __function_test(val_list,'g',2)
    print('- Index value 0 [Head]') # Correct index (Head)
    __function_test(val_list,'g',0)
    print(f'- Index value {str(len(val_list)-1)} [Tail]') # Correct index (Tail)
    __function_test(val_list,'g',len(val_list)-1)
    print('- Accessing element in empty list; Index value 0; Check integrity of list')
    print('  Before:')
    print(f'  {str(empty_list)}')
    print('  After:')
    __function_test(empty_list,'g',0)
    print(f'  {str(empty_list)}')
    print('')

    # Test: insert_element_at and out of bounds index, and empty list exceptions exceptions
    # Test Types: Out of Bounds (negative and large), at head, middle, and tail, and empty list
    print('* Test: insert_element_at and out of bounds index, and empty list exceptions')
    print(f'* List tested: {str(val_list)}')
    print('- Index value -1; Value insert 56') # Negative index
    __function_test(val_list,'i',-1,56)
    print(f'- Index value {str(len(val_list)+3)}; Value insert 56') # Too large index
    __function_test(val_list,'i',len(val_list)+3,56)
    print('- Index value 3; Value insert 100') # Correct index (Arbitrary)
    __function_test(val_list,'i',3,100)    
    print('- Index value 0; Value insert 56; Start of list') # Correct index (Head)
    __function_test(val_list,'i',0,56)   
    print(f'- Index value {str(len(val_list)-1)}; Value insert -73; End of list') # Correct index (Tail)
    __function_test(val_list,'i',len(val_list)-1,-73)
    print('- Inserting element into empty list; Index value 0; Value insert 89; Check integrity of list')
    print('  Before:')
    print(f'  {str(empty_list)}')
    print('  After:')
    __function_test(empty_list,'i',0,89)
    print('')

    # Test: remove_element_at and out of bounds index, and empty list exceptions exceptions
    # Test Types: Out of Bounds (negative and large), at head, middle, and tail, and empty list
    print('* Test: remove_element_at and out of bounds index, and empty list exceptions')
    print(f'* List tested: {str(val_list)}')
    print('- Index value -1') # Negative index
    __function_test(val_list,'r',-1)
    print(f'- Index value {str(len(val_list)+3)}') # Too large index
    __function_test(val_list,'r',len(val_list)+3)
    print('- Index value 3') # Correct index (arbitrary)
    __function_test(val_list,'r',3)  
    print('- Index value 0; Start of list') # Correct index (Head)
    __function_test(val_list,'r',0)
    print(f'- Index value {str(len(val_list)-1)}; End of list') # Correct index (Tail)
    __function_test(val_list,'r',len(val_list)-1)
    print('- Removing element from empty list; Index value 0; Check integrity of list')
    print('  Before:')
    print(f'  {str(empty_list)}')
    print('  After:')
    __function_test(empty_list,'r',0)
    print('')
    print('')

    #####
    
    # Test: Testing __iter__ and associated __next__
    # Test Types: Empty and non-empty lists
    print('*** Test Section 3\n*** Testing __iter__ and associated __next__')
    # Test: Iterator on empty and non-empty lists
    print('')
    print('* Test: Printing values using iterator on empty and non-empty lists')
    print('- Empty')
    __function_test(empty_list,'n')
    print('- Non-Empty')
    __function_test(val_list,'n')
    print('')
    print('')

    #####

    print('*** Test Section 4\n*** Testing rotate_left and __reversed__')
    # Test: rotate_left
    # Test Types: Empty list, single element, and non-empty list
    print('* Test: rotate_left method on empty, single element, and non-empty lists; list integrity')
    print('- Empty list')
    __function_test(empty_list, 'l')
    print('- List with one element')
    empty_list.append_element(46)
    __function_test(empty_list, 'l')
    empty_list.remove_element_at(0)
    print('- Non-Empty List')
    __function_test(val_list, 'l')
    print('')

    # Test: __reversed__
    # Test Types: Empty and non-empty lists, and originial list integrity
    print('* Test: __reversed__ on empty and non-empty lists; Original list integrity; Iterator test')
    print(f'* List to be tested: {str(val_list)}')
    print('- Empty List')
    __function_test(empty_list,'o')
    print('- Non-Empty List')
    __function_test(val_list,'o')