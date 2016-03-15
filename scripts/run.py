#!/usr/bin/python3

import entropy
import numpy

def singleRun():

    weight = 'farming'
    alpha = 1.05
    beta = 0.05
    harbourBonus = 3.0
    cost = entropy.loadCosts('../data/costMatrix.csv')
    sites = '../data/cities_weights.csv'

    experiment = entropy.Experiment(0,weight,alpha,beta,harbourBonus)
    entropy.runEntropy(experiment, cost, sites, True)
 
    relativeWeights = numpy.full((len(entropy.Site.sites), len(entropy.Site.sites)), 0, dtype=float)
    for i in range(len(entropy.Site.sites)):
        for j in range(i):
            relativeWeights[i][j] = entropy.Site.sites[i].weight/entropy.Site.sites[j].weight

    result = entropy.Site.relativeSizes-relativeWeights
    print('diff:',numpy.absolute(result.sum()))

if __name__ == "__main__":
    singleRun()

