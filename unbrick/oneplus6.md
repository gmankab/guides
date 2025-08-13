### unbrick oneplus 6 from fedora

at first you should try unbrick with fastboot - https://4pda.to/forum/index.php?showtopic=902608&view=findpost&p=111433217

it it not helped, then you should try unbrick with edl - https://github.com/bkerler/edl/issues/432

### installing python3-edl on fedora

```sh
# disable modem manager service
sudo systemctl disable --now ModemManager
sudo systemctl mask ModemManager

# enable copr repo with python3-edl
sudo dnf copr enable -y gmanka/gmanka

# install if you use fedora workstation
sudo dnf install python3-edl

# install if you use fedora silverblue
rpm-ostree install python3-edl
```
### download and decrypt edl

```sh
curl -LO https://onepluscommunityserver.com/list/Unbrick_Tools/OnePlus_6/Q/OnePlus_6_OxygenOS_10.3.8.zip
unzip ./OnePlus_6_OxygenOS_10.3.8.zip
git clone https://github.com/bkerler/oppo_decrypt
python -m venv .venv
.venv/bin/pip install -r oppo_decrypt/requirements.txt
.venv/bin/python oppo_decrypt/opscrypto.py decrypt enchilada_22_J.50_210121/enchilada_22_J.50_210121.ops
cd enchilada_22_J.50_210121/extract
```

### patch

```sh
curl -LO https://raw.githubusercontent.com/gmankab/guides/refs/heads/main/unbrick/patch.py
python patch.py
```

### go to edl mode

poweroff device, press both volume buttons, connect device to pc

### flash

```sh
edl qfil rawprogram0.xml patch0.xml .
edl qfil rawprogram1.xml patch1.xml .
edl qfil rawprogram2.xml patch2.xml .
edl qfil rawprogram3.xml patch3.xml .
edl qfil rawprogram4.xml patch4.xml .
edl qfil rawprogram5.xml patch5.xml .
```

### success

after that my oneplus 6 was successfully unbricked

