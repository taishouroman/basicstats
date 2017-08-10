# Basic statistics #
This process calculates basic statistical values along specified axis.

## Preparation ##
1. Put this directory under a Python module search path.
2. Copy or move 'basicstats' to a directory which is set PATH.

## Usage ##
From a terminal, run eigher of following commands:
```sh
$ python basicstats [OPTIONS]... FILE...
$ basicstats [OPTIONS]... FILE...
```

From Python interpreter or Python module, use like following:
```python
>>> import numpy as np;
>>> x = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]]);
>>> import basicstats;
>>> y_min, y_mean, y_max, y_sum, y_psd, y_ssd = basicstats.calc(x, 0);
```

## Command line options ##
usage: basicstats [OPTION]... FILE...

positional arguments:
  FILE                         Input files path

optional arguments:
  -h, --help                   show this help message and exit
  -a AXIS, --axis AXIS         Axis number along which the statistics are computed (default: 0)
  -d DELIM, --delimiter DELIM  String or character which separates columns (default: [whitespace])
  -f FMT, --format FMT         String which specifies the output format (default: %.18e)

If a FILE is '-', or there is no FILE and stdin is not a tty, read standard input.
