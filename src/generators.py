from src.transactions_generators import transactions_first, transactions_first_dollars, transactions_second, \
    transactions_second_dollars
#импортируем словари из отдельного модуля

"""определяем функцию для фильтрации по валюте вместе с типами данных"""
def filter_by_currency(transactions_first: list[dict], currency: str) -> filter:
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions_first)
    #создаем генеративное выражение с помощью filter и временную функцию lambda для того, чтобы отсортировать валюту

usd_transactions = filter_by_currency(transactions_first, "USD")
#создаем генеративное выражение с помощью filter и временную функцию lambda для того, чтобы отсортировать валюту
for _ in range(2):
    print(next(usd_transactions))
#функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
