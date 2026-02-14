import json

def calculate_prices(raw_items, config_path='config/settings.json'):
    with open(config_path, 'r') as f:
        cfg = json.load(f)
    
    final_catalog = []
    for item in raw_items:
        # Инженерный подход: расчет цены с маржой и конвертацией
        price_uah = round(item['price_usd'] * cfg['exchange_rate'] * cfg['margin'], 2)
        
        final_catalog.append({
            "product": item['name'],
            "price_uah": price_uah,
            "status": "In Stock" if item['stock'] > 0 else "Out of Stock",
            "last_update": "2026-02-14"
        })
    return final_catalog
