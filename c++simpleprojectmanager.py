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
    print(str(PATH.resolve()))
    modules, main = [], None
    
    *
    
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
            if not main.exists(PATH):
                for module_det in modules_names:
                    modules.append(Files.Module(module_det))
                for module in modules:
                    module.exists(PATH)
                    main.add_header_include(module.get_header_include())
                    module.deploy(PATH)
                main.deploy_init(PATH)
                


            else : ## main file provided already exists
                print(f"The main file you submited already exists at : \"{PATH}\"")



                
         

            
        

        ######## MAKEFILE TIME
        
        #checking is the make file if there 
        

