from PySide2 import QtWidgets
from ui import main_win
import pathlib as pl
from utils import finder, str_handling
import Files




class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_win.Ui_MainWindow()
        
        self.__generator_check = False
        self.__mode_check = False
        
        self.setup()
        
    #################################################################################################################
    ##################################################### SETUP #####################################################
    #################################################################################################################
    def setup(self):
        self.ui.setupUi(self)
        self.ui.lied_main_file.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.setup_connections()
        self.set_path_workspace()
        
        
    
    def setup_connections(self):
        # Buttons
        self.ui.btn_test.clicked.connect(lambda: self.test())
        self.ui.btn_deploy.clicked.connect(lambda: self.deploy())
        self.ui.tbtn_set_path_workspace.clicked.connect(lambda: self.set_path_workspace())

        # Combo Box
        self.ui.cbb_mode.currentTextChanged.connect(lambda: self.update_modes_main())

        
        self.ui.lied_main_file.editingFinished.connect(lambda: self.update_modes_main())
        self.ui.lied_main_file.textEdited.connect(lambda: self.update_modes_main())


        
        update_funct = lambda: self.update_generator() # fonction update pour tout les champs de génération
        for lied in self.line_edit_generator:
            lied.editingFinished.connect(update_funct)
            lied.textEdited.connect(update_funct)
        
    
    def update_init(self):
        ## main file and mode update
        self.update_modes_main()
        ## modules :
        self.update_modules()
        ## generator
        self.update_generator()
        

    def update_modules(self):
        self.ui.liwd_modules_existant.clear()
        for header in finder.find_headers(self.PATH):
            self.ui.liwd_modules_existant.addItem(header.name)
        print("update modules")

    def update_modes_main(self):
        self.mode_check = True
        if self.mode == "create":
            self.ui.lied_main_file.setReadOnly(False)

            if len(finder.find_main_file(self.PATH)) != 0: 
                # TODO : implement popup here ERROR
                print(f"There is already at least one main file in the workspace you provided .")
                # self.ui.lied_main_file.setReadOnly(True)
                self.set_main_file(finder.find_main_file(self.PATH)[0])
                self.ui.lied_main_file.setStyleSheet("background-color: #ff5252;")
                
                self.mode_check = False

            else:
                
                
                if str_handling.is_one_char_not_a_whitespace(self.ui.lied_main_file.text()) and self.ui.lied_main_file.text() != "":
                    self.ui.lied_main_file.setStyleSheet("background-color: white;")
                    self.mode_check = False
                else:
                    self.ui.lied_main_file.setStyleSheet("background-color: #ffe98f;")


        elif self.mode == "add":
            self.ui.lied_main_file.setReadOnly(True)

            if len(finder.find_main_file(self.PATH)) == 0: 
                # TODO : implement popup here ERROR
                print(f"There is already no main file in the workspace you provided .")
                self.ui.lied_main_file.clear()
                self.ui.lied_main_file.setStyleSheet("background-color: #ff5252;")
                self.mode_check = False

            elif len(finder.find_main_file(self.PATH)) > 1:
                # TODO : implement popup here ERROR
                print(f"There is already to many main file in the workspace you provided .")
                self.ui.lied_main_file.setStyleSheet("background-color: #ff5252;")
                self.mode_check = False

            else : # good ending
                self.set_main_file(finder.find_main_file(self.PATH)[0])
                self.ui.lied_main_file.setStyleSheet("background-color: #69ff78;")
        print("update modes main")

    def update_generator(self):
        self.generator_check = True

        for lied in self.line_edit_generator:            
            if str_handling.is_there_space_in_middle_str(lied.text()):
                lied.setStyleSheet("background-color: #ffd280;")
                self.generator_check = False
                

            else:
                lied.setStyleSheet("background-color: white;")



        for module_name, namespace, class_name in zip(self.module_names_list,self.namespaces_list, self.class_s_list):

            if str_handling.is_one_char_not_a_whitespace(namespace.text()) and not str_handling.is_one_char_not_a_whitespace(module_name.text()):
                module_name.setStyleSheet("background-color: #ff5252;")
                self.generator_check = False

            if str_handling.is_one_char_not_a_whitespace(class_name.text()) and not str_handling.is_one_char_not_a_whitespace(namespace.text()):
                namespace.setStyleSheet("background-color: #ff5252;")
                self.generator_check = False
        print("update generator")

        
    
    #################################################################################################################
    ##########################################  FUNC  ###############################################################
    #################################################################################################################
    def test(self, deploy = False):
        print(f"mode check : {self.mode_check} and generator check : {self.generator_check}")
        if self.generator_check and self.mode_check: # no errors in the completion of the areas
            if not deploy:
                ## success popup
                print("test Passed")
            return True
        else:
            if not deploy:
                ## ERROR POPUP
                print("test Failed")
            return False 
            
        

    def deploy(self):
        self.get_generator_formated_str()
        if self.test(deploy = True):
            if self.mode == "create" : 
                MAIN = Files.Main_File(finder.find_main_file(self.PATH)[0])
                
                
                
                HEADERS = []
        else:
            pass


    def get_generator_formated_str(self):
        str_s = []
        for module,namespace, class_name in zip(self.module_names_list, self.namespaces_list, self.class_s_list):
            if module.text() == "" or str_handling.is_only_whitespaces(module.text()) or (self.PATH / pl.Path(f"{module.text()}.hpp")).exists():
                pass
            else:
                if namespace.text() == "" or str_handling.is_only_whitespaces(namespace.text()):
                    elements = [module.text()] 
                else:
                    if class_name.text() == "" or str_handling.is_only_whitespaces(class_name.text()):
                        elements = [module.text(), namespace.text()]
                    else:
                        elements = [module.text(), namespace.text(), class_name.text()]
                         
                
                str_s.append("::".join(elements))
        print(str_s)
    #################################################################################################################
    ####################################  PROPERTIES AND SETTEUR  ###################################################
    #################################################################################################################

    def set_path_workspace(self):
        self.PATH = pl.Path(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Workspace"))
        self.ui.lbl_path_workspace.setText(self.str_path)
        # print(f"Path Set to {self.str_path}")
        self.update_init()
        
    def set_main_file(self, main_file):
        self.ui.lied_main_file.setText(main_file.name)
   
    @property
    def str_path(self):
        return str(self.PATH.resolve())

    @property
    def mode(self):
        return self.ui.cbb_mode.currentText().lower()

    @property
    def generator_check(self):
        return self.__generator_check
        
    @generator_check.setter
    def generator_check(self, b):
        try:
            if not type(b) is bool:
                raise TypeError("Must be an bool instance")
        except TypeError as e:
            print(e)
        else:
            self.__generator_check = b

    @property
    def mode_check(self):
        return self.__mode_check

    @mode_check.setter
    def mode_check(self, b):
        try:
            if not type(b) is bool:
                raise TypeError("Must be an bool instance")
        except TypeError as e:
            print(e)
        else:
            self.__mode_check = b


    @property
    def module_names_list(self):
        return [
            self.ui.lied_mod0,
            self.ui.lied_mod1,
            self.ui.lied_mod2
        ]

    @property
    def namespaces_list(self):
        return [
            self.ui.lied_namespace0,
            self.ui.lied_namespace1,
            self.ui.lied_namespace2
        ]

    @property
    def class_s_list(self):
        return [
            self.ui.lied_class0,
            self.ui.lied_class1,
            self.ui.lied_class2
        ]

    @property
    def line_edit_generator(self):
        return self.module_names_list + self.namespaces_list + self.class_s_list







if __name__ == "__main__":
    qt_app = QtWidgets.QApplication()
    app = App()
    app.show()
    qt_app.exec_()
