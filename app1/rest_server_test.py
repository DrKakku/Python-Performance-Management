from locust import TaskSet, task, HttpUser, between


class HttpTask(TaskSet):
    def on_start(self):
        """Called when a simulated user starts executing tasks."""
        print("Starting the test...")

    def on_stop(self):
        """Called when a simulated user stops executing tasks."""
        print("Stopping the test...")

    @task
    def my_task(self):
        """A simple task that prints a message."""
        print("Hello, I am running a locust test, Dankesher")
        with self.client.get("/api/v1/cpu-intensive?n=30",catch_response=True) as response:  # Example HTTP request
            if response.status_code == 200:
                response.success()
                print(response.text)
            else:
                response.failure("Request failed")


class MyUser(HttpUser):
    """A user class that defines the behavior of simulated users."""
    tasks = [HttpTask]
    wait_time = between(1, 3)  # Simulate a wait time between tasks