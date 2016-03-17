#!/usr/bin/env python
import sys
import argparse

# TODO: Add new indent character argument, now the same is used.
# Add argument parsing.
# Add some checks (e.g., for when the file has an unexpected # of indents).

def indentation_converter(filename,ind_char,old_ind,new_ind):
    """Converts indentation from one character and length to something else.
    Arguments:
    filename -- The file name to be changed. The original file will not be touched
    ind_char -- What character is used for indentation
    old_ind -- Old indentation (number of spaces, tabs etc.)
    new_ind -- New indent count
    Output:
    Returns nothing. Writes changes to [filename_new] file
    """
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',type=str,help='The filename the indentation of which needs to be changed',required=True)
    args = parser.parse_args()
    filename = args.filename
    indentation_converter(filename,' ',2,4)

if __name__=='__main__':
    main()
