from PySide2 import QtWidgets
from ui import main_win
import pathlib as pl
from utils import finder, str_handling
import Files
from Logger import Logger

COLORS = { "correct" : "white",
            "warning" : "#ffd280",
            "critical" : "#ff5252"}

def set_background_color(lied, level):
    """
    set the background of a QLineEdit with preset levels (dict COLORS)

    Args:
        lied (QtWidgets.QLineEdit): The line edit we want to change the appearance
        level (str): level of the color

    Raises:
        TypeError: wrong type for level argument
        TypeError: wrong type for lied argument
        KeyError: level selected doesn't exists
    """

    if not type(level) is str:
            raise TypeError("Wrong type for <level> argument for set_background_color(lied, level) function, str expected.")
    else:
        if not isinstance(lied, QtWidgets.QLineEdit):
            raise TypeError("Wrong type for <lied> argument for set_background_color(lied,level) function, QtWidgets.QLineEdit expected.")
        else:
            if not level in COLORS.keys():
                keys = ", ".join([f"\"{key}\"" for key in list(COLORS.keys())]) # format to list : ['"bla"', '"bla2"',...]
                raise NotImplementedError(f"Level {level} do not exists, please use one in this list : [{keys}]")
            else:
                lied.setStyleSheet(f"background-color: {COLORS[level]};")
        


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_win.Ui_MainWindow()
        # attr
        self.color = True #control if colors are displayed to help the user 
        self.__path = pl.Path()
        self.__main_file = None
        self.__modules = None
        self.logger = Logger()
        self.logger.set_level("DEBUG")
        self.setup()

    def setup(self):
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        # area buttons
        self.ui.btn_test.clicked.connect(lambda: self.test())
        self.ui.btn_deploy.clicked.connect(lambda: self.deploy())
        self.ui.btn_reload.clicked.connect(lambda: self.refresh_app())

        # area workspace 
        self.ui.tbtn_set_path_workspace.clicked.connect(lambda: self.set_workspace())

        # area mode
        self.ui.cbb_mode.currentTextChanged.connect(lambda: self.update_area_mode())


        # area main_file
        self.ui.lied_main_file.textEdited.connect(lambda: self.update_area_main_file())
        self.logger.debug("[SETUP] QtSignals are now connected")


        # area module
        #nothing here

        # area generator
        update_funct = lambda: self.update_area_generator() # fonction update pour tout les champs de gÃ©nÃ©ration
        for lied in self.line_edit_generator:
            lied.editingFinished.connect(update_funct)
            lied.textEdited.connect(update_funct)

    def test(self):
        try :
            self.check_area_generator()
            self.check_main_file()
            self.check_modules() ### changer le nom des fonctions
        except Exception as e:
            self.logger.warning(e)
            return False
        else:
            return True

    def deploy(self):
        if self.test():
            pass
            
        

    ### UPDATE AND REFRESH FUNC

    def refresh_app(self): #DONE
        """
        Refresh the whole app by :
            - Refreshing all the information from the workspace
            - Refreshing all the UI
        """
        self.refresh_workspace()
        self.update_ui()
        self.logger.info("[APP] App fully refreshed")

    def set_workspace(self): #DONE
        self.__path = pl.Path(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Workspace"))
        
        self.logger.debug(f"[WORKSPACE] Path updated to {self.__path}")   
         
        self.refresh_workspace()

    def refresh_workspace(self): #DONE
        count, mains = finder.extensive_find_main_file(self.__path)
        self.__modules = finder.find_headers(self.__path)
        if count == 0:
            self.__main = None
        elif count == 1:
            self.__main = mains[0]
        else:
            self.__main = mains[0]    
        self.logger.info("[WORKSPACE] Workspace refreshed")
        self.update_area_workspace()
        self.update_area_main_file()
        

    def update_area_workspace(self): #DONE
        self.ui.lbl_path_workspace.setText(self.str_path)

    def update_area_mode(self): #DONE
        """
            Update the main file area after a change in the mode
        """
        self.update_area_main_file()
        self.logger.debug(f"[UI] Area mode updated")

    def update_area_main_file(self):
        count, mains = finder.extensive_find_main_file(self.__path)    
        if self.mode == "create":
            self.ui.lied_main_file.setReadOnly(False)
            try :
                if count != 0: # to many main files
                    set_background_color(self.ui.lied_main_file, "critical")
                    
                    self.ui.lied_main_file.setReadOnly(True)
                    raise Exception(f"There is {count} main files at {self.str_path}.")
            except Exception as e:
                self.logger.warning(e)
            else: # everything is cool
                set_background_color(self.ui.lied_main_file, "correct")
                
                
                
                

        elif self.mode == "add":
            self.ui.lied_main_file.setReadOnly(True)
            try:
                if count != 1:
                    set_background_color(self.ui.lied_main_file, "critical")
                    
                    raise Exception(f"There is {count} main files at {self.str_path}.")
            except Exception as e:
                self.logger.warning(e)
            else:
                self.__main_file = mains[0]
                
            
        else:
            raise NotImplementedError("This functionnality is not implemented yet, put away your time machine.")
        
            
    
    def update_area_module(self): #DONE
        self.ui.liwd_modules_existant.clear()
        for header in self.__modules: # finder.find_headers(self.__path)
            self.ui.liwd_modules_existant.addItem(header.name)
        self.logger.info("[AREA] Module list updated")

    def update_area_generator(self): #DONE
        for lied in self.line_edit_generator:            
            if str_handling.is_there_space_in_middle_str(lied.text()):
                set_background_color(lied, "warning")
            else:
                set_background_color(lied, "correct")

        for module_name, namespace, class_name in zip(self.module_names_list,self.namespaces_list, self.class_s_list):
            if str_handling.is_one_char_not_a_whitespace(namespace.text()) and not str_handling.is_one_char_not_a_whitespace(module_name.text()):
                set_background_color(module_name, "critical")

            if str_handling.is_one_char_not_a_whitespace(class_name.text()) and not str_handling.is_one_char_not_a_whitespace(namespace.text()):
                set_background_color(namespace, "critical")
        self.logger.info('[AREA] Generator updated')

    def update_ui(self): #DONE
        self.update_area_main_file()
        self.update_area_mode()
        self.update_area_generator()
        self.update_area_module()
        self.update_area_workspace()
        self.logger.info("[AREA] UI fully updated")


    ### CHECK FUNC

    def check_area_workspace(self):
        pass

    def check_area_mode(self):
        pass

    def check_main_file(self):
        pass

    def check_modules(self):
        pass

    def check_area_generator(self):
        pass

    ### PROPERTIES

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

    @property
    def str_path(self):
        return str(self.__path.resolve())

    @property
    def mode(self):
        return self.ui.cbb_mode.currentText().lower()
    




if __name__ == "__main__":
    qt_app = QtWidgets.QApplication()
    app = App()
    app.show()
    qt_app.exec_()