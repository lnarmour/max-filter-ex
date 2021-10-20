import numpy as np
import sys

global OPS
OPS = 0


def _max(a, b):
    global OPS
    OPS += 1
    return max(a, b)


# As written, this has an asymptotic complexity of O(N*W) assuming N>W.
# Can you rewrite it so that its asymptotic complexity is lower?!
#
def pool(array, N, W):
    output = np.zeros(N - W)

    for i in range(N - W):
        for j in range(W):
            output[i] = _max(array[i + j], output[i])

    return output


def main():
    global OPS

    # set default problem size or parse args
    N = 10000
    W = 250
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    elif len(sys.argv) >= 3:
        N = int(sys.argv[1])
        W = int(sys.argv[2])
    assert N > W, "let's only consider cases when N>W"

    # initialize some random data
    array = np.random.randint(0, 10000, size=N)

    # main work
    output = pool(array, N, W)

    # print summary
    print('N =', N)
    print('W =', W)
    print('-> OPS =', OPS)

if __name__ == '__main__':
    main()
