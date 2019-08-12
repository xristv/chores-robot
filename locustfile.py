from locust import HttpLocust, TaskSet

def syncRequest(l):
    l.client.get("/api/HttpTriggerSync")

def asyncRequest(l):
    l.client.get("/api/HttpTriggerAsync")

class UserBehavior(TaskSet):
    tasks = {syncRequest: 1, asyncRequest: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
