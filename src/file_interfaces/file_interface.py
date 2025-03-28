from pathlib import Path
import pickle
import json
import numpy as np

def save_list(the_list: list, file_path: Path | str, file_format: str):
    file_format = file_format.lower()

    if isinstance(file_path, str):
        file_path = Path(file_path)

    full_path = file_path.with_suffix(f'{file_format}').expanduser()
    print(full_path)
    if file_format == '.csv':
        np.savetxt(full_path, the_list, delimiter=', ')
    elif file_format == '.json':
        with open(full_path, 'w') as f:
            json.dump({'the_list': the_list}, f) 
    elif file_format == '.pickle':
        with open(full_path, 'wb') as f:
            pickle.dump(the_list, f , pickle.HIGHEST_PROTOCOL)
    else:
        raise ValueError(f'File extension not recognized: {file_format}')
    return

if __name__ == '__main__':
    l = [1, 2, 3]
    save_list(l, 'test_csv', '.csv')
    save_list(l, Path('test_json'), '.json')
    save_list(l, Path('test_pickle'), '.pickle')