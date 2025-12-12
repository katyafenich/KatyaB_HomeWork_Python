from smartphone import Smartphone


catalog = [Smartphone("samsung", "S25", "+79117877845"),
           Smartphone("IPhone", "17", "+79117887844"),
           Smartphone("ONEPLUS", "13", "+79527787854"),
           Smartphone("Realme", "GT7", "+79525587854"),
           Smartphone("Xiaomi", "14T", "+79534587824")
           ]


for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.number}")
