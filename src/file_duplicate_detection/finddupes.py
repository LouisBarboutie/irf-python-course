"""Finds duplicates in the folder created by the create_files.py script

To check time to run, use command:
python -m cProfile finddupes.py
"""

from pathlib import Path
import time

TARGET = Path(".") / "a_few_files"
METHOD = 2


'''Method 1'''
if METHOD == 1:
    file_paths = list(TARGET.glob('*'))
    print(file_paths, sep='\n')

    t0 = time.time()
    duplicates = []
    indices = list(range(len(file_paths)))
    for index, file in enumerate(file_paths):
        t00 = time.time()
        with open(file, 'r') as f1:
            content1 = f1.read()

        for i in indices:
            
            # skip the already open file or already found duplicates
            if i == index: continue
            
            with open(file_paths[i], 'r') as f2:
                content2 = f2.read()
            
            if content1 == content2:
                duplicates.append({index, i})
        indices.pop(0)
    t1 = time.time()
    print(f'Found {len(duplicates)} duplicates in {t1-t0}s')

'''Method 2'''
if METHOD == 2:
    
    t0 = time.time()
    file_paths = list(TARGET.glob('*'))
    file_contents = [f.read_text() for f in file_paths] 
    file_dict = {key: content for (key, content) in zip(file_paths, file_contents)}
    n_files = len(file_paths)
    duplicates = set()
    for key1, val1 in file_dict.items():
        for key2, val2 in file_dict.items():
            if key1 == key2: 
                continue
            if val1 == val2:
                duplicates.add(frozenset({key1, key2}))
    t1 = time.time()
    print(f'Found {len(duplicates)} duplicates in {t1-t0}s')