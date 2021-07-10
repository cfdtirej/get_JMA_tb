from pathlib import Path
from typing import Any, List, Dict, Literal

import numpy as np
import pandas as pd
from tqdm import tqdm
from influxdb import InfluxDBClient

import settings


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
            elif col == '視程(km)':
                try:
                    val = float(val)
                except:
                    val = np.nan
            vals.append(val)
        df[col] = vals
    df['雲量'] = df['雲量'].astype(str)
    return df


def write(area: str) -> None:
    client = InfluxDBClient(**settings.SETTINGS['InfluxDB'])
    csvdir = Path(__file__).parent / 'data' / f'{area}'
    csvfiles = list(csvdir.glob('**/*.csv'))
    for csvfile in tqdm(csvfiles):
        prefecture: str = csvfile.parents[3].name
        place: str = csvfile.parents[2].name
        df: pd.DataFrame = pd.read_csv(csvfile, index_col=0)
        if place in ['金沢', '新潟', '高田']:
            df = type_conv_s1(df)
        else:
            df = type_conv_a1(df)
        for timestamp, values in zip(df.index, df.values):
            fields = {}
            for col, value in zip(df.columns ,values):
                if not pd.isna(value):
                    fields[col] = value
            lineprotocol = [{
                'time': timestamp.replace(' ', 'T') + '+09:00',
                'measurement': 'weather',
                'tags': {'prefecture': prefecture, 'area': place},
                'fields': fields
            }]
            client.write_points(lineprotocol)
    return

write('新潟')
write('石川')
