def char_regex(pattern, char):
    if pattern == "":
        return True
    elif pattern == ".":
        return len(char) == 1
    else:
        return char == pattern


def string_regex(regex, text):
    if regex == "":
        return True
    elif len(regex) > len(text):
        return False
    elif not char_regex(regex[0], text[0]):
        return False
    else:
        return string_regex(regex[1:], text[1:])


def partial_regex(regex, text):
    for i in range(len(text) - len(regex) + 1):
        if string_regex(regex, text[i:]):
            return True
    return False


def extended_regex(regex, text, offset=0):
    char_offset = regex.find("?", offset)
    if char_offset >= 0:
        return extended_regex_optional(regex, text, char_offset)

    char_offset = regex.find("*", offset)
    if char_offset >= 0:
        return extended_regex_zero_or_more(regex, text, char_offset)

    char_offset = regex.find("+", offset)
    if char_offset >= 0:
        return extended_regex_one_or_more(regex, text, char_offset)

    if regex[:1] == "^":
        return extended_regex(regex[1:], text[:len(decode_metacharacters(regex)) - 1], offset - 1)
    elif regex[-1:] == "$":
        return extended_regex(regex[:-1], text[-len(decode_metacharacters(regex)) + 1:], offset)
    else:
        return partial_regex(decode_metacharacters(regex), text)


def decode_metacharacters(regex):
    return regex \
        .replace("\\\\", "\\") \
        .replace("\\.", ".") \
        .replace("\\?", "?") \
        .replace("\\*", "*") \
        .replace("\\+", "+") \
        .replace("\\^", "^") \
        .replace("\\$", "$")


def extended_regex_optional(regex, text, offset):
    pos, end = metacharacter_positions(regex, "?", start=offset)
    if regex[pos - 2] == "\\":
        return extended_regex(regex, text, pos)
    else:
        return extended_regex(regex[:end] + regex[pos:], text, pos) or \
               extended_regex(regex[:end + 1] + regex[pos:], text, pos)


def extended_regex_zero_or_more(regex, text, offset):
    pos, end = metacharacter_positions(regex, "*", start=offset)
    if regex[pos - 2] == "\\":
        return extended_regex(regex, text, pos)
    elif extended_regex(regex[:end] + regex[pos:], text, pos):
        return True
    elif len(decode_metacharacters(regex)) - 4 < len(text):
        return extended_regex(regex[:end + 1] + regex[pos - 2:], text, pos)
    else:
        return False


def extended_regex_one_or_more(regex, text, offset):
    pos, end = metacharacter_positions(regex, "+", start=offset, delta=1)
    if regex[pos - 2] == "\\":
        return extended_regex(regex, text, pos)
    elif extended_regex(regex[:end] + regex[pos:], text, pos):
        return True
    elif len(decode_metacharacters(regex)) - 3 < len(text):
        return extended_regex(regex[:end] + regex[pos - 2:], text, pos)
    else:
        return False


def metacharacter_positions(regex, char, start=0, delta=2):
    pos = regex.find(char, start) + 1
    return pos, pos - delta


if __name__ == "__main__":
    print(extended_regex(*input().split("|")))
