####################################
Mean Squared Error
####################################

Full-Reference Quality Metrics

Also referred to as Mean Squared Deviation (MSD).

*********
Description
*********

The Mean Squared Error (MSE) measures the average squared difference between actual and ideal pixel values. 

******************
Interpretation
******************

When an image has no error, the MSE equals zero. As image error increases, its value increases.

*********
Limits
*********
MSE is simple to calculate but might not align well with the human perception of quality.

Furthermore, the Mean Squared Error depends heavily on the scaling of the image intensity. A mean square error of 100.0 for an 8-bit image (with pixel values in the range 0-255) looks terrible; but an MSE of 100.0 for a 10-bit image (pixel values in the range [0,1023]) is hardly noticeable.

******************
Example
******************




********************
Tools and Libraries
********************

Python
=========

MATLAB
=========

C++
=========

********************
Literature
********************
