# Normalized Compression Distance calculation
# Last modified by: 
# Romulo Antao
# 31 December 2017
import os
from glob import glob
from itertools import combinations
from datetime import datetime
import sys
startTime = datetime.now()

def compression_distance(data_x, data_y, compressor="zlib", level=6):
	if compressor == "zlib":
		from zlib import compress, decompress
	if compressor == "bz2":
		from bz2 import compress, decompress
	data_x_bytes = data_x.encode('utf-8')
	data_y_bytes = data_y.encode('utf-8')

	c_x = len(compress(data_x_bytes, level))
	c_y = len(compress(data_y_bytes, level))
	c_x_y = len(compress(data_x_bytes + b" " + data_y_bytes, level))

	ncd = (c_x_y - min(c_x, c_y)) / float(max(c_x, c_y))
	return ncd

def ncd_calc(glob_files, compressor="zlib", level=6):
	files = glob(glob_files+'*')

	if not files:
		print(f"No files found with the pattern: {glob_files+'*'}")
		return

	file_datas = {}

	for filec in files:
		try:
			with open(filec, 'r') as f:
				file_datas[filec] = f.read()
		except IOError as e:
			print(f"Error reading file {filec}: {os.strerror(e.errno)}")
			continue

	try:
		with open('q.phy', 'w') as f:
			f.write(str(len(files)))

			item_name = 'A'
			combo_prev = ''

			for combo in combinations(files, 2):
				if combo[0] != combo_prev:
					f.write('\n'+item_name*9)
					item_name = chr(ord(item_name) + 1)
					combo_prev = combo[0]

				ncd_distance = compression_distance(file_datas[combo[0]], file_datas[combo[1]], compressor, level)
				f.write(' '+str(ncd_distance))

			f.write('\n'+item_name*9+' ')

		print("Using compressor:", compressor)
		print("Script execution time:", str(datetime.now()-startTime)[0:7])
	except IOError as e:
		print(f"Error writing to file 'q.phy': {os.strerror(e.errno)}")

if len(sys.argv) < 3:
	print("syntax error: python ncd_calc.py data_folder compressor")
	print("compressors available: zlib or bz2")
	print("example: python ncd.py data/animals/ zlib")
else:
	ncd_calc(sys.argv[1], str(sys.argv[2]), 9)
