class ResultFetcher:
    def __init__(self) -> None:
        pass

    def fetch(self, num_results: int) -> list[int]:
        results = []
        page = 0

        while len(results) < num_results:
            # Llamar a la API paginada
            response = fetch_page(page)

            # Agregar los resultados obtenidos
            results.extend(response["results"])

            # Verificar si hay más páginas
            if response["next_page"] is None:
                break

            page = response["next_page"]

        # Limitar el tamaño al número de resultados requeridos
        return results[:num_results]