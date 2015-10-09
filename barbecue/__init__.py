# -*- coding: utf-8 -*-

from fractions import Fraction


def vnmax(features):
    return sum([max([j['value'] for j in i['enum']]) for i in features])


def calculate_coeficient(features, parameters):
    vmax = Fraction(vnmax(features))
    vn = sum([Fraction(i['value']) for i in parameters])
    return 1 + vn / (1 - vmax)


def cooking(price, features=None, parameters=None):
    """
    MEAT price normalization

    features = [
        {
            "code": "OCDS-123454-AIR-INTAKE",
            "description": "\u0415\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u0430 \u043f\u043e\u0442\u0443\u0436\u043d\u0456\u0441\u0442\u044c \u0432\u0441\u043c\u043e\u043a\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u043f\u0438\u043b\u043e\u0441\u043e\u0441\u0430,\u0432 \u0432\u0430\u0442\u0430\u0445 (\u0430\u0435\u0440\u043e\u0432\u0430\u0442\u0430\u0445)",
            "title": "\u041f\u043e\u0442\u0443\u0436\u043d\u0456\u0441\u0442\u044c \u0432\u0441\u043c\u043e\u043a\u0442\u0443\u0432\u0430\u043d\u043d\u044f",
            "enum": [
                {
                    "value": 0.1,
                    "title": "\u0414\u043e 1000 \u0412\u0442"
                },
                {
                    "value": 0.15,
                    "title": "\u0411\u0456\u043b\u044c\u0448\u0435 1000 \u0412\u0442"
                }
            ],
            "title_en": "Air Intake",
            "relatedItem": "123456",
            "featureOf": "item"
        },
        {
            "code": "OCDS-123454-YEARS",
            "description": "\u041a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u0440\u043e\u043a\u0456\u0432, \u044f\u043a\u0456 \u043e\u0440\u0433\u0430\u043d\u0456\u0437\u0430\u0446\u0456\u044f \u0443\u0447\u0430\u0441\u043d\u0438\u043a \u043f\u0440\u0430\u0446\u044e\u0454 \u043d\u0430 \u0440\u0438\u043d\u043a\u0443",
            "title": "\u0420\u043e\u043a\u0456\u0432 \u043d\u0430 \u0440\u0438\u043d\u043a\u0443",
            "enum": [
                {
                    "value": 0.05,
                    "title": "\u0414\u043e 3 \u0440\u043e\u043a\u0456\u0432"
                },
                {
                    "value": 0.1,
                    "title": "\u0412\u0456\u0434 3 \u0434\u043e 5 \u0440\u043e\u043a\u0456\u0432"
                },
                {
                    "value": 0.15,
                    "title": "\u0411\u0456\u043b\u044c\u0448\u0435 5 \u0440\u043e\u043a\u0456\u0432"
                }
            ],
            "title_en": "Years trading",
            "featureOf": "tenderer"
        }
    ]

    parameters = [
        {
            "code": "OCDS-123454-AIR-INTAKE",
            "value": 0.1
        },
        {
            "code": "OCDS-123454-YEARS",
            "value": 0.1
        }
    ]

    coef = 1 + Fraction(1, 5) / (1 - Fraction(3, 10)) = Fraction(9, 7)
    """
    if not features or not parameters:
        return price
    coef = calculate_coeficient(features, parameters)
    return Fraction(price) * coef


def chef(bids, features=None, ignore=[]):
    """
    MEAT bids sorting
    """
    sorted_bids = sorted(bids, key=lambda i: (cooking(i['value']['amount'], features, i['parameters']), i['date']))
    return [i for i in sorted_bids if i['id'] not in ignore]
