from gilded_rose import Item, GildedRose
import unittest

BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"

class GildedRoseTest(unittest.TestCase):
    def test_backstage_quality_increases_by_1_when_selling_in_is_more_than_10(self):
        items = [Item(BACKSTAGE, 11, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_backstage_quality_increases_by_2_when_selling_in_is_less_than_10_and_more_than_5(self):
        items = [Item(BACKSTAGE, 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_backstage_quality_increases_by_3_when_selling_in_is_less_than_5_and_more_than_0(self):
        items = [Item(BACKSTAGE, 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_backstage_quality_drops_to_0_when_sell_in_is_0(self):
        items = [Item(BACKSTAGE, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_drops_to_0_when_sell_in_is_less_than_0(self):
        items = [Item(BACKSTAGE, -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_is_never_more_than_50_when_sell_in_is_more_than_10(self):
        items = [Item(BACKSTAGE, 11, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_quality_is_never_more_than_50_when_sell_in_is_less_than_10_and_more_than_5(self):
        items = [Item(BACKSTAGE, 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_quality_is_never_more_than_50_when_sell_in_is_less_than_5_and_more_than_0(self):
        items = [Item(BACKSTAGE, 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)