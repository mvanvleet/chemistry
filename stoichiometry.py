#!/usr/bin/env python
"""A module that contains functions for performing basic stoichiometric tasks.
Includes the following functions:
    MolecularWeight(xyz_file)

Last Updated: 08/20/13 by mvanvleet
"""

from . import constants
from . import elementdata

# Function to obtain molecular weight of a compound from a .xyz file
def MolecularWeight(coordinates):
    """Given an input list of coordinates of one of the the following forms:
    A. list of lists: [[symbol1,x1,y1,z1],[symbol2,x2,y2,z2],...[symboln,xn,yn,zn]]
    B. list: [symbol1, symbol2, symbol3]
    returns the molecular weight (in g/mol) of
    the compound specified by the list.
    """

    if type(coordinates[0]) == list:
        elements=[atom[0] for atom in coordinates]
    elif type(coordinates[0]) == str:
        elements = coordinates
    else:
        raise TypeError('Input must be a list or a list of lists')

    # Calculate molecular weight
    molecular_weight=0.00
    for element in elements:
        try:
            atno=elementdata.AtomicNumber(element) 
        except KeyError:
            raise KeyError('Error: Element name "'+str(element)+\
                    '" not recognized. Check your .xyz file for errors.')
        #(column 3 of element_data list contains molecular weight data)
        molecular_weight += elementdata.Weight(atno) 
    return molecular_weight
        


if __name__=='__main__':
    from . import io
    import os
    pwd = os.path.dirname(os.path.abspath(__file__))
    coordinates,title=io.ReadCoordinates('/'.join([pwd,'tests','test.xyz']))
    print(MolecularWeight(coordinates))
    atoms=['C','H','H','H']
    print(MolecularWeight(atoms))
