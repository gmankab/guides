# toolbox arm

how to use toolbox on arm device

tested on xiaomi pad 5, host system is fedora 41

### fedora

```shell
toolbox create --distro=fedora
```

### arch

```shell
toolbox create --image quay.io/gmanka/arch-arm-toolbox:latest
```

### alpine

```shell
toolbox create --image quay.io/toolbx-images/alpine-toolbox:edge
```

### postmarket os

```shell
toolbox create --image quay.io/toolbx-images/alpine-toolbox:edge postmarketos-toolbox
toolbox enter postmarketos-toolbox
sudo wget https://gitlab.com/adamthiede/postmarketos-docker/-/raw/main/edge/repositories -O /etc/apk/repositories
sudo wget https://mirror.postmarketos.org/build.postmarketos.org.rsa.pub -O /etc/apk/keys/build.postmarketos.org.rsa.pub
sudo apk --no-interactive add postmarketos-base postmarketos-ui-console
sudo apk --no-interactive upgrade -Ua
```

