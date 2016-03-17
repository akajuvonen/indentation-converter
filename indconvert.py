#!/usr/bin/env python
import sys
import argparse

# TODO: Add new indent character argument, now the same is used.
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

def parse_args(args):
    """Argument parser for indentation converter.
    Arguments:
    args -- Command line arguments, can be retrieved from sys.argv[1:]
    Returns:
    filename -- The parsed filename (str)
    indchar -- Indentation character (str)
    oldind -- Old indentation (int)
    newind -- New indentation count (int)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',type=str,help='The filename of the file that needs its indentation changed',required=True)
    parser.add_argument('-i','--indchar',type=str,help='The character used for indentation',required=True)
    parser.add_argument('-o','--oldind',type=int,help='The existing number of indentation characters used (for one indentation)',required=True)
    parser.add_argument('-n','--newind',type=int,help='The new wanted number of indentation characters',required=True)
    arguments = parser.parse_args(args)
    v = vars(arguments)
    return v['filename'],v['indchar'],v['oldind'],v['newind']
def main():
    filename,indchar,oldint,newind = parse_args(sys.argv[1:])

if __name__=='__main__':
    main()
