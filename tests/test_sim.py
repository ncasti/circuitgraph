import unittest
import time

import circuitgraph as cg
from random import sample


# FIXME: Write a real unittest for this (or just remove PyVerilator support)
class TestCircuit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c432 = cg.from_lib('c432')

    def test_fanin(self):
        sim = cg.construct_simulator(self.c432)
        inputs = self.c432.inputs()

        start = time.time()
        for i in range(2**20):
            setattr(sim.io, sample(inputs, 1)[0], sample((0, 1), 1)[0])
            getattr(sim.io, 'N223')
        rt = time.time()-start
        print(rt)
        print(((rt/2**20)*2**32)/3600)
