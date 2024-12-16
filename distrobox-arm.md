# distrobox arm

how to use distrobox on arm device

tested on xiaomi pad 5, host system is fedora 41

### fedora

```shell
distrobox create --pull --image registry.fedoraproject.org/fedora-toolbox:latest fedora-distrobox
```

### arch

```shell
distrobox create --pull --image docker.io/menci/archlinuxarm arch-distrobox
```

### alpine

```shell
distrobox create --pull --image docker.io/arm64v8/alpine:edge alpine-distrobox
```

### postmarketos

```shell
distrobox create --pull --image docker.io/arm64v8/alpine:edge postmarketos-distrobox
distrobox enter postmarketos-distrobox
curl 'https://gitlab.com/adamthiede/postmarketos-docker/-/raw/main/edge/repositories?ref_type=heads&inline=false' | sudo tee /etc/apk/repositories
sudo wget https://mirror.postmarketos.org/build.postmarketos.org.rsa.pub -O /etc/apk/keys/build.postmarketos.org.rsa.pub
sudo apk --no-interactive add postmarketos-base postmarketos-ui-console
sudo apk --no-interactive upgrade -Ua
```

