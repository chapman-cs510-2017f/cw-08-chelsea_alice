# CS510 CW 8

**Author(s):** **Chelsea Parlett-Pelleriti and Alice Wong**

[![Build Status](https://travis-ci.org/chapman-cs510-2017f/cw-08-YOURNAME.svg?branch=master)](https://travis-ci.org/chapman-cs510-2017f/cw-08-YOURNAME)

## Specification

1. Copy your CW07 julia set modules into CW08. Modify your implementation so that it uses ```numba``` Just-In-Time (JIT) compilation to speed up your code, using the code block below as a guide. Specifically:
    * Import ```numba``` at the top of your module, in addition to ```numpy```.
    * When creating the ```julia``` function that transforms the entire complex plane, include a "decorator" (```@nb.vectorize```) just before your function definition to enable JIT compilation. (See below for the correct type signature.) 
    * Use the vectorization properly when applying the ```julia``` function to your complex plane as a ```numpy``` array (or ```DataFrame```). Note that if you called ```np.vectorize``` from ```numpy``` to vectorize your code before, this is no longer needed: the decorator for ```numba``` completely replaces this functionality by making your function a natively compiled ```ufunc``` directly.
1. In a notebook ```julia-benchmark.ipynb```, create a complex plane of size 5000 x 5000 points. First run your ```refresh``` method with the ```numba``` decorator commented out (and the ```numpy``` vectorization restored if necessary), and use ```%time``` to see how long your old implementation takes to compute the set (for an interesting ```c``` value that you like). Then uncomment the decorator to enable the JIT compilation with ```numba``` (removing the ```numpy``` vectorization if necessary), and again use ```%time``` to refresh the plane. How much faster does the code run after adding this one line of code? Detail your benchmarking investigation in your notebook.
1. More information about `numba` can be found here: [Numba Quickstart](http://numba.pydata.org/numba-doc/0.12.2/quickstart.html)
1. Work through the [Julia Overview Slides](http://slides.com/profdressel/julia-overview/). Create the appropriate notebooks and test functions as you follow along. Discuss and ask questions.

Example `numba` code:
```python
import numba as nb

@nb.vectorize([nb.int32(nb.complex128)])
def julia(z):
    # Your previous numpy code here
    pass

# Remove calls to np.vectorize if they exist elsewhere
```
## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**This was really helpful. This is a lot easier than using Pypy and the  speed up was insane for 2 added lines of  code. My current midterm assignment takes a long time to run, so this may help with that.**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Chelsea Parlett-Pelleriti and  Alice Wong**
