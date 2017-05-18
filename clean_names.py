# version 1 -- invalid

def namelist(names):
    clean_names = []
    for name in names:
        clean_names.append(name['name'])
    out_str = ', '.join(clean_names[0:len(clean_names) - 1])
    return out_str + ' & ' + clean_names[-1]



# version 2 -- valid
def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    clean_names = []
    for name in names:
        clean_names.append(name['name'])
    out_str = ', '.join(clean_names[0:len(clean_names)-1])
    return out_str + ' & ' + clean_names[-1]
