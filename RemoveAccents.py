import fmeobjects
import unicodedata as ud

def rmdiacritics(char):
    '''
    Return the base character of char, by "removing" any
    diacritics like accents, curls, strokes, etc.
    
    Examples
    Before:     name = `François', state = 'Tørst', type = `Salé'
    After:      name = `Francois', state = `Torst', type = `Sale'
    '''
    desc = ud.name(unicode(char))
    cutoff = desc.find(' WITH ')
    if cutoff != -1:
        desc = desc[:cutoff]
    return ud.lookup(desc)
    
def removeAccents(feature):
    attribute_list = ("name", "type", "state") # Modify as needed, case-sensitive
    for attrib in attribute_list:
        value = feature.getAttribute(attrib)
        if value:
            value = unicode(value)
            new_value = ''.join([rmdiacritics(char) for char in value])
            feature.setAttribute(attrib, new_value)