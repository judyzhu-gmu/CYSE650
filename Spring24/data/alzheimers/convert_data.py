import scipy.io as sio

mat_fname = "feature_name.mat"
data_fname = "ad_data.mat"
mat_contents = sio.loadmat(data_fname)
print(mat_contents)
#['X_test', 'X_train', '__globals__', '__header__', '__version__', 'y_test', 'y_train']
X_test = mat_contents['X_test']
y_test = mat_contents['y_test']
print(X_test.shape, y_test.shape)
mat_contents = sio.loadmat(mat_fname)
print(len(mat_contents['FeatureNames_PET']))
