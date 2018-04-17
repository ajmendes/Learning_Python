# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:41:41 2018

@author: antonio
"""

import xlrd
import xlwt
import numpy as np

def read_excel(filename, n=0):
    """Converts first sheet from an Excel file into an ndarray
    
    Parameters
    ----------
    filename : string
        Path to file.
        
    Returns
    -------
    ndarray with sheet contents (no conversion done)
    """
    contentstring = open(filename, 'rb').read()
    book  = xlrd.open_workbook(file_contents=contentstring)
    sheet = book.sheets()[n]
    array = np.zeros((sheet.ncols, sheet.nrows))
    
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            array[col][row] = sheet.cell(row, col).value
    
    return array

def write_excel(filename, sheetnames, arrays):
    """Creates an Excel file with given sheet names and arrays.
    
    Parameters
    ----------
    filename : string
        Path to file.
    sheetnames : iterable (string)
        List of names for the book's sheets
    arrays : iterable (ndarray)
        List of data arrays for the book's sheets    
    """
    if len(sheetnames) != len(arrays):
        raise IndexError("Array and sheet number must be equal.")
        
    book = xlwt.Workbook()
    
    for name, array in zip(sheetnames, arrays):
        sheet = book.add_sheet(name)
        cols, rows = array.shape
        
        for row in range(rows):
            for col in range(cols):
                sheet.write(row, col, array[col][row])
    
    book.save(filename)