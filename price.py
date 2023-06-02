from pathlib import Path

content_path = Path('/') / 'content'
data_path = content_path / "data"
data_path.mkdir(parents=True, exist_ok=True)

def shopping(shop_file):
    shop_dict = {}
    with open(data_path / shop_file, 'r') as f:
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
