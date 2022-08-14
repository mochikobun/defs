from ast import Str
from asyncio.windows_events import NULL
from typing import Dict
import pandas as pd

### データフレームに関する関数 ###

def convertDFToDict(df:pd.DataFrame, additional_key_list:list, combine_char=">"):
    """DataFrameを辞書に変換する
    DataFrameのy軸の列のカラム名にprefix(additional_key_listで複数の項目をprefixとしてつけることが可能)をつけ、
    DataFrameのindexをx軸に、0列からの各列をy軸に持ってきた、xyプロットのDataFrameをValueにする

    Args:
        df (pd.DataFrame): 辞書にしたいdf
        additional_key_list (): 辞書にする際にkeyに追加したい文字列を指定
        combine_char (str, optional): 結合に使う文字列. Defaults to ">".

    Returns:
        df_dict (dictionary): 生成した辞書
    """
    # keyに追加する文字列を生成
    additional_key = combineStr(additional_key_list, combine_char, True)

    # この辞書にdfのデータを追加していく
    df_dict = {}

    # カラムのリストを作成
    column_list = df.columns.to_list()

    # xyデータのデータフレームを辞書に追加
    for i in range(len(column_list)):
        # keyを生成
        key = additional_key + column_list[i]

        # xyデータを作成
        xy_df = pd.DataFrame()
        xy_df["x"] = df.index.to_list()
        xy_df["y"] = df.iloc[:,i].to_list()

        # 辞書に追加
        df_dict[key] = xy_df
    
    return df_dict

# 辞書からkeyが部分一致しているvalueを検索する
def searchValueInDictByKeyPartialMatch(dict:dict, key_str:str):
    for key, value in dict.items():
        if key_str in key:
            return value
    return NULL


### 一般的な関数 ###

# 文字列のリストと結合文字から結合文字列を生成する
def combineStr(str_list, combine_char, last_combine_flag):
    
    # これに文字列を結合していく
    combined_str = ""
    
    # 文字列結合
    for s in str_list:
        combined_str += s
        combined_str += combine_char
    
    # 最後の結合文字を残すかどうか
    if last_combine_flag:
        return combined_str
    else:
        return combined_str[:-len(combine_char)]
