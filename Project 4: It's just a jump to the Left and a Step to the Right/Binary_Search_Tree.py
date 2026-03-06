class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.
    __slots__ = 'value', 'height', 'left', 'right', 'bal'

    def __init__(self, value):
      self.value = value
      self.height = 0  #Track height of node
      self.bal = 0 # Keeping track of balance. Update with height update
      self.left = None #Left and right child nodes
      self.right = None

    ### Method to find the height of child nodes
    # Performance: O(1). Constant number of steps and no additional calls
    def child_node_height (self, child):
      # Child: 'left' = Left child node return height 
      #      : 'right' = Right child node return height
      match child:
        case 'left':
          if self.left is None: # If child does not exist
            return 0
          else:
            return self.left.height
        case 'right':
          if self.right is None:
            return 0
          else:
            return self.right.height
    
    ### Method to update the height of a node
    # Performance: O(1). Constant number of steps and no additional calls
    def update_height(self):
      h_left = self.child_node_height('left') # Store height information of children
      h_right = self.child_node_height('right')
      if h_left > h_right: # Update height to be tallest child + 1
        self.height = h_left + 1
      else:
        self.height = h_right + 1
      self.bal = h_right-h_left

  def __init__(self):
    self.__root = None

  ### Method to balance trees
  # Performance: O(1). No loops nor recursion and a constant number
  # of steps regardless of size of tree. The method calls themselves
  # are constant time.
  def __balanced (self, root):
    # Base case: Height difference stored in balance is 1 or 0, simply return
    # Algorithm steps - 1: Match left and right heavy nodes to apporpriate sub-algorithm
    #                 - 2: Call balancing helper method for a child node with opposite balance
    #                 - 3: Call helper method on the main node after adjusting the child
    #                 - 4: Return balanced node
    if abs(root.bal) < 2: # Base case
      return root
    else:
        match root.bal: # AS 1
          case -2:
            if root.left.bal == 1: # AS 2 (Left parent and right child)
              root.left = self.__balanced_helper_balancing(root.left)
            root = self.__balanced_helper_balancing(root) # AS 3
          case 2:
            if root.right.bal == -1: # AS 2 (Right parent and left child)
              root.right = self.__balanced_helper_balancing(root.right)
            root = self.__balanced_helper_balancing(root) # AS 3
    return root # AS 4

  ### Helper for __balance to balance a node
  # Performance: O(1). Takes a constant number of step, regardless of 
  # tree size. Method calls to __update_height are constant time as well.
  def __balanced_helper_balancing (self, root):
    # Cases - Negative balance: Left heavy node, checked by self.bal
    #       - Positive balance: Right heavy node, checked by self.bal
    # Algorithm: Store old root, reasign node to appropriate child (left -ve and right +ve)
    #           : Assign old root to new root (right child for left and left child for right)
    #           : Update heights for both new and old roots
    # Notes: Method does not differentiate on the amount of mis-balance, just direction. That is handled in __balanced().
    match root.bal:
      case -1 | -2:
        floater = root.left.right
        old_root = root
        root = root.left
        root.right = old_root
        root.right.left = floater
        root.right.update_height()
        root.update_height()

      case 1 | 2:
        floater = root.right.left
        old_root = root
        root = root.right
        root.left = old_root
        root.left.right = floater
        root.left.update_height()
        root.update_height()
    return root

###

  # Performance: O(logn). Same as the recursive method. Only goes down one
  # of the branches, cutting the number steps down to half.
  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # Performance: Same as recursive insert, which is O(logn).
    # Constant number of steps on each call and each call to insert
    # is the worst case to the end of the tree which takes logn steps
    self.__root = self.__recursive_insert(self.__root, value)

  ### Recursive method for insertion
  # Performance: O(logn). Constant number of steps on each call. Each call
  # goes to the bottom of the tree, which takes logn steps (nature of balanced
  # binary search trees). The calls to update height and balanced take a constant
  # number of steps and thus do not add to the big O time complexity.
  def __recursive_insert (self, root, value):
    # Base case 1: Empty node is reached
    # Base case 2: Same value found in a node
    # Recursive case: Update child to be the returned node from a recursive call
    #                 down the tree
    if root is None: # Base 1: Create new node, update height, return
      root = self.__BST_Node(value)
      root.height = 1
      return root
    if root.value == value: # Base 2: Raise error
      raise ValueError
    else: # Rescursive case: Go down tree based on value and Recursion
      if root.value > value: 
        root.left = self.__recursive_insert(root.left, value)
      else:
        root.right = self.__recursive_insert(root.right, value)
      root.update_height() # Update height of root
      return self.__balanced(root)


