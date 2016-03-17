#!/usr/bin/env python
import sys

# TODO: Add new indent character argument, now the same is used.
# Add argument parsing.
# Add some checks (e.g., for when the file has an unexpected # of indents).

def indentation_converter(line,ind_char=' ',old_ind=2,new_ind=4):
    """Converts indentation from one character and length to something else.
    Arguments:
    line -- The line to be changed
    ind_char -- What character is used for indentation
    old_ind -- Old indentation (number of spaces, tabs etc.)
    new_ind -- New indent count
    Output:
    newline -- The modified line
    """
    # Strip the indent characters
    strippedline = line.lstrip(ind_char)
    # Measure how many indents there were originally in the line
    indcount = len(line) - len(strippedline)
    # Create the new line with the desired indent count
    newline = ind_char*(indcount/old_ind*new_ind) + strippedline
    return newline

def main():
    pass

if __name__=='__main__':
    main()
