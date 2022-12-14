import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    ICON_EMPTY,
    LAST_RESET_TYPE_NEVER,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_NONE,
    UNIT_AMPERE,
    UNIT_EMPTY,
    UNIT_VOLT,
    UNIT_WATT_HOURS,
    UNIT_WATT,
)
from . import MHI_AC_CTRL, CONF_MHI_AC_CTRL_ID

AUTO_LOAD = ["mhi_ac_ctrl"]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_MHI_AC_CTRL_ID): cv.use_id(MHI_AC_CTRL),
        cv.Optional("testsensor"): sensor.sensor_schema(
            UNIT_EMPTY,
            ICON_EMPTY,
            3,
            DEVICE_CLASS_EMPTY,
            STATE_CLASS_MEASUREMENT,
            LAST_RESET_TYPE_NEVER,
        ),
    }
).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    hub = yield cg.get_variable(config[CONF_MHI_AC_CTRL_ID])

    sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf.get("id")
        if id and id.type == sensor.Sensor:
            s = yield sensor.new_sensor(conf)
            cg.add(getattr(hub, f"set_{key}")(s))
            sensors.append(f"F({key})")

    cg.add_define("MHI_AC_CTRL_SENSOR_LIST(F, sep)", cg.RawExpression(" sep ".join(sensors)))