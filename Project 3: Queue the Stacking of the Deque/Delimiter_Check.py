import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.

  delimiter_set= {'(':')', '{':'}', '[':']'} # Dictionary to match delimiters
  file_to_check = open(filename)

  char_stack = Stack()            # Stack to store characters read from the file
  for line in file_to_check:      # Successively read each line of the file
    for char in line:             # Successively read each character of the line
      if char in delimiter_set:   # Check if character is an opening delimiter (keys)
        char_stack.push(char)
      elif char in delimiter_set.values() and (char_stack.peek() is None or \
      delimiter_set[char_stack.pop()] != char): # Check (1)
        return False

  if char_stack.peek() is not None: # Check if stack empty once file is read
    return False
  else:
    file_to_check.close() # Close file
    return True

  # (1): Check if char is closing delimiter (values of dict), and check for a matching
  #      opening delimiter (true on mismatch or empty). Short-circuit prevents popping
  #      when non-delimiter char is encounterd

###

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


