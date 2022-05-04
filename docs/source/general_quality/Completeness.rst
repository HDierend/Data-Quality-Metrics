####################################
Completeness
####################################

*********
Description
*********

Measured, stored or recorded data must have all necessary attributes. So-called NaN values result from faulty operations and reduce completeness.
To improve this quality dimension, you can assess your data whether all your information is available or whether there are any missing elements.

********************
Tools and Libraries
********************

Python
=========

Working with Missing Data in Pandas

.. literalinclude:: examples/completeness/completeness_dataframe.py

.. literalinclude:: examples/completeness/completeness_func1.py

.. ipython::

   In [1]: missing_value_coordinates(dataframe)

   Out[2]: (array([0, 0, 2, 3, 3], dtype=int64), array([2, 3, 0, 1, 3], dtype=int64))


MATLAB
=========

C++
=========

********************
Literature
********************