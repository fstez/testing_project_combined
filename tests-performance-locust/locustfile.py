"""Locusti skript, mis simuleerib 20–50 kasutajad backend API-le."""

from locust import HttpUser, between, task


class KoondApiUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def lae_koond(self) -> None:
        vastus = self.client.get("/api/koond")
        vastus.raise_for_status()

    @task(1)
    def tervise_kontroll(self) -> None:
        self.client.get("/status")


# Käivitussoovitused:
# locust -f tests-performance-locust/locustfile.py --headless -u 20 -r 2 --run-time 3m --host http://localhost:8000 --csv docs/results/locust/koormus

