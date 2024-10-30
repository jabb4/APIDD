## API Docker Deployment

This project is a minimal FastAPI baseplate designed for simple API applications that do not require persistent data storage. The goal is to provide a streamlined, quick-to-deploy FastAPI environment, enabling you to focus on building your API without extensive setup. For a more advanced web application stack, check out [DSDD](https://github.com/jabb4/DSDD).

### Features

- **Easy API Development**: Designed to simplify building and deploying APIs with FastAPI.
- **Live Development Mode**: Edit files in the `app` directory, and the app will automatically reload without restarting the container.

### Installation

1. Clone the repository.
2. From the directory containing your `docker-compose.yml` file, run the following command to build and start the containers:

    ```bash
    docker compose up -d --build
    ```

### Other Useful Commands

- **Stop the Containers**: Stops and removes the containers.

    ```bash
    docker compose down
    ```

- **View Logs**: Shows logs for all running containers (useful for debugging).

    ```bash
    docker compose logs -f
    ```