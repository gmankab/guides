# install fedora 43 phosh on oneplus 6

### disclaimer

- all data on you device will be wiped
- this work-in-progress
- it may be not possible to update your system

### download fedora

```sh
curl -LO https://github.com/fedora-remix-mobility/fedora-kiwi-descriptions/releases/download/2025-04-04/Fedora-SDM845-Remix.tar.xz
tar -xf Fedora-SDM845-Remix.tar.xz
cd artifacts
```

### download u-boot

https://git.codelinaro.org/linaro/qcomlt/u-boot/-/releases

for oneplus 6 you should download u-boot-enchilada-boot.img

for oneplus 6t you should download u-boot-fajita-boot.img

### flash u-boot

```sh
fastboot flash boot u-boot-*-boot.img --slot=all
fastboot reboot
```

- after that u-boot will be booted
- in u-boot you should select "enable usb mass storage"
- all partitions on your phone will be mounted on your pc

### getting partition names

```sh
lsblk -o NAME,PARTLABEL | grep -E 'op2|system|userdata'
```

here is output i got on my device:

```sh
├─sdb7  op2
├─sdb13 system_a
├─sdb14 system_b
└─sdb17 userdata
```

### writing fedora on oneplus with dd

- esp.raw -> op2
- boot.raw -> system_a
- boot.raw -> system_b
- root.raw -> userdata

```sh
sudo dd if=esp.raw  of=/dev/sdb7  bs=4M status=progress
sudo dd if=boot.raw of=/dev/sdb13 bs=4M status=progress
sudo dd if=boot.raw of=/dev/sdb14 bs=4M status=progress
sudo dd if=root.raw of=/dev/sdb17 bs=4M status=progress
sync
```

then reboot phone and boot to system

