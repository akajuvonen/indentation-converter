#!/usr/bin/env python
import sys

def indentation_converter(filename,ind_char=' ',old_ind=2,new_ind=4):
    """Converts indentation from one character and length to something else.
    Arguments:
    filename -- The file name to be changed. The original file will not be touched
    ind_char -- What character is used for indentation
    old_ind -- Old indentation (number of spaces, tabs etc.)
    new_ind -- New indent count
    Output:
    Returns nothing. Writes changes to [filename_new] file
    """
    # Check for cli args. This will be changed to argparse
    if len(sys.argv)>1:
        filename = sys.argv[1]
    # Open the file
    with open(filename,'r') as f:
        # Process line by line
        for line in f:
            # Strip the indent characters
            strippedline = line.lstrip(ind_char)
            # Measure how many indents there were originally in the line
            indcount = len(line) - len(strippedline)
            # Create the new line with the desired indent count
            newline = ind_char*(indcount/old_ind*new_ind) + strippedline
            # Write to output file
            with open (filename+'_new','a') as of:
                of.write(newline)

def main():
    filename = 'testfile.txt'
    indentation_converter(filename)

if __name__=='__main__':
    main()
