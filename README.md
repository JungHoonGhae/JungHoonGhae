# The apps are separate. The work isn't.

Finance, messages, shopping, and public data arrive as different products with different
interfaces. For a person, they are often parts of one intent.

I'm building toward one open, inspectable system that can understand that intent, cross the
boundaries between products, act through the services people already use, and show its work.

I haven't found its final form yet. I'm building it from working parts, not a grand diagram. Each
CLI, MCP server, and native tool solves a real problem on its own—and becomes an adapter for
something larger.

`blocked workflow → reliable tool → composable adapter → larger system`

## Where the pieces converge

- **Open Invest** *(in development)* — market data, screening, judgment, risk gates, and execution in one local, inspectable investing workspace; the first place where several adapters are becoming a system
- **oddsock** *(preparing the public release)* — one ordinary question becomes datasets, inspected schemas, access applications, and first working API calls; a test of the same idea beyond finance

## Working parts

- **[tossinvest-cli](https://github.com/JungHoonGhae/tossinvest-cli)** (490★) — one CLI and MCP server for 100% of Toss Securities' official Open API plus 55 capabilities previously trapped in the web app
- **[openkakao-cli](https://github.com/JungHoonGhae/openkakao-cli)** (120★) — send and read KakaoTalk locally on macOS, using Accessibility automation when recent builds broke server login
- **[opencode-kilo-auth](https://github.com/JungHoonGhae/opencode-kilo-auth)** (41★) — add 342+ Kilo Gateway models to an existing OpenCode installation, without maintaining a separate fork

They look unrelated. They are fieldwork for the same larger system.

## How I get there

**Software should have handles.** So I start small: with the command the product forgot to ship.

- Build against the system that exists, not the API you wish it had.
- Treat login, permissions, files, and failure modes as part of the product.
- Keep every action observable for both people and agents.
- Compose useful tools instead of hiding them inside a black box.

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
