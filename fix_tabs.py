import sys

# Define the number of spaces that correspond to a single tab character
TAB_WIDTH = 4

# Open the input file for reading and the output file for writing
with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w') as outfile:
    # Read the input file line by line
    for line in infile:
        # Strip any leading and trailing whitespace characters from the line
        line = line.strip()

        # Count the number of spaces at the beginning of the line
        num_spaces = 0
        for char in line:
            if char == ' ':
                num_spaces += 1
            elif char == '\t':
                num_spaces += TAB_WIDTH
            else:
                break

        # Replace any leading spaces with tabs
        num_tabs = num_spaces // TAB_WIDTH
        num_spaces = num_spaces % TAB_WIDTH
        new_line = '\t' * num_tabs + ' ' * num_spaces + line[num_spaces:]

        # Write the modified line to the output file
        outfile.write(new_line + '\n')
