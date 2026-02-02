# Graffity Wall

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Version](https://img.shields.io/badge/version-v1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## Description
The Graffity Wall is a simple, Docker-containerized web application that allows users to post messages to a virtual wall. It provides an easy and portable way to deploy a collaborative message board, ideal for small communities or internal projects.

## Features
-   Post messages to a public wall.
-   Simple and intuitive web interface.
-   Easily deployable as a Docker container.
-   Supports persistent storage for messages via Docker volumes.

## Installation

### Prerequisites
-   Docker installed on your system.

### Steps
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/hoggie-homerserver/graffity-wall.git
    cd graffity-wall
    ```

2.  **Build the Docker Image:**
    Navigate to the `graffity-wall` directory and build the Docker image:
    ```bash
    docker build -t graffity-wall .
    ```

3.  **Run the Docker Container:**
    You can run the container, mapping a port (e.g., 8080) on your host to the container's internal port 5000:
    ```bash
    docker run -p 8080:5000 --name my-graffity-wall-app graffity-wall
    ```
    If you want to persist the messages, you can mount a volume for the `wall_data` directory:
    ```bash
    docker run -p 8080:5000 -v /path/to/your/host/data:/app/wall_data --name my-graffity-wall-app graffity-wall
    ```
    Replace `/path/to/your/host/data` with the actual path on your host machine where you want to store the `messages.txt` file.

## Usage
Once the Docker container is running, open your web browser and navigate to `http://localhost:8080` (or whatever port you mapped). You will see the Graffity Wall interface where you can post new messages.

## Project Structure
```
.
├── Dockerfile
├── README.md
├── app.py
└── wall_data/
    └── messages.txt
```
-   `Dockerfile`: Defines how the Docker image is built.
-   `app.py`: The main Python application logic for the Graffity Wall.
-   `wall_data/messages.txt`: Stores the messages posted on the wall. This file will be created if it doesn't exist when the application starts.