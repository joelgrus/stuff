from __future__ import division

import random
import collections


def squared_euclidean(x1, x2):
    return sum((a - b)**2 for a, b in zip(x1, x2))


distance = squared_euclidean


def assign_to_nearest(X, means):
    assignments = collections.defaultdict(list)
    for x in X:
        nearest_i, _ = min(enumerate(means), key=lambda m: distance(x, m[1]))
        assignments[nearest_i].append(x)
    return assignments


def mean(X):
    return [sum(p[i] for p in X) / len(X) for i in range(len(X[0]))]


def k_means_once(X, k):
    means = random.sample(X, k)
    while True:
        assignments = assign_to_nearest(X, means)
        new_means = [mean(group) for group in assignments.values()]
        if new_means == means:
            return new_means
        else:
            means = new_means


def total_mean_distance(X, means):
    assignments = assign_to_nearest(X, means)
    return sum(distance(means[i], x)
               for i, group in assignments.items()
               for x in group)


def k_means(X, k, restarts=1):
    all_means = [k_means_once(X, k) for _ in range(restarts)]
    return min(all_means, key=lambda mean: total_mean_distance(X, mean))

