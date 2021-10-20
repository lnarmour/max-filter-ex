## simple overlapped max-pooling (1D)

The python code in `main.py` implements a simple 1D overlapped max pooling computation.
Given an input array of size N, and a window size W, it produces an output array of size O(N) where the i'th element of the output is the maximum of the W successive elements of the input starting at i.

In other words:
```
output[0] = max(input[0], input[1], ..., input[0+W-1])
output[1] = max(input[1], input[2], ..., input[1+W-1])
output[2] = max(input[2], input[3], ..., input[2+W-1])
...
output[N-W] = max(input[N-W], input[N-W+1], ..., input[N-1])
```

This takes O(NW) time as written. 
```
$ python main.py 
N = 10000
W = 250
-> OPS = 2437500
```

## challenge

Can you rewrite the `pool` function so that its asymptotic complexity is lower?
