
def filter_alnum(alnum_text: str):
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
        if (character == '-') and ('-' not in filtered_alnum):
            filtered_alnum += character

        if not character.isalpha() and character.isalnum():
            filtered_alnum += character

    if len(filtered_alnum) == 1:
        if filtered_alnum == '-':
            return None

    return filtered_alnum
