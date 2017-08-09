# -*- coding: utf-8 -*-
#
from __future__ import division

from ..helpers import untangle, fsd, z


class Stenger(object):
    # TODO look up citation
    '''
    '''
    def __init__(self, n, variant):
        self.degree = 7
        self.dim = n

        if variant == 'a':
            if n == 3:
                u = 0.285231516480645
                v = 0.765055323929465
                B = [
                    -0.542565297000466e+01,
                    +0.490769827031175e+01,
                    +0.318402337562406,
                    -0.391335495408044e+01,
                    +0.436675887074467e-01,
                    +0.308676098900275e+01,
                    ]
            else:
                assert False
        else:
            assert variant == 'b'
            if n == 3:
                u = 0.765055323929465
                v = 0.285231516480645
                B = [
                    +0.192021185324132e+02,
                    +0.351560542364457,
                    -0.743934568569924e+01,
                    +0.270884863064213e-01,
                    +0.226016702392506e+01,
                    +0.828955120051268e-02,
                    ]
            else:
                assert False
        # TODO Stenger's original article has data up to n == 20.

        data = [
            (B[0], z(n)),
            (B[1], fsd(n, u, 1)),
            (B[2], fsd(n, v, 1)),
            (B[3], fsd(n, u, 2)),
            (B[4], fsd(n, v, 2)),
            (B[5], fsd(n, u, 3)),
            ]

        self.points, self.weights = untangle(data)
        return
