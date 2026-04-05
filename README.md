# 🩺 DevEnv Doctor

[![CI](https://github.com/YOUR_GITHUB_USER/devdoctor/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_GITHUB_USER/devdoctor/actions)
[![PyPI version](https://img.shields.io/pypi/v/devdoctor.svg)](https://pypi.org/project/devdoctor/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**DevEnv Doctor** — это профессиональный CLI-инструмент для автоматической диагностики и настройки окружения разработчика. Он проверяет инструменты, порты, переменные окружения и помогает исправить проблемы одной командой.

## 🚀 Быстрый старт

1. **Установка**:
   ```bash
   pip install devdoctor
   # или с поддержкой AI советов
   pip install "devdoctor[ai]"
   ```

2. **Инициализация**:
   ```bash
   devdoctor init
   ```

3. **Запуск диагностики**:
   ```bash
   devdoctor check
   ```

4. **Авто-исправление**:
   ```bash
   devdoctor check --fix
   ```

## 🛠 Возможности

- **Проверка инструментов**: Наличие и версии Git, Python, Docker, Node.js и др.
- **Свободные порты**: Поиск процессов, занимающих порты (PostgreSQL, Redis, и т.д.).
- **Дисковое пространство**: Контроль свободного места и наличия необходимых папок.
- **Environment**: Проверка `.env` файлов и обязательных переменных.
- **Custom Checks**: Возможность добавлять свои проверки прямо в YAML.
- **AI Advisor**: Получение советов по исправлению ошибок через GPT-4.

## ⚙️ Конфигурация (.devdoctor.yaml)

```yaml
tools:
  - name: git
    min_version: "2.30.0"

ports:
  - number: 5432
    description: "PostgreSQL"

env_files: [".env"]
required_env_vars: ["DATABASE_URL", "SECRET_KEY"]

custom_checks:
  - name: "Check Redis"
    command: "redis-cli ping"
    expected_output_contains: "PONG"
```

## 👨‍💻 Разработка

Инструкции по развертыванию и тестированию находятся в [CONTRIBUTING.md](docs/development.md).

---
**Автор**: [YOUR_NAME](https://github.com/YOUR_GITHUB_USER)  
**Лицензия**: MIT

## Установка

```bash
poetry install
```

## Использование

```bash
# Инициализация конфига
poetry run devdoctor init

# Проверка окружения
poetry run devdoctor check

# Попытка исправления (MVP: заглушка)
poetry run devdoctor check --fix
```
