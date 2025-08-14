# SpaceToilet

## Description

Python application for linux, that shows how full is International Space Station's urine tank. Inspired by pISSStream. Uses [Lightstreamer](https://lightstreamer.com/) and libappindicator.



## How to run

To run the program, make sure you have installed libappindicator and it's GIR.
On debian and its' derivatives this means installing the following packages:

```shell 
    sudo apt-get install gir1.2-appindicator3-0.1 libappindicator1
```

Then install the following packages in pip 
```shell
    pip install PyGObject
    pip install lightstreamer-client-lib
```

Now you can run the program:

-If you want to run the unpackaged script

```shell
    python3 space_toilet.py
```

-If you want to run the executable provided by me in the release:

```shell
    sudo chmod +x space_toilet
    ./space_toilet
```


## Icon resources

<a href="https://www.flaticon.com/free-icons/toilet" title="toilet icons">Toilet icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/universe" title="universe icons">Universe icons created by Design Circle - Flaticon</a>