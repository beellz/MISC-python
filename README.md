# MISC-python
# ip-tool: IP Network Collision Detector

## Overview

The `ip-tool` is a simple script designed to report configured IP networks within a container and detect overlapping IP ranges (collisions) across a Kubernetes cluster. This tool is useful for identifying potential network configuration issues.


## Requirements

*   Python 3.6 or higher
*   `ipaddress` module (usually included with Python 3.3+)
*   Docker (if you want to build and run the Docker image)
*   kubectl (if you want to deploy to Kubernetes)

## Installation and Setup

1.  **Clone the Repository**

    ```
    git clone https://github.com/beellz/MISC-python.git
    cd ip-tool
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**

    ```
    python3 -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

## Usage

### 1. Running the Script Locally

1.  **Make the script executable:**

    ```
    chmod +x main.py
    ```

2.  **Run the script to report configured IP networks (Default Function):**

    ```
    ./main.py
    ```

    This will output a JSON list of IP networks (using dummy data).

3.  **Check for IP collisions (Collision Check):**

    1.  Create a `network.json` file with a list of IP networks you want to check for collisions. For example:

        ```
        [
          "192.168.1.0/24",
          "192.168.0.0/16",
          "10.0.0.0/8",
          "10.1.0.0/16"
        ]
        ```

    2.  Run the script with the `--check-collision` flag:

        ```
        ./main.py --check-collision network.json
        ```

        This will report any overlapping IP networks found in the `network.json` file.


### 2. Running with Docker

1.  **Build the Docker image:**

    ```
    docker build -t ip-tool .
    ```

2.  **Run the container to report configured IP networks (Default Function):**

    ```
    docker run --rm ip-tool

    ```

3.  **Check for IP collisions (Collision Check):**

    1.  Mount the `network.json` file into the container:

        ```
        docker run --rm -v $(pwd)/network.json:/app/network.json ip-tool --check-collision /app/network.json
        ```

### 3. Running on Docker or Kubernetes 

1.  **Build and Push the Docker Image**

    First, you'll need to build the Docker image and push it to a container registry (e.g., Docker Hub, Google Container Registry, etc.).

    ```
    docker build -t your-dockerhub-username/ip-tool .

    ```
    You can push it to you docker repository

2.0  **Deploy using Docker-compose 
    
    To run docker-compose, Run the command of docker-compose

    '''
    docker-compose -f docker-compose.yaml up 

    '''
    as soon as the command is ran you will get the output for the collision ip's


2.  **Deploy to Kubernetes**

    1.  Apply the Kubernetes deployment:

        ```
        kubectl apply -f k8-ip-tool.yaml
        ```

3.  **Run Command in Kubernetes**

       *   List the pods to choose one:

        ```
        kubectl get pods
        ```

        This will output something like:

        ```
        NAME                                  READY   STATUS    RESTARTS   AGE
        k8-ip-tool-6b8b9b7f5f-4q9mz   1/1     Running   0          20m
        ```

4.  **Checking for IP Collisions**

      *  Copy the `network.json` file into the pod:

        ```
        kubectl cp network.json k8-ip-tool-6b8b9b7f5f-4q9mz:/app/network.json
        ```

         *   Then, execute the collision check command (again, replace the pod name if necessary):

        ```
        kubectl exec -it k8-ip-tool-6b8b9b7f5f-4q9mz -- python /app/main.py --check-collision /app/network.json
        ```

        This command is similar to the previous one, but it includes the `--check-collision /app/network.json` argument, which tells the script to check for collisions using the specified JSON file.


## License

[MIT License]

---




