# Використовуємо офіційний легкий образ Python
FROM python:3.12-slim

# Встановлюємо робочу папку всередині віртуального контейнера
WORKDIR /app

# Копіюємо наш список бібліотек і встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь наш код у контейнер
COPY . .

# Відкриваємо порт для доступу
EXPOSE 8000