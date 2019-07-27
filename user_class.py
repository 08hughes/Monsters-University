class User:

    def __init__(self, name, age, legs, scare_level):
        self.name = name
        self.age = age
        self.legs = legs
        self.scary_level = scare_level

    def scare(self):
        return "scream"

    def roar(self):
        return "ROARRRRRR"

    def pull_ugly_face(self):
        return "  o0o  o0o   \n" \
               "     00      \n" \
               " wwwwwwwwww "