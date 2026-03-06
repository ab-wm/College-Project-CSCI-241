import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_
  ### String and Structure Tests

  # Key:
  # DQ = Deque
  # Manip = Add and removal operations on Stacks and Queues
  # Large = Testing using large number of adds and removals
  #   - SQ = On Stacks and Queue
  #   - DQ = Deque
  # Cases tested for
  #   - Final string after additions and removals (finalstr)
  #   - Length reported (len)
  #   - Value returned by peeks (peek)
  #   - Value returned (returned/returnval) (When applicable)

  def test_str_empty_stack (self):
    self.assertEqual('[ ]', str(self.__stack))
  def test_str_empty_queue (self):
    self.assertEqual('[ ]', str(self.__queue))
  def test_str_singleton_element_stack (self):
    self.__stack.push('Value')
    self.assertEqual('[ Value ]', str(self.__stack))
  def test_str_singleton_element_queue (self):
    self.__queue.enqueue('Value')
    self.assertEqual('[ Value ]', str(self.__queue))
  def test_str_multiple_element_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.assertEqual('[ Value_3, Value_2, Value_1 ]', str(self.__stack))
  def test_str_multiple_element_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.assertEqual('[ Value_1, Value_2, Value_3 ]', str(self.__queue))
  
  ### Pushing and Popping: Empty, Made empty, Non empty. Str, return val, len
  # Remove from empty stack
  def test_manip_remove_empty_finalstr_stack (self):
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
  def test_manip_remove_empty_returnval_stack (self):
    returned_1 = self.__stack.pop()
    returned_2 = self.__stack.pop()
    returned_3 = self.__stack.pop()
    self.assertEqual(None, returned_1)
    self.assertEqual(None, returned_2)
    self.assertEqual(None, returned_3)
  def test_manip_remove_empty_len_stack (self):
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  # Remove from empty queue
  def test_manip_remove_empty_finalstr_queue (self):
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))
  def test_manip_remove_empty_returnval_queue (self):
    returned_1 = self.__queue.dequeue()
    returned_2 = self.__queue.dequeue()
    returned_3 = self.__queue.dequeue()
    self.assertEqual(None, returned_1)
    self.assertEqual(None, returned_2)
    self.assertEqual(None, returned_3)
  def test_manip_remove_empty_len_queue (self):
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  # Add then remove an element from stack
  def test_manip_addremove_1_1_finalstr_stack (self):
    self.__stack.push('Value')
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
  def test_manip_addremove_1_1_returnval_stack (self):
    self.__stack.push('Value')
    returned = self.__stack.pop()
    self.assertEqual('Value', returned)    
  def test_manip_addremove_1_1_len_stack (self):
    self.__stack.push('Value')
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack)) 

  # Add then remove an element from queue
  def test_manip_addremove_1_1_finalstr_queue (self):
    self.__queue.enqueue('Value')
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))
  def test_manip_addremove_1_1_returnval_queue (self):
    self.__queue.enqueue('Value')
    returned = self.__queue.dequeue()
    self.assertEqual('Value', returned)
  def test_manip_addremove_1_1_len_queue (self):
    self.__queue.enqueue('Value')
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  # Add 3 then remove 1 from stack
  def test_manip_addremove_3_1_finalstr_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.assertEqual('[ Value_2, Value_1 ]', str(self.__stack))
  def test_manip_addremove_3_1_removeval_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    returned = self.__stack.pop()
    self.assertEqual('Value_3', returned)
  def test_manip_addremove_3_1_len_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.assertEqual(2, len(self.__stack))

  # Add 3 then remove 1 from queue
  def test_manip_addremove_3_1_finalstr_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.assertEqual('[ Value_2, Value_3 ]', str(self.__queue))
  def test_manip_addremove_3_1_returnval_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    returned = self.__queue.dequeue()
    self.assertEqual('Value_1', returned)  
  def test_manip_addremove_3_1_len_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.assertEqual(2, len(self.__queue))

  # Add 3 then remove 2 from stack
  def test_manip_addremove_3_2_finalstr_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ Value_1 ]', str(self.__stack))
  def test_manip_addremove_3_2_returnval_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    returned_1 = self.__stack.pop()
    returned_2 = self.__stack.pop()
    self.assertEqual('Value_3', returned_1)
    self.assertEqual('Value_2', returned_2)
  def test_manip_addremove_3_2_len_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  # Add 3 then remove 2 from queue
  def test_manip_addremove_3_2_finalstr_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ Value_3 ]', str(self.__queue))
  def test_manip_addremove_3_2_returnval_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    returned_1 = self.__queue.dequeue()
    returned_2 = self.__queue.dequeue()
    self.assertEqual('Value_1', returned_1)
    self.assertEqual('Value_2', returned_2)
  def test_manip_addremove_3_2_len_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual(1, len(self.__queue))

  # Add 3 then remove 3 from stack
  def test_manip_addremove_3_3_finalstr_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
  def test_manip_addremove_3_3_returnval_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    returned_1 = self.__stack.pop()
    returned_2 = self.__stack.pop()
    returned_3 = self.__stack.pop()
    self.assertEqual('Value_3', returned_1)
    self.assertEqual('Value_2', returned_2) 
    self.assertEqual('Value_1', returned_3)
  def test_manip_addremove_3_3_len_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  # Add 3 then remove 3 from queue
  def test_manip_addremove_3_3_finalstr_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))
  def test_manip_addremove_3_3_returnval_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    returned_1 = self.__queue.dequeue()
    returned_2 = self.__queue.dequeue()
    returned_3 = self.__queue.dequeue()
    self.assertEqual('Value_1', returned_1)
    self.assertEqual('Value_2', returned_2)
    self.assertEqual('Value_3', returned_3)
  def test_manip_addremove_3_3_len_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  # Add 3, remove 3, add 2, remove 1 (in order) from stack
  def test_manip_addremoveaddremove_3_3_2_1_finalstr_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.push('Value_4')
    self.__stack.push('Value_5')
    self.__stack.pop()
    self.assertEqual('[ Value_4 ]', str(self.__stack))
  def test_manip_addremoveaddremove_3_3_2_1_return_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    returned_1 = self.__stack.pop()
    returned_2 = self.__stack.pop()
    returned_3 = self.__stack.pop()
    self.__stack.push('Value_4')
    self.__stack.push('Value_5')
    returned_4 = self.__stack.pop()
    self.assertEqual('Value_3', returned_1)
    self.assertEqual('Value_2', returned_2) 
    self.assertEqual('Value_1', returned_3)
    self.assertEqual('Value_5', returned_4)
  def test_manip_addremoveaddremove_3_3_2_1_len_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.push('Value_4')
    self.__stack.push('Value_5')
    self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  # Add 3, remove 3, add 2, remove 1 (in order) from queue
  def test_manip_addremoveaddremove_3_3_2_1_finalstr_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.enqueue('Value_4')
    self.__queue.enqueue('Value_5')
    self.__queue.dequeue()
    self.assertEqual('[ Value_5 ]', str(self.__queue))
  def test_manip_addremoveaddremove_3_3_2_1_return_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    returned_1 = self.__queue.dequeue()
    returned_2 = self.__queue.dequeue()
    returned_3 = self.__queue.dequeue()
    self.__queue.enqueue('Value_4')
    self.__queue.enqueue('Value_5')
    returned_4 = self.__queue.dequeue()
    self.assertEqual('Value_1', returned_1)
    self.assertEqual('Value_2', returned_2) 
    self.assertEqual('Value_3', returned_3)
    self.assertEqual('Value_4', returned_4)
  def test_manip_addremoveaddremove_3_3_2_1_len_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.enqueue('Value_4')
    self.__queue.enqueue('Value_5')
    self.__queue.dequeue()
    self.assertEqual(1, len(self.__queue))

  ### Peeking
  # Peek empty stack and queue
  def test_peek_empty_stack (self):
    self.assertEqual(None, self.__stack.peek())
  def test_peek_empty_queue (self):
    self.assertEqual(None, self.__queue.peek())

  # Peek after single element stack and queue
  def test_peek_singleadd_stack (self):
    self.__stack.push('Value')
    self.assertEqual('Value', self.__stack.peek())    
  def test_peek_singleadd_queue (self):
    self.__queue.enqueue('Value')
    self.assertEqual('Value', self.__queue.peek())

  # Peek after adding 3 elements stack and queue
  def test_peek_multiadd_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.assertEqual('Value_3', self.__stack.peek())    
  def test_peek_multiadd_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.assertEqual('Value_1', self.__queue.peek())

  # Peek after each removal: adding 3 and then remove 2 elements stack and queue
  def test_peek_addremove_3_2_peekafterremove_stack (self):    
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    peek_1 = self.__stack.peek()
    self.__stack.pop()
    peek_2 = self.__stack.peek()
    self.assertEqual('Value_2', peek_1)
    self.assertEqual('Value_1', peek_2)
  def test_peek_addremove_3_2_peekafterremove_queue (self):    
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    peek_1 = self.__queue.peek()
    self.__queue.dequeue()
    peek_2 = self.__queue.peek()
    self.assertEqual('Value_2', peek_1)
    self.assertEqual('Value_3', peek_2)

  # Peek after each removal: adding 3 and then remove 3 elements stack and queue
  def test_peek_addremove_3_3_peekafterremove_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    peek_1 = self.__stack.peek()
    self.__stack.pop()
    peek_2 = self.__stack.peek()
    self.__stack.pop()
    peek_3 = self.__stack.peek()
    self.assertEqual('Value_2', peek_1)
    self.assertEqual('Value_1', peek_2)
    self.assertEqual(None, peek_3)
  def test_peek_addremove_3_3_peekafterremove_queue (self):    
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    peek_1 = self.__queue.peek()
    self.__queue.dequeue()
    peek_2 = self.__queue.peek()
    self.__queue.dequeue()
    peek_3 = self.__queue.peek()
    self.assertEqual('Value_2', peek_1)
    self.assertEqual('Value_3', peek_2)
    self.assertEqual(None, peek_3)

  # Peek after adding 3 removing 3 adding 2 removing 1 (in order) stack and queue
  def test_peek_addremoveaddremove_3_3_2_1_finalpeek_stack (self):
    self.__stack.push('Value_1')
    self.__stack.push('Value_2')
    self.__stack.push('Value_3')
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.push('Value_4')
    self.__stack.push('Value_5')
    self.__stack.pop()
    self.assertEqual('Value_4', self.__stack.peek())
  def test_peek_addremoveaddremove_3_3_2_1_finalpeek_queue (self):
    self.__queue.enqueue('Value_1')
    self.__queue.enqueue('Value_2')
    self.__queue.enqueue('Value_3')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.enqueue('Value_4')
    self.__queue.enqueue('Value_5')
    self.__queue.dequeue()
    self.assertEqual('Value_5', self.__queue.peek())

  ### Dequeue Testing
  # Push front 1 element
  def test_DQ_pushfr1_finalstr (self):
    self.__deque.push_front('Value_1f')
    self.assertEqual('[ Value_1f ]', str(self.__deque))
  def test_DQ_pushfr1_len (self):
    self.__deque.push_front('Value_1f')
    self.assertEqual(1, len(self.__deque))
  def test_DQ_pushfr1_peeks (self):
    self.__deque.push_front('Value_1f')
    self.assertEqual('Value_1f', self.__deque.peek_front())
    self.assertEqual('Value_1f', self.__deque.peek_back())

  # Push back 1 element
  def test_DQ_pushba1_finalstr (self):
    self.__deque.push_back('Value_1b')
    self.assertEqual('[ Value_1b ]', str(self.__deque))
  def test_DQ_pushba1_len (self):
    self.__deque.push_back('Value_1b')
    self.assertEqual (1, len(self.__deque))
  def test_DQ_pushba1_peeks (self):
    self.__deque.push_front('Value_1b')
    self.assertEqual('Value_1b', self.__deque.peek_front())
    self.assertEqual('Value_1b', self.__deque.peek_back())

  # Pop front 1 element (initially empty)
  def test_DQ_popfr1_finalstr (self):
    self.__deque.pop_front()
    self.assertEqual ('[ ]', str(self.__deque))
  def test_DQ_popfr1_len (self):
    returned = self.__deque.pop_front()
    self.assertEqual (0, len(self.__deque))
  def test_DQ_popfr1_peeks (self):
    self.__deque.pop_front()
    self.assertEqual (None, self.__deque.peek_front())
    self.assertEqual (None, self.__deque.peek_back())
  def test_DQ_popfr1_returned (self):
    returned = self.__deque.pop_front()
    self.assertEqual (None, returned)

  # Pop back 1 element (initially empty)
  def test_DQ_popba1_finalstr (self):
    self.__deque.pop_back()
    self.assertEqual ('[ ]', str(self.__deque))
  def test_DQ_popba1_len (self):
    returned = self.__deque.pop_back()
    self.assertEqual (0, len(self.__deque))
  def test_DQ_popba1_peeks (self):
    self.__deque.pop_back()
    self.assertEqual (None, self.__deque.peek_front())
    self.assertEqual (None, self.__deque.peek_back())
  def test_DQ_popba1_returned (self):
    returned = self.__deque.pop_back()
    self.assertEqual (None, returned)

  # Push front 3 elements
  def test_DQ_pushfr3_finalstr (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.assertEqual('[ Value_3f, Value_2f, Value_1f ]', str(self.__deque))
  def test_DQ_pushfr3_len (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.assertEqual(3, len(self.__deque))
  def test_DQ_pushfr3_peeks (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.assertEqual('Value_3f', self.__deque.peek_front())
    self.assertEqual('Value_1f', self.__deque.peek_back())

  # Push back 3 elements
  def test_DQ_pushba3_finalstr (self):
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.assertEqual('[ Value_1b, Value_2b, Value_3b ]', str(self.__deque))
  def test_DQ_pushba3_len (self):
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.assertEqual (3, len(self.__deque))
  def test_DQ_pushba3_peeks (self):
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.assertEqual('Value_1b', self.__deque.peek_front())
    self.assertEqual('Value_3b', self.__deque.peek_back())

  # Push front then push back 3 elements
  def test_DQ_pushfr3_pushba3_finalstr (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.assertEqual('[ Value_3f, Value_2f, Value_1f, Value_1b, Value_2b, Value_3b ]', str(self.__deque))
  def test_DQ_pushfr3_pushba3_len (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.assertEqual(6, len(self.__deque))
  def test_DQ_pushfr3_pushba3_peeks (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.assertEqual('Value_3f', self.__deque.peek_front())
    self.assertEqual('Value_3b', self.__deque.peek_back())

  # Push front 3, push back 3, pop front 2, popback 1 (in order)
  def test_DQ_pushfr3_pushba3_popfr2_popba1_finalstr (self):  
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.__deque.pop_back()
    self.assertEqual('[ Value_1f, Value_1b, Value_2b ]', str(self.__deque))
  def test_DQ_pushfr3_pushba3_popfr2_popba1_len (self):  
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.__deque.pop_back()
    self.assertEqual(3, len(self.__deque))
  def test_DQ_pushfr3_pushba3_popfr2_popba1_peeks (self):  
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.__deque.pop_back()
    self.assertEqual('Value_1f', self.__deque.peek_front())
    self.assertEqual('Value_2b', self.__deque.peek_back())
  def test_DQ_pushfr3_pushba3_popfr2_popba1_returnedval (self):  
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    returned_1 = self.__deque.pop_front()
    returned_2 = self.__deque.pop_front()
    returned_3 = self.__deque.pop_back()
    self.assertEqual('Value_3f', returned_1)
    self.assertEqual('Value_2f', returned_2)
    self.assertEqual('Value_3b', returned_3)

  # Push front 2, pop back 2, push front 1, push back 3, pop front 2 (in order)
  def test_DQ_pushfr2_popba2_pushfr1_pushba3_popfr2_finalstr (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('[ Value_2b, Value_3b ]', str(self.__deque))
  def test_DQ_pushfr2_popba2_pushfr1_pushba3_popfr2_len (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual(2, len(self.__deque))
  def test_DQ_pushfr2_popba2_pushfr1_pushba3_popfr2_peeks (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('Value_2b', self.__deque.peek_front())
    self.assertEqual('Value_3b', self.__deque.peek_back())
  def test_DQ_pushfr2_popba2_pushfr1_pushba3_popfr2_returnval (self):
    self.__deque.push_front('Value_1f')
    self.__deque.push_front('Value_2f')
    returned_1 = self.__deque.pop_back()
    returned_2 = self.__deque.pop_back()
    self.__deque.push_front('Value_3f')
    self.__deque.push_back('Value_1b')
    self.__deque.push_back('Value_2b')
    self.__deque.push_back('Value_3b')
    returned_3 = self.__deque.pop_front()
    returned_4 = self.__deque.pop_front()
    self.assertEqual('Value_1f', returned_1)
    self.assertEqual('Value_2f', returned_2)
    self.assertEqual('Value_3f', returned_3)
    self.assertEqual('Value_1b', returned_4)


### Large Data Functionality Testing: Stacks and Queues
  # Stack and Queue: Add 100 elements
  def test_large_SQ_add100_remove0_finalstr_len_stack (self):
    test_list = '1 ]'
    self.__stack.push(1)
    for i in range(2,101):
      self.__stack.push(i)
      test_list = f'{i}, {test_list}'
    test_list = f'[ {test_list}'
    self.assertEqual(test_list, str(self.__stack))
    self.assertEqual(100, len(self.__stack))
  def test_large_SQ_add100_remove0_finalstr_len_queue (self):
    test_list = '[ 1'
    self.__queue.enqueue(1)
    for i in range(2,101):
      self.__queue.enqueue(i)
      test_list = f'{test_list}, {i}'
    test_list = f'{test_list} ]'
    self.assertEqual(test_list, str(self.__queue))
    self.assertEqual(100, len(self.__queue))

  # Stack and Queue: Add 100 elements and remove 90
  def test_large_SQ_add100_remove90_finalstr_len_stack (self):
    for i in range(1,101):
      self.__stack.push(i)
    for _ in range(90):
      self.__stack.pop()
    self.assertEqual('[ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]', str(self.__stack))
    self.assertEqual(10, len(self.__stack))
  def test_large_SQ_add100_remove90_finalstr_len_queue (self):
    for i in range(1,101):
      self.__queue.enqueue(i)
    for _ in range(90):
      self.__queue.dequeue()
    self.assertEqual('[ 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ]', str(self.__queue))
    self.assertEqual(10, len(self.__queue))

  # Stack and Queue: Add 100 elements and remove 100
  def test_large_SQ_add100_remove100_finalstr_len_stack (self):
    for i in range(1,101):
      self.__stack.push(i)
    for _ in range(100):
      self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
    self.assertEqual(0, len(self.__stack))
  def test_large_SQ_add100_remove100_finalstr_len_queue (self):
    for i in range(1,101):
      self.__queue.enqueue(i)
    for _ in range(100):
      self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))
    self.assertEqual(0, len(self.__queue))

### Large Data Functionality Testing: Deque
  # Deque: Push front 100 elements
  def test_large_DQ_pushfr100_finalstr_len (self):
    test_list = '1 ]'
    self.__deque.push_front(1)
    for i in range(2,101):
      self.__deque.push_front(i)
      test_list = f'{i}, {test_list}'
    test_list = f'[ {test_list}'
    self.assertEqual(test_list, str(self.__deque))
    self.assertEqual(100, len(self.__deque))

  # Deque: Push back 100 elements
  def test_large_DQ_pushba100_finalstr_len (self):
    test_list = '[ 1'
    self.__deque.push_back(1)
    for i in range(2,101):
      self.__deque.push_back(i)
      test_list = f'{test_list}, {i}'
    test_list = f'{test_list} ]'
    self.assertEqual(test_list, str(self.__deque))
    self.assertEqual(100, len(self.__deque))


  # Deque: Push front 100 and pop front 90 elements
  def test_large_DQ_pushfr100_popfr90_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_front(i)
    for _ in range(90):
      self.__deque.pop_front()
    self.assertEqual('[ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]', str(self.__deque))
    self.assertEqual(10, len(self.__deque))

  # Deque: Push front 100 and pop back 90 elements
  def test_large_DQ_pushfr100_popba90_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_front(i)
    for _ in range(90):
      self.__deque.pop_back()
    self.assertEqual('[ 100, 99, 98, 97, 96, 95, 94, 93, 92, 91 ]', str(self.__deque))
    self.assertEqual(10, len(self.__deque))

  # Deque: Push back 100 and pop back 90 elements
  def test_large_DQ_pushba100_popba90_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_back(i)
    for _ in range(90):
      self.__deque.pop_back()
    self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]', str(self.__deque))
    self.assertEqual(10, len(self.__deque))

  # Deque: Push back 100 and pop front 90 elements
  def test_large_DQ_pushba100_popfr90_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_back(i)
    for _ in range(90):
      self.__deque.pop_front()
    self.assertEqual('[ 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ]', str(self.__deque))
    self.assertEqual(10, len(self.__deque))

  # Deque: Push front 100 elements and pop front 100 elements
  def test_large_DQ_pushfr100_popfr100_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_front(i)
    for _ in range(100):
      self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
    self.assertEqual(0, len(self.__deque))

  # Deque: Push front 100 and pop back 100 elements
  def test_large_DQ_pushfr100_popba100_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_front(i)
    for _ in range(100):
      self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
    self.assertEqual(0, len(self.__deque))

  # Deque: Push back 100 and pop back 100 elements
  def test_large_DQ_pushba100_popba100_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_back(i)
    for _ in range(100):
      self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
    self.assertEqual(0, len(self.__deque))

  # Deque: Push back 100 and pop front 100 elements
  def test_large_DQ_pushba100_popfr100_finalstr_len (self):
    for i in range(1,101):
      self.__deque.push_back(i)
    for _ in range(100):
      self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
    self.assertEqual(0, len(self.__deque))

  # Deque: Push front 50, push back 150, pop front 150, pop back 50 (in order)
  def test_large_DQ_pushfr50_pushba150_popfr150_popba50_finalstr_len (self):
    for i in range(1, 51):
      self.__deque.push_front(i)
    for i in range(1, 151):
      self.__deque.push_back(i)
    for _ in range(150):
      self.__deque.pop_front()
    for _ in range(50):
      self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
    self.assertEqual(0, len(self.__deque))  

  # Deque: Push back 50, push front 150, pop back 150, pop front 50 (in order)
  def test_large_DQ_pushba50_pushfr150_popba150_popfr50_finalstr_len (self):
    for i in range(1, 51):
      self.__deque.push_back(i)
    for i in range(1, 151):
      self.__deque.push_front(i)
    for _ in range(150):
      self.__deque.pop_back()
    for _ in range(50):
      self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
    self.assertEqual(0, len(self.__deque)) 

if __name__ == '__main__':
  unittest.main()


