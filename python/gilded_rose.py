# -*- coding: utf-8 -*-
AGED_BRIE = "Aged Brie"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured"



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater:
    def update_quality(self, item:Item) -> None:
        pass

    def update_sell_in(self, item:Item) -> None:
        pass



class DefaultItemUpdater:
    def update_quality(self, item:Item) -> None:
        decrease_quality(item)
        if item.sell_in < 0:
            decrease_quality(item)

    def update_sell_in(self, item:Item) -> None:
        item.sell_in -= 1

class AgedBrieUpdater(DefaultItemUpdater):
    def update_quality(self, item:Item) -> None:
        increase_quality(item)
        if item.sell_in < 0:
            increase_quality(item)
    
    def update_sell_in(self, item:Item) -> None:
        item.sell_in -= 1

class BackstageUpdater(DefaultItemUpdater):
    def update_quality(self, item:Item) -> None:
        increase_quality(item)
        if item.sell_in < 10:
            increase_quality(item)
        if item.sell_in < 5:
            increase_quality(item)
        if item.sell_in < 0:
            item.quality = 0
    
    def update_sell_in(self, item:Item) -> None:
        item.sell_in -= 1

class SulfurasUpdater(DefaultItemUpdater):
    def update_quality(self, item:Item) -> None:
        pass
    
    def update_sell_in(self, item:Item) -> None:
        pass

class ConjuredUpdater(DefaultItemUpdater):
    def update_quality(self, item:Item) -> None:
        decrease_quality(item, 2)
        if item.sell_in < 0:
            decrease_quality(item, 2)
    
    def update_sell_in(self, item:Item) -> None:
        item.sell_in -= 1

ITEM_UPDATERS = {
    AGED_BRIE: AgedBrieUpdater(),
    BACKSTAGE: BackstageUpdater(),
    SULFURAS: SulfurasUpdater(),
    CONJURED: ConjuredUpdater()
}


def increase_quality( item:Item, amount:int=1, max_quality:int=50) -> None:
    item.quality = min(max_quality,item.quality + amount)

    
def decrease_quality( item:Item, amount:int=1, min_quality:int=0) -> None:
    item.quality = max(min_quality,item.quality - amount)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_single_item(item)

    
    def update_single_item(self, item):
        item_updater = ITEM_UPDATERS.get(item.name, DefaultItemUpdater())
        
        item_updater.update_sell_in(item)
        item_updater.update_quality(item)
            
        
                

