package claustra01.tfcelem.util;

import net.dries007.tfc.util.registry.RegistryRock;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.Material;

public enum TFCEOre {

    GALENA(true),
    NATIVE_PLATINUM(true),
    BAUXITE(true),
    PITCHBLENDE(true),
    NATIVE_OSMIUM(true);

    private final boolean grade;

    TFCEOre(boolean grade) {
        this.grade = grade;
    }

    public boolean isGraded() {
        return grade;
    }

    public Block create(RegistryRock rock) {
        BlockBehaviour.Properties properties = BlockBehaviour.Properties.of(Material.STONE).sound(SoundType.STONE).strength(rock.category().hardness(6.5F), 10.0F).requiresCorrectToolForDrops();
        return new Block(properties);
    }
}
