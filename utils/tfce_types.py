rocks = [
    "granite",
    "diorite",
    "gabbro",
    "shale",
    "claystone",
    "limestone",
    "conglomerate",
    "dolomite",
    "chert",
    "chalk",
    "rhyolite",
    "basalt",
    "andesite",
    "dacite",
    "quartzite",
    "slate",
    "phyllite",
    "schist",
    "gneiss",
    "marble"
]

ores = [
    # name, isGraded, metalName, hardness(wood/stone/iron/diamond/netherite)
    ["native_platinum", True, "platinum", "diamond"],
    ["bauxite", True, "aluminium", "iron"],
    ["native_osmium", True, "osmium", "diamond"]
]

grades = [
    "poor",
    "normal",
    "rich"
]

metals = [
    # name, enableTool, enablePart, enableArmor, enableUtility, [textureType(iron/silver/steel), h, s, v]
    ["platinum", False, True, False, True, ["silver", -148, 18, 0]],
    ["aluminum", True, True, True, True, ["iron", -179, 13, 0]],
    ["osmium", True, True, True, True, ["iron", -171, 17, 0]]
]

types_parts = [
    "double_ingot",
    "sheet",
    "double_sheet",
    "rod"
]

types_tools = [
    "tuyere",
    "fish_hook",
    "fishing_rod",
    "pickaxe",
    "pickaxe_head",
    "propick",
    "propick_head",
    "axe",
    "axe_head",
    "shovel",
    "shovel_head",
    "hoe",
    "hoe_head",
    "chisel",
    "chisel_head",
    "hammer",
    "hammer_head",
    "saw",
    "saw_blade",
    "javelin",
    "javelin_head",
    "sword",
    "sword_blade",
    "mace",
    "mace_head",
    "knife",
    "knife_blade",
    "scythe",
    "scythe_blade",
    "shears",
    "shield"
]

types_armors = [
    "helmet",
    "chestplate",
    "greaves",
    "boots",
    "unfinished_helmet",
    "unfinished_chestplate",
    "unfinished_greaves",
    "unfinished_boots"
]