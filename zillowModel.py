import pandas as pd

class ZillowModel:
    def __init__(self):
        self.data = {
            'ZHVI': ['ZHVI', pd.read_csv('data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv', delimiter=',', encoding='utf-8')], # Home Value Index - A measure of the typical home value and market changes across a given region and housing type. It reflects the typical value for homes in the 35th to 65th percentile range. Available as a smoothed, seasonally adjusted measure and as a raw measure.
            'ZHVF': ['ZHVF', pd.read_csv('data/Metro_zhvf_growth_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv', delimiter=',', encoding='utf-8')], # Home Value Forecast
            'ZORI': ['ZORI', pd.read_csv('data/Metro_zori_sm_month.csv', delimiter=',', encoding='utf-8')], # Observed Rent Index
            'inventory': ['inventory', pd.read_csv('data/Metro_invt_fs_uc_sfrcondo_sm_month.csv', delimiter=',', encoding='utf-8')],
            # "list_sale_prices": pd.read_csv(, sep='\t'),
            # "sales_count_price_cuts": pd.read_csv(, sep='\t'),
        }

    def get_ZHVI(self):
        return self.data['ZHVI']
    def get_ZHVF(self):
        return self.data['ZHVF']
    def get_ZORI(self):
        return self.data['ZORI']
    def get_inventory(self):
        return self.data['inventory']
