# Walkthrough — offensive-security-labs

How each technique works, by category, with the cleanups made along the way.
Everything here is for **authorized, educational use only** (see the README).

## password_cracking/

- **hash_generator.py** — takes a string and prints its md5, sha1, sha224, sha256, and sha512 hashes with `hashlib`. A good way to see what a "hash" actually looks like and why longer algorithms take more work to brute-force.
- **sha1_cracker.py** — given a SHA-1 hash, it hashes each word in `passwords.txt` and compares, stopping when it finds a match. This is exactly how an offline dictionary attack works against leaked hashes.
- **crypt_bruteforce.py** — the same idea against Unix `crypt(3)` hashes (the format in `/etc/shadow`), using the per-hash salt. *Cleanup: the `crypt` module was removed from Python 3.13, so the import is now guarded with a clear message instead of crashing.*

The `.txt` files are small practice wordlists — generic common passwords, not real credentials.

## ssh_ftp_bruteforce/

- **ssh_bruteforce.py / ssh_login.py** — use `pexpect` to drive the interactive `ssh` command: spawn it, answer the host-key prompt, send the password, and read the result. `ssh_bruteforce.py` loops over a wordlist; `ssh_login.py` logs in once and runs a command.
- **ftp_bruteforce.py** — uses `ftplib` to try `username:password` pairs from a file against an FTP server. *Cleanup: a `print('... ' + [passWord])` concatenated a list to a string (a crash); fixed to use the string, and the function now reads the file argument it's given.*
- **ftp_anonymous_login.py** — checks whether a server allows the classic `anonymous/anonymous` login, a common misconfiguration.

## reverse_shell/

- **server.py** — the attacker's listener: it binds a port, accepts a connection, and sends commands the victim machine runs, printing the output. Uses a `<sep>` separator to split command output from the new working directory.
- **client.py** — runs on the target: connects back to the server, receives commands, runs them with `subprocess`, handles `cd` specially, and sends the output back.
- **simple_reverse_shell.py** — a minimal version (moved here from the networking repo, since a reverse shell is offensive tooling).

This client/server pair shows exactly why outbound connections and unexpected
child processes matter to defenders.

## spoofing/

- **mac_address_changer.py / _v2.py** — change a network interface's MAC address with `ifconfig`/`subprocess`; v2 also reads back and verifies the new MAC with a regex. *Cleanup: the regex is now a raw string to avoid an escape-sequence warning.*
- **firefox_user_agent_spoof.py** — sends web requests with a spoofed `User-Agent` header so the server sees a different browser.

## web_recon/

- **site_check.py** — basic reconnaissance on a website (availability / response info).
- **cookie_info_extract.py** — demonstrates reading login-form fields and cookies. The username/password in it are obvious placeholders (`u@gmail.com` / `password`), not real credentials.

## General cleanups

- Fixed typo'd shebangs (`#!/ur/bin/env python` → `#!/usr/bin/env python3`) across every script.
- Removed an old portfolio website and the "little things" utilities that didn't belong in a security repo (the utilities moved to `python-mini-projects`).
- Moved the port scanners to `network-scanner` and the HTTP/FTP servers to `python-network-toolkit`, so this repo is purely offensive tooling.
