package claustra01.tfcelem.event;

import claustra01.tfcelem.block.TFCEBlocks;
import claustra01.tfcelem.util.TFCEMetal;
import net.dries007.tfc.client.RenderHelpers;
import net.dries007.tfc.util.Helpers;
import net.minecraft.client.renderer.ItemBlockRenderTypes;
import net.minecraft.client.renderer.RenderType;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.client.event.TextureStitchEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

public class ClientEvents {

    public static void init() {
        final IEventBus bus = FMLJavaModLoadingContext.get().getModEventBus();
        bus.addListener(ClientEvents::clientSetup);
        bus.addListener(ClientEvents::onTextureStitch);
    }

    public static void clientSetup(FMLClientSetupEvent event) {
        final RenderType cutout = RenderType.cutout();
        TFCEBlocks.GRADED_ORES.values().forEach(map -> map.values().forEach(inner -> inner.values().forEach(reg -> ItemBlockRenderTypes.setRenderLayer(reg.get(), cutout))));
    }

    public static void onTextureStitch(TextureStitchEvent.Pre event) {
        final ResourceLocation sheet = event.getAtlas().location();
        if (sheet.equals(RenderHelpers.BLOCKS_ATLAS)) {
            for (TFCEMetal metal : TFCEMetal.values()) {
                event.addSprite(Helpers.identifier("block/metal/full/" + metal.getSerializedName()));
            }
        }
    }
}
