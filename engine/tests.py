#!/usr/bin/env python

import mock
import unittest

from world import World
from overworld import Overworld
from town import Town
from player import Player

class WorldTests(unittest.TestCase):
    def setUp(self):
        pass

    def testCreate(self):
        w = World(name="TestWorld")
        self.assertEqual(w.name,"TestWorld")
        
    def testCreateDefaults(self):
        w = World(seed="1")
        self.assertEqual(w.name,"Default Name")
        self.assertEqual(80,w.width)
        self.assertEqual(80,w.height)
        self.assertEqual(w.seed,"1")

    def testSeeds(self):
        w1 = World(seed="1")
        w2 = World(seed="2")
        w1_clone = World(seed="1")
        self.assertNotEqual(w1.seed,w2.seed)
        self.assertNotEqual(w1.towns[0].name,w2.towns[0].name)
        self.assertEqual(w1.seed,w1_clone.seed)
        self.assertEqual(w1.towns[0].name,w1_clone.towns[0].name)
        
    def testGetData(self):
        w = World(width=2,height=2)
        data = w.getInitialData()
        self.assertTrue("towns" in data.keys())
        
