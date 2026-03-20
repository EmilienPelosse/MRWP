import engine as en
import random


# Generates a random list of sampleSize nodes from G ignoring the nodes in the
# list exclude
def generateRandomSample(G, sampleSize, exclude):
    sample = []
    nodelist = [n for n in G if n not in exclude]
    if len(nodelist) < sampleSize:
        return None
    while len(sample) < sampleSize:
        newExtraction = nodelist[random.randint(0, len(nodelist) - 1)]
        if newExtraction not in sample:
            sample.append(newExtraction)
    return sample

# runs the model on G starting with randomly selected nodes for
#groupA and groupB


def fullyRandomExperiment(G, tMax, initialNodesSizes):
    groupA = generateRandomSample(G, initialNodesSizes, [])
    groupB = generateRandomSample(G, initialNodesSizes, groupA)
    return en.graphModelRun(G, tMax, groupA, groupB)

# runs the model on G starting randomly selected groups of nodes for groupB and
# with the specified nodes in groupA


def halfRandomExperiment(G, tMax, groupA):
    groupB = generateRandomSample(G, len(groupA), groupA)
    return en.graphModelRun(G, tMax, groupA, groupB)

# runs the function experiment with paramethers G, tMax and
# thirdParameter for experimentsNumber times and
# returns a dictionary of the results


def repeatedExperiments(experiment, G, tMax,
                        thirdParameter, experimentsNumber):
    data = {}
    # run the experiments
    for n in range(experimentsNumber):
        data[n] = experiment(G, tMax, thirdParameter)
    return data

# takes a dictionary experimentDataDict as the one produced by
# repeatedExperiments and computes a list which contains
# the average number of nodes in state u, a, and b respectively


def averageExperiment(experimentDataDict, tMax):
    numberofStates = 3
    experimentsNumber = len(experimentDataDict)
    return [[sum([experimentDataDict[n][t][i] for n in range(experimentsNumber)]) /
             experimentsNumber for i in range(numberofStates)] for t in range(tMax)]
