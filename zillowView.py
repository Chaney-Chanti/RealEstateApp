import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image


#create widgets and return to controller
class ZillowView:
    def __init__(self, root):
        self.root = root

    def display_Unemployment_Widget(self):
        my_image = customtkinter.CTkImage(dark_image=Image.open('data/civilian-unemployment-ra.jpeg'),
                                            light_image=Image.open('data/civilian-unemployment-ra.jpeg'),
                                            size=(1000,1000))
        customtkinter.CTkLabel(master=self.root, image=my_image, text="").place(relx=0.5,rely=0.5)

        
    def display_ZHVI_Widget(self, data):
        # print(data['RegionName']) #region data
        # print(data.iloc[13, 5:290]) #price data
        # print(data['RegionName'] == 'Riverside, CA')

        latest_avg_home_price_35th_65th_percentile = data.iloc[:,-1]
        cities = data['RegionName']
        # print(latest_avg_home_price_35th_65th_percentile)

        grouped_by_state = data.groupby('StateName')

        cali = grouped_by_state.get_group('CA')
        cali_cities = cali['RegionName']
        cali_avg_home_prices = grouped_by_state.get_group('CA').iloc[:, -1]
        # print(len(cali))
        # print(len(cali_avg_home_prices))
        fig = plt.figure(figsize=(10, 5))
        plt.ylim(0, 1500000)
        plt.bar(cali_cities, cali_avg_home_prices)
        plt.xticks(cali_cities, rotation=90)

        # fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack()

        # plt.bar(cities, latest_avg_home_price_35th_65th_percentile)
        # plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
        # plt.xticks(cities, rotation=90)
        # plt.xlabel('City, State')
        # plt.ylabel('Avg Home Price')
        # plt.title('Avg Home Price Per State In 35th-65th Percentile')
        # plt.show()
    def display_ZHVF_Widget(self, data):
        pass
    def display_ZORI_Widget(self, data):
        pass
    def display_inventory_Widget(self, data):
        pass
