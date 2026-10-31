from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import INTERVAL_OPTIONS

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    zone_id = entry.data["zone_id"]
    zone_name = entry.data["zone_name"]

    async_add_entities([IrrigationIntervalSelect(entry, f"{zone_id}_interval", f"{zone_name} Interval")])

class IrrigationIntervalSelect(SelectEntity):
    def __init__(self, entry, key, name):
        self._attr_unique_id = f"simple_irrigation_{key}"
        self._attr_name = name
        self._attr_options = INTERVAL_OPTIONS
        self._attr_current_option = INTERVAL_OPTIONS[0]
        self._attr_icon = "mdi:calendar-repeat"

    async def async_select_option(self, option: str) -> None:
        self._attr_current_option = option
        self.async_write_ha_state()
