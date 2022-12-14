import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import (
    climate,
    sensor
)
from esphome.const import (
    CONF_ID,
    CONF_UART_ID,
    CONF_SENSOR
)

DEPENDENCIES = []
AUTO_LOAD = []

CONF_MHI_AC_CTRL_ID = "mhi_ac_ctrl_id"
CONF_DECRYPTION_KEY = "decryption_key"

mhi_ac_ctrl_ns = cg.esphome_ns.namespace("mhi_ac_ctrl_")
MHI_AC_CTRL = mhi_ac_ctrl_ns.class_("Mhi_ac_ctrl", cg.EntityBase)

CONFIG_SCHEMA = climate.CLIMATE_SCHEMA.extend({
    cv.GenerateID(): cv.declare_ID(mhi_ac_ctrl_ns),
    cv.Required(CONF_SENSOR): cv.use_id(sensor.Sensor),
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await climate.register_climate(var, config)
