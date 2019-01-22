class Recipe(object):

    def __init__(self, recipe_dict):
        self.name = recipe_dict['NAME']
        self.version = recipe_dict['VERSION']
        self.type = recipe_dict['TYPE']
        self.brewer = recipe_dict['BREWER']
        self.asst_brewer = recipe_dict['ASST_BREWER']
        self.batch_size = recipe_dict['BATCH_SIZE']
        self.boil_size = recipe_dict['BOIL_SIZE']
        self.boil_time = recipe_dict['BOIL_TIME']
        self.efficiency = recipe_dict['EFFICIENCY']
        self.hops = self.map_hops(recipe_dict['HOPS']['HOP'])
        self.fermentables = self.map_fermentables(recipe_dict['FERMENTABLES']['FERMENTABLE'])
        self.yeasts = self.map_yeasts(recipe_dict['YEASTS']['YEAST'])
        self.style = Style(recipe_dict['STYLE'])
        self.equipment = Equipment(recipe_dict['EQUIPMENT'])
        self.mash = Mash(recipe_dict['MASH'])
        self.notes = recipe_dict['NOTES']
        self.taste_notes = recipe_dict['TASTE_NOTES']
        self.taste_rating = recipe_dict['TASTE_RATING']
        self.og = recipe_dict['OG']
        self.fg = recipe_dict['FG']
        self.carbonation = recipe_dict['CARBONATION']
        self.fermentation_stages = recipe_dict['FERMENTATION_STAGES']
        self.primary_age = recipe_dict['PRIMARY_AGE']
        self.primary_temp = recipe_dict['PRIMARY_TEMP']
        self.secondary_age = recipe_dict['SECONDARY_AGE']
        self.secondary_temp = recipe_dict['SECONDARY_TEMP']
        self.tertiary_age = recipe_dict['TERTIARY_AGE']
        self.age = recipe_dict['AGE']
        self.age_temp = recipe_dict['AGE_TEMP']
        self.carbonation_used = recipe_dict['CARBONATION_USED']
        self.forced_carbonation = recipe_dict['FORCED_CARBONATION']
        self.priming_sugar_name = recipe_dict['PRIMING_SUGAR_NAME']
        self.priming_sugar_equiv = recipe_dict['PRIMING_SUGAR_EQUIV']
        self.keg_priming_factor = recipe_dict['KEG_PRIMING_FACTOR']
        self.carbonation_temp = recipe_dict['CARBONATION_TEMP']
        self.display_carb_temp = recipe_dict['DISPLAY_CARB_TEMP']
        self.date = recipe_dict['DATE']
        self.est_og = recipe_dict['EST_OG']
        self.est_fg = recipe_dict['EST_FG']
        self.est_color = recipe_dict['EST_COLOR']
        self.ibu = recipe_dict['IBU']
        self.ibu_method = recipe_dict['IBU_METHOD']
        self.est_abv = recipe_dict['EST_ABV']
        self.abv = recipe_dict['ABV']
        self.actual_efficiency = recipe_dict['ACTUAL_EFFICIENCY']
        self.calories = recipe_dict['CALORIES']
        self.display_batch_size = recipe_dict['DISPLAY_BATCH_SIZE']
        self.display_boil_size = recipe_dict['DISPLAY_BOIL_SIZE']
        self.display_og = recipe_dict['DISPLAY_OG']
        self.display_fg = recipe_dict['DISPLAY_FG']
        self.display_primary_temp = recipe_dict['DISPLAY_PRIMARY_TEMP']
        self.display_secondary_temp = recipe_dict['DISPLAY_SECONDARY_TEMP']
        self.display_tertiary_temp = recipe_dict['DISPLAY_TERTIARY_TEMP']
        self.display_age_temp = recipe_dict['DISPLAY_AGE_TEMP']

    def map_hops(self, hops_dict):
        hops = []
        if isinstance(hops_dict, (list)):
            for hop_dict in hops_dict:
                hops.append(Hop(hop_dict))
        else:
            hops.append(Hop(hops_dict))

        return hops

    def map_fermentables(self, fermentables_dict):
        fermentables = []
        if isinstance(fermentables_dict, (list)):
            for fermentable_dict in fermentables_dict:
                fermentables.append(Fermentable(fermentable_dict))
        else:
            fermentables.append(Fermentable(fermentables_dict))

        return fermentables

    def map_yeasts(self, yeasts_dict):
        yeasts = []
        if isinstance(yeasts_dict, (list)):
            for yeast_dict in yeasts_dict:
                yeasts.append(Yeast(yeast_dict))
        else:
            yeasts.append(Yeast(yeasts_dict))

        return yeasts

