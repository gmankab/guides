# gamescope with steam on fedora

![gamescope-steam](gamescope-steam.jpg)

this guide explains how to add gamescope to the gdm on fedora to get steamdeck-like experience

### install gamescope

for silverblue:

```sh
rpm-ostree install gamescope
```

for workstation:

```sh
sudo dnf install gamescope
```
### install steam

```sh
flatpak install flathub com.valvesoftware.Steam
```

### add session to gdm

```sh
echo '''
[Desktop Entry]
Name=gamescope
Comment=gamescope
Exec=gamescope --steam -- flatpak run com.valvesoftware.Steam -steamos3 -gamepadui -fulldesktopres
Type=Application
DesktopNames=gamescope
''' | sudo tee /usr/local/share/wayland-sessions/gamescope.desktop
```

