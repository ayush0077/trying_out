** start of main.py **

def add_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = ["Current User Settings:"]
    for key, value in settings.items():
        result.append(f"{key.capitalize()}: {value}")

    return "\n".join(result)+'\n'


# Test dictionary
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}


** end of main.py **

