def boolean_parser(data):
    data = data.strip()  
    if data.startswith("true"):
        return [True, data[4:].strip()]
    elif data.startswith("false"):
        return [False, data[5:].strip()]
    else:
        return None
    

def null_parser(data):
    data = data.strip()  
    if data.startswith("null"):
        return [None, data[4:].strip()]
    else:
        return None
    
    
def number_parser(data):
    regex_find = re.match(r"^\s*(-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)", data)
    if regex_find is None:
        return None
    matched_str = regex_find.group(1)
    pos = len(matched_str)
    try:
        return [int(matched_str), data[pos:].lstrip()]
    except ValueError:
        return [float(matched_str), data[pos:].lstrip()]
    
    
def string_parser(data):
    if data[0] == '"':
        data = data[1:]
        pos = data.find('"')
        while pos > 0 and data[pos - 1] == '\\':
            pos = data.find('"', pos + 1)
        return [data[:pos], data[pos + 1:].strip()]        
