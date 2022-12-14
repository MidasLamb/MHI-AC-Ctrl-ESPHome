import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import (
    CONF_ID,
    CONF_UART_ID,
)

DEPENDENCIES = []
AUTO_LOAD = ["sensor"]

CONF_MHI_AC_CTRL_ID = "mhi_ac_ctrl_id"
CONF_DECRYPTION_KEY = "decryption_key"

mhi_ac_ctrl_ns = cg.esphome_ns.namespace("mhi_ac_ctrl_")
MHI_AC_CTRL = mhi_ac_ctrl_ns.class_("Dsmr", cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({

}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    # uart_component = yield cg.get_variable(config[CONF_UART_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var)

    # # Crypto
    # cg.add_library("1168", "0.2.0")