import Controller

class TestAutoController:

    controller = Controller.Auto()

    def test_add_option(self):


        def option_test():
            print("option1")

        self.controller.addOption("option1", option_test)

        assert self.controller.get_options() == ["option1"]