package claustra01.tfcelem;

import claustra01.tfcelem.TFCElements;
import net.minecraft.core.Registry;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.tags.TagKey;
import net.minecraft.world.level.block.Block;

public class TFCETags {

    public static TagKey<Block> NEEDS_OSMIUM_TOOLS = create("needs_osmium_tools");

    private static TagKey<Block> create(String id) {
        return TagKey.create(Registry.BLOCK_REGISTRY, new ResourceLocation(TFCElements.namespace, id));
    }

}
