from deebotozmo.models import Vacuum
from deebotozmo.vacuum_bot import VacuumBot

from .const import DOMAIN


def get_device_info(vacuum_bot: VacuumBot):
    device: Vacuum = vacuum_bot.vacuum
    identifiers = set()
    if device.did:
        identifiers.add((DOMAIN, device.did))
    if device.name:
        identifiers.add((DOMAIN, device.name))

    if not identifiers:
        # we don't get a identifier to identify the device correctly abort
        return None

    return {
        "identifiers": identifiers,
        "name": device.get("nick", "Deebot vacuum"),
        "manufacturer": "Ecovacs",
        "model": device.get("deviceName", "Deebot vacuum"),
        "sw_version": vacuum_bot.fw_version,
    }
