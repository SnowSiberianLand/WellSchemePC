import mod_dm as dm
import mod_orm as db
from collections import OrderedDict
import db_utils


def ora_connection(connection_string, meta=None):
    if meta is None:
        meta = connection_string
    red = db_utils.openTargetRDS(db.db_oracle, connection_string, meta)
    if red is None:
        print("Can't open oracle connect.")
        return False, connection_string
    return red, connection_string


def rds_connect(connection_string):
    red = db_utils.openTargetRDS(db.db_sqlite, connection_string)
    if red is None:
        print("Can't open rds connect.")
        return False
    return red, connection_string


def base_data_loader_if_xml_exist(red: dm.IDataStorage, xml_dict: OrderedDict):
    connection_string = red.getPath().split('//')[1]
    if xml_dict['WellSchemeData']['StringOfBase'] == '@' + connection_string:
        name_finder = False
        key_for_find = '@id'
    else:
        name_finder = True
        key_for_find = '@Name'

    xdata = xml_dict['WellSchemeData']
    print("Try to parse rds base data...")
    registry = red.getRegHelper()

    if name_finder:
        profile_ = registry.getProfileRegistry().find(xdata['NameOfProfile'][key_for_find])
    else:
        profile_ = registry.getProfileRegistry().findByName(xdata['NameOfProfile'][key_for_find])
    if profile_ is None:
        print("Error: we have null count profiles list. App wasn't working")
        return False
    print("Profile read successfully")

    if name_finder:
        model_geo = registry.getModelRegistry().find(xdata['GeoModel'][key_for_find])
    else:
        model_geo = registry.getModelRegistry().findByName(xdata['GeoModel'][key_for_find])

    if model_geo is None:
        print("Error: we have null count model list. App wasn't working")
        return False
    print("Model read successfully")

    if name_finder:
        model_gvk = registry.getModelRegistry().find(xdata['GvkModel'][key_for_find])
    else:
        model_gvk = registry.getModelRegistry().findByName(xdata['GvkModel'][key_for_find])
    if model_gvk is None:
        print("Error: we have null count model list. App wasn't working")
        return False
    print("Model read successfully")
    print("Create rds settings successfully")
    return True


def set_base_data_loader_if_xml_exist(red: dm.IDataStorage, xml_dict, profile_name, model_name_geo, model_gvk_name):
    key_for_find = '@Name'
    xdata = xml_dict['WellSchemeData']
    print("Try to parse rds base data...")
    registry = red.getRegHelper()
    xdata['NameOfProfile'][key_for_find] = profile_name
    profile_ = registry.getProfileRegistry().findByName(profile_name)
    if profile_ is None:
        print("Error: we have null count profiles list. App wasn't working")
        return False
    else:
        xdata['NameOfProfile']["@id"] = profile_.getID()
    print("Profile read successfully")

    xdata['GeoModel'][key_for_find] = model_name_geo
    model_geo = registry.getModelRegistry().findByName(xdata['GeoModel'][key_for_find])
    if model_geo is None:
        print("Error: we have null count model list. App wasn't working")
        return False
    else:
        xdata['GeoModel']["@id"] = model_geo.getID()
    print("Model read successfully")

    xdata['GvkModel'][key_for_find] = model_gvk_name
    model_gvk = registry.getModelRegistry().findByName(xdata['GvkModel'][key_for_find])
    if model_gvk is None:
        print("Error: we have null count model list. App wasn't working")
        return False
    else:
        xdata['GvkModel']["@id"] = model_gvk.getID()
    print("Model read successfully")
    print("Create rds settings successfully")
    return True


def base_data_loader_if_xml_not_exist(red: dm.IDataStorage, profile_id: int, model_id_geo: int, model_gvk_id: int, xml_dict: OrderedDict):
    xml_dict['WellSchemeData']['StringOfBase'] = '@'+red.getPath().split('//')[1]
    xdata = xml_dict['WellSchemeData']
    xdata["GvkModel"]["@id"] = model_gvk_id
    xdata["GeoModel"]["@id"] = model_id_geo
    xdata["NameOfProfile"]["@id"] = profile_id
    registry = red.getRegHelper()
    profile_ = registry.getProfileRegistry().find(profile_id)
    if profile_ is None:
        print("Error: we have null count profiles list. App wasn't working")
        return False
    else:
        xdata['NameOfProfile']["@Name"] = profile_.getName()

    model_gvk = registry.getModelRegistry().find(model_gvk_id)
    if model_gvk is None:
        print("Error: we have null count model list. App wasn't working")
        return False
    else:
        xdata['GvkModel']["@Name"] = model_gvk.getName()

    model_geo = registry.getModelRegistry().find(model_id_geo)
    if model_geo is None:
        print("Error: we have null count model list. App wasn't working")
        return False
    else:
        xdata['GeoModel']["@Name"] = model_geo.getName()
    return base_data_loader_if_xml_exist(red, red.getPath(), xml_dict)


if __name__ == '__main__':
    conn_string = "D:\ResViewE.rds"
    dst, cn_string = rds_connect(conn_string)
    print(dst.getPath().split('//')[1])