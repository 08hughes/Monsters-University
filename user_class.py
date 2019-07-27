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
        return "o0 0o" \
               " www "