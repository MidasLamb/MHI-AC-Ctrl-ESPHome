import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import (
    climate
)
from esphome.const import (
    CONF_ID,
    CONF_UART_ID,
)

DEPENDENCIES = []
AUTO_LOAD = []

CONF_MHI_AC_CTRL_ID = "mhi_ac_ctrl_id"
CONF_DECRYPTION_KEY = "decryption_key"

mhi_ac_ctrl_ns = cg.esphome_ns.namespace("mhi_ac_ctrl_")
MHI_AC_CTRL = mhi_ac_ctrl_ns.class_("Mhi_ac_ctrl", cg.EntityBase)

CONFIG_SCHEMA = climate.CLIMATE_SCHEMA.extend({
    cv.GenerateID(): cv.declare_ID(mhi_ac_ctrl_ns),
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await climate.register_climate(var, config)

    cg.add(var.set_supports_cool(config[CONF_SUPPORTS_COOL]))
    cg.add(var.set_supports_heat(config[CONF_SUPPORTS_HEAT]))
    if CONF_SENSOR in config:
        sens = await cg.get_variable(config[CONF_SENSOR])
        cg.add(var.set_sensor(sens))
    if CONF_RECEIVER_ID in config:
        receiver = await cg.get_variable(config[CONF_RECEIVER_ID])
        cg.add(receiver.register_listener(var))

    transmitter = await cg.get_variable(config[CONF_TRANSMITTER_ID])
    cg.add(var.set_transmitter(transmitter))