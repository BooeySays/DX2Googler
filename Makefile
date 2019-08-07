PREFIX ?= /usr/local
HOMEDIR = ~
DX2DIR = $(DESTDIR)$(HOMEDIR)/.DX2test
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
DX2TEST = $(DESTDIR)$(DX2DIR)/test

.PHONY: all ttest prepbash prepzsh unprep install uninstall disable-self-upgrade

all:

ttest:
	test -d $(DX2DIR) || echo "System has not been prepped. prepping now:" && install -m755 -d $(DX2DIR) && echo "MAKING 1" && install -m755 -d $(DX2BIN) && echo "Making 2"
	@printf "\nSearching for .bashrc...\t"
	@test -f $(HOMEDIR)/.bashrc1 && echo "FOUND" && printf "Editing .bashrc:...\t\t" && echo "\n### BEG - SOURCE DX2RC ###\nif [ -f ~/.dx2rc ]; then\n\tsource ~/.dx2rc;\nfi\n### END - SOURCE DX2RC ###\n" >> ~/.bashrc2 && echo "DONE" || echo "NOT FOUND"

prepbash:
	test -d $(DX2DIR) || install -m755 -d $(DX2DIR)
	test -d $(DX2BIN) || install -m755 -d $(DX2BIN)
	test -d $(DX2RC) || install -m755 -d $(DX2RC)
	test -d $(DX2FN) || install -m755 -d $(DX2FN)
	test -d $(DX2TMP) || install -m755 -d $(DX2TMP)
	test -d $(DX2BK) || install -m755 -d $(DX2BK)
	test -d $(DX2GIT) || install -m755 -d $(DX2GIT)
	test -d $(DX2FILES) || install -m755 -d $(DX2FILES)
	test -d $(DX2AKA) || install -m755 -d $(DX2AKA)
	test -f $(HOMEDIR)/.dx2rc || install -m755 .dx2rc $(HOMEDIR)
	@printf "\nSearching for .bashrc...\t"
	@test -f $(HOMEDIR)/.bashrc && echo "FOUND" && printf "Editing .bashrc:...\t\t" && echo "\n### BEG - SOURCE DX2RC ###\nif [ -f ~/.dx2rc ]; then\n\tsource ~/.dx2rc;\nfi\n### END - SOURCE DX2RC ###\n" >> ~/.bashrc && echo "DONE" || echo "NOT FOUND"
	@printf "\nSearching for .zshrc...\t"
	@test -f $(HOMEDIR)/.zshrc && echo "FOUND" && printf "Editing .zshrc:...\t\t" && echo "\n### BEG - SOURCE DX2RC ###\nif [ -f ~/.dx2rc ]; then\n\tsource ~/.dx2rc;\nfi\n### END - SOURCE DX2RC ###\n" >> ~/.zshrc && echo "DONE" || echo "NOT FOUND"


	@printf "Searching for .bashrc:...\t"
	@test -f $(HOMEDIR)/.bashrc && echo "FOUND"; printf "Editing .bashrc:...\t\t"; echo "\n### BEG - SOURCE DX2RC ###\nif [ -f ~/.dx2rc ]; then\n\tsource ~/.dx2rc;\nfi\n### END - SOURCE DX2RC ###\n" >> ~/.bashrc; echo "DONE" || echo ".bashrc does not exist"
	@test -f $(HOMEDIR)/.zshrc && echo "\n### BEG - SOURCE DX2RC ###\nif [ -f ~/.dx2rc ]; then\n\tsource ~/.dx2rc;\nfi\n### END - SOURCE DX2RC ###\n" >> ~/.zshrc || echo ".zshrc does not exist"
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
