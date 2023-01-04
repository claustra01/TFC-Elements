package claustra01.tfcelem.item;

import claustra01.tfcelem.TFCEItemGroup;
import claustra01.tfcelem.TFCElements;
import claustra01.tfcelem.util.TFCEMetal;
import claustra01.tfcelem.util.TFCEOre;
import net.dries007.tfc.common.TFCItemGroup;
import net.dries007.tfc.common.blocks.rock.Ore;
import net.dries007.tfc.util.Helpers;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import java.util.Locale;
import java.util.Map;
import java.util.function.Supplier;

public class TFCEItems {

    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, TFCElements.namespace);

    public static final Map<TFCEOre, Map<Ore.Grade, RegistryObject<Item>>> GRADED_ORES = Helpers.mapOfKeys(TFCEOre.class, TFCEOre::isGraded, ore ->
            Helpers.mapOfKeys(Ore.Grade.class, grade ->
                    register("ore/" + grade.name() + '_' + ore.name(), TFCEItemGroup.ORES)
            )
    );

    public static final Map<TFCEMetal, Map<TFCEMetal.ItemType, RegistryObject<Item>>> METAL_ITEMS = Helpers.mapOfKeys(TFCEMetal.class, metal ->
            Helpers.mapOfKeys(TFCEMetal.ItemType.class, type -> type.has(metal), type ->
                    register("metal/" + type.name() + "/" + metal.name(), () -> type.create(metal))
            )
    );

    private static RegistryObject<Item> register(String name, CreativeModeTab group)
    {
        return register(name, () -> new Item(new Item.Properties().tab(group)));
    }

    private static <T extends Item> RegistryObject<T> register(String name, Supplier<T> item)
    {
        return ITEMS.register(name.toLowerCase(Locale.ROOT), item);
    }

}
