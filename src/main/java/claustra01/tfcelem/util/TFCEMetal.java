package claustra01.tfcelem.util;

import claustra01.tfcelem.misc.TFCEArmorMaterials;
import claustra01.tfcelem.misc.TFCEItemGroup;
import claustra01.tfcelem.misc.TFCETiers;
import net.dries007.tfc.common.TFCTags;
import net.dries007.tfc.common.blockentities.TFCBlockEntities;
import net.dries007.tfc.common.blocks.ExtendedProperties;
import net.dries007.tfc.common.blocks.TFCBlocks;
import net.dries007.tfc.common.blocks.TFCChainBlock;
import net.dries007.tfc.common.blocks.devices.AnvilBlock;
import net.dries007.tfc.common.blocks.devices.LampBlock;
import net.dries007.tfc.common.items.*;
import net.dries007.tfc.util.Metal;
import net.dries007.tfc.util.registry.RegistryMetal;
import net.minecraft.world.entity.EquipmentSlot;
import net.minecraft.world.item.*;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.TrapDoorBlock;
import net.minecraft.world.level.material.Material;
import net.minecraft.world.level.material.MaterialColor;

import javax.annotation.Nonnull;
import javax.annotation.Nullable;
import java.util.Locale;
import java.util.Objects;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public enum TFCEMetal implements RegistryMetal {

    LEAD(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_II, true, false, false),
    PLATINUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_VI, true, false, false),
    ELECTRUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_III, true, false, false),
    INVAR(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_VI, true, false, false),
    CONSTANTAN(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_IV, true, false, false),
    SIGNALUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_IV, true, false, false),
    LUMIUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_V, true, false, false),
    ENDERIUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_VI, true, false, false),
    ALUMINUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_IV, true, false, false),
    URANIUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_VI, true, false, false),
    OSMIUM(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_VI, true, false, false),
    REFINED_OBSIDIAN(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_VI, true, false, false),
    REFINED_GLOWSTONE(0xFF9DADC0, Rarity.COMMON, Metal.Tier.TIER_VI, true, false, false);

    private final String serializedName;
    private final boolean parts, armor, utility;
    private final Metal.Tier metalTier;
    @Nullable
    private final net.minecraft.world.item.Tier toolTier;
    @Nullable
    private final ArmorMaterial armorTier;
    private final Rarity rarity;
    private final int color;

    TFCEMetal(int color, Rarity rarity, Metal.Tier tier, boolean parts, boolean armor, boolean utility)
    {
        this(color, rarity, tier, null, null, parts, armor, utility);
    }

    TFCEMetal(int color, Rarity rarity, Metal.Tier metalTier, @Nullable net.minecraft.world.item.Tier toolTier, @Nullable ArmorMaterial armorTier, boolean parts, boolean armor, boolean utility)
    {
        this.serializedName = name().toLowerCase(Locale.ROOT);
        this.metalTier = metalTier;
        this.toolTier = toolTier;
        this.armorTier = armorTier;
        this.rarity = rarity;
        this.color = color;

        this.parts = parts;
        this.armor = armor;
        this.utility = utility;
    }

    @Nonnull
    @Override
    public String getSerializedName()
    {
        return serializedName;
    }

    public int getColor()
    {
        return color;
    }

    public Rarity getRarity()
    {
        return rarity;
    }

    public boolean hasParts()
    {
        return parts;
    }

    public boolean hasArmor()
    {
        return armor;
    }

    public boolean hasTools()
    {
        return toolTier != null;
    }

    public boolean hasUtilities()
    {
        return utility;
    }

    @Nonnull
    @Override
    public net.minecraft.world.item.Tier toolTier()
    {
        return Objects.requireNonNull(toolTier, "Tried to get non-existent tier from " + name());
    }

    @Nonnull
    @Override
    public ArmorMaterial armorTier()
    {
        return Objects.requireNonNull(armorTier, "Tried to get non-existent armor tier from " + name());
    }

    @Nonnull
    @Override
    public Metal.Tier metalTier()
    {
        return metalTier;
    }

    private enum Type {
        DEFAULT((metal) -> true),
        PART(TFCEMetal::hasParts),
        TOOL(TFCEMetal::hasTools),
        ARMOR(TFCEMetal::hasArmor),
        UTILITY(TFCEMetal::hasUtilities);

        private final Predicate<TFCEMetal> predicate;

        Type(Predicate<TFCEMetal> predicate) {
            this.predicate = predicate;
        }

        boolean hasType(TFCEMetal metal) {
            return this.predicate.test(metal);
        }
    }

    public enum ItemType {
        INGOT(Type.DEFAULT, true),
        DOUBLE_INGOT(Type.PART, false),
        SHEET(Type.PART, false),
        DOUBLE_SHEET(Type.PART, false),
        ROD(Type.PART, false),
        TUYERE(Type.TOOL, (metal) -> {
            return new TieredItem(metal.toolTier(), properties());
        }),
        FISH_HOOK(Type.TOOL, false),
        FISHING_ROD(Type.TOOL, (metal) -> {
            return new TFCFishingRodItem(properties().defaultDurability(metal.toolTier().getUses()), metal.toolTier());
        }),
        PICKAXE(Type.TOOL, (metal) -> {
            return new PickaxeItem(metal.toolTier(), (int) ToolItem.calculateVanillaAttackDamage(0.75F, metal.toolTier()), -2.8F, properties());
        }),
        PICKAXE_HEAD(Type.TOOL, true),
        PROPICK(Type.TOOL, (metal) -> {
            return new PropickItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(0.5F, metal.toolTier()), -2.8F, properties());
        }),
        PROPICK_HEAD(Type.TOOL, true),
        AXE(Type.TOOL, (metal) -> {
            return new AxeItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(1.5F, metal.toolTier()), -3.1F, properties());
        }),
        AXE_HEAD(Type.TOOL, true),
        SHOVEL(Type.TOOL, (metal) -> {
            return new ShovelItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(0.875F, metal.toolTier()), -3.0F, properties());
        }),
        SHOVEL_HEAD(Type.TOOL, true),
        HOE(Type.TOOL, (metal) -> {
            return new TFCHoeItem(metal.toolTier(), -1, -2.0F, properties());
        }),
        HOE_HEAD(Type.TOOL, true),
        CHISEL(Type.TOOL, (metal) -> {
            return new ChiselItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(0.27F, metal.toolTier()), -1.5F, properties());
        }),
        CHISEL_HEAD(Type.TOOL, true),
        HAMMER(Type.TOOL, (metal) -> {
            return new ToolItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(1.0F, metal.toolTier()), -3.0F, TFCTags.Blocks.MINEABLE_WITH_HAMMER, properties());
        }),
        HAMMER_HEAD(Type.TOOL, true),
        SAW(Type.TOOL, (metal) -> {
            return new AxeItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(0.5F, metal.toolTier()), -3.0F, properties());
        }),
        SAW_BLADE(Type.TOOL, true),
        JAVELIN(Type.TOOL, (metal) -> {
            return new JavelinItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(1.0F, metal.toolTier()), -2.2F, properties(), metal.getSerializedName());
        }),
        JAVELIN_HEAD(Type.TOOL, true),
        SWORD(Type.TOOL, (metal) -> {
            return new SwordItem(metal.toolTier(), (int)ToolItem.calculateVanillaAttackDamage(1.0F, metal.toolTier()), -2.4F, properties());
        }),
        SWORD_BLADE(Type.TOOL, true),
        MACE(Type.TOOL, (metal) -> {
            return new MaceItem(metal.toolTier(), (int)ToolItem.calculateVanillaAttackDamage(1.3F, metal.toolTier()), -3.0F, properties());
        }),
        MACE_HEAD(Type.TOOL, true),
        KNIFE(Type.TOOL, (metal) -> {
            return new ToolItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(0.6F, metal.toolTier()), -2.0F, TFCTags.Blocks.MINEABLE_WITH_KNIFE, properties());
        }),
        KNIFE_BLADE(Type.TOOL, true),
        SCYTHE(Type.TOOL, (metal) -> {
            return new ScytheItem(metal.toolTier(), ToolItem.calculateVanillaAttackDamage(0.7F, metal.toolTier()), -3.2F, TFCTags.Blocks.MINEABLE_WITH_SCYTHE, properties());
        }),
        SCYTHE_BLADE(Type.TOOL, true),
        SHEARS(Type.TOOL, (metal) -> {
            return new ShearsItem(properties().defaultDurability(metal.toolTier().getUses()));
        }),
        UNFINISHED_HELMET(Type.ARMOR, false),
        HELMET(Type.ARMOR, (metal) -> {
            return new ArmorItem(metal.armorTier(), EquipmentSlot.HEAD, properties());
        }),
        UNFINISHED_CHESTPLATE(Type.ARMOR, false),
        CHESTPLATE(Type.ARMOR, (metal) -> {
            return new ArmorItem(metal.armorTier(), EquipmentSlot.CHEST, properties());
        }),
        UNFINISHED_GREAVES(Type.ARMOR, false),
        GREAVES(Type.ARMOR, (metal) -> {
            return new ArmorItem(metal.armorTier(), EquipmentSlot.LEGS, properties());
        }),
        UNFINISHED_BOOTS(Type.ARMOR, false),
        BOOTS(Type.ARMOR, (metal) -> {
            return new ArmorItem(metal.armorTier(), EquipmentSlot.FEET, properties());
        }),
        SHIELD(Type.TOOL, (metal) -> {
            return new TFCShieldItem(metal.toolTier(), properties());
        });

        private final Function<RegistryMetal, Item> itemFactory;
        private final Type type;
        private final boolean mold;

        public static Item.Properties properties() {
            return (new Item.Properties()).tab(TFCEItemGroup.METAL);
        }

        ItemType(Type type, boolean mold) {
            this(type, mold, (metal) -> {
                return new Item(properties());
            });
        }

        ItemType(Type type, Function<RegistryMetal, Item> itemFactory) {
            this(type, false, itemFactory);
        }

        ItemType(Type type, boolean mold, Function<RegistryMetal, Item> itemFactory) {
            this.type = type;
            this.mold = mold;
            this.itemFactory = itemFactory;
        }

        public Item create(RegistryMetal metal) {
            return this.itemFactory.apply(metal);
        }

        public boolean has(TFCEMetal metal) {
            return this.type.hasType(metal);
        }

        public boolean hasMold() {
            return this.mold;
        }
    }

    public enum BlockType {
        ANVIL(Type.UTILITY, (metal) -> {
            return new AnvilBlock(ExtendedProperties.of(Material.METAL).noOcclusion().sound(SoundType.METAL).strength(10.0F, 10.0F).requiresCorrectToolForDrops().blockEntity(TFCBlockEntities.ANVIL), metal.metalTier());
        }),
        CHAIN(Type.UTILITY, (metal) -> {
            return new TFCChainBlock(net.minecraft.world.level.block.state.BlockBehaviour.Properties.of(Material.METAL, MaterialColor.NONE).requiresCorrectToolForDrops().strength(5.0F, 6.0F).sound(SoundType.CHAIN));
        }),
        LAMP(Type.UTILITY, (metal) -> {
            return new LampBlock(ExtendedProperties.of(Material.METAL).noOcclusion().sound(SoundType.LANTERN).strength(4.0F, 10.0F).randomTicks().lightLevel((state) -> {
                return (Boolean)state.getValue(LampBlock.LIT) ? 15 : 0;
            }).blockEntity(TFCBlockEntities.LAMP));
        }, (block, properties) -> {
            return new LampBlockItem(block, properties);
        }),
        TRAPDOOR(Type.UTILITY, (metal) -> {
            return new TrapDoorBlock(net.minecraft.world.level.block.state.BlockBehaviour.Properties.of(Material.METAL).requiresCorrectToolForDrops().strength(5.0F).sound(SoundType.METAL).noOcclusion().isValidSpawn(TFCBlocks::never));
        });

        private final Function<RegistryMetal, Block> blockFactory;
        private final BiFunction<Block, Item.Properties, ? extends BlockItem> blockItemFactory;
        private final Type type;

        BlockType(Type type, Function<RegistryMetal, Block> blockFactory, BiFunction<Block, Item.Properties, ? extends BlockItem> blockItemFactory) {
            this.type = type;
            this.blockFactory = blockFactory;
            this.blockItemFactory = blockItemFactory;
        }

        BlockType(Type type, Function<RegistryMetal, Block> blockFactory) {
            this(type, blockFactory, BlockItem::new);
        }

        public Supplier<Block> create(RegistryMetal metal) {
            return () -> (Block)this.blockFactory.apply(metal);
        }

        public Function<Block, BlockItem> createBlockItem(Item.Properties properties) {
            return (block) -> (BlockItem)this.blockItemFactory.apply(block, properties);
        }

        public boolean has(TFCEMetal metal) {
            return this.type.hasType(metal);
        }
    }
}
