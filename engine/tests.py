#!/usr/bin/env python

import mock
import unittest

from world import World

class WorldTests(unittest.TestCase):
    def setUp(self):
        pass

    def testCreate(self):
        w = World(name="TestWorld")
        self.assertEqual(w.name,"TestWorld")
        
