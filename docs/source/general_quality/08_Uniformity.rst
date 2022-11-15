####################################
Uniformity
####################################

*********
Description
*********

The information of a data set must be structured in a uniform way.
Data of the same type should also have the same dimensions.

Uniformity is therefore specific to metrics and units of measurement, and is particularly important when data comes from different sources.

In the following examples, data will be compared for uniformity and if necessary recalculated to fit uniformity.

********************
Tools and Libraries
********************

Python
=========

Install **pandas**
:: 
  pip install pandas

.. literalinclude:: examples/uniformity/uniformity_func1.py

.. code-block:: pycon

   In [1]: print(df.head())
           
   Out[2]:       Name  Height Handedness
          0      Jon    6'5"      Right
          1      Rob  6'7.5"       Left
          2   Sharon    6'3"      Right
          3     Alex    6'2"      Right
          4  Rebecca      7'      Right

As you can see, the height column contains impirical dimensions. For further processing or comparison with metric data,
it is necessary to convert from feet and inches to metres and centimetres.

.. literalinclude:: examples/uniformity/count_inches.py

Now you can apply this function to the whole column and recalculate to meters



MATLAB
=========

C++ 
=========

********************
Literature
********************