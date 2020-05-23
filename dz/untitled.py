
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class SimpleCalculator(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(SimpleCalculator, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return SimpleCalculator.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_editor_newclass = False
        container0.css_height = "210.0px"
        container0.css_left = "20px"
        container0.css_margin = "0px"
        container0.css_position = "absolute"
        container0.css_top = "20px"
        container0.css_width = "420.0px"
        container0.variable_name = "container0"
        btnClose = Button()
        btnClose.attr_editor_newclass = False
        btnClose.css_height = "30px"
        btnClose.css_left = "300.0px"
        btnClose.css_margin = "0px"
        btnClose.css_position = "absolute"
        btnClose.css_top = "165.0px"
        btnClose.css_width = "100px"
        btnClose.text = "Close"
        btnClose.variable_name = "btnClose"
        btnClose.onclick.do(btnClose.onclick)
        container0.append(btnClose,'btnClose')
        label0 = Label()
        label0.attr_editor_newclass = False
        label0.css_background_color = "rgb(206,248,194)"
        label0.css_font_weight = "bold"
        label0.css_height = "15.0px"
        label0.css_left = "20px"
        label0.css_margin = "0px"
        label0.css_position = "absolute"
        label0.css_top = "20px"
        label0.css_width = "165.0px"
        label0.text = "Simple Calculator"
        label0.variable_name = "label0"
        container0.append(label0,'label0')
        txt1 = TextInput()
        txt1.attr_editor_newclass = False
        txt1.attr_maxlength = "0"
        txt1.css_height = "30px"
        txt1.css_left = "30.0px"
        txt1.css_margin = "0px"
        txt1.css_position = "absolute"
        txt1.css_top = "105.0px"
        txt1.css_width = "100px"
        txt1.text = ""
        txt1.variable_name = "txt1"
        container0.append(txt1,'txt1')
        txt2 = TextInput()
        txt2.attr_editor_newclass = False
        txt2.attr_maxlength = "0"
        txt2.css_height = "30px"
        txt2.css_left = "180.0px"
        txt2.css_margin = "0px"
        txt2.css_position = "absolute"
        txt2.css_top = "105.0px"
        txt2.css_width = "100px"
        txt2.text = ""
        txt2.variable_name = "txt2"
        container0.append(txt2,'txt2')
        label1 = Label()
        label1.attr_editor_newclass = False
        label1.css_height = "15px"
        label1.css_left = "150px"
        label1.css_margin = "0px"
        label1.css_position = "absolute"
        label1.css_top = "120px"
        label1.css_width = "15px"
        label1.text = "+"
        label1.variable_name = "label1"
        container0.append(label1,'label1')
        txtAnswer = Label()
        txtAnswer.attr_editor_newclass = False
        txtAnswer.css_height = "30px"
        txtAnswer.css_left = "300.0px"
        txtAnswer.css_margin = "0px"
        txtAnswer.css_position = "absolute"
        txtAnswer.css_top = "105.0px"
        txtAnswer.css_width = "100px"
        txtAnswer.text = "Answer"
        txtAnswer.variable_name = "txtAnswer"
        container0.append(txtAnswer,'txtAnswer')
        

        self.container0 = container0
        return self.container0
    


#Configuration
configuration = {'config_project_name': 'SimpleCalculator', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(SimpleCalculator, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
