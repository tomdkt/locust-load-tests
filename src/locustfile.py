from locust import HttpUser, task, between

class ApiUser(HttpUser):
    """A user that tests the /users API endpoint."""

    # The base URL of the API you are testing
    host = "http://localhost:3000"

    # A virtual user will wait between 1 and 3 seconds after each task
    wait_time = between(1, 3)

    @task(1)
    def get_all_users(self):
        """Task to simulate a GET request to /users."""
        self.client.get(
            "/users",
            name="/users [GET]"  # Optional: Group stats by method
        )

    @task(2)
    def create_user(self):
        """Task to simulate a POST request to /users."""
        # Define the JSON payload for creating a user
        user_data = {
            "name": "Test User From Locust",
            "age": 42
        }

        self.client.post(
            "/users",
            json=user_data,
            name="/users [POST]"  # Optional: Group stats by method
        )