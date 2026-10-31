from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    zone_id = entry.data["zone_id"]
    zone_name = entry.data["zone_name"]

    switches = [
        IrrigationSwitch(entry, f"{zone_id}_global_auto", f"{zone_name} Global Auto", "mdi:robot"),
        IrrigationSwitch(entry, f"{zone_id}_manual", f"{zone_name} Manual Run", "mdi:hand-tap"),
        IrrigationSwitch(entry, f"{zone_id}_s1_enabled", f"{zone_name} Schedule 1 Enable", "mdi:clock-check"),
        IrrigationSwitch(entry, f"{zone_id}_s2_enabled", f"{zone_name} Schedule 2 Enable", "mdi:clock-check"),
        IrrigationSwitch(entry, f"{zone_id}_s3_enabled", f"{zone_name} Schedule 3 Enable", "mdi:clock-check"),
    ]
    async_add_entities(switches)

class IrrigationSwitch(SwitchEntity):
    def __init__(self, entry, key, name, icon):
        self._entry = entry
        self._attr_unique_id = f"simple_irrigation_{key}"
        self._attr_name = name
        self._attr_icon = icon
        self._is_on = False

    @property
    def is_on(self) -> bool:
        return self._is_on

    async def async_turn_on(self, **kwargs):
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        self._is_on = False
        self.async_write_ha_state()
