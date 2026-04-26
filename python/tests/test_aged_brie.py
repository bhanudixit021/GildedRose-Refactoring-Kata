# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
AGED_BRIE = "Aged Brie"

class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_quality_increases_by_1(self):
        items = [Item(AGED_BRIE, 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

     
if __name__ == '__main__':
    unittest.main()
