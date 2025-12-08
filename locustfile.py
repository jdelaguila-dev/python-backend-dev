from locust import HttpUser, task, between


class UsuarioHambriento(HttpUser):
    # Tiempo de espera entre acciones (simula a un humano pensando)
    wait_time = between(1, 3)

    @task(3)  # Peso 3: Es más probable que vean el menú
    def ver_menu(self):
        self.client.get("/api/productos/")

    @task(1)  # Peso 1: Menos probable que vean una categoría
    def ver_categoria(self):
        self.client.get("/api/categoria/")  # Ejemplo: categoría 1
