# GİB MCP

An MCP project for searching Turkish tax rulings (özelge) from the [Turkish Revenue Administration (GİB)](https://gib.gov.tr/mevzuat/arama?tur=vergi-mevzuati&ktype=99&kanun-turu=ozelge) with Claude.

Built with Python, the MCP SDK, and Playwright. No Claude browser extension required.

## Setup

Requires Python 3.11+.

```sh
sh scripts/setup.sh
```

## Usage

Inspect the GİB page:

```sh
sh scripts/discover.sh
```

Start the MCP server:

```sh
sh scripts/serve.sh
```

For Claude Code, update the project path in `.mcp.json`, then enable the server through `/mcp`.

## Status

Work in progress. Page discovery and the MCP scaffold are available. Live ruling search and detail retrieval are not implemented yet.

See [the roadmap](docs/ROADMAP.md) for next steps.

## License

See [LICENSE](LICENSE).
