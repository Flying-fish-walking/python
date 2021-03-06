from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


group, labels = createDataSet()
print(classify0([0, 0], group, labels, 1))


def file2matrix(filename):
    fr = open(filename)
    lines = fr.readlines()
    nlines = len(lines)
    levelmap={'didntLike':1,'smallDoses':2,'largeDoses':3}
    retMap = zeros((nlines, 3))
    classLabelVector = []
    index = 0
    for line in lines:
        line = line.strip()
        listFromLine = line.split('\t')
        retMap[index,:] = listFromLine[0:3]
        literal0=listFromLine[-1]
        classLabelVector.append(levelmap[literal0] if literal0 in levelmap.keys() else 0)
        index += 1
    return retMap,classLabelVector


datingDate,datingLabels=file2matrix('machinelearninginaction/Ch02/datingTestSet.txt')
