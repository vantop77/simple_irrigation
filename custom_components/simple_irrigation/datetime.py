from datetime import time
from homeassistant.components.datetime import TimeEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    zone_id = entry.data["zone_id"]
    zone_name = entry.data["zone_name"]

    times = [
        IrrigationTimeEntity(entry, f"{zone_id}_s1_time", f"{zone_name} S1 Time", time(8, 0)),
        IrrigationTimeEntity(entry, f"{zone_id}_s2_time", f"{zone_name} S2 Time", time(14, 0)),
        IrrigationTimeEntity(entry, f"{zone_id}_s3_time", f"{zone_name} S3 Time", time(20, 0)),
    ]
    async_add_entities(times)

class IrrigationTimeEntity(TimeEntity):
    def __init__(self, entry, key, name, default_time):
        self._attr_unique_id = f"simple_irrigation_{key}"
        self._attr_name = name
        self._attr_native_value = default_time
        self._attr_icon = "mdi:clock-outline"

    async def async_set_value(self, value: time) -> None:
        self._attr_native_value = value
        self.async_write_ha_state()
