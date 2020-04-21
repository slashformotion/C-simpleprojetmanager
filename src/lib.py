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
    """
    find_headers find the files ending with ".hpp" in the path given as an argment
    
    Args:
        path (pathlib.Path): directory where the function search for .hpp files
    
    Returns:
        list(pathlib.path): list of the headers found
    """
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

    
def is_one_char_not_a_whitespace(text):
    assert type(text) is str

    for c in text:
        if c!= " ": # if one on the caracter of txt is not a whitespace
            return True
    
    return False

def is_there_space_in_middle_str(text):
    assert type(text) is str

    while text.startswith(" ") or text.endswith(" "):
        if text.startswith(" "):
            text = text[1:]

        if text.endswith(" "):
            text = text[:-1]

    
    for c in text:
        if c == " ":
            return True
    return False

        




if __name__ == "__main__":
    # test __func__ find_main_file()
    print(find_main_file(pl.Path("/home/slash/Documents/Programmation/projets/cppsimpleprojetmanager/test/lib")))