####
  # Performance: O(logn), same as the recursive remove mothod. Worst
  # case scenario would be to the end of the tree, which will take
  # logn steps. Each recursive call takes a constant number of steps
  # as well as the additional recursive calls to min_element. As it
  # is big O time complexity, the multiple logn calls in other method
  # calls add up (instead of multiplying) to an amortalized times of logn
  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__recursive_remove_element(self.__root, value)

  ### Recursive method for removal
  # Performance: O(logn). Constant number of steps in each call. Worst case
  # will reach the end of the tree which will take logn steps. The call to itself
  # in the base case will take logn steps, as well as min_element. However, as these
  # calls happen only once in the base case, it will add logn steps, instead of 
  # increasing the time complexity by happening at every call (which it doesn't).
  # Other method calls are all constant time and involve no recursion/loops. All add 
  # up for big O of log n
  def __recursive_remove_element(self, root, value):
    # Base case 1: No values are found in tree
    # Base case 2: Value is found in tree
      #       2.1: If leaf node, simply remove the node via None and return
      #       2.2: If 1 non empty child, make node equal to that child node and return
      #       2.3: If all child non-empty, replace root value with lowest value from
      #            the right subtree by calling __recursive_min_element(). Delete the node 
      #            via __recrusive_remove_element. Update height and return.
    # Rescursive case: Attempt to find the value by going down the appropriate child
    #                  Recursively. Child is updated with return value.
    if root is None: # Base 1: Raise error
      raise ValueError
    if root.value == value: # Base 2
      # Base 2.1
      if root.height == 1: 
        return None
      # Base 2.2
      elif root.child_node_height('left') != 0 and root.child_node_height('right') == 0:
        root = root.left
      elif root.child_node_height('left') == 0 and root.child_node_height('right') != 0:
        root = root.right
      # Base 2.3
      else:
          root.value = self.__recursive_min_element(root.right)
          root.right = self.__recursive_remove_element(root.right, root.value)
          root.update_height()
    elif value < root.value: # Recursive
      root.left = self.__recursive_remove_element(root.left, value)
      root.update_height()
    elif value > root.value: # Recursive
      root.right = self.__recursive_remove_element(root.right, value)
      root.update_height()
    return self.__balanced(root)

  ### Find the minimum value for replacement in removal operation
  # Performance: O(logn): Constant number of steps in each call, logn calls
  # in the worst case, which is when the root value is removed.
  def __recursive_min_element (self, root):
    # Base case: The lowest left tree is found (left child = 0 height).
    #            Return root.value.
    # Recursive case: Recursively call to move down the left side. Will return value
    if root.child_node_height('left') == 0: # Base case
      return root.value
    else: # Recursive case
      return self.__recursive_min_element(root.left)
      
#####
  #######
  # Performance for the four transversals and their recursive calls
  #######
  # Performance: O(n^2). Regardless of the structure of the tree, each and every
  # node has to be transversed to build the string. The fstrings are not exactly
  # constant time due to it being closer to a O(n) method, especially so as the  
  # returned strings get larger. As a result, the transverals have a O(n^2) time
  # complexit.
  # To note for to_list: The same performance issue applies with append, as it
  # requires the reallocation of memory and copying of data each time .append()
  # is called when the python array (which is a list) runs out of space.
  #######

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      return f'[ {self.__recursive_in_order(self.__root)} ]'

  ### Recursive method for in order transveral
  def __recursive_in_order (self, root):
    # Base case: Empty tree is reached. Return empty string
    # Recursive case: Build string by <left child in order transversal> +
    #                 root value + <right child in order transversal>. Return
    #                 completed string
    #               : In order transversal by calling recursively on the left child
    #                 and then right child
    if root == None: # Base
      return ''
    else: # Recursive
      trans_string = ''
      if root.child_node_height('left') != 0: # Left in order
          trans_string += f'{self.__recursive_in_order(root.left)}, '
      trans_string += f'{root.value}' # Root value
      if root.child_node_height('right') != 0: # Right in order
        trans_string += f', {self.__recursive_in_order(root.right)}'
      return trans_string 

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      return f'[ {self.__recursive_pre_order(self.__root)} ]'

  ### Recursive method for pre order transversal
  def __recursive_pre_order (self, root):
    # Base case: Empty tree is reached. Return empty string
    # Recursive case: Build string by root value + <left child pre order
    #                 transversal> + <right child pre order transversal>. 
    #                 Return completed string.
    #               : Pre order transversal by calling recursively on the left child
    #                 and then right child
    if root == None: # Base
      return ''
    else: # Recursive
      trans_string = ''
      trans_string += f'{root.value}' # Root value
      if root.child_node_height('left') != 0: # Left pre order
          trans_string += f', {self.__recursive_pre_order(root.left)}'
      if root.child_node_height('right') != 0: # Right pre order
        trans_string += f', {self.__recursive_pre_order(root.right)}'
      return trans_string
    
  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      return f'[ {self.__recursive_post_order(self.__root)} ]'

  ### Recursive method for post order transveral
  def __recursive_post_order (self, root):
    # Base case: Empty tree is reached. Return empty string
    # Recursive case: Build string by root value + <left child pre order
    #                 transversal> + <right child pre order transversal>. 
    #                 Return completed string.
    #               : Pre order transversal by calling recursively on the left child
    #                 and then right child
    if root == None: # Base
      return ''
    else: # Recursive
      trans_string = ''
      if root.child_node_height('left') != 0: # Left post order
          trans_string += f'{self.__recursive_post_order(root.left)}, '
      if root.child_node_height('right') != 0: # Right post order
        trans_string += f'{self.__recursive_post_order(root.right)}, '
      trans_string += f'{root.value}' # Root value
      return trans_string

  def to_list(self):
    # Construct and return a Python list/array containing the in-order
    # traversal of the tree. Your solution must be recursive. This will
    # involve the introduction of additional private methods to support
    # the recursion control variable.
    if self.__root is None:
      return([])
    else:
      return self.__recursive_to_list(self.__root)

  ### Recursive method for to list
  def __recursive_to_list (self, root):
    # Base case: Empty tree is reached. Return empty array
    # Recursive case: Build array by <left child to_list transversal> +
    #                 root value + <right child to_list transversal>. Return
    #                 completed array (built by .extend())
    #               : to_list transversal by calling recursively on the left child
    #                 and then right child
    #               : to_list follows in-order transversal algorithm
    if root == None: # Base case
      return []
    else: # Recursive
      return_arr = []
      if root.child_node_height('left') != 0: # Left to_list
          return_arr.extend(self.__recursive_to_list(root.left))
      return_arr.extend([root.value]) # Root value
      if root.child_node_height('right') != 0: # Right to_list
        return_arr.extend(self.__recursive_to_list(root.right))
      return return_arr

####

  # Performance: O(1) Constant number of steps, no need of checking
  # other nodes.
  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.

