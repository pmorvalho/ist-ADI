import numpy as np

# a.1 Transition probability matrix for dice = 1
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

# a.2. Use matrix power to obtain remaining dice cases based on dice = 1
md2 = np.linalg.matrix_power(md1,2)
md3 = np.linalg.matrix_power(md1,3)
md4 = np.linalg.matrix_power(md1,4)
md5 = np.linalg.matrix_power(md1,5)
md6 = np.linalg.matrix_power(md1,6)

# a.3. Average all the matrixes to obtain the TPM for the whole model
mdt = (md1+md2+md3+md4+md5+md6)/6

# b.1. Matrix power of 3 to obtain t=3 relative to t=0
m_bt3 = np.linalg.matrix_power(mdt,3)

# b.2. Select row with distribution assuming player departed from center (10) at t=0
dist_t3_c10 = m_bt3[-1]

# write to csv helper to prettify data in excel/google docs
import csv
def write_to_csv(filename, matrix):
	with open(filename,"w") as output:
		writer = csv.writer(output, lineterminator="\n")
		writer.writerows(matrix)