# crystal-calculator
Crystal calculator is an APP used to calculate the spacing and angle in any type of crystal.

Crystal calculator是一款用于计算任意类型晶体中的晶面间距和晶面夹角的小工具。

## How to use/使用

#### Input lattice parameter/输入晶格参数

You can input lattice parameter in two ways：
1.  Input lattice parameter(a, b, c, alpha, beta, gamma) in "Set abcαβγ"
2.  Import lattice parameter from a cif file.

目前支持两种方式导入晶格参数：
1. 将晶格常数（a、b、c、alpha、beta、gamma）输入到“Set abcαβγ”对应栏目中
2. 从cif文件导入晶格参数

#### Calculate the spacing of crystal plane/计算晶面间距
Click “Get d-list”. Then crystal plane spacing (d) and corresponding reciprocal vector will 
be listed in d-list window.

点击“Get d-list”按钮，弹出d-list窗口，即可看到当前晶体结构中主要晶面的面间距（d）和对应的倒易矢量长度（d*）

#### Calculate the Angle/计算晶面夹角
1. Input lattice parameter(a, b, c, alpha, beta, gamma) and two group index (HKL).

在输入晶格常数（a、b、c、alpha、beta、gamma）后，分别在“Set H1 K1 L1”和“Set H2 K2 L2”中输入两个晶面的晶面指数（HKL）

2. Click "Get Theta", the result is here

点击“Get Theta”即可得到二者夹角

Note: The result is shown in the unit of degree rather than rad.

注意：角度以°为单位

## Release/发行版

#### Windows user
You can download a exe file build for windows system at Release Page.

Windows用户可以直接通过Release页面下载

##### System compatibility/系统兼容性
Works on/工作条件：
+ Windows 10 2004 64bit
+ Windows 8.1 64 bit
+ Windows 7 SP1 32bit (need KB2533623 update/需要更新KB2533623)

* For win7/8 user: If *.dll lost, you may need install [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)

win7/8用户如果提示dll丢失请安装[Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)

##### Note for the different exe/不同exe文件的区别
Exe file with "nuitka" in filename is packed using nuitka. 文件名中包含nuitka的文件使用nuitka打包

Exe file without "nuitka" is packed using pyinstaller. 文件名中包含nuitka的文件使用pyinstaller打包

#### Other user/其他系统用户
If the all used module has been installed, you can execute the py file directly.

如果所有的module都被安装，则py文件可以直接执行

The list of used module is here/所需的module列表:
* numpy (removed in 1.23+)
* PIL (for linux/mac)

## Acknowledgements/致谢
Thanks for the testing and support from University of Science and Technology Beijing (USTB, Beijing, China) and Hefei University of Technology (HFUT, Hefei, China).

感谢北京科技大学和合肥工业大学的支持和测试工作。
