execute unless block ~ ~3 ~ minecraft:gravel run return 0
tag @e[type=marker,limit=1,distance=5..40,tag=!HasLoot,sort=random] add AddLoot
tag @e[type=marker,limit=1,distance=..5,tag=HasLoot,sort=nearest] remove HasLoot
execute at @e[tag=AddLoot,distance=..40] run setblock ~ ~ ~ suspicious_gravel{LootTable:"minecon_ruins:archaeology/minecon_ruins_modfest"}
tag @e[tag=AddLoot,distance=..40] add HasLoot
tag @e[tag=AddLoot,distance=..40] remove AddLoot
