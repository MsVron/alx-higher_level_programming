#!/usr/bin/python3

"""
Appends a line of text after each line containing
a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after each line
        containing the search string.

    Raises:
        None

    Returns:
        None
    """
    tmp_fn = 'temp.txt'  # Name of the temporary file
    
    # Open the input file in read mode and create a temporary output file
    with open(filename, 'r') as input_file, open(tmp_fn, 'w') as output_file:
        # Iterate through each line in the input file
        for line in input_file:
            # Write the current line to the output file
            output_file.write(line)
            
            # Check if the search string is present in the current line
            if search_string in line:
                # Write the new string after the line
                # containing the search string
                output_file.write(new_string + '\n')
    
    # Replace the input file with the temporary output file
    with open(tmp_fn, 'r') as temp_file, open(filename, 'w') as input_file:
        # Copy the contents of the temporary file back to the input file
        for line in temp_file:
            input_file.write(line)
    
    # Remove the temporary file
    remove_file(tmp_fn)

"""
Removes a file.
"""


def remove_file(filename):
    """
    Args:
        filename (str): The name of the file to remove.

    Raises:
        None

    Returns:
        None
    """
    with open(filename, 'w') as file:
        file.write('')
