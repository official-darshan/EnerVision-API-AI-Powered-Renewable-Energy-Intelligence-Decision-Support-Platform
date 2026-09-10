# Deployment

## Current Status
This project runs locally via Docker Compose (`docker compose up --build`). Public/cloud deployment has not been performed as part of this academic project — this document describes deployment considerations, not a live deployment.

## Local Deployment (verified approach)
1. Clone the repository
2. Copy `.env.example` to `.env` and fill in real values
3. Run `docker compose up --build`
4. API available at `http://127.0.0.1:8000`

## Potential Free-Tier Cloud Options (not implemented)
- **Render** or **Railway**: both offer free tiers suitable for small FastAPI + PostgreSQL projects, with GitHub-based auto-deploy
- **Fly.io**: free allowance suitable for small containerized apps

## Considerations for Future Deployment
- Environment variables must be set via the platform's secret management, never committed
- NASA POWER historical ingestion is a one-time/manual step; a hosted deployment would need the model artifact (`models/random_forest.pkl`) either committed (current approach, small file) or generated at build/startup time
- CORS configuration would need real allowed origins (currently unconfigured, since this runs locally only)
- No authentication is currently implemented; a public deployment would need at least basic rate limiting to avoid abuse of the free Open-Meteo API allowance

## Known Limitation
Full Docker Compose startup (`docker compose up --build`, both `db` and `api` services reaching a running state together) was fixed after an initial Dockerfile configuration issue, but was not independently re-verified end-to-end in this development session. Before relying on this for a demo or submission, run `docker compose up --build` and `docker ps` yourself and confirm both containers show `Up`.