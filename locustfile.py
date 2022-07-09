import base64
import locust
import random


class WebTasks(locust.TaskSet):

    @locust.task
    def load(self):
        base64string = base64.b64encode(('%s:%s' % ('user', 'password')).encode()).decode().replace('\n', '')

        catalogue = self.client.get("/catalogue").json()
        category_item = random.choice(catalogue)
        item_id = category_item["id"]

        self.client.get("/")
        self.client.get("/login", headers={"Authorization":"Basic %s" % base64string})
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))
        self.client.delete("/cart")
        self.client.post("/cart", json={"id": item_id, "quantity": 1})
        self.client.get("/basket.html")
        self.client.post("/orders")


class Web(locust.HttpUser):
    tasks = [WebTasks]
    min_wait = 0
    max_wait = 0
