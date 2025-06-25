from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import random

# Buat matriks jarak (termasuk kemacetan)
def create_data_model():
    data = {}
    n = 20
    # Simulasi matriks jarak dengan kemacetan (misal random antara 10-100)
    data['distance_matrix'] = [
        [0 if i == j else random.randint(10, 100) for j in range(n)]
        for i in range(n)
    ]
    data['num_vehicles'] = 1
    data['depot'] = 0  # Titik awal kurir
    return data

def print_solution(manager, routing, solution):
    print('Jalur efektif kurir:')
    index = routing.Start(0)
    route = []
    route_distance = 0
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    route.append(manager.IndexToNode(index))
    print(" -> ".join(map(str, route)))
    print('Total jarak/waktu tempuh (termasuk macet): {} satuan'.format(route_distance))

def main():
    data = create_data_model()

    # Buat manajer dan model routing
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        # Konversi index internal ke node sebenarnya
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Strategi awal pencarian solusi
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Cari solusi
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print_solution(manager, routing, solution)
    else:
        print('Tidak ditemukan solusi.')

if __name__ == '__main__':
    main()
