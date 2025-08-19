### creating config required for gnome-boxes to work

```sh
mkdir -p ~/.config/libvirt
echo 'max_core = 0' | tee ~/.config/libvirt/qemu.conf
```

this config should be created before your distrobox container started, otherwise creating vms will fail

### creating container

```sh
distrobox create --pull --root --init --image quay.io/fedora/fedora-toolbox
distrobox enter --root fedora-toolbox
```

### installing boxes

```sh
sudo dnf -y install gnome-boxes
sudo systemctl enable --now virtqemud.socket virtqemud-ro.socket virtnetworkd.socket virtnetworkd-ro.socket virtstoraged.socket virtstoraged-ro.socket virtnodedevd.socket virtnodedevd-ro.socket
```

### run boxes

```sh
gnome-boxes
```

### if you getting errors, just restart container

```sh
distrobox stop --all --root
distrobox enter --root fedora-toolbox
gnome-boxes
```
