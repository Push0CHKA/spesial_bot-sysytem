def for_loading_data(col_count):
    load = '('
    for i in range(col_count - 1):
        load += '?,'
    load += '?)'
    return load
