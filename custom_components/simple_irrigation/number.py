from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    zone_id = entry.data["zone_id"]
    zone_name = entry.data["zone_name"]

    numbers = [
        IrrigationDurationEntity(entry, f"{zone_id}_s1_duration", f"{zone_name} S1 Duration", 15),
        IrrigationDurationEntity(entry, f"{zone_id}_s2_duration", f"{zone_name} S2 Duration", 15),
        IrrigationDurationEntity(entry, f"{zone_id}_s3_duration", f"{zone_name} S3 Duration", 15),
    ]
    async_add_entities(numbers)

class IrrigationDurationEntity(NumberEntity):
    def __init__(self, entry, key, name, default_val):
        self._attr_unique_id = f"simple_irrigation_{key}"
        self._attr_name = name
        self._attr_native_value = default_val
        self._attr_native_min_value = 1
        self._attr_native_max_value = 120
        self._attr_native_step = 1
        self._attr_native_unit_of_measurement = "min"
        self._attr_icon = "mdi:timer-outline"

    async def async_set_native_value(self, value: float) -> None:
        self._attr_native_value = int(value)
        self.async_write_ha_state()
