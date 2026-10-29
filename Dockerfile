# Используем официальный легкий образ Python
FROM python:3.11-slim

# Рабочая директория
WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Открываем порт
EXPOSE 3000

# Команда запуска через Gunicorn или встроенный сервер Flask
CMD ["python", "app.py"]
