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

### alpine

```shell
toolbox create --image quay.io/toolbx-images/alpine-toolbox:edge
```

### postmarket os

```shell
toolbox create --image quay.io/toolbx-images/alpine-toolbox:edge postmarketos-toolbox
toolbox enter postmarketos-toolbox
curl 'https://gitlab.com/adamthiede/postmarketos-docker/-/raw/main/edge/repositories?ref_type=heads&inline=false' | sudo tee /etc/apk/repositories
sudo wget https://mirror.postmarketos.org/build.postmarketos.org.rsa.pub -O /etc/apk/keys/build.postmarketos.org.rsa.pub
sudo apk --no-interactive add postmarketos-base postmarketos-ui-console
sudo apk --no-interactive upgrade -Ua
```

