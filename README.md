# Docker Workshop - Part 1: Simple Python Application

A hands-on workshop demonstrating the classic "but it works on my machine" problem and how Docker solves it.

## Table of Contents
- [The Problem](#the-problem)
- [Getting Started](#getting-started)
- [Workshop Structure](#workshop-structure)
- [Step 1: Run Locally (The Problem)](#step-1-run-locally-the-problem)
- [Step 2: Create a Dockerfile](#step-2-create-a-dockerfile)
- [Step 3: Build Your Docker Image](#step-3-build-your-docker-image)
- [Step 4: Run Your Container](#step-4-run-your-container)
- [Step 5: Share Your Image (Docker Hub)](#step-5-share-your-image-docker-hub)
- [Essential Docker Commands](#essential-docker-commands)
- [What You've Learned](#what-youve-learned)

---

## The Problem

Ever heard **"but it works on my machine"**? This happens when code runs perfectly on one developer's machine but fails on another due to different:
- **Python versions** (this app requires Python 3.10+ for pattern matching)
- **Operating systems** (Windows, macOS, Linux handle things differently)
- **Environment configurations** (different libraries, paths, etc.)

### Real-World Team Scenario:
Imagine a team of 5 developers:
- Dev A: Ubuntu 22.04, Python 3.10
- Dev B: Windows 11, Python 3.9
- Dev C: macOS, Python 3.11
- Dev D: Ubuntu 20.04, Python 3.8
- Dev E: Arch Linux, Python 3.12

**The app works on Dev A's machine but breaks on Dev B and Dev D's machines!** Why?
- Dev B has Python 3.9 (doesn't support `match` statement)
- Dev D has Python 3.8 (doesn't support `match` statement)

Each developer would need to:
1. Install the correct Python version
2. Set up a virtual environment
3. Deal with OS-specific issues
4. Hope they configured everything correctly

**This wastes hours of development time every single day!**

---

## The Solution: Docker

Docker packages your application with **ALL** its dependencies into a **container** that runs consistently **everywhere**. Think of it as shipping your entire development environment, not just the code.

### Why Docker Images > Dockerfiles for Teams

**Sharing Dockerfiles:**
- Each developer must build the image (takes time)
- Builds might fail due to network issues, different Docker versions, etc.
- Inconsistent build results possible
- Wastes bandwidth downloading base images repeatedly

**Sharing Docker Images (via Docker Hub):**
- Pull once, run anywhere
- Guaranteed consistency (exact same image)
- Faster onboarding (no build step)
- Single source of truth

---

## Getting Started

### Prerequisites:
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Git installed
- Text editor of your choice

### Clone and Navigate:
```bash
# Clone the repository
git clone https://github.com/Adamo08/runs-on-my-machine-demo.git

# Navigate to the project directory
cd runs-on-my-machine-demo
```

---

## Workshop Structure

### Branches:
- `main` - Starting point (code only, no Docker files)
- `solution` - Complete solution with Dockerfile

### Switching Branches:
```bash
# View all branches
git branch -a

# Switch to solution branch (if you get stuck)
git checkout solution

# Go back to main to continue the workshop
git checkout main
```

---

## Step 1: Run Locally (The Problem)

Try running the application locally:

```bash
python app.py
```

**What this app does:**
- Asks: "Sh7al 3yiti lyoma (0-5)?" (How much u are tired today?)
- Responds based on your input using Python 3.10+ pattern matching

**If you have Python 3.10+:** It works!
**If you have Python 3.9 or below:** It crashes with a syntax error!

This is the "works on my machine" problem in action.

---

## Step 2: Create a Dockerfile

Now let's containerize this application. Create a file named `Dockerfile` (no extension) in the project root.

### Your Task:
Create a `Dockerfile` with the following requirements:

1. **Base Image:** Use Python 3.10 slim variant (smaller, faster)
2. **Working Directory:** Set to `/app` inside the container
3. **Copy Files:** Copy your application code into the container
4. **Run Command:** Execute `python app.py` when container starts

### Dockerfile Structure Hints:
```dockerfile
# Use an official Python runtime as base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy application file(s) to container
COPY app.py .

# Command to run when container starts
CMD ["python", "app.py"]
```

**Note:** This is just a hint! Try to understand each line:
- `FROM` - What base operating system and runtime?
- `WORKDIR` - Where should files live inside container?
- `COPY` - What files need to be in the container?
- `CMD` - What command runs when container starts?

---

## Step 3: Build Your Docker Image

Once you've created your Dockerfile, build the image:

```bash
# Build the image with a tag name
docker build -t code_212_first_image:v1 .

# Explanation:
# docker build    - Command to build an image
# -t code_212_first_image:v1 - Tag the image with name:version
# .               - Build context (current directory)
```

### What happens during build?
1. Docker reads your Dockerfile
2. Downloads the Python 3.10 base image (if not already cached)
3. Creates a new layer for each instruction
4. Produces a final image with your app and all dependencies

### Verify your image was created:
```bash
docker images

# You should see:
# REPOSITORY    TAG    IMAGE ID      CREATED        SIZE
# code_212_first_image    v1     abc123def     2 minutes ago  125MB
```

---

## Step 4: Run Your Container

Now run your containerized application:

```bash
# Run the container interactively
docker run -it code_212_first_image:v1

# Explanation:
# docker run     - Create and start a container
# -it            - Interactive mode + allocate a terminal
#                 (-i keeps STDIN open, -t allocates pseudo-TTY)
# code_212_first_image:v1  - The image to run
```

### Try these variations:

```bash
# Run with a custom container name
docker run -it --name my-code_212_first_image code_212_first_image:v1

# Run and automatically remove container after exit
docker run -it --rm code_212_first_image:v1

# Run in detached mode (background)
docker run -d --name code_212_background code_212_first_image:v1
```

### Important Docker Run Options:

| Option | Description | Example |
|--------|-------------|---------|
| `-i` | Interactive (keep STDIN open) | `docker run -i` |
| `-t` | Allocate pseudo-TTY (terminal) | `docker run -t` |
| `-it` | Combine both for interactive terminal | `docker run -it` |
| `--rm` | Auto-remove container when it exits | `docker run --rm` |
| `--name` | Give container a custom name | `docker run --name myapp` |
| `-d` | Detached mode (run in background) | `docker run -d` |
| `-p` | Publish port (host:container) | `docker run -p 8080:80` |
| `-e` | Set environment variable | `docker run -e API_KEY=secret` |
| `-v` | Mount volume (host:container) | `docker run -v /data:/app/data` |

---

## Step 5: Share Your Image (Docker Hub)

Now let's share this image so your entire team can use it without building!

### 5.1: Create Docker Hub Account
1. Go to [hub.docker.com](https://hub.docker.com)
2. Sign up for a free account
3. Remember your username (you'll need it)

### 5.2: Login to Docker Hub
```bash
docker login

# Enter your Docker Hub username and password
```

### 5.3: Tag Your Image
```bash
# Tag format: dockerhub-username/image-name:version
docker tag code_212_first_image:v1 YOUR_USERNAME/code_212_first_image:v1

# Example:
# docker tag code_212_first_image:v1 Adamo08/code_212_first_image:v1
```

### 5.4: Push to Docker Hub
```bash
docker push YOUR_USERNAME/code_212_first_image:v1

# Example:
# docker push Adamo08/code_212_first_image:v1
```

### 5.5: Test Pulling (Simulate Teammate)
```bash
# Remove local images first
docker rmi code_212_first_image:v1
docker rmi YOUR_USERNAME/code_212_first_image:v1

# Now pull from Docker Hub
docker pull YOUR_USERNAME/code_212_first_image:v1

# Run the pulled image
docker run -it YOUR_USERNAME/code_212_first_image:v1
```

### The Power of Docker Hub:

**Before Docker Hub (Sharing Dockerfile):**
```
Dev A → Sends Dockerfile → Dev B
Dev B → Runs `docker build` (5 minutes)
Dev B → Build fails (network issue)
Dev B → Tries again (5 more minutes)
Dev B → Different base image version downloaded
Dev B → Subtle bugs appear due to version differences
Total time: 15+ minutes per developer
```

**With Docker Hub (Sharing Image):**
```
Dev A → Pushes image once → Docker Hub
Dev B → Runs `docker pull` (30 seconds)
Dev B → Runs `docker run` (instant)
Total time: 30 seconds per developer
Guaranteed: EXACT same environment
```

**For a team of 10 developers:**
- Dockerfile sharing: ~150 minutes total + debugging time
- Docker Hub: ~5 minutes total + zero debugging

---

## Essential Docker Commands

### Image Management:
```bash
# List all images
docker images

# Remove an image
docker rmi image-name:tag

# Remove all unused images
docker image prune -a

# Inspect image details
docker inspect image-name:tag

# View image history (layers)
docker history image-name:tag
```

### Container Management:
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a running container
docker stop container-name

# Start a stopped container
docker start container-name

# Restart a container
docker restart container-name

# Remove a container
docker rm container-name

# Remove all stopped containers
docker container prune

# View container logs
docker logs container-name

# Follow container logs in real-time
docker logs -f container-name

# Execute command in running container
docker exec -it container-name bash

# View container resource usage
docker stats container-name

# Inspect container details
docker inspect container-name
```

### Useful Combinations:
```bash
# Stop and remove a container
docker stop container-name && docker rm container-name

# Remove all stopped containers and unused images
docker container prune && docker image prune

# View all containers with custom format
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"

# Copy file from container to host
docker cp container-name:/path/in/container /path/on/host

# Copy file from host to container
docker cp /path/on/host container-name:/path/in/container
```

---

## What You've Learned

1. **The Problem:** Environment inconsistencies break code across different machines
2. **Dockerfile:** Blueprint for creating a Docker image
3. **Docker Build:** Creating an image from a Dockerfile
4. **Docker Run:** Starting a container from an image
5. **Docker Hub:** Sharing images for consistent deployments
6. **Key Insight:** Sharing images is faster and more reliable than sharing Dockerfiles

---

## Next Steps

Head to the `devops-social` folder for Part 2, where you'll learn:
- Multi-container applications
- Service dependencies
- Docker Compose
- Networking between containers
- Managing complex applications with a single command

---

## Troubleshooting

### Build fails with "cannot find Dockerfile":
- Make sure the file is named exactly `Dockerfile` (capital D, no extension)
- Make sure you're in the correct directory

### Container exits immediately:
- For interactive apps, use `-it` flags
- Check logs with `docker logs container-name`

### Permission denied on Docker commands:
- On Linux: Add your user to docker group or use `sudo`
- `sudo usermod -aG docker $USER` then logout/login

### Image push fails:
- Make sure you're logged in: `docker login`
- Check your image tag matches your Docker Hub username

---

Happy Dockerizing! 🐳
