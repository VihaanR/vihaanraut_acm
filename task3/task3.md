# Task 3

Blog chosen : Hybrid Programming using Python and Dart by Mihir Panchal on [GeeksforGeeks](https://www.geeksforgeeks.org/python/hybrid-programming-using-python-and-dart/)

## Review:

This blog post provides a progressive description on hybrid programming utilizing the example of Python and Dart. At the beginning , the approach is branched into two 
possiblilities such that either can be divided to perform specified functions according , or instead opt for a wrapper library called DartPy which hence leads to the 
practical application of Hybrid programming through the lens of DartPy which in its literal sense is a hybrid of both the programming languages.

The working is then explained by the elaboration of API calling where Python C-API and dart:ffi are used for embedding python code. I really like that the pathing issue is 
addressed beforehand to make the readers be wary of the dependancy issues that might come up before the methodology and listed out. This Dart library is imported into the 
flutter environment.

The methodology was upfront to point out the need for the additional DartPy API, despite the rich core libraries already present in Dart Programming , as it is employed
to achieve hybrid programming in mobile applications. The pre-requesites to be downloaded are mentioned in a concise step-by-step manner , following which we can use
the methods from the DartPly library by simply calling them by using `dartpyc.Py\_Initialize();` line of code to initialize python object instance.

The blog cleverly then calls back to the working of DartPly library. The python code is stored in a Dart  string variable which itself gets converted 
into C-encoded nativeutf8 by dart:ffi library thus displaying the concept of hybrid programming. The ouptut from the python code is then used by dart for 
implementation in mobile application features and functionality.

## Conclusion: 

Introduced me to a whole new framework called Dart while teaching me hybrid programming at the same time . Helped me become consious abut paths and pre-requisites before
code exectution.

One of the key details I adored was the constant callbacks on concepts which really matters a lot , especially in ACM Research where *each word matters* . 
I would keep such things in mind when I become a Co-com member in ACM Research to note down concepts that will be implemented throughout the research paper and blogs.
