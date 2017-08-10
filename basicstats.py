# -*- encoding: utf-8 -*-

"""Calculate basic statistics values along axis.

Examples:
	There is an input file, named 'x.csv', which has following data:
		0,0,0
		0,1,2
		2,3,4
		1,5,1
		3,8,1
	Execute the following command:
		$ python stats.py -a0 -d, -f'%.6f' x.csv
	Then, you will get the following output:
		min 0.000000 0.000000 0.000000
		mean 1.200000 3.400000 1.600000
		max 3.000000 8.000000 4.000000
		sum 6.000000 17.000000 8.000000
		psd 1.166190 2.870540 1.356466
		ssd 1.303840 3.209361 1.516575
"""

import numpy as np;


def __write_each_col(out, stats, labels, fmt):
	"""Write the value to specified output stream

	Args:
		out (stream):           Output stream
		stats (tuple(ndarray)): Tuple of statistics values
		labels (tuple(str):     List or tuple of name of statictics
		fmt (str):              Format string

	Returns:
		Nothing
	"""
	stats = np.hstack(stats);
	np.savetxt(out, stats, fmt=fmt, header=' '.join(labels), comments='');


def __write_each_row(out, stats, labels, fmt):
	"""Write the value to specified output stream

	Args:
		out (stream):           Output stream
		                        An instance which have a method named 'write'
		stats (tuple(ndarray)): Tuple of statistics values
		labels (tuple(str):     List or tuple of name of statictics
		fmt (str):              Format string

	Returns:
		Nothing
	"""
	for (l, r) in zip(labels, stats):
		out.write((l + ' ').encode('utf-8'));
		np.savetxt(out, r, fmt=fmt);


def calc(x, axis):
	"""Calculate basic statistics values along specified axis

	Args:
		x (ndarray): Input array
		axis (int):  Axis along which the statistics are computed

	Returns:
		(ndarray): Minimum
		(ndarray): Arithmetic mean
		(ndarray): Maximum
		(ndarray): Summation
		(ndarray): Population standard deviation
		(ndarray): Sample standard deviation
	"""
	y0 = np.min(x, axis=axis, keepdims=True);
	y1 = np.mean(x, axis=axis, keepdims=True);
	y2 = np.max(x, axis=axis, keepdims=True);
	y3 = np.sum(x, axis=axis, keepdims=True);
	y4 = np.std(x, axis=axis, ddof=0, keepdims=True);
	y5 = np.std(x, axis=axis, ddof=1, keepdims=True);
	return y0, y1, y2, y3, y4, y5;
