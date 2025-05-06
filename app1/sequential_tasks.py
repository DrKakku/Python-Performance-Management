from locust import User, task, between, SequentialTaskSet


class TaskSet1(SequentialTaskSet):

    @task
    def my_task(self):
        print("Hello i am running a locust test, Dankesher")

    @task
    def my_task2(self):
        print("This is the task 2, Can i have some sugar")

    @task
    def my_task3(self):
        print("This tea is amazing")

class MyUser(User):
    wait_time = between(1,3)
    tasks = [TaskSet1]
