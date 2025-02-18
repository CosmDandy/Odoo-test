# Odoo-test
## Описание проекта  
Этот модуль реализует новую модель `test.model` и промежуточную модель `test.model.line`, которая имитирует связь "многие ко многим" в Odoo. Также  модуль предоставляет интерфейс для работы с ними.  

---

## Установка  
```bash
git clone https://github.com/CosmDandy/Odoo-test.git
```

---

## Файловая структура
```
Odoo-test/
│── config/                  # Конфигурационные файлы
│── extra-addons/            # Дополнительные модули
│   └── test_module/         # Основной модуль
│       ├── __init__.py      # Инициализация модуля
│       ├── __manifest__.py  # Описание модуля
│       ├── models/          # Бизнес-логика
│       │   ├── __init__.py
│       │   ├── test_model.py
│       │   ├── test_model_line.py
│       ├── views/           # Представления (интерфейс)
│       │   ├── test_model_views.xml
│       │   ├── test_model_wizard_views.xml
│       │   ├── test_model_menu.xml
│       ├── security/        # Права доступа
│       │   ├── ir.model.access.csv
│       ├── wizard/          # Вспомогательные мастера
|       │   ├── test_model_wizard.py
│── doc/                     # Документация
│── docker-compose.yml       # Конфигурация Docker
│── .gitignore               # Игнорируемые файлы Git
│── README.md                
```

---

## Запуск
```bash
cd Odoo-test
docker-compose up -d
```

---

## Используемые технологии
- Odoo 16+
- Python 3.x
- PostgreSQL

---

## Лицензия
- Этот проект распространяется под лицензией LGPL-3.
