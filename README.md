# CurrencyConversionAPI

CurrencyConversionAPI - это веб-сервис, предоставляющий несколько полезных функций, связанных с конвертацией валют и управлением актуальными курсами валют. Данный API позволяет вам легко выполнять следующие операции:

- **Конвертация Валют:** Производить конвертацию между различными валютами на основе актуальных курсов обмена.

- **Обновление Курсов Валют:** Автоматически обновлять курсы валют с внешних источников, чтобы всегда иметь доступ к актуальной информации.

- **Время Последнего Обновления:** Получать информацию о времени последнего обновления курсов валют, чтобы всегда знать, насколько актуальная ваша информация.

## Содержание

1. [Установка](#установка)
2. [Запуск](#запуск)
3. [Примеры использования API](#примеры-использования)

## Установка

Чтобы установить проект, его нужно склонировать себе на компьютер, прописав в терминале команду ниже.
```bash
git clone https://github.com/vtecovsky/CurrencyConversionAPI
```

## Запуск

Для запуска проекта с использованием Docker Compose, находясь в директории проекта, необходимо прописать в терминале следующую команду:   
```bash
docker-compose up -d
```

Проект будет запущен и доступен по адресу 127.0.0.1:8000 .

## Примеры использования

Всего реализовано 3 эндпоинта:

POST /api/v1/currency/exchange_rates - актуализирует данные в базе данных
    
    Например, http://127.0.0.1:8000/api/v1/currency/exchange_rates

GET /api/v1/currency/last_update - возвращает время последнего изменения курса валют в базе данных

    Например, http://127.0.0.1:8000/api/v1/currency/last_update

GET /api/v1/currency/convert - производит конвертацию валют 

    ? from_currency = USD, AUD, CAD, RUB, MXN...
  
    & target_currency = USD, AUD, CAD, RUB, MXN...
  
    & amount = any non-negative float number

    Например, http://127.0.0.1:8000/api/v1/currency/convert?from_currency=USD&target_currency=RUB&amount=1000

Вы можете протестировать API по адресу 127.0.0.1:8000/docs

