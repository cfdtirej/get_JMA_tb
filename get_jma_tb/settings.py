from pathlib import Path
import yaml

# 緑の場所
url_a1: str = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php?prec_no={prec_no}&block_no={block_no}&year={year}&month={month}&day={day}&view='
# 赤の場所
url_s1: str = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no={prec_no}&block_no={block_no}&year={year}&month={month}&day={day}&view='

jma_no_yaml = Path(__file__).parent / 'jma_no.yaml'
with open(jma_no_yaml) as yf:
    # 気象庁の地方区分・観測地点番号
    JMA_NO: dict = yaml.safe_load(yf)
