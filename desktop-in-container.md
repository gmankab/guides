# desktop in container

### gnome

```shell
toolbox create --distro=fedora gnome
toolbox enter gnome
sudo dnf install @gnome-desktop
MUTTER_DEBUG_DUMMY_MODE_SPECS=1920x1040 dbus-run-session -- gnome-shell --nested --wayland
```

### plasma

```shell
distrobox create --pull --image registry.fedoraproject.org/fedora-toolbox:latest plasma
distrobox enter plasma
sudo dnf install @kde-desktop
dbus-run-session -- startplasma-wayland
```

