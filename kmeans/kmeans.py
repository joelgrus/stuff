from solution.kmeans import k_means

# def k_means(X, k):
#     pass


def test():

    X = [
        [1, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],

        [0, 0, 5, 5],
        [0, 1, 4, 5],
        [1, 0, 5, 4],
        [0, 1, 5, 4],

        [5, 4, 0, 0],
        [4, 5, 1, 0],
        [5, 5, 1, 0],
        [5, 4, 0, 1],
    ]

    answer = {
        (0.5, 0.5, 0.5, 0.25),
        (0.25, 0.5, 4.75, 4.5),
        (4.75, 4.5, 0.5, 0.25),
    }

    result = k_means(X, 3)
    print('result:\n{}\ncorrect: {}'.format(
          '\n'.join(map(str, sorted(result))),
          set(map(tuple, result)) == answer))


test()
