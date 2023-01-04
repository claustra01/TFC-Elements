package claustra01.tfcelem.misc;

import claustra01.tfcelem.TFCElements;
import net.dries007.tfc.common.blocks.rock.Ore;
import net.dries007.tfc.common.capabilities.food.FoodCapability;
import net.dries007.tfc.common.items.TFCItems;
import net.dries007.tfc.util.Metal;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.common.util.Lazy;

import javax.annotation.Nonnull;
import java.util.function.Supplier;

public class TFCEItemGroup extends CreativeModeTab {

    public static final CreativeModeTab METAL = new TFCEItemGroup("metals", () -> new ItemStack((TFCItems.METAL_ITEMS.get(Metal.Default.WROUGHT_IRON)).get(Metal.ItemType.INGOT).get()));
    public static final CreativeModeTab ORES = new TFCEItemGroup("ores", () -> new ItemStack((TFCItems.GRADED_ORES.get(Ore.NATIVE_COPPER).get(Ore.Grade.NORMAL)).get()));

    private final Lazy<ItemStack> iconStack;

    private TFCEItemGroup(String label, Supplier<ItemStack> iconSupplier) {
        super(TFCElements.namespace + "." + label);
        this.iconStack = Lazy.of(() -> FoodCapability.setStackNonDecaying(iconSupplier.get()));
    }

    @Nonnull
    public ItemStack makeIcon() {
        return this.iconStack.get();
    }
}
