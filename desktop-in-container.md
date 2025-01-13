# desktop in container

this giude allows you to run different desktop environments in toolbox containers

### gnome

```shell
toolbox create --distro=fedora gnome
toolbox enter gnome
sudo dnf install -y @gnome-desktop
MUTTER_DEBUG_DUMMY_MODE_SPECS=1920x1040 dbus-run-session -- gnome-shell --nested --wayland
```

### phosh

```shell
toolbox create --distro=fedora phosh
toolbox enter phosh
sudo dnf install -y phosh
phoc -E '/usr/libexec/phosh -U'
```

### cosmic

```shell
toolbox create --distro=fedora cosmic
toolbox enter cosmic
sudo dnf install -y cosmic-comp
cosmic-comp
```

### plasma

```shell
toolbox create --distro=fedora plasma
toolbox enter plasma
sudo dnf install -y @kde-desktop
dbus-run-session -- startplasma-wayland # worked before, shows black screen now
dbus-run-session -- plasmashell # works but very buggy
```

