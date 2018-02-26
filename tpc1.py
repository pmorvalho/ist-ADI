import numpy as np
md1 = np.array([
	[0,1/3,0,0,0,1/3,1/3,0,0,0],
	[1/2,0,1/2,0,0,0,0,0,0,0],
	[0,1/3,0,1/3,0,0,0,1/3,0,0],
	[0,0,1/2,0,1/2,0,0,0,0,0],
	[0,0,0,1/3,0,1/3,0,0,1/3,0],
	[1/2,0,0,0,1/2,0,0,0,0,0],
	[1/2,0,0,0,0,0,0,0,0,1/2],
	[0,0,1/2,0,0,0,0,0,0,1/2],
	[0,0,0,0,1/2,0,0,0,0,1/2],
	[0,0,0,0,0,0,1/3,1/3,1/3,0]
])
md2 = np.linalg.matrix_power(md1,2)
md3 = np.linalg.matrix_power(md1,3)
md4 = np.linalg.matrix_power(md1,4)
md5 = np.linalg.matrix_power(md1,5)
md6 = np.linalg.matrix_power(md1,6)
mdt = (md1+md2+md3+md4+md5+md6)/6
m_bt3 = np.linalg.matrix_power(mdt,3)
m_average_bt3 = np.average(np.linalg.matrix_power(mdt,3),axis=0)

# write to csv helper
import csv
def write_to_csv(filename, matrix):
	with open(filename,"w") as output:
		writer = csv.writer(output, lineterminator="\n")
		writer.writerows(matrix)