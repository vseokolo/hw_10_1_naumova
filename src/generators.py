from black import Iterator

from src.transactions_generators import transactions, transactions_dollars
#импортируем словари из отдельного модуля

def filter_by_currency(transactions: list[dict], currency: str) -> filter:
    """определяем функцию для фильтрации по валюте вместе с типами данных"""
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    #создаем генеративное выражение с помощью filter и временную функцию lambda для того, чтобы отсортировать валюту

usd_transactions = filter_by_currency(transactions, "USD")
#создаем генеративное выражение с помощью filter и временную функцию lambda для того, чтобы отсортировать валюту
for _ in range(2):
    print(next(usd_transactions))
#функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной



def transaction_descriptions(transactions: list[dict]):
    """определяем функцию для возврата описания каждой операции в списке"""
    for t in transactions:
        yield t["description"]
#yield возвращает требуемый генератор

descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))
#функция возвращает описание каждой операции в списке


def card_number_generator(start, stop) -> Iterator[str]:
    """определяем функцию для генератора случайного номера карты"""
    for number in range(start, stop + 1):
        # Форматируем длину номера карты
        card_number = f"{number:016d}"
        formatted_card_number = " ".join(
            [card_number[i:i + 4] for i in range(0, 16, 4)]
        )
        yield formatted_card_number