if __name__ == '__main__':
    NameToAge: dict = {
        "Philipe": 12,
        "Alex": 33,
        "Leonidas": 35,
        "Achilles": 26
    }

    minimumSalary: float = 12.35
    NameToSalary: dict = {name: minimumSalary for name in NameToAge.keys()}

    Augmentation_ratio: float = 0.1

    NameToSalary["Leonidas"] = NameToSalary.get("Leonidas") \
                               + NameToSalary.get("Leonidas") * Augmentation_ratio

    print(NameToSalary)
