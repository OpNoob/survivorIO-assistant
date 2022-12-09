from tiers import Tier_List
from data import *


class Game:
    max_tiers = 5
    max_weapon_skills = 6
    max_supply_skills = 6

    def __init__(self):
        self.upgrades = self.Upgrades()

    class Upgrade:
        def __init__(self, typ: MainWeapons or WeaponSkills or Supplies):
            self.type = typ
            self.tier = 1

        def incrementTier(self):
            self.tier += 1

    class Upgrades:
        def __init__(self):
            self.weapons = list()
            self.skills = list()

        def addUpgrade(self, upgrade: MainWeapons or WeaponSkills or Supplies):
            if isinstance(upgrade, MainWeapons):
                self.weapons.append(upgrade)
            elif isinstance(upgrade, WeaponSkills):
                self.weapons.append(upgrade)
            elif isinstance(upgrade, Supplies):
                self.skills.append(upgrade)

        def getMainWeapon(self):
            for x in self.weapons:
                if isinstance(x, MainWeapons):
                    return x

        def getWeaponSpace(self, potential=False):
            if potential:
                add_potential = 0
                # Add potential

            return Game.max_weapon_skills - len(self.weapons)

        def getBestChoice(self, options):
            flatten_tier = [upgrade for tier in Tier_List for evolution in tier for upgrade in evolution]
            for up in flatten_tier:
                if up in options:
                    return up


g = Game()
c = g.getBestChoice([WeaponSkills.Type_A_Drone, WeaponSkills.Boomerang, WeaponSkills.Modular_Mine])
print(c)
