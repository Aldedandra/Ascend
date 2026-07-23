# The Journey Hub

A self-hosted DevOps learning platform designed to organize lessons, audio scripts, labs, quizzes, reflections, XP, achievements, and portfolio progress.

## Stack

- React + Vite
- FastAPI
- SQLite
- Nginx
- Docker Compose

## Start with Docker

```bash
docker compose up -d --build
```

Open:

```text
http://<your-windows-computer-ip>:3001
```

Examples:

```text
http://localhost:3001
http://192.168.1.50:3001
```

## Stop

```bash
docker compose down
```

## View logs

```bash
docker compose logs -f
```

## Rebuild after code changes

```bash
docker compose up -d --build
```

## Data persistence

Progress, journal entries, quiz submissions, and achievements are stored in the Docker volume:

```text
journey_data
```

Removing containers will not remove your progress. To delete all stored data intentionally:

```bash
docker compose down -v
```

## Windows Firewall

If another device cannot open the site, allow inbound TCP traffic on port `3001` in Windows Defender Firewall.

## Suggested repository name

```text
the-journey-hub
```

## MVP boundaries

This version intentionally avoids authentication, cloud hosting, AI API integration, and complex administration. It is designed to get running quickly and become the hands-on application used throughout the DevOps curriculum.
