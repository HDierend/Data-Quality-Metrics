####################################
Unambiguous
####################################

*********
Description
*********
Each data record must be unambiguously interpretable.
If entries differ only by one characteristic or only by the ID, a duplicate analysis
is to be preferred because there is reasonable doubt that it is not the same entry.

********************
Tools and Libraries
********************

Python
=========

In Python’s Pandas library, Dataframe class provides a member function to find duplicate rows based on all columns or some specific columns.
It returns a Boolean Series with True value for each duplicated row.

To check if rows occur multiple time you can use this code snippet which will check if an row is identical to a provious row.

.. literalinclude:: examples/completeness/unambiguous_func1.py



MATLAB
=========

C++
=========

********************
Literature
********************