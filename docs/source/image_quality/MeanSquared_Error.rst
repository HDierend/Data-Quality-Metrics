####################################
Mean Squared Error
####################################

Full-Reference Quality Metrics

Also referred to as Mean Squared Deviation (MSD).

*********
Description
*********

The Mean Squared Error (MSE) measures the average squared difference between actual and ideal pixel values. It therefore compares an ideal reference image with an actual image.

******************
Interpretation
******************

When an image has no pixel differences (no errors), the MSE equals zero. As image differences increase, its value increases.

*********
Limits
*********
MSE is simple to calculate but might not align well with the human perception of quality.

Furthermore, the Mean Squared Error depends heavily on the scaling of the image intensity. A mean square error of 100.0 for an 8-bit image (with pixel values in the range 0-255) looks terrible; but an MSE of 100.0 for a 10-bit image (pixel values in the range [0,1023]) is hardly noticeable.

Only images showing the same scene should be compared. 

******************
Example
******************
An image from a traffic surveillance camera in Germany is used to show the MSE results.

.. image:: examples/Reference_Image.png
  :width: 640
 
Reference Image

.. image:: examples/Image_Dark.png
  :width: 640
  
MSE of 2075.3
  
.. image:: examples/Image_Sunshine.png
  :width: 640

MSE of 917.8

********************
Tools and Libraries
********************

Python
=========

MATLAB
=========
Within the MATLAB Image Processing Toolbox a function to calculate the MSE exists:
::
  ref = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  MSE_dark = immse(dark, ref);
  fprintf('The mean-squared error for the dark image is %0.4f\n', MSE_dark);

  MSE_sun = immse(sun, ref);
  fprintf('The mean-squared error for the sun image is %0.4f\n', MSE_sun);

A detailed description can be found at the `Mathworks Website <https://de.mathworks.com/help/images/ref/immse.html>`_. For an RGB image the MSE for each channel is calculated and the average of all channel MSEs is the MSE of the image. It is also possible to only calculate the MSE for one channel:
:: 
  ref = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  MSE_R = immse(dark(:,:,1), ref(:,:,1));
  MSE_G = immse(dark(:,:,2), ref(:,:,2));
  MSE_B = immse(dark(:,:,3), ref(:,:,3));
  fprintf('\nThe mean-squared error for R-channel %0.4f\n', MSE_R);
  fprintf('The mean-squared error for G-channel %0.4f\n', MSE_G);
  fprintf('The mean-squared error for B-channel %0.4f\n', MSE_B);
  
If access to the MATLAB Image Processing Toolbox is denied, one can program the MSE by their own:
::
  num_pixel = size(ref,1)*size(ref,2)*size(ref,3);
  MSE = sum((double(ref) - double(dark)).^2,'all') / num_pixel;
  fprintf('The mean-squared error for the dark image is %0.4f\n', MSE);

C++
=========
OpenCV contains a class for calculating the MSE. A detailed description can be found in the `OpenCV Docs <https://docs.opencv.org/4.x/d7/d80/classcv_1_1quality_1_1QualityMSE.html#a82ba740a06f48562a08517079712218c>`_. 

********************
Literature
********************
