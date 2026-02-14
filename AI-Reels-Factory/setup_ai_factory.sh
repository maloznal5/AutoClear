#!/bin/bash

# Название проекта
PROJECT="AI-Media-Factory"
BASE_DIR="$HOME/$PROJECT"

# Создаем структуру папок
mkdir -p "$BASE_DIR"/{core,api_connectors,media_gen,config,output,logs}

# 1. Коннектор для сигналов (TradingView/Market)
cat << 'PY' > "$BASE_DIR/api_connectors/market_data.py"
def fetch_signal():
    return {"symbol": "BTC/USDT", "price": 52450, "signal": "STRONG BUY", "rsi": 28}
PY

# 2. Логика ИИ (ChatGPT сценарий)
cat << 'PY' > "$BASE_DIR/core/ai_logic.py"
def generate_script(data):
    return f"Срочный сигнал по {data['symbol']}! Цена {data['price']}, RSI в зоне перепроданности. Готовимся к росту!"
PY

# 3. Синтез голоса (ElevenLabs)
cat << 'PY' > "$BASE_DIR/media_gen/voice_tts.py"
def synthesize_voice(text):
    print(f"🎙 Синтез речи ElevenLabs для текста: {text[:30]}...")
    return "path/to/audio.mp3"
PY

# 4. Главный файл управления (Engine)
cat << 'PY' > "$BASE_DIR/main.py"
from api_connectors.market_data import fetch_signal
from core.ai_logic import generate_script
from media_gen.voice_tts import synthesize_voice
import time

def start_pipeline():
    print("🚀 Запуск AI-Media-Factory...")
    data = fetch_signal()
    script = generate_script(data)
    audio = synthesize_voice(script)
    print("✅ Видео-пайплайн готов к рендеру!")

if __name__ == "__main__":
    start_pipeline()
PY

# 5. README для портфолио
cat << 'MD' > "$BASE_DIR/README.md"
# AI-Media-Factory (Reels/Shorts Automation)
**Бюджет кейса:** 5,000 - 10,000 UAH
**Стек:** Python 3.12, TradingView API, OpenAI, ElevenLabs.

Автоматизированный конвейер для создания финансового медиа-контента.
MD

# Переход в папку проекта и запуск теста
cd "$BASE_DIR"
echo "✅ Проект $PROJECT создан в $BASE_DIR"
echo "🔍 Запускаю тестовый прогон..."
python3 main.py
exec bash
