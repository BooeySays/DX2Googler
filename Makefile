PREFIX ?= /usr/local
HOMEDIR = ~
DX2DIR = $(DESTDIR)$(HOMEDIR)/.DX2
BINDIR = $(DESTDIR)$(PREFIX)/bin
MANDIR = $(DESTDIR)$(PREFIX)/share/man/man1
DOCDIR = $(DESTDIR)$(PREFIX)/share/doc/googler
DX2BIN = $(DESTDIR)$(DX2DIR)/bin
DX2RC = $(DESTDIR)$(DX2DIR)/rc
DX2FN = $(DESTDIR)$(DX2DIR)/functions
DX2TMP = $(DESTDIR)$(DX2DIR)/temp
DX2BK = $(DESTDIR)$(DX2DIR)/backups
DX2GIT = $(DESTDIR)$(DX2DIR)/github
DX2FILES = $(DESTDIR)$(DX2DIR)/files
DX2AKA = $(DESTDIR)$(DX2DIR)/aliases


.PHONY: all ttest prepbash prepzsh unprep install uninstall disable-self-upgrade

all:

ttest:
	. ./installer-b.sh

prepbash:
	install -m755 -d $(DX2DIR)
	install -m755 -d $(DX2BIN)
	install -m755 -d $(DX2RC)
	install -m755 -d $(DX2FN)
	install -m755 -d $(DX2TMP)
	install -m755 -d $(DX2BK)
	install -m755 -d $(DX2GIT)
	install -m755 -d $(DX2FILES)
	install -m755 -d $(DX2AKA)
	install -m755 .dx2rc $(HOMEDIR)
	echo "\n### BEG - SOURCE DX2RC ###\nif [ -f ~/.dx2rc ]; then\n\tsource ~/.dx2rc;\nfi\n### END - SOURCE DX2RC ###\n" >> ~/.bashrc
	bash

prepzsh:
	install -m755 -d $(DX2DIR)
	install -m755 -d $(DX2BIN)
	install -m755 -d $(DX2RC)
	install -m755 -d $(DX2FN)
	install -m755 -d $(DX2TMP)
	install -m755 -d $(DX2BK)
	install -m755 -d $(DX2GIT)
	install -m755 -d $(DX2FILES)
	install -m755 -d $(DX2AKA)
	install -m755 .dx2rc $(HOMEDIR)
	echo "\n### BEG - SOURCE DX2RC ###\nif [ -f ~/.dx2rc ]; then\n\tsource ~/.dx2rc;\nfi\n### END - SOURCE DX2RC ###\n" >> ~/.zshrc
	zsh

unprep:
	rm -rf $(DX2DIR)
	rm $(HOMEDIR)/.dx2rc
	sed -i '/### BEG - SOURCE DX2RC ###/,/### END - SOURCE DX2RC ###/d' ~/.bashrc

install:
	install -m755 -d $(BINDIR)
	install -m755 -d $(MANDIR)
	install -m755 -d $(DOCDIR)
	gzip -c googler.1 > googler.1.gz
	install -m755 googler $(BINDIR)
	install -m755 GooglePrompt $(DX2BIN)
	install -m755 DX2Googler.rc $(DX2RC)
	install -m644 googler.1.gz $(MANDIR)
	install -m644 README.md $(DOCDIR)
	rm -f googler.1.gz

uninstall:
	rm -f $(BINDIR)/googler
	rm -f $(DX2BIN)/GooglePrompt
	rm -f $(DX2RC)/DX2Googler.rc
	rm -f $(MANDIR)/googler.1.gz
	rm -rf $(DOCDIR)

# Disable the self-upgrade mechanism entirely. Intended for packagers.
#
# We assume that sed(1) has the -i option, which is not POSIX but seems common
# enough in modern implementations.
disable-self-upgrade:
	sed -i.bak 's/^ENABLE_SELF_UPGRADE_MECHANISM = True$$/ENABLE_SELF_UPGRADE_MECHANISM = False/' googler
