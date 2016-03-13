#!/usr/bin/env python

def indentation_converter(filename,ind_char=' ',old_ind=2,new_ind=4):
    with open(filename,'r') as f:
        for line in f:
            strippedline = line.lstrip(ind_char)
            indcount = len(line) - len(strippedline)
            newline = ind_char*(indcount/old_ind*new_ind) + strippedline
            with open (filename+'_new','a') as of:
                of.write(newline)

def main():
    filename = 'testfile.txt'
    indentation_converter(filename)

if __name__=='__main__':
    main()
