import unittest

from gilded_rose import Item, GildedRose

SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_quality_does_not_change(self):
        items = [Item(SULFURAS, 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

if __name__ == "__main__":
    unittest.main()
