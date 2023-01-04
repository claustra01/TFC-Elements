package claustra01.tfcelem.item;

import claustra01.tfcelem.TFCElements;
import net.dries007.tfc.client.TFCSounds;
import net.dries007.tfc.util.PhysicalDamageType;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.world.entity.EquipmentSlot;
import net.minecraft.world.item.ArmorMaterial;
import net.minecraft.world.item.crafting.Ingredient;

import javax.annotation.Nonnull;
import java.util.Locale;

public enum TFCEArmorMaterials implements ArmorMaterial, PhysicalDamageType.Multiplier {

    OSMIUM(904, 1040, 1030, 735, 4, 6, 8, 4, 23, 3f, 0.1f, 62.5f, 50f, 62.5f);

    private final ResourceLocation serializedName;
    private final int feetDamage;
    private final int legDamage;
    private final int chestDamage;
    private final int headDamage;
    private final int feetReduction;
    private final int legReduction;
    private final int chestReduction;
    private final int headReduction;
    private final int enchantability;
    private final float toughness;
    private final float knockbackResistance;
    private final float crushingModifier;
    private final float piercingModifier;
    private final float slashingModifier;

    TFCEArmorMaterials(int feetDamage, int legDamage, int chestDamage, int headDamage, int feetReduction, int legReduction, int chestReduction, int headReduction, int enchantability, float toughness, float knockbackResistance, float crushingModifier, float piercingModifier, float slashingModifier)
    {
        this.serializedName = new ResourceLocation(TFCElements.namespace, name().toLowerCase(Locale.ROOT));
        this.feetDamage = feetDamage;
        this.legDamage = legDamage;
        this.chestDamage = chestDamage;
        this.headDamage = headDamage;
        this.feetReduction = feetReduction;
        this.legReduction = legReduction;
        this.chestReduction = chestReduction;
        this.headReduction = headReduction;
        this.enchantability = enchantability;
        this.toughness = toughness;
        this.knockbackResistance = knockbackResistance;

        // Since each slot is applied separately, the input values are values for a full set of armor of this type.
        this.crushingModifier = crushingModifier * 0.25f;
        this.piercingModifier = piercingModifier * 0.25f;
        this.slashingModifier = slashingModifier * 0.25f;
    }

    @Override
    public float crushing()
    {
        return crushingModifier;
    }

    @Override
    public float piercing()
    {
        return piercingModifier;
    }

    @Override
    public float slashing()
    {
        return slashingModifier;
    }

    @Override
    public int getDurabilityForSlot(EquipmentSlot slot)
    {
        return switch (slot)
                {
                    case FEET -> feetDamage;
                    case LEGS -> legDamage;
                    case CHEST -> chestDamage;
                    case HEAD -> headDamage;
                    default -> 0;
                };
    }

    @Override
    public int getDefenseForSlot(EquipmentSlot slot)
    {
        return switch (slot)
                {
                    case FEET -> feetReduction;
                    case LEGS -> legReduction;
                    case CHEST -> chestReduction;
                    case HEAD -> headReduction;
                    default -> 0;
                };
    }

    @Override
    public int getEnchantmentValue()
    {
        return enchantability;
    }

    @Nonnull
    @Override
    public SoundEvent getEquipSound()
    {
        return TFCSounds.ARMOR_EQUIP.get(this).get();
    }

    /**
     * Use {@link #getId()} because it doesn't have weird namespaced side effects.
     */
    @Nonnull
    @Override
    @Deprecated
    public String getName()
    {
        // Note that in HumanoidArmorLayer, the result of getName() is used directly in order to infer the armor texture location
        // So, this needs to be properly namespaced despite being a string.
        return serializedName.toString();
    }

    public ResourceLocation getId()
    {
        return serializedName;
    }

    @Override
    public float getToughness()
    {
        return toughness;
    }

    @Override
    public float getKnockbackResistance()
    {
        return knockbackResistance;
    }

    @Nonnull
    @Override
    public Ingredient getRepairIngredient()
    {
        return Ingredient.EMPTY;
    }
}
