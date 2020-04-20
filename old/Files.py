import pathlib as pl
from pathlib import Path
import datetime as det
import dateutil.tz as tz
import os
import getpass



class Module():

    def __init__(self, det): # det is modulename::namespacename
        assert isinstance(det, str)

        self.namespace = None
        self.class_name = None
        if len(det.split("::"))==1:
                self.module_name = det.split("::")[0]
        elif len(det.split("::"))==2:
            self.module_name = det.split("::")[0]
            self.namespace = det.split("::")[1].lower()
        elif len(det.split("::"))==3:
            self.module_name = det.split("::")[0]
            self.namespace = det.split("::")[1].lower()
            self.class_name = det.split("::")[2].title()

    def exists(self, path_init):
        path_hpp = path_init / Path(self.module_name + ".hpp")
        path_cpp = path_init / Path(self.module_name + ".cpp")
        if path_hpp.exists():
            print(f"The file {self.module_name}.hpp already exists, aborting...")
            os.abort()
        if path_cpp.exists():
            print(f"The file {self.module_name}.cpp already exists, aborting...")
            os.abort()


    def deploy(self, path_init):
        ################ HPP ###############

        path = path_init / Path(self.module_name + ".hpp")
        with path.open("w") as f:
            if self.namespace != None:
                id = "_".join([self.module_name.upper(),self.namespace.upper(),"HPP"])
            else:
                id = "_".join([self.module_name.upper(),"HPP"])


            f.write(f"#ifndef {id}\n#define {id}\n\n\n\n")

            if self.namespace != None:
                f.write(f"namespace {self.namespace}\n@\n    \n".replace("@", "{"))

                if self.class_name !=None:
                    f.write(f"    class {self.class_name}\n    @\n        public:\n\n        private:\n\n".replace("@", "{"))
                    f.write(f"    @; // class {self.class_name}\n\n".replace("@", "}"))
                f.write(f"@ // namespace {self.namespace}\n\n\n".replace("@", "}"))
            f.write(f"#endif // {id}")


        ################ CPP ###############
        path = path_init / Path(self.module_name + ".cpp")
        with path.open("w") as f:
            f.write(f"#include \"{self.module_name}.hpp\"\n")

            if self.namespace != None:
                f.write(f"namespace {self.namespace}\n@\n    \n".replace("@", "{"))
                f.write(f"@ // namespace {self.namespace}\n\n\n".replace("@", "}"))

    def get_header_include(self):
        return f"#include \"{self.module_name}.hpp\""











class Main_File:
    def __init__(self, det):
        assert type(det) is str
        self._name = det + ".cpp"
        self.headers_includes = []

    def add_header_include(self, include):
        assert type(include) is str
        assert include.startswith("#include ")
        self.headers_includes.append(include)



    def deploy_at_init(self,PATH):

        time = det.datetime.now(tz.tzlocal())
        path = PATH / Path(self._name)
        with path.open("w") as f:
            f.write(f"// File : {self._name}\n")

            f.write("// Created : " + time.strftime("%A %d %B") + " at " + time.strftime("%H") + "h - " + time.strftime("%M") + "min\n")
            f.write(f"// user : {getpass.getuser()}")
            f.write(f"\n\n//// PERSONAL MODULES\n")

            if len(self.headers_includes)!=0:
                for include in self.headers_includes:
                    f.write(f"{include}\n")
            f.write("\n\n\n//// BUILTIN LIBS\n#include <iostream>\n\n\n\nint main(){\n\n     return 0;\n}\n")      

    def deploy_at_runtime(self,PATH):
        path = PATH / Path(self._name)
        raw_data = None
        with path.open("r") as f:
            raw_data = f.read()
        sep = "//// PERSONAL MODULES\n"
        if sep in raw_data:
            raw_data_splited = raw_data.split(sep)
            start, end = raw_data_splited[0], raw_data_splited[1]
            new_includes = str()
            for include in self.headers_includes:
                new_includes+= include + "\n"
            new_raw_data = start + sep+new_includes+end
            with path.open("w") as f:
                f.write(new_raw_data)
        else:
            for include in self.headers_includes:
                new_includes+= include + "\n"
            with path.open("w") as f:

                f.write(new_includes + raw_data)



    def exists(self, PATH):
        return self.get_path(PATH).exists()

    def get_path(self, PATH):
        return PATH / Path(self._name)
