def data_raw():
    data = {
        'unit,sex,age,geo\time': ['YR,F,Y1,AL','YR,F,Y1,AL','YR,F,Y1,PT'],
        '2021': ['79.4','79.6','79.6'],
        '2022': ['79.4','79.6','79.6'],
        '2023': ['83.2 ','79.6','79.6']
    }
    return data

def data_expect():
    data = {
        'unit': ['YR','YR','YR'],
        'sex': ['F','F','F'],
        'age': ['Y1','Y1','Y1'],
        'region': ['PT','PT','PT'],
        'year': [2021,2022,2023],
        'value': [79.6,79.6,79.6]
    }
    return data