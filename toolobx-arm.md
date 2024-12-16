# toolbox arm

how to use toolbox on arm device

tested on xiaomi pad 5, host system is fedora 41

### fedora

```shell
toolbox create --distro=fedora
```

### arch

```shell
toolbox create --image ghcr.io/menci/archlinuxarm arch
podman start arch
podman exec -it -u root arch pacman -Syu sudo
podman exec -it -u root arch bash -c 'echo "%wheel ALL=(ALL:ALL) NOPASSWD: ALL" | tee -a /etc/sudoers'
toolbox enter arch
```

