import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use("fivethirtyeight")


dataset = { 'k': [[1,2], [2,3], [3,1]], 'r':[[6,5], [7,7], [8,6]]}
print ("type(dataset)=", type(dataset))
#added a second new_features to demonstrate the k_nearest_neighbors result.
new_features = [5,7]
new_features2 = [7,6]
new_features3 = [4,4]

def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less than total voting groups. IDIOT!!")
    distances = []
    for group in data:
        for features in data[group]:
            #euclidian_distance = sqrt( (features[0]-predict[0])**2 + (features[1]-predict[1])**2 )
            # this is not fast. iterating through list of lists will be big O n^2. bad.
            #this is 2D only. often need N dimensions.
            euclidian_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidian_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    #i is the group. i[1] is the point nearest to i[0]
    #[:k] = subsetting list from start to k
    #this one liner above would be equivalent to
    # votes = []
    #for i in sorted(distances)[:k]
    #    votes.append(i[1])
    vote_result = Counter(votes).most_common(1)[0][0]
    print ("type(Counter(votes).most_common(1))=", type(Counter(votes).most_common(1)) )
    print ("type(Counter(votes).most_common(1)[0])=", type(Counter(votes).most_common(1)[0]) )
    print ("Counter(votes).most_common(1)=", Counter(votes).most_common(1))
    #Counter(votes).most_common(1) is a list of a tuple.
    #we only want the most common result. most_common(1)
    return vote_result

result = k_nearest_neighbors(dataset, new_features2, k=3)
print ("result=", result)
