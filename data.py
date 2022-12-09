from enum import Enum


class MainWeapons(Enum):
    Katana = 0
    Kunai = 1
    Bat = 2
    Revolver = 3
    Lightchaser = 4
    Shotgun = 5


class WeaponSkills(Enum):
    Modular_Mine = 0
    RPG = 1
    Drill_Shot = 2
    Boomerang = 3
    Guardian = 4
    Forcefield_Device = 5
    Lightning_Emitter = 6
    Soccer_Ball = 7
    Molotov = 8
    Brick = 9
    Type_A_Drone = 10
    Type_B_Drone = 11
    Durian = 12
    Laser_Launcher = 13


class Supplies(Enum):
    Ronin_Oyoroi = 0
    Koga_Ninja_Scroll = 1
    HE_Fuel = 2
    Armor = 3
    Ammo_Thruster = 4
    Hi_Power_Magnet = 5
    Exo_Bracer = 6
    Energy_Drink = 7
    Energy_Cube = 8
    Sports_Shoes = 9
    Oil_Bond = 10
    Fitness_Guide = 11
    Hi_Power_Bullet = 12


class Evolutions:
    Demon_Blade = frozenset({MainWeapons.Katana, Supplies.Ronin_Oyoroi})
    Spirit_Shuriken = frozenset({MainWeapons.Kunai, Supplies.Koga_Ninja_Scroll})
    Sharkmaw_Gun = frozenset({WeaponSkills.RPG, Supplies.HE_Fuel})
    Whistling_Ammo = frozenset({WeaponSkills.Drill_Shot, Supplies.Ammo_Thruster})
    Magnetic_Dart = frozenset({WeaponSkills.Boomerang, Supplies.Hi_Power_Magnet})
    Defender = frozenset({WeaponSkills.Guardian, Supplies.Exo_Bracer})
    Pressure_Forcefield = frozenset({WeaponSkills.Forcefield_Device, Supplies.Energy_Drink})
    Thunderbolt_Power_Cell = frozenset({WeaponSkills.Lightning_Emitter, Supplies.Energy_Cube})
    Quantum_Ball = frozenset({WeaponSkills.Soccer_Ball, Supplies.Sports_Shoes})
    Fuel_Barrel = frozenset({WeaponSkills.Molotov, Supplies.Oil_Bond})
    Dumbbell = frozenset({WeaponSkills.Brick, Supplies.Fitness_Guide})
    Destroyer = frozenset({WeaponSkills.Type_A_Drone, WeaponSkills.Type_B_Drone})
    Caltrops = frozenset({WeaponSkills.Durian, Supplies.HE_Fuel})
    Inferno_Mine = frozenset({WeaponSkills.Modular_Mine, WeaponSkills.Molotov})
    Thunderbolt_Mine = frozenset({WeaponSkills.Modular_Mine, WeaponSkills.Lightning_Emitter})
    Death_Ray = Matrix = frozenset({WeaponSkills.Laser_Launcher, Supplies.Energy_Cube})
    Gatling = frozenset({MainWeapons.Shotgun, Supplies.Hi_Power_Bullet})
    Reaper = frozenset({MainWeapons.Revolver, Supplies.Hi_Power_Bullet})
    Eternal_Light = frozenset({MainWeapons.Lightchaser, Supplies.Ronin_Oyoroi})
    Lucile = frozenset({MainWeapons.Bat, Supplies.Fitness_Guide})

    @staticmethod
    def __iter__():
        for key, value in Evolutions.__dict__.items():
            if isinstance(value, frozenset):
                yield key, value

    @staticmethod
    def getDoubleWeaponEVO():
        double_list = list()
        for key, value in Evolutions.__iter__():
            same_type = True
            current_type = None
            for x in value:
                if current_type is None:
                    current_type = type(x)
                elif current_type != type(x):
                    same_type = False
                    break
            if same_type:
                double_list.append((key, value))
        return double_list


if __name__ == "__main__":
    print(Evolutions.getDoubleWeaponEVO())
