from scipy.io import loadmat
fmridata = loadmat('test_data/matrix_network.mat')
music_array = fmridata['matrix_network']


print music_array