CONST_NUM_COLUMNS = ['бин', 'окэд', 'окпо']
CONST_STRING_COLUMNS = ['юридический адрес', 'руководитель']
CONST_DATE_COLUMNS = ['образовано', ]

reverse_dictionary = {'бин': 'bin',
                      'окэд': 'oked',
                      'окпо': 'okpo',
                      'юридический адрес': 'address',
                      'руководитель': 'owner',
                      'образовано': 'created'}

bins = {'altyn': '980740000057',
        'atf': '951140000151',
        'asia-credict': '920140000508',
        'alpha': '941240000341',
        'bck': '980640000093',
        'rbk': '920440001102',
        'china-bank': '930440000156',
        'kzi': '930140000323',
        'halyk': '940140000385',
        'vtb': '080940010300',
        }


def dict_filler(reg_exp, columns, row):
    """

    :param reg_exp:
    :param columns:
    :param row:
    :return:
    """
    import re
    buffer_dictionary = dict()
    for col in columns:
        p = re.compile(f'{col}{reg_exp}', re.IGNORECASE)
        m = p.search(row)
        val = m.group(1) if m else None
        buffer_dictionary[reverse_dictionary[col]] = val
    return buffer_dictionary


def parse_string(row):
    """

    :param row:
    :return:
    """
    from datetime import datetime

    result_dict = dict()
    nums_dict = dict_filler(reg_exp=':\n([0-9]+)\n', columns=CONST_NUM_COLUMNS, row=row)
    string_dict = dict_filler(reg_exp=':\n(.*)\n', columns=CONST_STRING_COLUMNS, row=row)
    date_dict = dict_filler(reg_exp=':\n(\d+.\d+.\d+)\n', columns=CONST_DATE_COLUMNS, row=row)
    # refill result dict
    for d in [nums_dict, string_dict, date_dict]:
        result_dict.update(d)
    result_dict['created'] = datetime.strptime(result_dict['created'], "%d.%m.%Y").strftime("%Y-%m-%d")
    return result_dict
