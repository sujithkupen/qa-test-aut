# Deployment

1. Navigate to the qa-test project directory:
    ```bash
    cd qa-test
    ```

2. Build the Docker images:
    ```bash
    docker build -t frontend-image:latest ./frontend
    docker build -t backend-image:latest ./backend
    ```

3. Start Minikube:
    ```bash
    minikube start
    ```

4. Deploy the application in Minikube:
    ```bash
    minikube kubectl -- apply -f ./Deployments
    ```

5. Setup port forwarding for the backend service:
    ```bash
    minikube kubectl port-forward svc/backend-service 3000:3000
    ```

6. Get the frontend URL:
    ```bash
    minikube service frontend-service --url
    ```

# Test Setup

1. Clone this repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the `qa-test-aut` directory:
    ```bash
    cd qa-test-aut
    ```

3. Install dependencies:
    ```bash
    npm install
    ```

4. Setup URLs in `config.js` as needed.

5. Run the integration tests:
    ```bash
    npx playwright test integration.spec.js
    ```
