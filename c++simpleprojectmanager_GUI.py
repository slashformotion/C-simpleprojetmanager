from PySide2 import QtWidgets
from ui import main_win
import pathlib as pl 
import lib




class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_win.Ui_MainWindow()
        
        self.setup()
        
    #################################################################################################################
    ##################################################### SETUP #####################################################
    #################################################################################################################
    def setup(self):
        self.ui.setupUi(self)
        self.setup_connections()
        self.set_path_workspace()
        
        
    
    def setup_connections(self):
        # Buttons
        self.ui.btn_test.clicked.connect(lambda: self.test())
        self.ui.btn_deploy.clicked.connect(lambda: self.deploy())
        self.ui.tbtn_set_path_workspace.clicked.connect(lambda: self.set_path_workspace())

        # Combo Box
        self.ui.cbb_mode.currentIndexChanged.connect(lambda: self.update_init())

        # generator line edit
        module_names_list = [
            self.ui.lied_mod0,
            self.ui.lied_mod1,
            self.ui.lied_mod2,
            self.ui.lied_namespace0,
            self.ui.lied_namespace1,
            self.ui.lied_namespace2,
            self.ui.lied_class0,
            self.ui.lied_class1,
            self.ui.lied_class2
        ]
        update_funct = lambda: self.update_generator()
        for lied in module_names_list:
            lied.editingFinished.connect(update_funct)
            lied.textEdited.connect(update_funct)
        
    
        
    def update_init(self):
        ## main file and mode update
        self.update_modes_main()
        ## modules :
        self.update_modules()
        print("update init")

    def update_modules(self):
        self.ui.liwd_modules_existant.clear()
        for header in lib.find_headers(self.PATH):
            self.ui.liwd_modules_existant.addItem(header.name)

    def update_modes_main(self):
        if self.mode == "create":
            self.ui.lied_main_file.setReadOnly(False)

            if len(lib.find_main_file(self.PATH)) != 0: 
                # TODO : implement popup here ERROR
                print(f"There is already at least one main file in the workspace you provided .")
                self.ui.lied_main_file.setReadOnly(True)
                self.set_main_file(lib.find_main_file(self.PATH)[0])
                self.ui.lied_main_file.setStyleSheet("background-color: red;")
            else:
                self.ui.lied_main_file.clear()
                self.ui.lied_main_file.setStyleSheet("background-color: white;")
        elif self.mode == "add":
            self.ui.lied_main_file.setReadOnly(True)

            if len(lib.find_main_file(self.PATH)) == 0: 
                # TODO : implement popup here ERROR
                print(f"There is already no main file in the workspace you provided .")
                self.ui.lied_main_file.clear()
                print("debug")
                self.ui.lied_main_file.setStyleSheet("background-color: red;")
            elif len(lib.find_main_file(self.PATH)) > 1:
                # TODO : implement popup here ERROR
                print(f"There is already to many main file in the workspace you provided .")
                self.ui.lied_main_file.setStyleSheet("background-color: red;")
            else : # good ending
                self.set_main_file(lib.find_main_file(self.PATH)[0])
                self.ui.lied_main_file.setStyleSheet("background-color: green;")

    def update_generator(self):
        module_names_list = [
            self.ui.lied_mod0,
            self.ui.lied_mod1,
            self.ui.lied_mod2
        ]
        namespaces_list = [
            self.ui.lied_namespace0,
            self.ui.lied_namespace1,
            self.ui.lied_namespace2
        ]
        class_s_list = [
            self.ui.lied_class0,
            self.ui.lied_class1,
            self.ui.lied_class2
        ]
        for module_name, namespace in zip(module_names_list,namespaces_list):
            if namespace.text() != "" and module_name.text() == "":
                module_name.setStyleSheet("background-color: red;")
            else:
                module_name.setStyleSheet("background-color: white;")

        for namespace, class_name in zip(namespaces_list, class_s_list):
            if class_name.text() != "" and namespace.text() == "":
                namespace.setStyleSheet("background-color: red;")
            else:
                namespace.setStyleSheet("background-color: white;")


    
    #################################################################################################################
    ##########################################  FUNC  ###############################################################
    #################################################################################################################
    def test(self):
        print("func test")
        

    def deploy(self):
        print("func deploy")

    #################################################################################################################
    ####################################  PROPERTIES AND SETTEUR  ###################################################
    #################################################################################################################

    def set_path_workspace(self):
        self.PATH = pl.Path(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Workspace"))
        self.ui.lbl_path_workspace.setText(self.str_path)
        print(f"Path Set to {self.str_path}")
        self.update_init()
        
    def set_main_file(self, main_file):
        self.ui.lied_main_file.setText(main_file.name)

    @property
    def str_path(self):
        return str(self.PATH.resolve())

    @property
    def mode(self):
        return self.ui.cbb_mode.currentText().lower()







if __name__ == "__main__":
    qt_app = QtWidgets.QApplication()
    app = App()
    app.show()
    qt_app.exec_()