class Hop(object):

    def __init__(self, hop_dict):
        self.name = hop_dict['NAME']
        self.version = hop_dict['VERSION']
        self.origin = hop_dict['ORIGIN']
        self.alpha = hop_dict['ALPHA']
        self.amount = hop_dict['AMOUNT']
        self.use = hop_dict['USE']
        self.time = hop_dict['TIME']
        self.notes = hop_dict['NOTES']
        self.type = hop_dict['TYPE']
        self.form = hop_dict['FORM']
        self.beta = hop_dict['BETA']
        self.hsi = hop_dict['HSI']
        self.display_amount = hop_dict['DISPLAY_AMOUNT']
        self.inventory = hop_dict['INVENTORY']
        self.display_time = hop_dict['DISPLAY_TIME']

class Fermentable(object):
    def __init__(self, fermentable_dict):
        self.name = fermentable_dict['NAME']
        self.version = fermentable_dict['VERSION']
        self.type = fermentable_dict['TYPE']
        self.amount = fermentable_dict['AMOUNT']
        self.yielding = fermentable_dict['YIELD']
        self.color = fermentable_dict['COLOR']
        self.add_after_boil = fermentable_dict['ADD_AFTER_BOIL']
        self.origin = fermentable_dict['ORIGIN']
        self.supplier = fermentable_dict['SUPPLIER']
        self.notes = fermentable_dict['NOTES']
        self.coarse_fine_diff = fermentable_dict['COARSE_FINE_DIFF']
        self.moisture = fermentable_dict['MOISTURE']
        self.diastatic_power = fermentable_dict['DIASTATIC_POWER']
        self.protein = fermentable_dict['PROTEIN']
        self.max_in_batch = fermentable_dict['MAX_IN_BATCH']
        self.recommend_mash = fermentable_dict['RECOMMEND_MASH']
        self.ibu_gal_per_lb = fermentable_dict['IBU_GAL_PER_LB']
        self.display_amount = fermentable_dict['DISPLAY_AMOUNT']
        self.inventory = fermentable_dict['INVENTORY']
        self.potential = fermentable_dict['POTENTIAL']
        self.display_color = fermentable_dict['DISPLAY_COLOR']
        self.extract_substitute = fermentable_dict['EXTRACT_SUBSTITUTE']

class Yeast(object):

    def __init__(self, yeast_dict):
        self.name = yeast_dict['NAME']
        self.version = yeast_dict['VERSION']
        self.type = yeast_dict['TYPE']
        self.form = yeast_dict['FORM']
        self.amount = yeast_dict['AMOUNT']
        self.amount_is_weight = yeast_dict['AMOUNT_IS_WEIGHT']
        self.laboratory = yeast_dict['LABORATORY']
        self.product_id = yeast_dict['PRODUCT_ID']
        self.min_temperature = yeast_dict['MIN_TEMPERATURE']
        self.max_temperature = yeast_dict['MAX_TEMPERATURE']
        self.flocculation = yeast_dict['FLOCCULATION']
        self.attenuation = yeast_dict['ATTENUATION']
        self.notes = yeast_dict['NOTES']
        self.best_for = yeast_dict['BEST_FOR']
        self.max_reuse = yeast_dict['MAX_REUSE']
        self.times_cultured = yeast_dict['TIMES_CULTURED']
        self.add_to_secondary = yeast_dict['ADD_TO_SECONDARY']
        self.display_amount = yeast_dict['DISPLAY_AMOUNT']
        self.disp_min_temp = yeast_dict['DISP_MIN_TEMP']
        self.disp_max_temp = yeast_dict['DISP_MAX_TEMP']
        self.inventory = yeast_dict['INVENTORY']
        self.culture_date = yeast_dict['CULTURE_DATE']

class Style(object):

    def __init__(self, style_dict):
        self.name = style_dict['NAME']
        self.version = style_dict['VERSION']
        self.category = style_dict['CATEGORY']
        self.category_number = style_dict['CATEGORY_NUMBER']
        self.style_letter = style_dict['STYLE_LETTER']
        self.style_guide = style_dict['STYLE_GUIDE']
        self.type = style_dict['TYPE']
        self.og_min = style_dict['OG_MIN']
        self.og_max = style_dict['OG_MAX']
        self.fg_min = style_dict['FG_MIN']
        self.fg_max = style_dict['FG_MAX']
        self.ibu_min = style_dict['IBU_MIN']
        self.ibu_max = style_dict['IBU_MAX']
        self.color_min = style_dict['COLOR_MIN']
        self.color_max = style_dict['COLOR_MAX']
        self.carb_min = style_dict['CARB_MIN']
        self.carb_max = style_dict['CARB_MAX']
        self.abv_min = style_dict['ABV_MIN']
        self.abv_max = style_dict['ABV_MAX']
        self.notes = style_dict['NOTES']
        self.profile = style_dict['PROFILE']
        self.ingredients = style_dict['INGREDIENTS']
        self.examples = style_dict['EXAMPLES']
        self.display_og_min = style_dict['DISPLAY_OG_MIN']
        self.display_og_max = style_dict['DISPLAY_OG_MAX']
        self.display_fg_min = style_dict['DISPLAY_FG_MIN']
        self.display_fg_max = style_dict['DISPLAY_FG_MAX']
        self.display_color_min = style_dict['DISPLAY_COLOR_MIN']
        self.display_color_max = style_dict['DISPLAY_COLOR_MAX']
        self.og_range = style_dict['OG_RANGE']
        self.fg_range = style_dict['FG_RANGE']
        self.ibu_range = style_dict['IBU_RANGE']
        self.carb_range = style_dict['CARB_RANGE']
        self.color_range = style_dict['COLOR_RANGE']
        self.abv_range = style_dict['ABV_RANGE']

