from django.core.management.base import BaseCommand
from django.db import transaction

from pedidos.models import Categoria, Producto, Pedido


class Command(BaseCommand):
    help = "Populate the database with sample categories, products, and orders"

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(
                self.style.MIGRATE_HEADING("Creating Burger Queen demo data...")
            )
            categorias = self._create_categorias()
            productos = self._create_productos(categorias)
            self._create_pedidos(productos)
        self.stdout.write(self.style.SUCCESS("Seed data created successfully."))

    def _create_categorias(self):
        catalog = {
            "Hamburguesas": {
                "descripcion": "Clásicos de la casa con combinaciones especiales",
            },
            "Bebidas": {
                "descripcion": "Refrescos, malteadas y opciones sin azúcar",
            },
            "Acompañamientos": {
                "descripcion": "Papas fritas, aros de cebolla y más",
            },
        }
        categorias = {}
        for nombre, campos in catalog.items():
            categoria, _created = Categoria.objects.get_or_create(
                nombre=nombre, defaults=campos
            )
            categorias[nombre] = categoria
            action = "Created" if _created else "Skipped"
            self.stdout.write(f"  {action} categoria: {nombre}")
        return categorias

    def _create_productos(self, categorias):
        catalog = [
            {
                "nombre": "Classic Queen",
                "descripcion": "Carne 100% res, queso cheddar y salsa especial",
                "precio": 8.50,
                "categoria": categorias["Hamburguesas"],
            },
            {
                "nombre": "Royal Bacon",
                "descripcion": "Doble carne, tocino ahumado y cebolla caramelizada",
                "precio": 10.90,
                "categoria": categorias["Hamburguesas"],
            },
            {
                "nombre": "Mega Papas",
                "descripcion": "Papas crujientes con salsa de queso",
                "precio": 4.75,
                "categoria": categorias["Acompañamientos"],
            },
            {
                "nombre": "Malteada Fresa",
                "descripcion": "Helado artesanal con leche entera",
                "precio": 5.40,
                "categoria": categorias["Bebidas"],
            },
            {
                "nombre": "Refresco Cola",
                "descripcion": "Bebida gaseosa clásica en lata",
                "precio": 2.00,
                "categoria": categorias["Bebidas"],
            },
            {
                "nombre": "Aros de Cebolla",
                "descripcion": "Aros crujientes con salsa tártara",
                "precio": 3.80,
                "categoria": categorias["Acompañamientos"],
            },
            {
                "nombre": "Veggie Delight",
                "descripcion": "Hamburguesa vegetariana con aguacate y brotes frescos",
                "precio": 9.20,
                "categoria": categorias["Hamburguesas"],
            },
            {
                "nombre": "Malteada Vainilla",
                "descripcion": "Helado de vainilla con leche entera",
                "precio": 5.40,
                "categoria": categorias["Bebidas"],
            },
            {
                "nombre": "Papas con Queso y Tocino",
                "descripcion": "Papas fritas cubiertas con queso derretido y trozos de tocino",
                "precio": 6.00,
                "categoria": categorias["Acompañamientos"],
            },
            {
                "nombre": "Doble Queso",
                "descripcion": "Doble carne con doble queso cheddar",
                "precio": 11.50,
                "categoria": categorias["Hamburguesas"],
            },
        ]
        productos = []
        for campos in catalog:
            producto, created = Producto.objects.get_or_create(
                nombre=campos["nombre"],
                defaults={
                    "descripcion": campos["descripcion"],
                    "precio": campos["precio"],
                    "categoria": campos["categoria"],
                },
            )
            productos.append(producto)
            action = "Created" if created else "Skipped"
            self.stdout.write(f"  {action} producto: {producto.nombre}")
        return productos

    def _create_pedidos(self, productos):
        if Pedido.objects.exists():
            self.stdout.write("  Skipped pedidos: records already exist")
            return

        sample_orders = [
            {
                "producto": productos[0],
                "nombre_cliente": "María Fernanda",
                "direccion": "Av. Central 123",
            },
            {
                "producto": productos[1],
                "nombre_cliente": "Luis Alberto",
                "direccion": "Calle 45 #98",
            },
            {
                "producto": productos[2],
                "nombre_cliente": "Daniela R.",
                "direccion": "Residencial Los Pinos",
            },
        ]
        for campos in sample_orders:
            pedido = Pedido.objects.create(**campos)
            self.stdout.write(f"  Created pedido: {pedido}")
