### The number of elements, as well as the number of runs can be controlled
# by array_size.

### Additional Resources used:
# geeksforgeeks.org for information on how to make plots using
# matplotlib and using .find()
# stackoverflow (Aleksander Lidtke) on how to make multiple plots
# using figure()
# realpython.com (Ian Currie) on how to use the subprocess module

### Modules 
import subprocess # To run Sort.py
import matplotlib.pyplot as plt

## Function to extract number of line executions for given run of Sort.py. Values extracted from
# generated Sort.cover file. Values stored in relevent array for each sort at correct index. 
# i_select -> 0=inc, 1=dec, 2=ran.
## The for loops are designed with the the file structure of Sort.Cover in mind, skipping over
# uncessary or un-executed lines
def extract_values (arr_insertion, arr_selection, i_select):
    line_read = '' 
    section_sum = 0
    cf = open('Sort.cover', 'r')
    for _ in range(4):
        line_read = cf.readline()

    # Insertion Sort
    for i in range(8):
        line_read = cf.readline()
        val_endindex = line_read.find(':')
        if val_endindex > -1:
            section_sum += int(line_read[:val_endindex])
            # To double the while loop
            if (i == 4):
                section_sum += int(line_read[:val_endindex])
    arr_insertion[i_select].append(section_sum)
    section_sum = 0

    # Selection sort
    line_read = cf.readline()
    for _ in range(11):
        line_read = cf.readline()
        val_endindex = line_read.find(':')
        if val_endindex > -1:
            section_sum += int(line_read[:val_endindex])
    arr_selection[i_select].append(section_sum)
    cf.close()

####

if __name__ == '__main__':
    # Variables to store number of line executions for each type of sort
    # under various test cases. Stored as [[increasing], [decreasing], [random]]
    insertion_runcount = [[] * 3 for i in range(3)]
    selection_runcount = [[] * 3 for i in range(3)]
    array_size = [100, 200, 300, 400, 500] # Also x-axis

    # Run Sort.py for each of the situations, each loop cycling through
    # the increasing number of values, extract the line execution
    # counts and store in relevent arrays. Each array will store the
    # coordinates for the graphs 
    # Increasing
    for i in range(len(array_size)):
        subprocess.run(['python', '-m', 'trace', '--count', '-C', '.', 'Sort.py', str(array_size[i]), 'increasing'])
        extract_values(insertion_runcount, selection_runcount, 0)
    # Decreasing
    for i in range(len(array_size)):
        subprocess.run(['python', '-m', 'trace', '--count', '-C', '.', 'Sort.py', str(array_size[i]), 'decreasing'])
        extract_values(insertion_runcount, selection_runcount, 1)
    # Random
    for i in range(len(array_size)):
        subprocess.run(['python', '-m', 'trace', '--count', '-C', '.', 'Sort.py', str(array_size[i]), 'random'])
        extract_values(insertion_runcount, selection_runcount, 2)
    print (insertion_runcount)
    print (selection_runcount)

    # Create plots using pyplot
    dataorder = ['Increasing', 'Decreasing', 'Random']
    for i in range(3):
        plt.figure()
        plt.plot(array_size, insertion_runcount[i], label = 'Insertion Sort')
        plt.plot(array_size, selection_runcount[i], label = 'Selection Sort')
        plt.xlabel('Number of Sorted Elements')
        plt.ylabel('Instruction Count')
        plt.title(dataorder[i] + ' order of Data')
        plt.legend()

    plt.show()







