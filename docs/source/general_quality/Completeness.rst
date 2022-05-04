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

In order to measure the completeness of a data set, it makes most sense to identify data gaps and, if necessary, to quantify them.
In the following, a simple example and functions will show how data gaps can be identified.

Identifying missing data
-----------------------

Simple dataframe with four columns where :literal:`text`, ''None''- and :literal:`text`, ''NaN''-Values occur.

.. literalinclude:: examples/completeness/completeness_dataframe.py

Following functions can be used to create two arrays with row- and column-coordinates of the missing data for later computation.

.. literalinclude:: examples/completeness/completeness_func1.py

Output of the function :literal:`text`, ''missing_value_coordinates()''

.. code-block:: pycon

   In [1]: missing_value_coordinates(dataframe)

   Out[2]: (array([0, 0, 2, 3, 3], dtype=int64), array([2, 3, 0, 1, 3], dtype=int64))


MATLAB
=========

C++
=========

********************
Literature
********************