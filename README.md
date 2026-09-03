# Software should have handles.

**I build the command the product forgot to ship.**

A useful workflow can technically exist and still be impossible to grab: it is trapped behind a
browser-only screen, an incomplete API, repetitive clicks, or a file nobody has opened yet.

I go one layer deeper and give it a handle—a small, inspectable CLI, MCP server, or native tool. A
person can run it. An agent can call it. Both can verify what happened.

## The operating idea

- Build against the system that exists, not the API you wish it had.
- Login, permissions, files, and failure modes are part of the product.
- People and agents should be able to use the same observable interface.
- Ship the smallest end-to-end tool that is genuinely useful.

## Now

**oddsock** *(preparing the public release)* — Korean public data is technically open. Using it
still means guessing portal vocabulary, downloading files to discover their contents, applying for
access, and wiring the first call by hand.

`one ordinary question → datasets → inspected schemas → access → first real call`

## Selected work

- **[tossinvest-cli](https://github.com/JungHoonGhae/tossinvest-cli)** (490★) — one CLI and MCP server for 100% of Toss Securities' official Open API plus 55 capabilities previously trapped in the web app
- **[openkakao-cli](https://github.com/JungHoonGhae/openkakao-cli)** (120★) — send and read KakaoTalk locally on macOS, using Accessibility automation when recent builds broke server login
- **[opencode-kilo-auth](https://github.com/JungHoonGhae/opencode-kilo-auth)** (41★) — add 342+ Kilo Gateway models to an existing OpenCode installation, without maintaining a separate fork

They look unrelated. The method is the same: start with the blocked last mile, find the real system
boundary, and make the whole path operable.

## Recently shipped

<!-- releases:start -->
- `2026-09-03` — [openkakao-cli v1.8.1](https://github.com/JungHoonGhae/openkakao-cli/releases/tag/v1.8.1)
- `2026-09-02` — [tossinvest-cli v0.49.0](https://github.com/JungHoonGhae/tossinvest-cli/releases/tag/v0.49.0)
- `2026-07-28` — [claude-statusline v1.7.0](https://github.com/JungHoonGhae/claude-statusline/releases/tag/v1.7.0)
<!-- releases:end -->

<details>
<summary><strong>More shipped tools</strong></summary>

- **[claude-statusline](https://github.com/JungHoonGhae/claude-statusline)** (33★) — a rich Claude Code statusline in pure Bash
- **[smartstore-cli](https://github.com/JungHoonGhae/smartstore-cli)** (23★) — Naver Smart Store seller-center data from the terminal
- **[tailbar](https://github.com/JungHoonGhae/tailbar)** (6★) — a native macOS menu bar for Tailscale serves, peers, and exit nodes
- **[capacities-cli](https://github.com/JungHoonGhae/capacities-cli)** (5★) — unofficial full-CRUD access to Capacities.io
- **[skills](https://github.com/JungHoonGhae/skills)** (4★) — reusable skills for Claude Code, OpenCode, and other coding agents
- **[k-vote-cli](https://github.com/JungHoonGhae/k-vote-cli)** (3★) — reproducible Korean election data with no API key

</details>

---

<a href="https://github.com/sponsors/JungHoonGhae"><img src="assets/sponsor.svg" height="44" alt="Sponsor my open-source work" /></a>

<!-- sponsors:start -->

<sub>backed by <a href="https://github.com/sponsors/JungHoonGhae" title="비공개 후원자 / private sponsor"><img src="assets/anonymous.svg" width="22" height="22" alt="private sponsor" /></a> · <strong>1</strong> sponsor so far (one-time included). be the next.</sub>

<!-- sponsors:end -->

Seoul · [Email](mailto:lucas.ghae@remodule.dev) · [LinkedIn](https://www.linkedin.com/in/junghoonghae/) · [X](https://x.com/lucas_ghae)
