VOL = 1000000
DIMENSION = 150
KILO = 20


class Package:
    def __init__(self, stack, width, height, length, mass):
        self.stack = stack
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    def __repr__(self):
        return (f"Package(stack={self.stack!r}, width={self.width}, "
                f"height={self.height}, length={self.length}, "
                f"mass={self.mass})")

    def is_bulky(self):
        return ((self.width * self.height * self.length) >= VOL or (self.width >= DIMENSION) or
                (self.height >= DIMENSION) or (self.length >= DIMENSION))

    def is_heavy(self):
        return self.mass >= KILO

    def rejected(self) -> bool:
        return self.is_bulky() and self.is_heavy()

    def special(self) -> bool:
        return self.is_bulky() or self.is_heavy()

    def standard(self) -> bool:
        return not (self.is_bulky() or self.is_heavy())

    def sort(self) -> str:
        if self.rejected():
            return "REJECTED"
        elif self.special():
            return "SPECIAL"
        else:
            return "STANDARD"


def main():
    packages = [
        Package(stack="Package 01", width=200, height=150, length=10, mass=30),
        Package(stack="Package 02", width=10, height=10, length=10, mass=10),
        Package(stack="Package 03", width=10, height=110, length=20, mass=200),
    ]
    for package in packages:
        print(f"Stack:{package.stack} -> {package.sort()} \n{package}\n")


if __name__ == "__main__":
    main()

