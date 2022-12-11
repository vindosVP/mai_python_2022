def look_for_drones(input_vendor, drone_list):
    
    respond = []

    for drone in drone_list:
        vendor = drone.split()[0]
        vendor_upper = vendor.upper()
        if input_vendor == vendor_upper:
            respond.append(f"{drone[len(vendor) + 1:]}")

    return(respond)

def upcase_drones(drone_list):

    up_list = []

    for drone in drone_list:
        up_list.append(drone.upper())
    
    return up_list

def vendors(upcased_list):

    vendor_list = []

    for drone in upcased_list:
        vendor_list.append(drone.split()[0])

    return vendor_list

def count_drones(vendor_list, upcased_list):

    dict = {}

    for vendor in vendor_list:
        count = 0
        for drone in upcased_list:
            if drone.split()[0] == vendor:
                count += 1
        dict[vendor] = count
    
    return dict

def count_vendor_drones(drone_list):

    upcased_list = upcase_drones(drone_list)
    vendor_list = vendors(upcased_list)

    dict = count_drones(vendor_list, upcased_list)

    items = dict.items()
    for item in items:
        print(f"{correct(item[0])} : {item[1]}")

def need_register(drone_list, drone_weight_list):

    reg_list = []

    count = 0

    for drone, weight in zip(drone_list,  drone_weight_list):
        if weight > 150:
            reg_list.append(drone)
            count += 1
    
    return count, sorted(reg_list)

def no_need_register(drone_list, drone_weight_list):

    no_reg_list = []
    no_count = 0

    for drone, weight in zip(drone_list,  drone_weight_list):
        if not weight > 150:
            no_reg_list.append(drone)
            no_count += 1
    
    return no_count, sorted(no_reg_list)

def correct(drone):

    if drone.split()[0].upper() == "DJI":
        return f"DJI {drone[3:len(drone)]}"
    elif drone.split()[0].upper() == "AUTEL":    
        return f"Autel {drone[5:len(drone)]}"
    elif drone.split()[0].upper() == "PARROT":
        return f"Parrot {drone[6:len(drone)]}"
    elif drone.split()[0].upper() == "RYZE":
        return f"Ryze {drone[4:len(drone)]}"
    elif drone.split()[0].upper() == "EACHINE":
        return f"Eachine {drone[7:len(drone)]}"

def check_need_register(drone_list, drone_weight_list, height, np, no_closed_zone, in_wision):
    
    for drone, weight in zip(drone_list,  drone_weight_list):
        if (height > 150) or (np and weight > 150) or (not no_closed_zone) or (not in_wision):
            print(f"{drone} с весом {weight} нужно регистрировать при таких условиях")
        else: 
            print(f"{drone} с весом {weight} не нужно регистрировать при таких условиях") 


if __name__ == "__main__":

    drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", 
    "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", 
    "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", 
    "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", 
    "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

    drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

    input_vendor = input("\nВведите назавние производителя:\n").upper()
    print("\nTODO1/5\n")
    found_list = look_for_drones(input_vendor, drone_list)
    if len(found_list) > 0:
        str = found_list[0]
        for i in range(1,len(found_list)):
            str = str + f", {found_list[i]}"
        str = str + "."
        print(str)
    else:
        print("Ничего не найдено")

    print("\nTODO2\n")

    count_vendor_drones(drone_list)

    print("\nTODO3\n")

    reg_count, need_register_list = need_register(drone_list, drone_weight_list)
    print(f"Нужно регистрировать {reg_count} :")
    for drone in need_register_list:
        print(correct(drone))

    print("\n")

    no_reg_count, no_need_register_list = no_need_register(drone_list, drone_weight_list)
    print(f"Не нужно регистрировать {no_reg_count} :")
    for drone in no_need_register_list:
        print(correct(drone))

    print("\nTODO4\n")

    height = 100
    np = True
    no_closed_zone = True
    in_wision = True

    check_need_register(drone_list, drone_weight_list, height, np, no_closed_zone, in_wision)

    print("\n")
    