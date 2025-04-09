class RoutesGen4:
    #Pokemon at routes {Pokemon, min_level, max_lelvel, weight}
    ### Biomes: ARCTIC, COAST, FOREST, GRASSLAND, MOUNTAIN, OCEAN, SWAMP, UNDERGROUND, CITY

    BIOME_FOREST_EASY = [['Tangrowth', 40, 60, 10], ['Leafeon', 40, 60, 5], ['Venusaur', 40, 60, 10], ['Vileplume', 40, 60, 10], ['Victreebel', 40, 60, 10], 
                                    ['Breloom', 40, 60, 10], ['Tropius', 40, 60, 20], ['Torterra', 40, 60, 5], ['Amoonguss', 40, 60, 10], ['Ferrothorn', 40, 60, 5], 
                                    ['Chesnaught', 40, 60, 5], ['Parasect', 40, 60, 20], ['Pidgeot', 40, 60, 20], ['Fearow', 40, 60, 20], ['Scyther', 40, 60, 10], 
                                    ['Pinsir', 40, 60, 10], ['Arbok', 40, 60, 5], ['Seviper', 40, 60, 5], ['Beedrill', 40, 60, 10], ['Venomoth', 40, 60, 10], 
                                    ['Ariados', 40, 60, 5], ['Dustox', 40, 60, 10], ['Ursaring', 40, 60, 10], ['Stantler', 40, 60, 5], ['Zangoose', 40, 60, 5], 
                                    ['Ambipom', 40, 60, 5], ['Staraptor', 40, 60, 5], ['Swellow', 40, 60, 5], ['Heracross', 40, 60, 10], ['Lopunny', 40, 60, 10], 
                                    ['Toxicroak', 40, 60, 10], ['Gallade', 40, 60, 10], ['Snorlax', 40, 60, 5], ['Noctowl', 40, 60, 5], ['Breloom', 40, 60, 10], 
                                    ['Butterfree', 40, 60, 10], ['Raichu', 40, 60, 5], ['Galvantula', 40, 60, 10], ['Vikavolt', 40, 60, 10], ['Dugtrio', 40, 60, 5], 
                                    ['Mudsdale', 40, 60, 10], ['Gliscor', 40, 60, 10], ['Ninjask', 40, 60, 5], ['Xatu', 40, 60, 10], ['Celebi', 150, 200, 1], 
                                    ['Gardevoir', 40, 60, 10], ['Gallade', 40, 60, 10], ['Exeggutor', 40, 60, 10], ['Sudowoodo', 40, 60, 10], ['Shuckle', 40, 60, 10],
                                    ['Forretress', 40, 60, 10], ['Beautifly', 40, 60, 10], ['Kricketune', 40, 60, 10], ['Parasect', 40, 60, 10], ['Shedinja', 40, 60, 10], 
                                    ['Yanmega', 40, 60, 10], ['Scolipede', 40, 60, 10], ['Escavalier', 40, 60, 10], ['Drapion', 40, 60, 10], ['Mismagius', 40, 60, 10],
                                    ['Dusknoir', 40, 60, 10], ['Gengar', 40, 60, 10], ['Spiritomb', 40, 60, 10], ['Trevenant', 40, 60, 10], ['Gourgeist', 40, 60, 10], 
                                    ['Mimikyu', 40, 60, 5], ['Aegislash', 40, 60, 20], ['Persian', 40, 60, 10], ['Umbreon', 40, 60, 15], ['Mightyena', 40, 60, 10], 
                                    ['Absol', 40, 60, 10], ['Darkrai', 150, 200, 1], ['Liepard', 40, 60, 10], ['Zoroark', 40, 60, 10], ['Raticate', 40, 60, 10], 
                                    ['Honchkrow', 40, 60, 20], ['Shiftry', 40, 60, 5], ['Cacturne', 40, 60, 10], ['Skuntank', 40, 60, 15], ['Pangoro', 40, 60, 10], 
                                    ['Aromatisse', 40, 60, 10], ['Togekiss', 40, 60, 5], ['Whimsicott', 40, 60, 20], ['Dedenne', 40, 60, 10], 
                                    ['Klefki', 40, 60, 10], ['Ribombee', 40, 60, 10], ['Shiinotic', 40, 60, 10]]

    BIOME_FOREST_MEDIUM = [['Tangrowth', 50, 70, 10], ['Leafeon', 50, 70, 5], ['Venusaur', 50, 70, 10], ['Vileplume', 50, 70, 10], ['Victreebel', 50, 70, 10], 
                                    ['Breloom', 50, 70, 10], ['Tropius', 50, 70, 20], ['Torterra', 50, 70, 5], ['Amoonguss', 50, 70, 10], ['Ferrothorn', 50, 70, 5], 
                                    ['Chesnaught', 50, 70, 5], ['Parasect', 50, 70, 20], ['Pidgeot', 50, 70, 20], ['Fearow', 50, 70, 20], ['Scyther', 50, 70, 10], 
                                    ['Pinsir', 50, 70, 10], ['Arbok', 50, 70, 5], ['Seviper', 50, 70, 5], ['Beedrill', 50, 70, 10], ['Venomoth', 50, 70, 10], 
                                    ['Ariados', 50, 70, 5], ['Dustox', 50, 70, 10], ['Ursaring', 50, 70, 10], ['Stantler', 50, 70, 5], ['Zangoose', 50, 70, 5], 
                                    ['Ambipom', 50, 70, 5], ['Staraptor', 50, 70, 5], ['Swellow', 50, 70, 5], ['Heracross', 50, 70, 10], ['Lopunny', 50, 70, 10], 
                                    ['Toxicroak', 50, 70, 10], ['Gallade', 50, 70, 10], ['Snorlax', 50, 70, 5], ['Noctowl', 50, 70, 5], ['Breloom', 50, 70, 10], 
                                    ['Butterfree', 50, 70, 10], ['Raichu', 50, 70, 5], ['Galvantula', 50, 70, 10], ['Vikavolt', 50, 70, 10], ['Dugtrio', 50, 70, 5], 
                                    ['Mudsdale', 50, 70, 10], ['Gliscor', 50, 70, 10], ['Ninjask', 50, 70, 5], ['Xatu', 50, 70, 10], ['Celebi', 150, 200, 2], 
                                    ['Gardevoir', 50, 70, 10], ['Gallade', 50, 70, 10], ['Exeggutor', 50, 70, 10], ['Sudowoodo', 50, 70, 10], ['Shuckle', 50, 70, 10],
                                    ['Forretress', 50, 70, 10], ['Beautifly', 50, 70, 10], ['Kricketune', 50, 70, 10], ['Parasect', 50, 70, 10], ['Shedinja', 50, 70, 10], 
                                    ['Yanmega', 50, 70, 10], ['Scolipede', 50, 70, 10], ['Escavalier', 50, 70, 10], ['Drapion', 50, 70, 10], ['Mismagius', 50, 70, 10],
                                    ['Dusknoir', 50, 70, 10], ['Gengar', 50, 70, 10], ['Spiritomb', 50, 70, 10], ['Trevenant', 50, 70, 10], ['Gourgeist', 50, 70, 10], 
                                    ['Mimikyu', 50, 70, 5], ['Aegislash', 50, 70, 20], ['Persian', 50, 70, 10], ['Umbreon', 50, 70, 15], ['Mightyena', 50, 70, 10], 
                                    ['Absol', 50, 70, 10], ['Darkrai', 150, 200, 2], ['Liepard', 50, 70, 10], ['Zoroark', 50, 70, 10], ['Raticate', 50, 70, 10], 
                                    ['Honchkrow', 50, 70, 20], ['Shiftry', 50, 70, 5], ['Cacturne', 50, 70, 10], ['Skuntank', 50, 70, 15], ['Pangoro', 50, 70, 10], 
                                    ['Aromatisse', 50, 70, 10], ['Togekiss', 50, 70, 5], ['Whimsicott', 50, 70, 20], ['Dedenne', 50, 70, 10], 
                                    ['Klefki', 50, 70, 10], ['Ribombee', 50, 70, 10], ['Shiinotic', 50, 70, 10]]

    BIOME_FOREST_HARD = [['Tangrowth', 60, 80, 10], ['Leafeon', 60, 80, 5], ['Venusaur', 60, 80, 10], ['Vileplume', 60, 80, 10], ['Victreebel', 60, 80, 10], 
                                    ['Breloom', 60, 80, 10], ['Tropius', 60, 80, 20], ['Torterra', 60, 80, 5], ['Amoonguss', 60, 80, 10], ['Ferrothorn', 60, 80, 5], 
                                    ['Chesnaught', 60, 80, 5], ['Parasect', 60, 80, 20], ['Pidgeot', 60, 80, 20], ['Fearow', 60, 80, 20], ['Scyther', 60, 80, 10], 
                                    ['Pinsir', 60, 80, 10], ['Arbok', 60, 80, 5], ['Seviper', 60, 80, 5], ['Beedrill', 60, 80, 10], ['Venomoth', 60, 80, 10], 
                                    ['Ariados', 60, 80, 5], ['Dustox', 60, 80, 10], ['Ursaring', 60, 80, 10], ['Stantler', 60, 80, 5], ['Zangoose', 60, 80, 5], 
                                    ['Ambipom', 60, 80, 5], ['Staraptor', 60, 80, 5], ['Swellow', 60, 80, 5], ['Heracross', 60, 80, 10], ['Lopunny', 60, 80, 10], 
                                    ['Toxicroak', 60, 80, 10], ['Gallade', 60, 80, 10], ['Snorlax', 60, 80, 5], ['Noctowl', 60, 80, 5], ['Breloom', 60, 80, 10], 
                                    ['Butterfree', 60, 80, 10], ['Raichu', 60, 80, 5], ['Galvantula', 60, 80, 10], ['Vikavolt', 60, 80, 10], ['Dugtrio', 60, 80, 5], 
                                    ['Mudsdale', 60, 80, 10], ['Gliscor', 60, 80, 10], ['Ninjask', 60, 80, 5], ['Xatu', 60, 80, 10], ['Celebi', 150, 200, 3], 
                                    ['Gardevoir', 60, 80, 10], ['Gallade', 60, 80, 10], ['Exeggutor', 60, 80, 10], ['Sudowoodo', 60, 80, 10], ['Shuckle', 60, 80, 10],
                                    ['Forretress', 60, 80, 10], ['Beautifly', 60, 80, 10], ['Kricketune', 60, 80, 10], ['Parasect', 60, 80, 10], ['Shedinja', 60, 80, 10], 
                                    ['Yanmega', 60, 80, 10], ['Scolipede', 60, 80, 10], ['Escavalier', 60, 80, 10], ['Drapion', 60, 80, 10], ['Mismagius', 60, 80, 10],
                                    ['Dusknoir', 60, 80, 10], ['Gengar', 60, 80, 10], ['Spiritomb', 60, 80, 10], ['Trevenant', 60, 80, 10], ['Gourgeist', 60, 80, 10], 
                                    ['Mimikyu', 60, 80, 5], ['Aegislash', 60, 80, 20], ['Persian', 60, 80, 10], ['Umbreon', 60, 80, 15], ['Mightyena', 60, 80, 10], 
                                    ['Absol', 60, 80, 10], ['Darkrai', 150, 200, 3], ['Liepard', 60, 80, 10], ['Zoroark', 60, 80, 10], ['Raticate', 60, 80, 10], 
                                    ['Honchkrow', 60, 80, 20], ['Shiftry', 60, 80, 5], ['Cacturne', 60, 80, 10], ['Skuntank', 60, 80, 15], ['Pangoro', 60, 80, 10], 
                                    ['Aromatisse', 60, 80, 10], ['Togekiss', 60, 80, 5], ['Whimsicott', 60, 80, 20], ['Dedenne', 60, 80, 10], 
                                    ['Klefki', 60, 80, 10], ['Ribombee', 60, 80, 10], ['Shiinotic', 60, 80, 10]]

    ROUTE_201_SPAWNS = [['Starly', 2, 3, 5], ['Bidoof', 2, 4, 5], ['Kricketot', 2, 3, 4], ['Doduo', 2, 3, 3], ['Growlithe', 2, 3, 2], ['Nidoran♀', 2, 3, 1], ['Nidoran♂', 2, 3, 1]]
    ###202
    ROUTE_202_SPAWNS = [['Starly', 2, 4, 5], ['Bidoof', 2, 4, 5], ['Kricketot', 2, 3, 4], ['Shinx', 3, 4, 2], ['Zigzagoon', 2, 3, 4], ['Sentret', 2, 4, 4], ['Growlithe', 2, 3, 2]]
    ###203
    ROUTE_203_SPAWNS = [['Zubat', 4, 5, 10], ['Abra', 4, 5, 15], ['Starly', 4, 7, 25], ['Bidoof', 4, 6, 15], ['Kricketot', 4, 7, 15], ['Shinx', 4, 5, 25], ['Cubone', 4, 5, 10], 
                            ['Pineco', 5, 6, 8], ['Lotad', 5, 6, 8], ['Seedot', 5, 6, 8], ['Ralts', 4, 6, 21], ['Kirlia', 6, 7, 1]]
    ROUTE_203_SPAWNS_SURF = [['Psyduck', 20, 40, 90], ['Golduck', 20, 40, 10]]
    ROUTE_203_SPAWNS_FISHING_OLD = [['Magikarp', 3, 15, 1]]
    ROUTE_203_SPAWNS_FISHING_GOOD = [['Magikarp', 10, 25, 55], ['Goldeen', 10, 25, 45]]
    ROUTE_203_SPAWNS_FISHING_SUPER = [['Seaking', 20, 50, 45], ['Gyarados', 30, 55, 55]]
    ###204
    ROUTE_204_SPAWNS_S = [['Zubat', 3, 4, 20], ['Wurmple', 3, 4, 20], ['Starly', 4, 6, 25], ['Bidoof', 4, 6, 25], ['Kricketot', 3, 4, 20], ['Shinx', 4, 5, 15], ['Budew', 3, 5, 40],
                            ['Caterpie', 5, 6, 16], ['Weedle', 5, 6, 16], ['Pineco', 5, 6, 18], ['Lotad', 5, 6, 16], ['Seedot', 5, 6, 16], ['Ralts', 4, 6, 21], ['Kirlia', 6, 9, 1]]
    ROUTE_204_SPAWNS_SURF = [['Phyduck', 20, 40, 90], ['Golduck', 20, 40, 10]]
    ROUTE_204_SPAWNS_FISHING_OLD = [['Magikarp', 3, 15, 1]]
    ROUTE_204_SPAWNS_FISHING_GOOD = [['Magikarp', 10, 25, 55], ['Goldeen', 10, 25, 45]]
    ROUTE_204_SPAWNS_FISHING_SUPER = [['Seaking', 30, 55, 45], ['Gyarados', 30, 55, 55]]
    ROUTE_204_SPAWNS_N = [['Zubat', 6, 8, 20], ['Wurmple', 9, 10, 10], ['Starly', 6, 11, 25], ['Bidoof', 6, 11, 25], ['Kricketot', 6, 9, 10], ['Shinx', 6, 10, 15], 
                                ['Budew', 6, 10, 40], ['Caterpie', 6, 7, 8], ['Weedle', 6, 7, 8], ['Pineco', 8, 10, 16], ['Lotad', 8, 10, 16], ['Seedot', 8, 10, 16], 
                                ['Sunkern', 6, 11, 22]]
    ###205
    ROUTE_205_SPAWNS_S = [['Bidoof', 9, 10, 20], ['Pachirisu', 9, 11, 20], ['Buizel', 8, 11, 50], ['Shellos', 8, 12, 100], ['Hoppip', 9, 12, 22], ['Elekid', 10, 11, 8]]
    ROUTE_205_SPAWNS_S_SURF = [['Wingull', 20, 30, 30], ['Pelipper', 20, 40, 5], ['Tentacool', 20, 30, 45], ['Tentacruel', 20, 40, 4], ['Shellos', 20, 30, 60], 
                                    ['Gastrodon', 20, 40, 9]]
    ROUTE_205_SPAWNS_S_FISHING_OLD = [['Magikarp', 3, 15, 1]]
    ROUTE_205_SPAWNS_S_FISHING_GOOD = [['Magikarp', 10, 25, 55] ,['Finneon', 10, 25, 45]]
    ROUTE_205_SPAWNS_S_FISHING_SUPER = [['Shellder', 20, 50, 15], ['Gyarados', 30, 55, 40], ['Lumineon', 20, 55, 45]]
    #
    ROUTE_205_SPAWNS_N = [['Hoothoot', 12, 13, 10], ['Wurmple', 13, 14, 10], ['Silcoon', 14, 15, 10], ['Beautifly', 15, 16, 1], ['Cascoon', 14, 15, 10], 
                                ['Dustox', 15, 16, 1], ['Bidoof', 10, 14, 30], ['Kricketot', 12, 13, 10], ['Budew', 12, 14, 30], ['Pachirisu', 11, 12, 10], 
                                ['Buizel', 10, 12, 35], ['Shellos', 11, 12, 10], ['Slowpoke', 11, 15, 22], ['Hoppip', 11, 12, 20], ['Skiploom', 12, 13, 2], 
                                ['Lotad', 12, 14, 8]]
    ROUTE_205_SPAWNS_N_SURF = [['Psyduck', 20, 40, 90], ['Golduck', 20, 40, 10]]
    ROUTE_205_SPAWNS_N_FISHING_OLD = [['Magikarp', 3, 15, 1]]
    ROUTE_205_SPAWNS_N_FISHING_GOOD = [['Magikarp', 10, 25, 55] ,['Barboach', 10, 25, 45]]
    ROUTE_205_SPAWNS_N_FISHING_SUPER = [['Whiscash', 20, 50, 45], ['Gyarados', 30, 55, 55]]
    ###206
    ROUTE_206_SPAWNS = [['Zubat', 14, 17, 10], ['Machop', 17, 19, 20], ['Geodude', 14, 16, 20], ['Ponyta', 14, 17, 30], ['Gligar', 16, 18, 20], 
                            ['Kricketot', 14, 15, 10], ['Stunky', 14, 16, 25], ['Bronzor', 15, 16, 10], ['Larvitar', 14, 16, 10], ['Nosepass', 14, 15, 10], 
                            ['Gligar', 15, 16, 8], ['Baltoy', 14, 19, 22]]
    ###207
    ROUTE_207_SPAWNS = [['Zubat', 5, 6, 10], ['Machop', 5, 8, 35], ['Geodude', 5, 7, 55], ['Ponyta', 5, 7, 25], ['Kricketot', 5, 6, 10], ['Phanpy', 5, 7, 40], ['Gligar', 7, 9, 9],
                            ['Stantler', 5, 7, 8], ['Larvitar', 5, 10, 8]]

    ###Eterna Forest
    ROUTE_ETERNA_FOREST = [['Gastly', 13, 15, 4], ['Hoothoot', 12, 14, 10], ['Murkrow', 10, 11, 20], ['Misdreavus', 10, 11, 20], ['Wurmple', 10, 11, 20], ['Silcoon', 10, 12, 10], 
                                ['Beautifly', 10, 14, 2], ['Cascoon', 10, 12, 15], ['Dustox', 10, 14, 2], ['Bidoof', 12, 13, 10], ['Kricketot', 10, 11, 10], ['Budew', 10, 12, 30], 
                                ['Buneary', 10, 13, 20], ['Slakoth', 10, 12, 10], ['Caterpie', 13, 15, 4], ['Metapod', 13, 15, 8], ['Weedle', 13, 15, 4], ['Kakuna', 12, 15, 8], 
                                ['Seedot', 12, 15, 8], ['Pineco', 12, 13, 8], ['Nincada', 10, 14, 22]]
    ROUTE_OLD_CHATEAU =[['Gastly', 14, 20, 60], ['Haunter', 19, 35, 40], ['Misdreavus', 14, 20, 10], ['Shuppet', 14, 20, 10], ['Duskull', 12, 18, 10], ['Drifloon', 16, 20, 10],
                            ['Litwick', 14, 18, 10], ['Spiritomb', 25, 40, 5], ['Phantump', 14, 18, 5], ['Pumpkaboo', 14, 18, 5]]

    ###Mounten Coronet
    ROUTE_MTCORONET_1F1 = [['Clefairy', 17, 20, 10], ['Zubat', 14, 19, 20], ['Machop', 15, 20, 25], ['Geodude', 14, 19, 30], ['Cleffa', 13, 14, 25], ['Nosepass', 18, 19, 5],
                                ['Meditite', 15, 20, 20], ['Chingling', 15, 19, 10], ['Bronzor', 18, 19, 20]]
    ROUTE_MTCORONET_1F1_SURF = [['Zubat', 20, 40, 90], ['Golbat', 20, 40, 10]]
    ROUTE_MTCORONET_1F1_FISHING_OLD = [['Magikarp', 3, 15, 1]]
    ROUTE_MTCORONET_1F1_FISHING_GOOD = [['Magikarp', 10, 25, 55] ,['Barboach', 10, 25, 45]]
    ROUTE_MTCORONET_1F1_FISHING_SUPER = [['Whiscash', 20, 50, 45], ['Gyarados', 30, 55, 55]]

    ###208
    ROUTE_208_SPAWNS = [['Zubat', 16, 19, 20], ['Psyduck', 16, 18, 30], ['Machop', 16, 17, 10], ['Ralts', 17, 18, 15], ['Meditite', 16, 17, 15], ['Roselia', 19, 20, 15],
                            ['Bidoof', 16, 18, 20], ['Bibarel', 17, 20, 20], ['Budew', 18, 19, 20], ['Dunsparce', 16, 18, 10], ['Smeargle', 18, 20, 22], ['Tyrogue', 17, 18, 22],
                            ['Zangoose', 18, 20, 8], ['Seviper', 18, 20, 8]]
    ROUTE_208_SPAWNS_SURF = [['Psyduck', 20, 40, 90], ['Golduck', 20, 40, 10]]
    ROUTE_208_SPAWNS_FISHING_OLD = [['Magikarp', 3, 15, 1]]
    ROUTE_208_SPAWNS_FISHING_GOOD = [['Magikarp', 10, 25, 55], ['Goldeen', 10, 25, 45], ['Barboach', 10, 25, 45]]
    ROUTE_208_SPAWNS_FISHING_SUPER = [['Seaking', 30, 55, 45], ['Gyarados', 30, 55, 55], ['Whiscash', 20, 50, 45]]