MIN_SENSITIVITY = 0.0
MAX_SENSITIVITY = 10.0


def _get_settings_core():
    from helpers import dependency
    from skeletons.account_helpers.settings_core import ISettingsCore

    return dependency.instance(ISettingsCore)


def clamp_sensitivity(value):
    return max(MIN_SENSITIVITY, min(MAX_SENSITIVITY, float(value)))


def parse_sensitivity(value, default):
    try:
        return clamp_sensitivity(float(value))
    except (TypeError, ValueError):
        return clamp_sensitivity(default)


def format_sensitivity(value):
    return "%.6f" % clamp_sensitivity(value)


def get_arcade_sensitivity():
    from account_helpers.settings_core.settings_constants import CONTROLS

    return _get_settings_core().getSetting(CONTROLS.MOUSE_ARCADE_SENS)


def get_sniper_sensitivity():
    from account_helpers.settings_core.settings_constants import CONTROLS

    return _get_settings_core().getSetting(CONTROLS.MOUSE_SNIPER_SENS)


def apply_sensitivities(arcade, sniper):
    import BigWorld
    from account_helpers.settings_core.settings_constants import CONTROLS

    arcade_value = clamp_sensitivity(arcade)
    sniper_value = clamp_sensitivity(sniper)

    settings_core = _get_settings_core()
    settings_core.applySetting(CONTROLS.MOUSE_ARCADE_SENS, arcade_value)
    settings_core.applySetting(CONTROLS.MOUSE_SNIPER_SENS, sniper_value)
    BigWorld.savePreferences()

    return arcade_value, sniper_value
