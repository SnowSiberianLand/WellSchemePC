from collections import OrderedDict
import mod_dm as dm
import mod_cmn as cmn


def generate_default_well(red: dm.IDataStorage, well_from_dst: dm.IWell, profile: dm.IProfile, geo_model: dm.IModel, gvk_model: dm.IModel):
    well_dict = OrderedDict()
    return well_dict