#!/bin/bash

set -e

echo "🚀 Starting Clinic Management System..."

# Копирование конфигурации
cp .env.example .env

# Запуск сервисов
docker compose up -d --build

# Ожидание готовности
echo "⏳ Waiting for services..."
timeout 45s bash -c 'until curl -s http://localhost:8000/health > /dev/null; do sleep 2; done'

echo "✅ System is ready!"
echo "🌐 Health check: curl http://localhost:8000/health"
