import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig
from .const import DOMAIN

class SimpleIrrigationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            zone_id = str(user_input["zone_id"])
            await self.async_set_unique_id(f"simple_irrigation_zone_{zone_id}")
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=f"Zone {zone_id}: {user_input['zone_name']}",
                data={
                    "zone_name": user_input["zone_name"],
                    "zone_id": zone_id,
                    "relay_switch": user_input["relay_switch"],
                },
            )

        data_schema = vol.Schema(
            {
                vol.Required("zone_name"): str,
                vol.Required("zone_id"): int,
                vol.Required("relay_switch"): EntitySelector(
                    EntitySelectorConfig(domain="switch")
                ),
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
