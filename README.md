# crystal-calculator
Crystal calculator is an APP used to calculate the spacing and angle in any type of crystal.

## How to use

#### Input lattice parameter

You can input lattice parameter in two ways：
1.  Input lattice parameter(a, b, c, alpha, beta, gamma) in "Set abcαβγ"
2.  Import lattice parameter from a cif file.

Note: The default lattice parameter is bcc-Fe

#### Calculate the spacing of crystal plane
Click “Get d-list”. Then crystal plane spacing (d) and corresponding reciprocal vector will be listed in d-list window.

#### Calculate the Angle
1. Input lattice parameter(a, b, c, alpha, beta, gamma) and two group index (HKL).
2. Click "Get Theta", the result is here

Note: The result is shown in the unit of degree rather than rad.

## Release

#### Windows user
You can download a exe file build for windows system at [release page](https://github.com/liingdujun-mmtq/crystal-calculator/releases/tag/release).

#### System compatibility
Works on：
+ Windows 10 2004 64bit
+ Windows 8.1 64 bit
+ Windows 7 SP1 32bit (need KB2533623 update)

* For win7/8 user: If *.dll lost, you may need install [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)

#### Other user
If the all used module has been installed, you can execute the py file directly.

Note: Crystal_calculator_linux_mac.py is recommended for use in Linux/Mac 

The list of used module is here:
* numpy
* PIL (for linux/mac)
