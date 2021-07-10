from datetime import datetime, timedelta
from pathlib import Path
from typing import Union

import pandas as pd

import get_jma_tb.settings as settings


def get_past_weather_df_a1(prec_no: int, 
                        block_no: Union[str, int], 
                        year: int, 
                        month: int, 
                        day: int) -> pd.DataFrame:
    """
    気象庁から過去の天気テーブルを取得(白山河内:prec_no=56, block_no=0973)
    緑のマークの場所
    :param prec_no: 都道府県・地方区分番号
    :param block_no: 観測地点番号
    :param year: year
    :param month: month
    :param day: day
    """
    url: str = settings.url_a1.format(prec_no=prec_no,
                                        block_no=block_no,
                                        year=year, 
                                        month=month, 
                                        day=day)
    df: pd.DataFrame = pd.read_html(url)[0]
    df.columns = [col[1] for col in df.columns]
    timestamp = datetime(year, month, day, 0)
    timestamp = [timestamp + timedelta(hours=hour) for hour in df['時']]
    df.index = timestamp 
    return df


def get_past_weather_df_s1(prec_no: int, 
                        block_no: Union[str, int], 
                        year: int, 
                        month: int, 
                        day: int) -> pd.DataFrame:
    """
    気象庁から過去の天気テーブルを取得(金沢:prec_no=56, block_no=47605)
    赤いマークの場所
    :param prec_no: 都道府県・地方区分番号
    :param block_no: 観測地点番号
    :param year: year
    :param month: month
    :param day: day
    """
    url: str = settings.url_s1.format(prec_no=prec_no,
                                        block_no=block_no,
                                        year=year, 
                                        month=month, 
                                        day=day)
    df: pd.DataFrame = pd.read_html(url)[0]
    df.columns = [col[1] for col in df.columns]
    timestamp = datetime(year, month, day, 0)
    timestamp = [timestamp + timedelta(hours=hour) for hour in df['時']]
    df.index = timestamp 
    return df

