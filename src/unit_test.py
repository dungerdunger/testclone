import numpy as np
import itertools
import data_reading
import rooting
import os
import time
import subprocess
import random

start_time = time.time()
indices_string = '913143542'#'313192832'#
model_condition = 'avian-2X-1000-500-all'
gene_tree_path = 'data/avian_dataset/extracted_quintets/' + model_condition + '/gene_trees_mapped' + indices_string + '.tre'
species_tree_path = 'data/avian_dataset/extracted_quintets/species_tree_mapped' + indices_string + '.tre'
cmd = 'python3 rooting.py -i ' + species_tree_path + ' -o ' + gene_tree_path
print(cmd)

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
print(out.decode("utf-8"))
lis = list(out.decode("utf-8").split("\n"))
length = len(lis)

#topk_count = int(lis[length-5])
#correct_tree_count = int(lis[length-4])
#correct_topology_count = int(lis[length-3])
#avg_rf_dist = int(lis[length-2])
print(time.time() - start_time)

data_size = 1

'''print("Percentage of tests where the true species tree is among the top 3 (of 105) rooted candidates:")
print(topk_count/data_size*100)
print("Percentage of tests where the infered tree had the correct topology:")
print(correct_topology_count/data_size*100)
print("Percentage of tests where the inferred tree was the true rooted species tree :")
print(correct_tree_count/data_size*100)
print("Average RF distance (rooted, not normalized, i.e. fp+fn)")
print(avg_rf_dist/data_size)'''
