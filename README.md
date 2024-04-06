[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/fyEiQoo6)
## SOAP
Формат(протокол) передачи сообщений в распределенной сети. **Не является архитектурным стилем**

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
     <getProductDetails xmlns="http://warehouse.example.com/ws">
       <productID>12345</productID>
     </getProductDetails>
   </soap:Body>
</soap:Envelope>
```

<details>
<summary><h4>Спойлер</h4></summary>

* Из-за повсеместного распространения JSON, стал неактуальным.
* Очень тяжело читается людьми - одна из возможных причин угасания.
</details>


## GraphQL
**GraphQL** — язык запросов к API и одновременно движок с открытым исходным кодом. Был разработан в Facebook для упрощения управления API на основе REST.

Репозиторий: https://github.com/graphql

Спецификация: https://github.com/graphql/graphql-spec/tree/main/spec

## ДЗ 
<details>
<summary><h4></h4></summary>

(До)реализовать апи на основе GraphQL:
* Реализовать адаптер для работы с Cart(3)
* (До)реализовать адаптер для работы с Product(2)
* Реализовать методы:
  * Создание корзины _create_cart_(1)
  * Получения корзины _cart_(1)
  * Добавления товара в корзину _add_to_cart_(1)
  * Изменение имени и цены продукта _update_product_info_(2)

#### Рекомендации
* Python 3.9
* Придерживаться правил чистой архитектуры
* Логирование
* Основным фреймворком считать Strawberry
* Работа с зависимостями через poetry
</details>