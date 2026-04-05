# 🩺 DevEnv Doctor

Professional CLI tool for developer environment diagnostics and auto-fixing.

**DevEnv Doctor** — это профессиональный CLI-инструмент для автоматической диагностики и настройки окружения разработчика. Он проверяет инструменты, порты, переменные окружения и помогает исправить проблемы одной командой.

---

**Разработчик**: [Стариков А.В.](https://github.com/AttackBeaver) — преподаватель БПОУ ОО "СПК"  
**GitHub**: [AttackBeaver/devdoctor](https://github.com/AttackBeaver/devdoctor)  
**PyPI**: [pypi.org/project/devdoctor](https://pypi.org/project/devdoctor/)

## 🚀 Быстрый старт

```bash
# Установка
pip install devdoctor

# Инициализация
devdoctor init

# Запуск диагностики
devdoctor check
```

## 🛠 Основные возможности

- **Проверка инструментов**: Наличие и версии Git, Python, Docker, Node.js и др.
- **Свободные порты**: Поиск процессов, занимающих порты.
- **Дисковое пространство**: Контроль свободного места.
- **Environment**: Проверка `.env` файлов и обязательных переменных.
- **Custom Checks**: Возможность добавлять свои проверки прямо в YAML.
- **AI Advisor**: Получение советов по исправлению ошибок через GPT-4.
