import unittest

from gilded_rose import Item, GildedRose

CONJURED = "Conjured"

class GildedRoseTest(unittest.TestCase):
    def test_conjured_quality_decreases_by_2(self):
        items = [Item(CONJURED, 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
    
    def test_conjured_quality_decreases_by_4_when_sell_in_is_zero(self):
        items = [Item(CONJURED, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

if __name__ == "__main__":
    unittest.main()
