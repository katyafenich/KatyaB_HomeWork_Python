# KatyaB_HomeWork_Python

# Проект автоматизации тестирования с Allure
Проект автоматизированного тестирования веб-приложений с использованием:
- **Python** и **pytest** для написания тестов
- **Selenium WebDriver** для автоматизации браузера
- **Page Object Pattern** для структурирования кода
- **Allure Framework** для генерации отчетов

### Форматирование кода

- Код форматируется в соответствии с PEP 8 (стиль написания кода на Python).
- Используются docstrings для документирования методов и функций.
- Все шаги теста размечаются с помощью `@allure.step` или `with allure.step` для улучшения читаемости отчетов.

### 3. Установите Allure Commandline

#### Для Windows (с помощью Scoop):
```powershell
# Установите Scoop
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Установите Allure
scoop install allure
```

## Инструкция по запуску тестов для формирования отчета Allure

1. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Запустите тесты с генерацией отчета Allure:
   ```bash
   pytest --alluredir=./allure-result
   ```

   Эта команда запустит все тесты и сохранит результаты в директорию `./allure-result`.

В отчете Allure вы увидите:
   - **Название тестов**
   - **Описание тестоов**
   - **Шаги тестов**:
   - **Результаты**