# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # def check_request(self, req):
        # #probably have a dictionary of different reqs linked to buttons on the GUI
        # if req:
        #     self.data = self.model.do_request(req)
        #     self.update_view(self.data)
    def get_ZHVI(self):
        self.update_view(self.model.get_ZHVI())

    def update_view(self, data):
        # probably determine which view to call via dictionary
        if data[0] == 'ZHVI':
            self.view.display_ZHVI_Widget(data[1])
        elif data[0] == 'ZHVF':
            self.view.display_ZHVF_Widget(data[1])
        elif data[0] == 'ZORI':
            self.view.display_ZORI_Widget(data[1])
        elif data[0] == 'inventory':
            self.view.display_inventory_Widget(data[1])