class Equipment(object):

    def __init__(self, equipment_dict):
        self.name = equipment_dict['NAME']
        self.version = equipment_dict['VERSION']
        self.boil_size = equipment_dict['BOIL_SIZE']
        self.batch_size = equipment_dict['BATCH_SIZE']
        self.tun_volume = equipment_dict['TUN_VOLUME']
        self.tun_weight = equipment_dict['TUN_WEIGHT']
        self.tun_specific_heat = equipment_dict['TUN_SPECIFIC_HEAT']
        self.top_up_water = equipment_dict['TOP_UP_WATER']
        self.trub_chiller_loss = equipment_dict['TRUB_CHILLER_LOSS']
        self.evap_rate = equipment_dict['EVAP_RATE']
        self.boil_time = equipment_dict['BOIL_TIME']
        self.calc_boil_volume = equipment_dict['CALC_BOIL_VOLUME']
        self.lauter_deadspace = equipment_dict['LAUTER_DEADSPACE']
        self.top_up_kettle = equipment_dict['TOP_UP_KETTLE']
        self.hop_utilization = equipment_dict['HOP_UTILIZATION']
        self.cooling_loss_pct = equipment_dict['COOLING_LOSS_PCT']
        self.notes = equipment_dict['NOTES']
        self.display_boil_size = equipment_dict['DISPLAY_BOIL_SIZE']
        self.display_batch_size = equipment_dict['DISPLAY_BATCH_SIZE']
        self.display_tun_volume = equipment_dict['DISPLAY_TUN_VOLUME']
        self.display_tun_weight = equipment_dict['DISPLAY_TUN_WEIGHT']
        self.display_top_up_water = equipment_dict['DISPLAY_TOP_UP_WATER']
        self.display_trub_chiller_loss = equipment_dict['DISPLAY_TRUB_CHILLER_LOSS']
        self.display_lauter_deadspace = equipment_dict['DISPLAY_LAUTER_DEADSPACE']
        self.display_top_up_kettle = equipment_dict['DISPLAY_TOP_UP_KETTLE']

class Mash(object):

    def __init__(self, mash_dict):
        self.name = mash_dict['NAME']
        self.version = mash_dict['VERSION']
        self.grain_temp = mash_dict['GRAIN_TEMP']
        self.sparge_temp = mash_dict['SPARGE_TEMP']
        self.ph = mash_dict['PH']
        self.tun_weight = mash_dict['TUN_WEIGHT']
        self.tun_specific_heat = mash_dict['TUN_SPECIFIC_HEAT']
        self.equip_adjust = mash_dict['EQUIP_ADJUST']
        self.notes = mash_dict['NOTES']
        self.display_grain_temp = mash_dict['DISPLAY_GRAIN_TEMP']
        self.display_tun_temp = mash_dict['DISPLAY_TUN_TEMP']
        self.display_sparge_temp = mash_dict['DISPLAY_SPARGE_TEMP']
        self.mash_steps = self.map_mash_steps(mash_dict['MASH_STEPS']['MASH_STEP'])

    def map_mash_steps(self, mash_step_dicts):
        mash_steps = []
        if isinstance(mash_step_dicts, (list)):
            for mash_step_dict in mash_step_dicts:
                mash_steps.append(MashStep(mash_step_dict))
        else:
            mash_steps.append(MashStep(mash_step_dict))

        return mash_steps


class MashStep(object):

    def __init__(self, mash_step_dict):
        self.name = mash_step_dict['NAME']
        self.version = mash_step_dict['VERSION']
        self.type = mash_step_dict['TYPE']
        self.infuse_amount = mash_step_dict['INFUSE_AMOUNT']
        self.step_time = mash_step_dict['STEP_TIME']
        self.step_temp = mash_step_dict['STEP_TEMP']
        self.ramp_time = mash_step_dict['RAMP_TIME']
        self.end_temp = mash_step_dict['END_TEMP']
        self.description = mash_step_dict['DESCRIPTION']
        self.water_grain_ratio = mash_step_dict['WATER_GRAIN_RATIO']
        self.decoction_amt = mash_step_dict['DECOCTION_AMT']
        self.infuse_temp = mash_step_dict['INFUSE_TEMP']
        self.display_step_temp = mash_step_dict['DISPLAY_STEP_TEMP']
        self.display_infuse_amt = mash_step_dict['DISPLAY_INFUSE_AMT']
