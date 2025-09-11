# class attribute and object instances in python: 

class Computer:  # create class
    device_name = "" 
    processor = ""
    device_id = "" 
    system_type = ""
    edition = ""

com1 = Computer()  # object for class
com2 = Computer()  # object for class
com3 = Computer()

com1.device_name = "Dell " 
com1.processor = "i7"
com1.device_id = "3C4F" 
com1.system_type = "64 bits Os"
com1.edition = "11 Pro"

com2.device_name = "Dell " 
com2.processor = "i5"
com2.device_id = "224F" 
com2.system_type = "32 bits Os"
com2.edition = "11 "

com3.device_name = "Dell " 
com3.processor = "i3"
com3.device_id = "554F" 
com3.system_type = "64 bits Os"
com3.edition = "10"

print(f"This is first computer details:", {com1.device_name}, {com1.processor}, {com1.device_id}, {com1.system_type}, {com1.edition})

print(f"This is second computer details:", {com2.device_name}, {com2.processor}, {com2.device_id}, {com2.system_type}, {com2.edition})

print(f"This is third computer details:", {com3.device_name}, {com3.processor}, {com3.device_id}, {com3.system_type}, {com3.edition})

