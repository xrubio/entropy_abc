#!/usr/bin/python3

import sampler
import threshold
import lognorm
import numpy as np

def postfn(params):
    numSites = 140
    experiment = lognorm.Experiment(0, params[0], params[1], params[2], numSites)
    simSizes = lognorm.run(experiment, False)
    return simSizes

    
numSites = 140
sites = '../data/cities_weights.csv'
data = lognorm.loadHistoricalSites(sites, numSites)
eps = threshold.LinearEps(15, 200, 150)
priors = sampler.TophatPrior([0,0,0],[2,2,0.1])

sampler = sampler.Sampler(N=5, Y=data, postfn=postfn, dist=lognorm.distRelative, threads=16)

for pool in sampler.sample(priors, eps):
    print("T: {0}, eps: {1:>.4f}, ratio: {2:>.4f}".format(pool.t, pool.eps, pool.ratio))
    for i, (mean, std) in enumerate(zip(np.mean(pool.thetas, axis=0), np.std(pool.thetas, axis=0))):
        print(u"    theta[{0}]: {1:>.4f} \u00B1 {2:>.4f}".format(i, mean,std))
    np.savetxt("result_"+str('%.2f')%pool.eps+'.csv', pool.thetas, delimiter=";", fmt='%1.5f')

print(pool.thetas)
np.savetxt("foo.csv", pool.thetas, delimiter=";", fmt='%1.5f')
