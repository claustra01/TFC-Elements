package claustra01.tfcelem.block;

import claustra01.tfcelem.misc.TFCEItemGroup;
import claustra01.tfcelem.TFCElements;
import claustra01.tfcelem.item.TFCEItems;
import claustra01.tfcelem.util.TFCEMetal;
import claustra01.tfcelem.util.TFCEOre;
import net.dries007.tfc.common.blocks.GroundcoverBlock;
import net.dries007.tfc.common.blocks.rock.Ore;
import net.dries007.tfc.common.blocks.rock.Rock;
import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.util.registry.RegistrationHelpers;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.Material;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import javax.annotation.Nullable;
import java.util.Map;
import java.util.function.Function;
import java.util.function.Supplier;

public class TFCEBlocks {

    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, TFCElements.namespace);

    public static final Map<Rock, Map<TFCEOre, Map<Ore.Grade, RegistryObject<Block>>>> GRADED_ORES = Helpers.mapOfKeys(Rock.class, rock ->
            Helpers.mapOfKeys(TFCEOre.class, TFCEOre::isGraded, ore ->
                    Helpers.mapOfKeys(Ore.Grade.class, grade ->
                            register(("ore/" + grade.name() + "_" + ore.name() + "/" + rock.name()), () -> ore.create(rock), TFCEItemGroup.ORES)
                    )
            )
    );
    public static final Map<TFCEOre, RegistryObject<Block>> SMALL_ORES = Helpers.mapOfKeys(TFCEOre.class, TFCEOre::isGraded, type ->
            register(("ore/small_" + type.name()), () -> GroundcoverBlock.looseOre(BlockBehaviour.Properties.of(Material.GRASS).strength(0.05F, 0.0F).sound(SoundType.NETHER_ORE).noCollission()), TFCEItemGroup.ORES)
    );

    public static final Map<TFCEMetal, Map<TFCEMetal.BlockType, RegistryObject<Block>>> METALS = Helpers.mapOfKeys(TFCEMetal.class, metal ->
            Helpers.mapOfKeys(TFCEMetal.BlockType.class, type -> type.has(metal), type ->
                    register(("metal/" + type.name() + "/" + metal.name()), type.create(metal), type.createBlockItem(new Item.Properties().tab(TFCEItemGroup.METAL)))
            )
    );


    private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> blockSupplier)
    {
        return register(name, blockSupplier, (Function<T, ? extends BlockItem>) null);
    }

    private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> blockSupplier, CreativeModeTab group)
    {
        return register(name, blockSupplier, block -> new BlockItem(block, new Item.Properties().tab(group)));
    }

    private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> blockSupplier, @Nullable Function<T, ? extends BlockItem> blockItemFactory)
    {
        return RegistrationHelpers.registerBlock(BLOCKS, TFCEItems.ITEMS, name, blockSupplier, blockItemFactory);
    }

}
