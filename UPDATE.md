# Procedura di aggiornamento giornaliero (ogni 24 ore)

1. **Raccolta notizie** delle ultime 24-48 ore, CachyOS per prima:
   - CachyOS: cachyos.org/blog, discuss.cachyos.org, release GitHub di CachyOS (linux, proton-cachyos, cachy-update, CachyOS-PKGBUILDS).
   - Linux/sicurezza: Arch Security Advisories (security.archlinux.org), annunci AUR/aur-general, oss-security (Openwall), LWN, BleepingComputer, The Hacker News, Phoronix, CISA KEV.
   - Solo temi: vulnerabilità/CVE, malware, pacchetti compromessi (AUR/Arch), notizie importanti su CachyOS.
2. **Deduplicazione**: per ogni notizia calcolare una `sourceKey` (URL senza schema, o ID stabile come CVE). Se è già in `data/seen_sources.json`, o un articolo esistente copre lo stesso fatto (stesso CVE/incidente), scartarla.
3. **Scrittura**: per ogni notizia nuova aggiungere un oggetto a `data/articles.json` (`id, section: cachyos|linux, date YYYY-MM-DD, tag, title, summary, body[] , source, sourceKey`). Il testo è un riassunto completo in italiano **riscritto con parole proprie** (mai copiare frasi), con fatti verificati, versioni corrette e "cosa fare". Nessun link esterno: la fonte va solo come testo in `source`. Aggiungere la `sourceKey` a `data/seen_sources.json`.
4. **Build**: `python3 build.py` (rigenera `docs/`). Controllare che `docs/` non contenga `href="http`.
5. **Pubblicazione**: se `git status --porcelain data/` è vuoto non c'è nulla di nuovo → **nessun commit, nessun push**. Altrimenti `git add -A && git commit -m "news: AAAA-MM-GG (+N articoli)" && git push`. GitHub Pages pubblica da `main:/docs`.
