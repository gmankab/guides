# desktop in container

this guide allows you to run different desktop environments in toolbox containers on fedora

### gnome

tested host environments:
- hyprland (work)
- gnome (work)
- niri (not work)

```shell
toolbox create -y --distro=fedora gnome
toolbox enter gnome
sudo dnf install -y @gnome-desktop
MUTTER_DEBUG_DUMMY_MODE_SPECS=1920x1040 dbus-run-session -- gnome-shell --nested
```

### gnome mobile

note thet gnome mobile will look like a desktop version of gnome untill you install [force phone mode](https://github.com/vixalien/force-phone-mode) extension

tested host environments:
- hyprland (work)
- gnome (work)
- niri (not work)

```shell
toolbox create -y --distro=fedora gnome-mobile
toolbox enter gnome-mobile
sudo dnf copr enable -y silliewous/gnome-mobile
sudo dnf install -y mobile-shell
MUTTER_DEBUG_DUMMY_MODE_SPECS=1920x1040 dbus-run-session -- gnome-shell --nested
```

### phosh

tested host environments:
- hyprland (work)
- gnome (work)
- niri (work)

```shell
toolbox create -y --distro=fedora phosh
toolbox enter phosh
sudo dnf install -y phosh
phoc -E '/usr/libexec/phosh -U'
```

### cosmic

tested host environments:
- hyprland (not work)
- gnome (work but buggy)
- niri (work but buggy)

```shell
toolbox create -y --distro=fedora cosmic
toolbox enter cosmic
sudo dnf install -y cosmic-comp
cosmic-comp
```

### plasma

tested host environments:
- hyprland (work)
- gnome (problems)
- niri (problems)

```shell
toolbox create -y --distro=fedora plasma
toolbox enter plasma
sudo dnf install -y @kde-desktop
dbus-run-session -- startplasma-wayland # works on hyprland, does not work on gnome and niri
dbus-run-session -- plasmashell # works everywhere but buggy
```

### what does not work

- gnome in alpine/postmarketos toolbox container does not work

