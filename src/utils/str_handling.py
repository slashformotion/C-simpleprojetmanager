def is_one_char_not_a_whitespace(text):
    assert type(text) is str

    for c in text:
        if c!= " ": # if one on the caracter of txt is not a whitespace
            return True
    
    return False

def is_there_space_in_middle_str(text):
    assert type(text) is str

    while text.startswith(" ") or text.endswith(" "):
        if text.startswith(" "):
            text = text[1:]

        if text.endswith(" "):
            text = text[:-1]

    
    for c in text:
        if c == " ":
            return True
    return False

def is_only_whitespaces(text):
    assert type(text) is str

    for c in text:
        if c!= " ": # if one on the caracter of txt is not a whitespace
            return False
    
    return True