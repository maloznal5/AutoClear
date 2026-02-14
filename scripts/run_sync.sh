#!/bin/bash
echo "💳 Обработка прайс-листов поставщиков (Кейс: 10,000 UAH)..."
python3 -c "from core.processor import calculate_prices; \
data = [{'name': 'Pixel 7 Pro Case', 'price_usd': 10, 'stock': 5}, {'name': 'Fast Charger 30W', 'price_usd': 15, 'stock': 0}]; \
print('✅ РЕЗУЛЬТАТ ДЛЯ КЛИЕНТА:'); \
print(calculate_prices(data))"
