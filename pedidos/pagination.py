from rest_framework.pagination import PageNumberPagination


class PaginacionGrande(PageNumberPagination):
    page_size = 50  # Queremos 50 ítems aquí
    page_size_query_param = "page_size"  # Permite al cliente decidir: ?page_size=100
    max_page_size = 100  # Tope de seguridad


class PaginacionPeque(PageNumberPagination):
    page_size = 2  # Solo 2 ítems (ej: para widgets pequeños)
