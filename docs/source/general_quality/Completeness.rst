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

Simple dataframe with four columns where :literal:`None`- and :literal:`NaN`-Values occur.

.. literalinclude:: examples/completeness/completeness_dataframe.py

Following functions can be used to create two arrays with row- and column-coordinates of the missing data for later computation.

.. literalinclude:: examples/completeness/completeness_func1.py

Output of the function :literal:`missing_value_coordinates()`

.. code-block:: pycon

   In [1]: missing_value_coordinates(dataframe)

   Out[2]: (array([0, 0, 2, 3, 3], dtype=int64), array([2, 3, 0, 1, 3], dtype=int64))

To count the number of missing values columnwise you can the following function which is a combination of two functions.

.. literalinclude:: examples/completeness/completeness_func2.py

The output when the example dataframe is used.

.. code-block:: pycon

   In [1]: count_missing_value(dataframe)

   Out[2]: column a    1
           column b    1
           column c    1
           column d    2


Removing missing data
----------------------

Missing data can be problematic for machine-learning algorithms, for example, because many models cannot handle missing values.
For this situation, it makes sense to remove rows with missing data.

To do this, several steps must be carried out. The first step is to declare what constitutes a missing datum and the second
step is to convert these values into nan values and remove the corresponding row.

.. literalinclude:: examples/completeness/completeness_func3.py

For example :literal:`None` and :literal:`0` will be replaced with :literal:`NaN`-Values

.. code-block:: pycon

   In [1]: replace_missing_value(dataframe, value_types = [str(None), 0])

   Out[2]:      column a  column b  column c  column d
          0       NaN      30.0       NaN       NaN
          1      90.0      45.0      40.0      12.0
          2       NaN      56.0      80.0      35.0
          3      95.0       NaN      98.0       NaN






MATLAB
=========

C++
=========

********************
Literature
********************