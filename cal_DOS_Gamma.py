import numpy as np
import os

def makeDirectory(path):
        try:
                os.makedirs(path)
        except OSError:
                if not os.path.isdir(path):
                        raise

makeDirectory('results')

nRun = 5
n_bins = 1000
omega_min = -100
omega_max = 800
binsize = (omega_max-omega_min)/n_bins

def calculateDOS_gamma(eigenvalues, gamma):
    hist, bin_edges = np.histogram(eigenvalues, bins=n_bins, range=(omega_min,omega_max), density=True)
    omega_mod = eigenvalues

    gammaCG = np.zeros(n_bins)
    count = np.zeros(n_bins)
    omega_mod += abs(omega_min)

    for i in range(len(gamma)):
        binId = int(omega_mod[i]/binsize)
        if( (binId>=0) and (binId<n_bins) ):
            count[binId] += 1
            gammaCG[binId] += gamma[i]

    for i in range(n_bins):
        if(count[i] != 0):
            gammaCG[i] /= count[i]

    return hist, gammaCG


dos = np.zeros((n_bins,2))
dos[:,0] = np.linspace(omega_min, omega_max, n_bins)
gammaCG = np.zeros((n_bins,2))
gammaCG[:,0] = np.linspace(omega_min, omega_max, n_bins)

for r in range(1,nRun):
        data = np.genfromtxt('../T300/runs/run0/data/'+str(r)+'/G_T300.data')
        eigenvalues = data[:,2]
        gamma = data[:,1]
        temp1, temp2 = calculateDOS_gamma(eigenvalues, gamma)
        dos[:,1] += temp1
        gammaCG[:,1] += temp2


dos[:,1] /= (nRun-1)
gammaCG[:,1] /= (nRun-1)
np.savetxt('DOS_ave.txt',dos)
np.savetxt('gamma_ave.txt',gammaCG)
