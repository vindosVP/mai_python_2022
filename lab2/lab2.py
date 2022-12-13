import json

class Aircraft:
    def __init__(self, weight):
        self._weight = weight

class UAV:

    # TODO 3-1
    def __init__(self):
        self._has_autopilot = True
        self._missions = []

    # TODO 3-2
    @property
    def missions(self):
        return self._missions 

    @missions.setter
    def missions(self, mission):
        self._missions.append(mission)

    # TODO 3-3
    def missions_count(self):
        count = len(self.missions)
        return count         

class MultirotorUAV(Aircraft, UAV):

    def __init__(self, weight, model, brand):
        super().__init__(weight)
        UAV.__init__(self)
        self.__weight = weight
        self.__brand = brand
        self.__model = model

    def get_info(self):
        return f"масса {self.__weight}, производитель {self.__brand}, количество миссий {self.missions_count()}"

    def get_model(self):
        return self.__model


def read_json(filename):

    with open(filename) as json_file:
        data = json.load(json_file)
    
    return data


def missions_by_pilot(pilot, data):
    return data[pilot]["missions"]


def missions_by_pilots(data):
    missions_count_by_pilots = {}
    for pilot in data.keys():
        missions = missions_by_pilot(pilot, data)
        missions_count_by_pilots[pilot] = len(missions)

    return dict(sorted(missions_count_by_pilots.items(), key=lambda item: item[1], reverse=True))


def all_drone_types(data):
    
    used_drones = []

    drones_missions = missions_by_drones(data)

    for drone in drones_missions.keys():
        if not drone in used_drones:
            used_drones.append(drone)

    return used_drones           
            

def missions_by_drones(data):

    drones_missions_dict = {}

    for pilot in data.keys():
        missions = missions_by_pilot(pilot, data)
        for mission in missions:
            drone = mission["drone"]
            if not drone in drones_missions_dict.keys():
                drones_missions_dict[drone] = []    
            drones_missions_dict[drone].append(mission["mission"])


    return drones_missions_dict 


def count_missions_by_drones(data):

    drones_missions = missions_by_drones(data)
    result = {}

    for drone in drones_missions.keys():
        result[drone] = len(drones_missions[drone])

    return result    


def choose_drone(lower_input):
    
    drones = {
        "dji inspire 2" : "DJI Inspire 2",
        "dji mavic 2 pro" : "DJI Mavic 2 Pro",
        "dji mavic 2 enterprise advanced" : "DJI Mavic 2 Enterprise Advanced",
        "dji mavic 3" : "DJI Mavic 3",
        "dji mavic 2 zoom" : "DJI Mavic 2 Zoom"
    }

    return drones[lower_input]


if __name__ == "__main__":

    # TODO 1-1
    filename = "pilot_path.json"
    json_data = read_json(filename)

    # TODO 2-1
    pilots_missions_count = missions_by_pilots(json_data)
    print(pilots_missions_count)
    print("\n")

    # TODO 2-2
    used_drones = all_drone_types(json_data)
    print(f'Полеты совершались на дронах следующих моделей: {", ".join(used_drones)}')
    print("\n")

    # TODO 2-3
    drones_missions_count = count_missions_by_drones(json_data)
    for drone in drones_missions_count.keys():
        print(f"Дрон {drone} отлетал {drones_missions_count[drone]} миссий")
    print("\n")

    drone_catalog = {
        "DJI Mavic 2 Pro": {"weight": 903, "brand": "DJI"},
        "DJI Mavic 2 Zoom": {"weight": 900, "brand": "DJI"},
        "DJI Mavic 2 Enterprise Advanced": {"weight": 920, "brand": "DJI"},
        "DJI Inspire 2": {"weight": 1500, "brand": "DJI"},
        "DJI Mavic 3": {"weight": 1000, "brand": "DJI"}
    }

    missions_drones = missions_by_drones(json_data)
    drone_exs = []

    # TODO 4-1
    for drone in used_drones:

        # TODO 4-2
        drone_ex = MultirotorUAV(
            weight = drone_catalog[drone]["weight"], 
            model = drone, 
            brand = drone_catalog[drone]["brand"]
        )

        # TODO 4-3
        for mission in missions_drones[drone]:
            drone_ex.missions.append(mission)
        drone_exs.append(drone_ex)


    # TODO 4-4
    user_input = str(input("Введите модель дрона (полностью) в любом регистре\n"))
    lower_input = user_input.lower()
    chosen_drone = choose_drone(lower_input)  
    for drone in drone_exs:
        model = drone.get_model()
        if model == chosen_drone:
            print(f"Информация о дроне {model}: {drone.get_info()}")  
    