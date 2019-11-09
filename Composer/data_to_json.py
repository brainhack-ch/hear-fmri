from scipy.io import loadmat
fmridata = loadmat('test_data/matrix_network.mat')
music_array = fmridata['matrix_network']

import json
my_dict = {}
for t in range(len(music_array[0])):
	my_dict[t] = {}
	for c in range(len(music_array)):
		my_dict[t]["Channel{0}".format(c)] = int(music_array[c][t])
with open("matrix_network.json", 'w') as outfile:  
	json.dump(my_dict , outfile, indent=4)