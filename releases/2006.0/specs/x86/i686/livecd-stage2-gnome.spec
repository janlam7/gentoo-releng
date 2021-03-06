subarch: i686
version_stamp: 20060123
target: livecd-stage2
rel_type: default
profile: default-linux/x86/2006.0
snapshot: 20060123
source_subpath: default/livecd-stage1-i686-installer-20060123

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.09-memtest86+-cdtar.tar.bz2
#livecd/fsscript: /root/livecd/scripts/livecd-fsscript2.sh
livecd/iso: /tmp/livecd-i686-installer-20060123.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2006.0
livecd/xdm: gdm
livecd/xsession: gnome

# DO NOT USE livecd/type: gentoo-release-livecd unless you are duplicating a
# Gentoo release and understand what this means.  We will not support broken
# builds if you use this and don't know what you're doing.  Please use
# generic-livecd instead for any builds.
livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux 2006.0 x86 LiveCD

livecd/overlay: /root/livecd/overlays/livecd/2006.0
livecd/root_overlay: /root/livecd/overlays/root-livecd

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm2 --dmraid --evms2
#--unionfs-dev

#livecd/rcadd: x-setup|default spind|default xdm|default famd|default

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/releases/2006.0/x86/livecd-2.6.15.config

boot/kernel/gentoo/use: pcmcia usb oss atm

boot/kernel/gentoo/packages:
	splashutils
	splash-themes-livecd
	pcmcia-cs
#	speedtouch
	slmodem
	globespan-adsl
#	hostap-driver
	hostap-utils
#	ipw2100
#	ipw2200
	fritzcapi
	fcdsl
	acpid
	cryptsetup
#	at76c503a
#	rt2500
#	rtl8180
#	adm8211
	acx100
#	orinoco
	nvidia-kernel
	nvidia-glx
	ati-drivers
	alsa-lib
	alsa-oss
	alsa-utils
#	alsa-driver

livecd/unmerge:
	gentoo-sources

livecd/empty:
	/var/tmp
	/var/empty
	/var/run
	/var/state
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src
	/root/.ccache
	/etc/splash/gentoo
	/etc/splash/emergence
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
