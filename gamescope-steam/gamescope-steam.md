# add gamescope with steam to gdm on fedora

![gamescope-steam](gamescope-steam.jpg)

this guide explains how to add gamescope to the gdm on fedora to get steamdeck-like experience

### why?

- less input lag compared to gnome, because gamescope allow tearing, useful for online shooters like cs
- gamepad friendly ui

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

### fix switch to desktop button in power menu


```sh
mkdir /var/home/gmanka/.var/app/com.valvesoftware.Steam/bin
echo '''
#!/usr/bin/bash
flatpak-spawn --host bash -c "pkill -u $USER"
''' | tee ~/.var/app/com.valvesoftware.Steam/bin/steamos-session-select
chmod +x ~/.var/app/com.valvesoftware.Steam/bin/steamos-session-select

export flatpak_path=$(flatpak run --command=bash com.valvesoftware.Steam -c 'echo $PATH')
export newpath=$HOME/.var/app/com.valvesoftware.Steam/bin:$flatpak_path
sudo flatpak override --system --talk-name=org.freedesktop.Flatpak --env=PATH=$newpath com.valvesoftware.Steam
```

### done

now you can reboot and you will see a gamescope session in gdm

### bugs in power menu

- turn off system (black screen instead of turn off)
- suspend system (black screen instead of suspend)
- restart system (black screen instead of restart)

if you know how to fix bugs please show me, i will add it to guide

### credits

https://discussion.fedoraproject.org/t/notes-from-building-a-steam-appliance-on-silverblue/35267

