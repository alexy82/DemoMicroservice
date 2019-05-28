# coding=utf-8
"""
Utility helpers for text, string
"""
import re

TCVN3TAB = [
    "µ", "¸", "¢", "·", "Ì", "Ð", "£", "×", "Ý", "ß",
    "ã", "¤", "â", "ï", "ó", "ý", "µ", "¸", "©", "·",
    "Ì", "Ð", "ª", "×", "Ý", "ß", "ã", "«", "â", "ï",
    "ó", "ý", "¡", "¨", "§", "®", "Ü", "Ü", "ò", "ò",
    "¥", "¬", "¦", "­", "¹", "¹", "¶", "¶", "Ê", "Ê",
    "Ç", "Ç", "È", "È", "É", "É", "Ë", "Ë", "¾", "¾",
    "»", "»", "¼", "¼", "½", "½", "Æ", "Æ", "Ñ", "Ñ",
    "Î", "Î", "Ï", "Ï", "Õ", "Õ", "Ò", "Ò", "Ó", "Ó",
    "Ô", "Ô", "Ö", "Ö", "Ø", "Ø", "Þ", "Þ", "ä", "ä",
    "á", "á", "è", "è", "å", "å", "æ", "æ", "ç", "ç",
    "é", "é", "í", "í", "ê", "ê", "ë", "ë", "ì", "ë",
    "î", "î", "ô", "ô", "ñ", "ñ", "ø", "ø", "õ", "õ",
    "ö", "ö", "÷", "÷", "ù", "ù", "ú", "ú", "þ", "þ",
    "û", "û", "ü", "ü"
]

UNICODETAB = [
    "À", "Á", "Â", "Ã", "È", "É", "Ê", "Ì", "Í", "Ò",
    "Ó", "Ô", "Õ", "Ù", "Ú", "Ý", "à", "á", "â", "ã",
    "è", "é", "ê", "ì", "í", "ò", "ó", "ô", "õ", "ù",
    "ú", "ý", "Ă", "ă", "Đ", "đ", "Ĩ", "ĩ", "Ũ", "ũ",
    "Ơ", "ơ", "Ư", "ư", "Ạ", "ạ", "Ả", "ả", "Ấ", "ấ",
    "Ầ", "ầ", "Ẩ", "ẩ", "Ẫ", "ẫ", "Ậ", "ậ", "Ắ", "ắ",
    "Ằ", "ằ", "Ẳ", "ẳ", "Ẵ", "ẵ", "Ặ", "ặ", "Ẹ", "ẹ",
    "Ẻ", "ẻ", "Ẽ", "ẽ", "Ế", "ế", "Ề", "ề", "Ể", "ể",
    "Ễ", "ễ", "Ệ", "ệ", "Ỉ", "ỉ", "Ị", "ị", "Ọ", "ọ",
    "Ỏ", "ỏ", "Ố", "ố", "Ồ", "ồ", "Ổ", "ổ", "Ỗ", "ỗ",
    "Ộ", "ộ", "Ớ", "ớ", "Ờ", "ờ", "Ở", "ở", "Ỡ", "ỡ",
    "Ợ", "ợ", "Ụ", "ụ", "Ủ", "ủ", "Ứ", "ứ", "Ừ", "ừ",
    "Ử", "ử", "Ữ", "ữ", "Ự", "ự", "Ỳ", "ỳ", "Ỵ", "ỵ",
    "Ỷ", "ỷ", "Ỹ", "ỹ"
]

TCVN3_PATTERN = re.compile("|".join(TCVN3TAB))
UNICODE_PATTERN = re.compile("|".join(UNICODETAB))

TCVN3_REPLACES_DICT = dict(zip(TCVN3TAB, UNICODETAB))
UNICODE_REPLACES_DICT = dict(zip(UNICODETAB, TCVN3TAB))


def tcvn3_to_unicode(tcvn3str: str, default='', encoding=None) -> str:
    """
    Convert TCVN3 to Unicode
    :param tcvn3str: source string
    :param default: default value if fail
    :return: result string
    """
    try:
        result = TCVN3_PATTERN.sub(lambda m: TCVN3_REPLACES_DICT[m.group(0)], tcvn3str)
    except:
        result = default

    if encoding is not None and isinstance(encoding, str):
        return result.encode(encoding=encoding, errors='ignore')
    return result


def unicode_to_tcvn3(unicodestr: str, default='', encoding=None) -> str:
    """
    Convert Unicode string into TCVN3 string
    :param unicodestr: source string
    :param default: default value if fail
    :return: result string
    """
    try:
        result = UNICODE_PATTERN.sub(lambda m: UNICODE_REPLACES_DICT[m.group(0)], unicodestr)
    except:
        result = default

    if encoding is not None and isinstance(encoding, str):
        return result.encode(encoding=encoding, errors='ignore')
    return result


if __name__ == '__main__':
    print(unicode_to_tcvn3('VŨ (unicode tổ hợp)'))
    print(tcvn3_to_unicode(unicode_to_tcvn3('VŨ (unicode tổ hợp)')))
