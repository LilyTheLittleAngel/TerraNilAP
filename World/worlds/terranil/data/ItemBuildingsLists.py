from enum import Enum

class BuildingEnum(Enum):
    def get_internalID(self, ignore_missing_ids = False) -> int:
        internal_id = self.value[0]
        if internal_id == 999 and not ignore_missing_ids:
            raise NotImplementedError(f"The building {str(self)} is not implemented yet.")
        return internal_id
    
    def get_displayName(self) -> str:
        return self.value[1]
    
    def get_tier(self) -> int:
        return self.value[2]
    
    def __int__(self) -> int: 
        return self.get_internalID()

    def __str__(self) -> str:
        return self.get_displayName()


## Region Temperate

class RiverValleyBuildings(BuildingEnum):
    "The building IDs for all buildings in River Valley"
    Turbine =           (100, "Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    
    Airship =           (300, "Airship", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    PoundLock =         (302, "Pound Lock", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 2)


class HillAndDaleBuildings(BuildingEnum):
    "The building IDs for all buildings in Hill and Dale"
    Turbine =           (100, "Wind Turbine", 1)
    ConeFilterInternalName = (999, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    ChaparrallumInternalName = (999, "Chaparrallum", 2)
    
    Airship =           (300, "Airship", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    PoundLock =         (302, "Pound Lock", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    CombustorInternalName = (999, "Combustor", 4)


class PollutedBayBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Bay"
    TidalTurbineInternalName = (999, "Tidal Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    PylonInternalName = (999, "Pylon", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    ConservatoryInternalName = (999, "Conservatory", 2)
    
    Airship =           (300, "Airship", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)


class AbandonedQuarryBuildings(BuildingEnum):
    "The building IDs for all buildings in Abandoned Quarry"
    Turbine =           (100, "Wind Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    SeismicDetonatorInternalName = (999, "Seismic Detonator", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    FlyingRecyclingDroneInternalName = (999, "Flying Recycling Drone", 3)
    StandaloneBeaconInternalName = (999, "Standalone Beacon", 3)
    RockHopperInternalName = (999, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)



## Region Tropical

class DesolateIslandBuildings(BuildingEnum):
    "The building IDs for all buildings in Desolate Island"
    Turbine =           (100, "Wind Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    WaterPump =         (104, "Water Pump", 1)
    MineralizerInternalName =         (999, "Mineralizer", 1)
    SandBankInternalName = (999, "Sand Bank", 1)
    
    Hydroponium =       (201, "Hydroponium", 2)
    LittariumInternalName = (999, "Littarium", 2)
    SalinatorInternalName = (999, "Salinator", 2)
    ShadeclothPillarInternalName = (999, "Shadecloth Pillar", 2)
    MonorailNodeInternalName = (999, "Monorail Node", 2)
    CoralLabInternalName = (999, "Coral Lab", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStationInternalName = (999, "Recycler Station", 3)
    RecyclingBeaconInternalName = (999, "Recycling Beacon", 3)
    RockHopperInternalName = (999, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    CombustorInternalName = (999, "Combustor", 4)


class ScorchedCalderaBuildings(BuildingEnum):
    "The building IDs for all buildings in Scorched Caldera"
    GeothermalPlantInternalName = (999, "Geothermal Plant", 1)
    SeismicDetonatorInternalName = (999, "Seismic Detonator", 1)
    ConeFilterInternalName = (999, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    
    ShadeclothPillarInternalName = (999, "Shadecloth Pillar", 2)
    MiniBambooNurseryInternalName = (999, "Mini Bamboo Nursery", 2)
    PercolotriumInternalName = (999, "Percolotrium", 2)
    RockHopperInternalName = (999, "Rock Hopper", 2)
    MonorailNodeInternalName = (999, "Monorail Node", 2)
    TranspiratorInternalName = (999, "Transpirator", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStationInternalName = (999, "Recycler Station", 3)
    RecyclingBeaconInternalName = (999, "Recycling Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CombustorInternalName = (999, "Combustor", 4)


class ArchipelagoBuildings(BuildingEnum):
    "The building IDs for all buildings in Archipelago (the map)"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")



## Region Polar

class VolcanicGlacierBuildings(BuildingEnum):
    "The building IDs for all buildings in Volcanic Glacier"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class SubpolarRiverBuildings(BuildingEnum):
    "The building IDs for all buildings in Subpolar River"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class PollutedFjordBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Fjord"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")



# Region Continental

class FloodedCityBuildings(BuildingEnum):
    "The building IDs for all buildings in Flooded City"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class IrradiatedSprawlBuildings(BuildingEnum):
    "The building IDs for all buildings in Irradiated Sprawl"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class ContinentalOutskirtsBuildings(BuildingEnum):
    "The building IDs for all buildings in Continental Outskirts"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")



# Region Arid

class ParchedDunesBuildings(BuildingEnum):
    "The building IDs for all buildings in Parched Dunes"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class CanyonPeaksBuildings(BuildingEnum):
    "The building IDs for all buildings in Canyon Peaks"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class FrackedFloodplainBuildings(BuildingEnum):
    "The building IDs for all buildings in Fracked Floodplain"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")
    

def test_building_enum(enum_to_test):
    print()
    for i in enum_to_test:
        display_name = i.get_displayname()
        try:
            building_id = i.get_internal_id()
        except NotImplementedError:
            print(f"Building {display_name:<30} has unknown ID (999).")
        
        try: 
            tier_number = i.get_tier()
        except KeyError:
            print(f"Building {display_name} has no assigned tier.")
        

def main():
    test_building_enum(RiverValleyBuildings)
    test_building_enum(HillAndDaleBuildings)
    test_building_enum(PollutedBayBuildings)
    test_building_enum(AbandonedQuarryBuildings)
    test_building_enum(DesolateIslandBuildings)
    test_building_enum(ScorchedCalderaBuildings)

if __name__ == "__main__":
    main()    
