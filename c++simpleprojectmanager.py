import os
import sys 
import pathlib as pl 
from pathlib import Path

import lib
import Files






if __name__ == "__main__": 
    
    #executing
    modes = ['create', 'add']
    mode_submited, main_name, modules_names = lib.unpack_args(sys.argv)
    PATH = Path(os.getcwd())
    modules, main = [], None
    
    ### Checking if the submited mode exists
    if mode_submited not in modes: 
        line =str()
        for index, mode in enumerate(modes):
            if index!=len(mode)-1 :
                line += "\"" + mode + "\", "
            else:
                line +=  "\"" + mode + "\""
        print(f"This mode \"{mode_submited}\" do not exist, please retry with a correct one ({line})")
        
    else:
        if len(modules_names)==0 and mode_submited==mode[1]:
            print("This mode (add) is not usable with 0 modules names provided")


        else:
            main = Files.Main_File(main_name)
            if not main.exists(PATH): ## MODE : CREATE
                for module_det in modules_names:
                    modules.append(Files.Module(module_det))
                for module in modules:
                    module.exists(PATH)
                    main.add_header_include(module.get_header_include())
                    module.deploy(PATH)
                main.deploy_at_init(PATH)
                if len(modules)!=0:
                        
                        print("~~~ Files Created : ~~~")
                        for module in modules:
                            print(f"    - {module.module_name}.cpp")
                            print(f"    - {module.module_name}.hpp")
                        print(f"    - {main_name}.cpp")
                        
                else: 
                       print("Nothing happened, my friend! (You submited 0 name for module creation.)")

            else : ## main file provided already exists 
                if mode_submited == modes[0]: # secu
                    print(f"The file <{main_name}.cpp> you submited already exists, aborting ...  ")
                    os.abort()
                else: ## MODE ADD
                    for module_det in modules_names:
                        modules.append(Files.Module(module_det))
                    for module in modules:
                        module.exists(PATH)
                        main.add_header_include(module.get_header_include())
                        module.deploy(PATH)
                    if len(modules)!=0:
                        main.deploy_at_runtime(PATH)
                        print("~~~ Files Created : ~~~")
                        for module in modules:
                            print(f"    - {module.module_name}.cpp")
                            print(f"    - {module.module_name}.hpp")

                        print(f"{main_name}.cpp have been modified")
                    else: 
                        print("Nothing happened, my friend! (You submited 0 name for module creation.)")
                        
        ######## MAKEFILE TIME
        
        #checking is the make file if there 
        lib.check_makefile(PATH)
        

