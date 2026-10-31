from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    zone_id = entry.data["zone_id"]
    zone_name = entry.data["zone_name"]

    sensors = [
        IrrigationStatusSensor(entry, f"{zone_id}_next_run", f"{zone_name} Next Run", "mdi:clock-end"),
        IrrigationStatusSensor(entry, f"{zone_id}_last_run", f"{zone_name} Last Run", "mdi:history"),
    ]
    async_add_entities(sensors)

class IrrigationStatusSensor(SensorEntity):
    def __init__(self, entry, key, name, icon):
        self._attr_unique_id = f"simple_irrigation_{key}"
        self._attr_name = name
        self._attr_icon = icon
        self._attr_native_value = "Never"

    def set_status(self, status_str: str):
        self._attr_native_value = status_str
        self.async_write_ha_state()
