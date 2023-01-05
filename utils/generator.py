import gen_models
import gen_states
import gen_lang

gen_models.ore_model_gen()
gen_models.metal_model_gen()

gen_states.ore_blockstate_gen()

gen_lang.gen_ore_lang()
