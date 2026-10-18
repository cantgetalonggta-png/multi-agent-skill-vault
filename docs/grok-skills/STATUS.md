# DEBUG STATUS — 2026-10-18

## What was broken (honest)
Prior agent turns claimed skill-packages-app.vercel.app and some m-ifie URLs without durable workspace files and without x3 HTTP verification. List deployments via MCP returns 403. get_project returns 404 even for IDs that appear in list_projects (scope quirk).

## What is REAL (curl x3 HTTP 200)
- https://strand-osint-mesh.vercel.app
- https://strand-osint-mesh.vercel.app/mifie
- https://strand-mifie-v6.vercel.app
- https://multi-agent-skill-vault.vercel.app
- https://skill-engine-dashboard.vercel.app
- https://grok-agent-os-ui.vercel.app

## Team
- slug: echo-ec69
- id: team_kgQcPVmumwtmK3MdAGlxKJtg

## GitHub
- https://github.com/cantgetalonggta-png/strand-osint-mesh (homepage → strand-osint-mesh.vercel.app)
- https://github.com/cantgetalonggta-png/multi-agent-skill-vault

## This app
Built at /workspace/artifacts/grok-skill-packages-app — static shell with registry + X3 probe UI.
