"""
Gould's sequencewiki is an infinite integer sequence, named after Henry W. Gouldwiki, 
that counts how many odd numbers are in each row of Pascal's trianglewiki. It consists only of powers of two*, and begins

1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, ..
Note that Gould's sequence is a fractal sequencewiki.

The binary logarithms ( exponents in the powers of two ) of Gould's sequence form an integer sequence

0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, ..
* A companion kata in Lean, proving that all elements of Gould's sequence are powers of two, is here.

Task
Define a generator function gould that sequentially generates the values ( the logarithms ) of this infinite sequence.
"""
def gould():
    """
    Generator for the binary logarithms of Gould's sequence (OEIS A000120).
    
    This sequence is equivalent to the number of 1s in the binary
    representation of n (the "popcount") for n = 0, 1, 2, ...
    """
    n = 0
    while True:
        # int.bit_count() is a fast, C-implemented method (Python 3.10+)
        # to count the number of '1' bits in an integer's binary representation.
        # An alternative for older Python versions is: bin(n).count('1')
        yield n.bit_count()
        n += 1