class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot build!"


def check_material(material1, limit):
    if material1 >= limit:
        print("Go!")
    else:
        raise BuildingError()


materials = 400
limits = 350
check_material(materials, limits)
