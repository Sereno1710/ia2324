import time

from problem import *
from utils import *
from hill_climbing import *
from simulated_annealing import *
from tabu_search import *
from genetic import *

num_packages = 50
map_size = num_packages*4

def main():
    package_stream = generate_package_stream(num_packages, map_size)
    solution, hc_scores = get_hc_solution(package_stream, 1000, scores_info=True)
    
    solution, sahc_scores = get_sahc_solution(package_stream, scores_info=True)
    
    show_hc_iteration_comparison_graph(hc_scores, sahc_scores)

"""def main():
    num_packages_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]
    hc_scores = []
    sahc_scores = []
    
    hc_times = []
    sahc_times = []

    
    for num_packages in num_packages_list:        
        map_size = num_packages*4
        package_stream = generate_package_stream(num_packages, map_size)

        start_time = time.time()
        solution = get_hc_solution(package_stream, 1000)
        end_time = time.time()
        execution_time = end_time - start_time
        hc_scores.append(evaluate_solution(solution))
        hc_times.append(execution_time)

        start_time = time.time()
        solution = get_sahc_solution(package_stream)
        end_time = time.time()
        execution_time = end_time - start_time
        sahc_scores.append(evaluate_solution(solution))
        sahc_times.append(execution_time)
        
    show_hc_score_comparison_graph(num_packages_list, hc_scores, sahc_scores)
    show_hc_time_comparison_graph(num_packages_list, hc_times, sahc_times)"""

"""
def main():
    num_packages_list = [15, 20, 25, 30, 35, 40, 45, 50]
    hc_scores = []
    sahc_scores = []
    sa_scores = []
    ts_scores = []
    ga_scores = []
    
    hc_times = []
    sahc_times = []
    sa_times = []
    ts_times = []
    ga_times = []
    
    for num_packages in num_packages_list:        
        map_size = num_packages*4
        package_stream = generate_package_stream(num_packages, map_size)

        start_time = time.time()
        solution1 = get_hc_solution(package_stream, 1000, True)
        end_time = time.time()
        execution_time = end_time - start_time
        hc_scores.append(evaluate_solution(solution1))
        hc_times.append(execution_time)

        start_time = time.time()
        #solution2 = get_sahc_solution(package_stream, True)
        end_time = time.time()
        execution_time = end_time - start_time
        sahc_scores.append(0)
        sahc_times.append(execution_time)

        start_time = time.time()
        solution3 = get_sa_solution(package_stream, 1000, True, False)
        end_time = time.time()
        execution_time = end_time - start_time
        sa_scores.append(evaluate_solution(solution3))
        sa_times.append(execution_time)

        start_time = time.time()
        solution4 = get_tabu_solution(package_stream, 200, 3, 10 ,True, False)
        end_time = time.time()
        execution_time = end_time - start_time
        ts_scores.append(evaluate_solution(solution4))
        ts_times.append(execution_time)
        
        start_time = time.time()
        generations = num_packages*20
        population_size = int(generations/10)
        solution5 = genetic_algorithm(generations, package_stream, population_size, False)
        end_time = time.time()
        execution_time = end_time - start_time
        ga_scores.append(evaluate_solution(solution5))
        ga_times.append(execution_time)
        
    show_best_scores_graph(num_packages_list, hc_scores, sahc_scores, sa_scores, ts_scores, ga_scores)
    show_times_graph(num_packages_list, hc_times, sahc_times, sa_times, ts_times, ga_times)"""
    


if __name__ == "__main__":
    main()
