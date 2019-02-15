import numpy as np

run = 10
N = 1000
dist_list = []
for i in range(run):
    x = np.random.uniform(size=N)
    y = np.random.uniform(size=N)
    dist = np.abs(x - y)
    dist_list.append(np.mean(dist))
ux = np.mean(dist_list)
sigma = np.std(dist_list)
print ('mean value: ', ux)
print ('confidence interval: ', [ux-2*sigma, ux+2*sigma])
print ('accuracy: ', (2. * sigma / ux))