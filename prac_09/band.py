
class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        output = []
        for musician in self.musicians:
            if not musician.instruments:
                output.append(f"{musician.name} needs an instrument!")
            else:
                output.append(f"{musician.name} is playing: {musician.instruments[0]}")
        return '\n'.join(output)

