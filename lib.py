import pathlib as pl



def find_main_file(path):
    """
    find_main_file find .cpp files with an "int main(args)" function declaration        
    
    Args:
        path (pathlib.Path): path to a folder
    
    Returns:
        list(path like objects)
    """
    file_list = []
    for cpp in find_files(path, "cpp"):
        cpp = pl.Path(cpp)
        with cpp.open('r') as flux:
            cpp_content = flux.read()
            if "int main(" in cpp_content:
                file_list.append(cpp)
    return file_list

def find_headers(path):
    file_list = []
    for cpp in find_files(path, "hpp"):
        file_list.append(cpp)
    return file_list


def find_files(path, ext):
    """
    find_files : return files with <.ext> at the given path
    
    Args:
        path (pathlib.Path): where to search files  
        ext (str): extension of the files to retreive
    
    Returns:
        list(pathlib.Path): list of the path of the files searched
    """
    assert isinstance(ext, str)
    file_list = []
    for cpp in sorted(path.glob(f"*.{ext}")):
        file_list.append(pl.Path(cpp))
    return file_list

    
        




if __name__ == "__main__":
    # test __func__ find_main_file()
    print(find_main_file(pl.Path("/home/slash/Documents/Programmation/projets/cppsimpleprojetmanager/test/lib")))


