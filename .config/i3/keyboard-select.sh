#!/bin/sh


case "$1" in
    HHKB)
        xmodmap ~/Dropbox/Startup/xmodmap-config/xmodmap_desktop_hhkb
        ;;
    normal)
        xmodmap ~/Dropbox/Startup/xmodmap-config/xmodmap_desktop_original
        ;;
    *)
        echo "Usage: $0 {HHKB|normal}"
        exit 2
esac

exit 0
