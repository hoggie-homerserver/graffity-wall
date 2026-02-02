# Graffity Wall

## Description
The Graffity Wall is a simple web application that allows users to post messages to a virtual wall. It's designed to be run as a Docker container, providing an easy way to deploy a collaborative message board.

## Features
-   Post messages to a public wall.
-   Simple web interface.
-   Containerized for easy deployment with Docker.

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