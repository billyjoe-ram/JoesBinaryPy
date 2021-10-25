def filter_alnum(alnum_text):
    """
    Receives an alphanumeric string and returns its only
    numbers, without regex

    :param alnum_text:
    :type alnum_text: str
    :return: filtered_alnum
    :rtype: str
    """
    filtered_alnum = ""
    for character in str(alnum_text):
        if check_allowed_chars(character):
            if character not in filtered_alnum:
                filtered_alnum += character

    if check_no_number_numeric(filtered_alnum):
        return None
    return filtered_alnum


def check_allowed_chars(character):
    """
    :param character:
    :type character: str
    :return: allow_char
    :rtype: bool
    """
    allow_char = True
    allowed_chars = ('-', '.')
    if character.isalpha() and not character.isnumeric():
        if character not in allowed_chars:
            allow_char = False

    return allow_char


def check_no_number_numeric(alnum_text):
    """
    Checks if, for the string, if
    :param alnum_text:
    :type alnum_text: str
    :return: no_number_numeric
    :rtype: bool
    """
    no_number_numeric = False
    if len(alnum_text) == 1 and not alnum_text.isalnum():
        no_number_numeric = True

    return no_number_numeric
