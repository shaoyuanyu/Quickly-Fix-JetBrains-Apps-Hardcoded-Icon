import os

# the ".desktop" files of jetbrains applications lie in "~/.local/share/applications/" by default
jetbrains_desktop_path = os.path.expanduser("~/.local/share/applications/")

# add here if you have other jetbrains applications
# key is the prefix of the ".desktop" file
# value is <product-name> for Icon
app_to_icon_map = {
    "Android Studio": "android-studio",
    "jetbrains-idea": "idea",
    "jetbrains-pycharm": "pycharm",
    "jetbrains-rustrover": "rustrover",
    "jetbrains-toolbox": "jetbrains-toolbox",
    "jetbrains-webstorm": "webstorm",
    "jetbrains-clion": "clion",
    "jetbrains-datagrip": "datagrip",
}

def main():
    for root, dirs, filenames in os.walk(jetbrains_desktop_path):
        for filename in filenames:
            for app, icon in app_to_icon_map.items():
                if filename.startswith(app):
                    new_icon_value = icon
                    file_path = os.path.join(root, filename)

                    with open(file_path, 'r') as file:
                        lines = file.readlines()

                    # modify the line starting with "Icon="
                    with open(file_path, 'w') as file:
                        for line in lines:
                            if line.startswith('Icon='):
                                print("Found ", filename, ", ", line, ", changing to ", new_icon_value)
                                file.write(f'Icon={new_icon_value}\n')
                            else:
                                file.write(line)

if __name__ == '__main__':
    main()