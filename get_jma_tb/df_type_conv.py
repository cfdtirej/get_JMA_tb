from typing import Any, List, Dict, Literal

import numpy as np
import pandas as pd


def type_conv_a1(df: pd.DataFrame) -> pd.DataFrame:
    cols_name: List[str] = ['降水量(mm)', '気温(℃)', '風速', '風向', '日照時間(h)', '降雪', '積雪']
    for col in cols_name:
        vals: List[Any] = []
        for val in df[col]:
            if col == '降水量(mm)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '気温(℃)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '風速':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '風向':
                if val in ['///', '--']:
                    val = np.nan
            elif col == '日照時間(h)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '降雪':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '積雪':
                try:
                    val = float(val)
                except:
                    val = np.nan
            vals.append(val)
        df[col] = vals
    return df


def type_conv_s1(df: pd.DataFrame) -> pd.DataFrame:
    cols_name: List[str] = ['現地', '海面', '降水量(mm)', '気温(℃)', '露点温度(℃)', '蒸気圧(hPa)', '湿度(％)', 
                            '風速', '風向', '日照時間(h)', '全天日射量(MJ/㎡)', '降雪', '積雪', '天気', '雲量', '視程(km)']
    for col in cols_name:
        vals: List[Any] = []
        for val in df[col]:
            if col == '現地':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '海面':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '降水量(mm)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '気温(℃)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '露点温度(℃)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '蒸気圧(hPa)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '湿度(％)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '風速':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '風向':
                if val in ['///', '--']:
                    val = np.nan
            elif col == '日照時間(h)':
                try:
                    val = float(val)
                except:
                    val = np.nan
                    
            elif col == '全天日射量(MJ/㎡)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '降雪':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '積雪':
                try:
                    val = float(val)
                except:
                    val = np.nan
            elif col == '天気':
                if val in ['///', '--']:
                    val == np.nan
            elif col == '雲量':
                if val in ['///', '--']:
                    val == np.nan
            elif col == '視程(km)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            vals.append(val)
        df[col] = vals
    return df