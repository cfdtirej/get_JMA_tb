import time
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd

from get_tb import get_past_weather_df_a1, get_past_weather_df_s1
import settings

def main() -> None:
    JMA_NO = settings.JMA_NO
    dl_path = Path(__file__).parent / 'data'
    if not dl_path.is_dir():
        dl_path.mkdir(parents=True)
    # 昨日の日付
    _yesterday = datetime.now().date() - timedelta(1)
    # 新潟の気象データ取得
    nigata_place_no: dict = JMA_NO['新潟']
    for dt in pd.date_range('2002-01-01', '2006-01-01', freq='1d'):
        dt: date = dt.date()
        for place in nigata_place_no.keys():
            if (place == '新潟') or (place == '高田'):
                df: pd.DataFrame = get_past_weather_df_s1(
                    prec_no=nigata_place_no[place]['prec_no'],
                    block_no=nigata_place_no[place]['block_no'],
                    year=dt.year, month=dt.month, day=dt.day
                )
            else:
                df: pd.DataFrame = get_past_weather_df_a1(
                    prec_no=nigata_place_no[place]['prec_no'],
                    block_no=nigata_place_no[place]['block_no'],
                    year=dt.year, month=dt.month, day=dt.day
                )
            csvfile = dl_path / '新潟' / f'{place}' / f'{dt.year}' / f'{dt.month}' / f'{dt}.csv'
            if not csvfile.parent.is_dir():
                csvfile.parent.mkdir(parents=True)
            if not csvfile.exists():
                df.to_csv(csvfile)
        time.sleep(0.2)
    return

main()
