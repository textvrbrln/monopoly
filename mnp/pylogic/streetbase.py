def get_field_type(from_dice_number):
    fieldtypes = 'street', 'community', 'street', 'taxes', 'station', 'street', 'event', 'street', 'street', 'visiting', 'street', 'plant', 'station'
    return fieldtypes[from_dice_number]

class Street:
    allstreets = 'Badstraße', 0, 'Turmstraße', 0, 0, 'Chausseestraße', 0, 'Elisenstraße', 'Poststraße', 0, 'Seestraße', 0, 0
    allrents = 2, 0, 4, 0, 0, 6, 0, 6, 8, 0, 10, 0, 0

class Station:
    allstations = 0, 0, 0, 0, 'Südbahnhof', 0, 0, 0, 0, 0, 0, 0, 'Westbahnhof'

class Plant:
    pass

class Community:
    pass

class Event:
    pass

class Go:
    pass

class Taxes:
    pass

class Jail:
    pass
