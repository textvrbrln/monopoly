
    #streetname = streetbase.get_streetname(moveto)
    #base_rent = streetbase.get_base_rent(moveto)
    
    #stop_on_street = streetbase.Street(streetname, base_rent)
    #print(stop_on_street.name)
    #print(stop_on_street.base_rent)

    #print("Feldnummer:", moveto)
    #print("Straße:", streetname)
    #print("Basismiete:", base_rent)


def get_streetname(streetname):
    #badstraße_mieten = 2, 4, 10, 30, 90, 160, 250
    badstraße_kaufen = 60, 50 
    return badstraße_kaufen[streetname]


#def get single_street():
#    street_field    = 1
#    street_name  = 

    def __init__(self, name, base_rent):
        self.name = name
        self.base_rent = base_rent


class Badstraße:
    field = "0"
    field_type = "street"
    name = "Badstraße"
    base_rent = 4

class Turmstraße:
    field = "1"
    field_type = "street"
    name = "Turmstraße"
    base_rent = 6

streetnames = 'Badstraße', 0
strasse = streetnames[0]
strasse = Badstraße()
print(strasse.field)
print(strasse.name)
print(strasse.base_rent)


streetname = streetbase.get_streetname(moveto)
        print(streetname)




def get_streetname(from_dice_number):
    streetnames = 'Badstraße', 0, 'Turmstraße', 0, 0, 'Chausseestraße', 0, 'Elisenstraße', 'Poststraße', 0, 'Seestraße', 0, 0
    return streetnames[from_dice_number]

def get_stationname(from_dice_number):
    stationname = 0, 0, 0, 0, 'Südbahnhof', 0, 0, 0, 0, 0, 0, 0, 'Westbahnhof'
    return stationname[from_dice_number]

def get_base_rent(from_dice_number):
    base_rents = 2, 0, 4, 200, 25, 6, 0, 6, 8, 0, 10, 44, 25
    return base_rents[from_dice_number]