def shopping(shop_file, data_path):
    shop_dict = {}
    with open(data_path / shop_file, 'r') as f:
        next(f)
        for line in f:
            elements = line.strip().split()
            if len(elements) == 2:
                name, price = elements
                shop_dict[name] = price

    return shop_dict
