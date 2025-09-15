# __init__ method in python:

class Computer:  # create class

    def __init__(self, device_name, processor, device_id, system_type,edition):
        self.device_name = device_name
        self.procesor = processor
        self.device_id = device_id
        self.system_type = system_type
        self.edition = edition

com1 = Computer("Dell","i7","3C4F","64 bits Os"," 11 Pro" )
com2 = Computer("Dell", "i5", "224F", "32 bits Os", "11"  )
com3 = Computer("Dell","i3","554F","64 bits Os","10")

print(f"This is first computer details:", com1.device_name,com1.procesor, com1.device_id, com1.system_type, com1.edition )

print(f"This is second computer details:", com2.device_name,com2.procesor, com2.device_id, com2.system_type, com2.edition )

print(f"This is third computer details:", com3.device_name,com3.procesor, com3.device_id, com3.system_type, com3.edition )



