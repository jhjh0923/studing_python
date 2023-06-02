from pathlib import Path

def shopping(shop_file, apath):
    shop_dict = {}
    with open(apath / shop_file, 'r') as f:
        next(f)
        for line in f:
            elements = line.strip().split()
            if len(elements) == 2:
                name, price = elements
                shop_dict[name] = price

    return shop_dict

def item_price(shop_file, item):
  price_dict = shopping(shop_file)

  return price_dict[item]
