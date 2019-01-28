all:

install:
	mkdir -p "$(DESTDIR)/usr/share/modern/config" 
	mkdir -p "$(DESTDIR)/usr/share/modern/wallpaper" 
	cp -r config/* "$(DESTDIR)/usr/share/modern/config" 
	cp wallpaper/* "$(DESTDIR)/usr/share/modern/wallpaper" 
	install -D -m 644 modern.desktop "$(DESTDIR)/usr/share/xsessions/modern.desktop"
	install -D -m 644 bin/modern-session "$(DESTDIR)/usr/bin/modern-session"
	install -D -m 755 bin/lock_watch.py "$(DESTDIR)/usr/share/modern/bin/lock_watch.py"
	install -D -m 755 bin/select_wallpaper.py "$(DESTDIR)/usr/share/modern/bin/select_wallpaper.py"
