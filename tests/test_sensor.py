"""Test NFL Scores Sensors"""
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.nfl.const import DOMAIN
from tests.const import CONFIG_DATA


async def test_sensor(hass):

    entry = MockConfigEntry(
        domain=DOMAIN,
        title="NFL Scores",
        data=CONFIG_DATA,
    )

    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert "nfl" in hass.config.components
