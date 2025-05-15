# HA_MCP
Homme Assistant simple MCP server

## Just a start

## Create project
uv init HA_MCP


## Init virtual envionnemet
uv venv

## Libraries
uv add "mcp[cli]" httpx

## Lancement
source .venv/bin/activate
python3 main.py --host localhost --port 8080


