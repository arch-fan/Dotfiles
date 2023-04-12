# Dotfiles

Welcome to my dotfiles

(Future img)

## Arch Linux minimal installation

First we load our keyboard language, in my case **es** (`ls /usr/share/kbd/keymaps/**/*.map.gz` for listing all available keyboard layout)

`loadkeys es`

Now depending on what system are we working, bootloader installation will change, in my case I will use grub on a VM (for uefi installation you will need other steps will be detailed in a future). If we want to check if out system is efi try listing efivars directory (if output, means you have efi).

`ls /sys/firmware/efi/efivars`

Check if internet connection is stablished, if not try nmcli [link](https://www.youtube.com/watch?v=3zqITuprlL8)

`ping google.es`

For partitoning we're gonna follow a simple table using cfdisk, supposing we have 20GB

`cfdisk /dev/sdx`

| Device | Partition type | Space | 
| ------- | ------------- | ------ |
| /dev/sda1 | Linux filesystem | 512M | 
| /dev/sda2 | Linux filesystem | 15GB |
| /dev/sda3 | Linux swap | 4,5G |

Once partitioned, we have to give format to partitions

`mkfs.vfat -F 32 /dev/sda1`
`mkfs.ext4 /dev/sda2`
`mkswap /dev/sda3`

Now we have to mount them, we're following this scheme

`mount /dev/sda2 /mnt`

Inside /mnt directory, create boot directory

`mkdir /mnt/boot`

Continue mounting

`mount /dev/sda1 /mnt/boot`
`swapon /dev/sda3`

Once partitions are mounted, let's install the base system adding some utils

`pacstrap /mnt base linux linux-firmware nano grub networkmanager`

Generate fstab file so partitions are automounted at boot

`genfstab -U /mnt >> /mnt/etc/fstab`

After generating fstab, we're chrooting into our arch

`arch-chroot /mnt`

Let's set timezone with (in my case Europe/Madrid, change to your city)

`ln -sf /usr/share/zoneinfo/Europe/Madrid /etc/localtime` 

Edit /etc/locale.gen and uncomment es_ES.UTF-8 or the one you need, we will be using nano

`nano /etc/locale.gen`

After uncommenting the languages you want, launch locele-gen

`locale-gen`

Lets create locale.conf file and set our lang (again in my case es_ES.UTF-8)

`echo LANG=es_ES.UTF-8 >> /etc/locale.conf`

And set our keymap for console (pick your language, es in my case)

`echo KEYMAP=es >> /etc/vconsole.conf`

Set hostname for your machine

`echo your_name >> /etc/hostname`

We're almost finished, I recommend creating a user for personal use

`useradd -m username`

And stablish a password

`passwd username`

Also for root user

`passswd`

Let's enable network service (because internet isn't gonna be available when arch is booted)

`systemctl enable NetworkManager`

Finally lets install grub and create config file

`grub-install /dev/sda`
`grub-mkconfig -o /boot/grub/grub.cfg`

And basic installation will be finished, just reboot the system.



## Dotfiles packages

| Package  | Description |
| ------------- | ------------- |
| sudo | Permissions pls | 
| git | Clone repooooos | 
| python | Just python | 
| python-pip | And install psutil with pip | 
| qtile | Window manager |
| Alacritty | Terminal |
| lightdm  | Display manager |
| lightdm-gtk-greeter | Dependencies for lightdm |
| picom | Image compositor |
| htop | Task manager |
| neofetch | Just neofetch KEKW |
| rofi | Window switcher |
| feh | Wallpaper btw |
| xorg-xinit | xinit |
| base-devel | Fakeroot binaries for yay |
| yay | AUR repositories installer |
| ttf-jetbrains-mono | Nerd font (with yay) |
