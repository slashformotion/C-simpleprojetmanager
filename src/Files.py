import pathlib as pl
from pathlib import Path
import datetime as det
import dateutil.tz as tz
import os
import getpass


class MetaFile(type):
    def __new__(cls, name, bases, body):
        """
        Me
        """
        print(name,bases, body)
        if not 'EXTENSION' in body:
            raise NotImplementedError("EXTENSION class attr is not declared")
        else:
            if not isinstance(body['EXTENSION'],str):
                raise TypeError("Wrong type for \"EXTENSION\" class attr is not declared")

        return super().__new__(cls, name, bases, body)

class File(metaclass = MetaFile):
    """
    sub class : define file 

    Args:
        metaclass (MetaFile), optional): . Defaults to MetaFile.
    """
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name

    @property
    def reduced_path(self):
        return Path("".join([self.name, self.EXTENSION]))


class Main(File):
    
    EXTENSION = "cpp"
    def __init__(self, name):
        super().__init__(name)
        self.headers_names = []

    def add_header(self, header_name):
        """
        add header_name argument to headers_names attribut list 

        Args:
            header_name (str): header_name to include

        Raises:
            TypeError: Error on the argument type
        """
        try:
            if not isinstance(header_name, str):
                raise TypeError("Wrong type for <header_name> argument in Main.add_header() function")
        except TypeError as e:
            print(e)
        else:
            self.headers_names.append(header_name)
        
    def __get_includes(self):
        """
        return a single string containing all of the includes for the deploy function

        Returns:
            str: all of the includes we need
        """
        str_includes = ""

        for hn in self.headers_names:
            str_includes += f"#include \"{hn}.{self.EXTENSION}\"\n" 

        return str_includes
        
    def __get_date(self):
        """
        return the date

        Returns:
            datetime.datetime: current date of the detected timezone
        """
        return det.datetime.now(tz.tzlocal())

    def __deploy_on_create(self,MAIN_FILE):
        """
        deploy main file when it doesn't exist

        Args:
            WORKSPACE (pathlib.Path): path to workspace
        """
        time = self.__get_date()
        with MAIN_FILE.open("w") as f:
            #PRESENTATION HEADER
            f.write(f"// File : {self.reduced_path.name}\n")
            f.write("// Created : " + time.strftime("%A %d %B") + " at " + time.strftime("%H") + "h - " + time.strftime("%M") + "min\n")
            f.write(f"// user : {getpass.getuser()}\n")
            # INCLUDE INSTRUCTION AND MAIN FUNC
            f.write(f"\n//// PERSONAL MODULES\n")
            f.write(self.__get_includes())
            f.write("\n\n//// BUILTIN LIBS\n#include <iostream>\n\n\n\nint main(){\n\n     return 0;\n}\n")   

    def __deploy_on_edit(self,MAIN_FILE):
        raw_data = None
        with MAIN_FILE.open("r") as f:
            raw_data = f.read()
        sep = "//// PERSONAL MODULES\n"
        if sep in raw_data:
            raw_data_splited = raw_data.split(sep)
            del raw_data
            start, end = raw_data_splited
            new_includes = self.__get_includes()   
            
            new_raw_data = start + sep + new_includes + end
            with MAIN_FILE.open("w") as f:
                f.write(new_raw_data)
        else:
            with MAIN_FILE.open("w") as f:

                f.write(self.__get_includes() + raw_data)
        
    def deploy(self,WORKSPACE):
        if not WORKSPACE.is_dir():
            raise TypeError("Wrong type for <WORKSPACE> argument")
        
        MAIN_FILE = WORKSPACE / self.reduced_path
        if not MAIN_FILE.exists():
            self.__deploy_on_create(MAIN_FILE)
        else:
            self.__deploy_on_edit(MAIN_FILE)


        
        
   
    





    

