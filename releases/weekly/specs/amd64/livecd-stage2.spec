subarch: amd64
version_stamp: 2008.0
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/13.0/desktop
snapshot: 2008.0
source_subpath: default/livecd-stage1-amd64-installer-2008.0

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fsscript: /release/releng/releases/2008.0/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --mdadm --makeopts=-j8
livecd/iso: livecd-amd64-installer-2008.0.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo Linux 2008.0 amd64 LiveCD
livecd/xsession: xfce
livecd/xdm: gdm

livecd/overlay: /release/releng/releases/2008.0/overlays/common/overlay/livecd
livecd/root_overlay: /release/releng/releases/2008.0/overlays/common/root_overlay

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /release/releng/releases/2008.0/kconfig/amd64/livecd-2.6.24.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb
boot/kernel/gentoo/packages:
	media-libs/alsa-oss
	media-sound/alsa-utils
### Masked (~amd64)
#	net-dialup/fcdsl
### Masked (~amd64)
#	net-dialup/fritzcapi
	net-dialup/globespan-adsl
### Masked (~amd64)
#	net-dialup/slmodem
	net-misc/br2684ctl
### Masked (~amd64)
#	net-wireless/acx
	net-wireless/hostap-utils
#	net-wireless/ipw3945
#	net-wireless/madwifi-ng-tools
#	net-wireless/rt2500
### Masked (~amd64)
#	net-wireless/rtl8187

	sys-apps/pcmciautils

	sys-fs/ntfs3g

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
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
