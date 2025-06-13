# distrobox arm

how to use distrobox on arm device

tested on xiaomi pad 5, host system is fedora 41

### fedora

```shell
distrobox create --pull --image registry.fedoraproject.org/fedora-toolbox:latest fedora-distrobox
```

### arch

```shell
distrobox create --image quay.io/gmanka/arch-arm-toolbox:latest
```

### alpine

```shell
distrobox create --pull --image quay.io/toolbx-images/alpine-toolbox:edge
```

### postmarketos

```shell
toolbox create --image quay.io/gmanka/pmos-toolbox
```

