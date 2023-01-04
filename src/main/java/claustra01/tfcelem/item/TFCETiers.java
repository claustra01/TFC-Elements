package claustra01.tfcelem.item;

import claustra01.tfcelem.TFCElements;
import net.dries007.tfc.common.TFCTags;
import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.util.ToolTier;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.tags.TagKey;
import net.minecraft.world.item.Tier;
import net.minecraft.world.item.Tiers;
import net.minecraft.world.item.crafting.Ingredient;
import net.minecraft.world.level.block.Block;
import net.minecraftforge.common.TierSortingRegistry;

import javax.annotation.Nullable;
import java.util.List;

public class TFCETiers {

    public static final Tier OSMIUM = register("osmium", Tiers.NETHERITE, null, TFCTags.Blocks.NEEDS_COLORED_STEEL_TOOL, 6, 9200, 20f, 11.1f, 24);

    private static Tier register(String name, Tier before, @Nullable Tier after, TagKey<Block> tag, int level, int uses, float speed, float damage, int enchantmentValue)
    {
        return register(name, List.of(before), after == null ? List.of() : List.of(after), tag, level, uses, speed, damage, enchantmentValue);
    }

    private static Tier register(String name, List<Object> before, List<Object> after, TagKey<Block> tag, int level, int uses, float speed, float damage, int enchantmentValue)
    {
        final Tier tier = new ToolTier(name, level, uses, speed, damage, enchantmentValue, tag, () -> Ingredient.EMPTY);
        if (!Helpers.BOOTSTRAP_ENVIRONMENT) TierSortingRegistry.registerTier(tier, new ResourceLocation(TFCElements.namespace, name), before, after);
        return tier;
    }

}
