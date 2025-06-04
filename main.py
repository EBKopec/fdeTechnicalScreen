import csv
import re

import pandas as pd

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
    # packages = [
    #     Package(stack="Package 01", width=200, height=150, length=10, mass=30),
    #     Package(stack="Package 02", width=10, height=10, length=10, mass=10),
    #     Package(stack="Package 03", width=10, height=110, length=20, mass=200),
    # ]

    data = cleanup("./packages.csv")
    df = pd.DataFrame(data, columns=['width', 'height', 'length', 'mass'])
    df['pack'] = None
    df['volume'] = None

    for idx, row in df.iterrows():
        pack = Package(
            stack="package",
            width=row.iloc[0],
            height=row.iloc[1],
            length=row.iloc[2],
            mass=row.iloc[3])

        df.at[idx, 'pack'] = pack.sort()
        df.at[idx, 'volume'] = row.iloc[0] * row.iloc[1] * row.iloc[2]

    df_stats = pd.DataFrame(df, columns=['pack', 'mass', 'volume'])

    df_stats['Count'] = df_stats.groupby('pack')['pack'].transform('count')
    df_stats['Min_Mass'] = df_stats.groupby('pack')['mass'].transform('min')
    df_stats['Max_Mass'] = df_stats.groupby('pack')['mass'].transform('max')
    df_stats['Mean_Mass'] = df_stats.groupby('pack')['mass'].transform('mean')

    df_stats['Min_volume'] = df_stats.groupby('pack')['volume'].transform('min')
    df_stats['Max_volume'] = df_stats.groupby('pack')['volume'].transform('max')
    df_stats['Mean_volume'] = df_stats.groupby('pack')['volume'].transform('mean')

    df_stats.drop(columns=['mass', 'volume'], inplace=True)
    df_stats = df_stats.drop_duplicates()
    print(df)
    print(df_stats)


if __name__ == "__main__":
    main()

