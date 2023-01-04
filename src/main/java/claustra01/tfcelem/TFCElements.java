package claustra01.tfcelem;

import claustra01.tfcelem.item.TFCEItems;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.ForgeHooksClient;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.fml.loading.FMLEnvironment;

@Mod("tfcelem")
public class TFCElements {

    public static final String namespace = "tfc";

    public TFCElements() {
        final IEventBus bus = FMLJavaModLoadingContext.get().getModEventBus();
        TFCEItems.ITEMS.register(bus);

        if (FMLEnvironment.dist == Dist.CLIENT) {
            //ForgeHooksClient.ClientEvents.init();
        }
    }

}
