# Watchdog setup for pocketblue

Watchdog is useful for llm-driven debug of kernel or U-Boot.
When debugging kernel, after it crashed,
wathdog can reboot your device to U-Boot,
then you can select different grub entry with stable kernel.
When debugging U-Boot, after it crashed,
wathdog can reboot your device to fastboot,
then you can reflash different U-Boot build

## Kernel configs

First,
[arkify your kernel](../tips-and-tricks/kernel-build.md#run-arkify-in-kernel-repo)

Set these kernel configs

```bash
echo CONFIG_WATCHDOG_HANDLE_BOOT_ENABLED=y | tee redhat/configs/fedora/generic/arm/aarch64/CONFIG_WATCHDOG_HANDLE_BOOT_ENABLED
echo CONFIG_WATCHDOG_SYSFS=y | tee redhat/configs/fedora/generic/arm/aarch64/CONFIG_WATCHDOG_SYSFS
echo CONFIG_WATCHDOG_CORE=y | tee redhat/configs/fedora/generic/arm/aarch64/CONFIG_WATCHDOG_CORE
echo CONFIG_WATCHDOG=y | tee redhat/configs/fedora/generic/arm/aarch64/CONFIG_WATCHDOG
echo CONFIG_QCOM_WDT=y | tee redhat/configs/fedora/generic/arm/aarch64/CONFIG_QCOM_WDT
```

Then [build](https://pocketblue.github.io/tips-and-tricks/kernel-build/#build-kernel-locally)
and [install](https://pocketblue.github.io/tips-and-tricks/kernel-build/#installing-kernel) kernel

## U-Boot configs

Check that watchdog support is enabled in `qcom_defconfig`.
`tauchgang/u-boot` repo already has it enabled by default

```bash
grep CONFIG_CMD_WDT=y configs/qcom_defconfig
```

To enable U-Boot's serial console gadget by default,
open `board/qualcomm/qcom-phone.env`,
and replace line that starts with `preboot=` with this

```bash
preboot=run serial_gadget; scsi scan; run setup_rootdev; run setup_blkmap
```

Rebuild U-Boot after this change

## Check watchdog state in linux

```bash
cat /sys/class/watchdog/watchdog0/identity
cat /sys/class/watchdog/watchdog0/state
cat /sys/class/watchdog/watchdog0/timeout
cat /sys/class/watchdog/watchdog0/nowayout
systemctl show --property=RuntimeWatchdogUSec
```

## Connect to U-Boot serial console

- [Get into U-Boot bootmenu](https://pocketblue.github.io/fetching-logs/serial-console/#get-into-uboot-bootmenu)
- [Enable serial console](https://pocketblue.github.io/fetching-logs/serial-console/#enabling-uboot-serial-console)
- [Connect via picocom](https://pocketblue.github.io/fetching-logs/serial-console/#connecting-to-serial-console-via-picocom)

## Start timer in U-Boot

Start watchdog from U-Boot so it is active before linux boots

```text
wdt list
```

Select watchdog by name from `wdt list`.
Replace `xxxxxxxx` with output you got

```text
wdt dev watchdog@xxxxxxxx
```

Start timer. 30000 means 30 seconds here

```text
wdt start 30000
```

Resume boot from U-Boot console

```text
bootefi bootmgr
```

Select test entry in grub

## Testing watchdog

See [editing-kernel-arguments](https://pocketblue.github.io/fetching-logs/serial-console/#editing-kernel-arguments)

Add these kernel arguments to pause boot in initramfs

```text
watchdog.open_timeout=120 rd.systemd.break=pre-switch-root
```

`watchdog.open_timeout=120` means that linux kernel
will feed watchdog for 120 seconds.
After 120 seconds, watchdog will reboot your device.
Timing is measured after kernel registers watchdog

Setting `watchdog.open_timeout=0` lets kernel feed watchdog indefinitely.
Watchdog can still reset device if feeding stops

Initramfs systemd must use `RuntimeWatchdogSec=0`,
this is already default on Fedora.
Otherwise systemd will feed watchdog throughout pause

Reboot, start watchdog from U-Boot, and expect device to hang in initramfs,
then it should automatically reboot.
Editing arguments with `rpm-ostree kargs` makes modified deployment default.
You can then switch to previous stable grub entry
by pressing volume down button,
or by connecting to U-Boot's serial console and pressing down-arrow key in grub.
Alternatively, change default boot entry before rebooting

```shell
sudo ostree admin set-default 1
```

## Disarming watchdog

```bash
cat /sys/class/watchdog/watchdog0/nowayout
```

Expected result is 0

```bash
printf V | sudo tee /dev/watchdog0
cat /sys/class/watchdog/watchdog0/state
```

Expected result is `inactive`.
`Device or resource busy` means that wathdog is owned by another process

## Related docs

- <https://docs.u-boot.org/en/v2026.04/usage/cmd/wdt.html>
- <https://docs.kernel.org/watchdog/index.html>
- <https://freedesktop.org/software/systemd/man/latest/systemd-system.conf.html>
