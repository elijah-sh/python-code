import pandas as pd
from xlrd import xldate_as_datetime
from collections import OrderedDict, defaultdict
from datetime import datetime
import numpy as np
import os
import argparse
import json
from config import CONFIG


def _transform_date(df, col, date_format):
    if "int" in str(df[col].dtype):
        df[col] = df[col].apply(lambda x: xldate_as_datetime(x, 0))
    elif "str" in str(df[col].dtype) or "object" in str(df[col].dtype):
        df[col] = pd.to_datetime(df[col], format=date_format)
    return df


def _fill_column(df, col):
    prev_value = None

    def value(x):
        global prev_value
        if not pd.isna(x) or x == '':
            prev_value = x
            return x
        return prev_value

    df[col] = df[col].apply(value)


def _merge_multi_df(data):
    if isinstance(data, OrderedDict):
        return pd.concat([data[item] for item in data])
    return data


def _filter_summary(df):
    cols = ["date", "company", "cardType", "mcc", "range"]
    for col in cols:
        if col in df.columns:
            df = df[df[col].astype(str) != "总计"]
    return df


class FileChecker:
    def __init__(self, path, columns, target_columns, date_col, date_format):
        self.df = None
        self.file = path
        self.columns = columns
        self.date_col = date_col
        self.date_format = date_format
        self.target_columns = target_columns
        self.load()

    def load(self):
        data = pd.read_excel(self.file, sheet_name=None)
        data = _merge_multi_df(data)
        if isinstance(data.index, pd.MultiIndex):
            data.reset_index(inplace=True)
        self.df = data

    def check_columns(self):
        df_cols = self.df.columns
        if len(df_cols) != len(self.columns):
            raise RuntimeError("文件列数量不匹配")
        self.df.columns = self.columns
        for col in self.columns:
            if col not in self.target_columns:
                _fill_column(self.df, col)
            else:
                self.df[col] = self.df[col].astype(np.double)
        self.df.fillna(0, inplace=True)
        self.df = _filter_summary(self.df)

    def check_date(self):
        if "int" not in str(self.df[self.date_col].dtype) and "str" not in str(
                self.df[self.date_col].dtype) and "object" not in str(self.df[self.date_col].dtype):
            raise RuntimeError("日期列格式不匹配")
        _transform_date(self.df, self.date_col, self.date_format)


def separate_df(df, col):
    values = df[col].unique()
    df_map = dict()
    for value in values:
        tmp_df = df[df[col] == value]
        if isinstance(value, datetime):
            df_map[value.strftime("%Y%m")] = tmp_df
        elif isinstance(value, np.datetime64):
            df_map[pd.to_datetime(value).strftime("%Y%m")] = tmp_df
        else:
            df_map[str(value)] = tmp_df
    return df_map


def get_summary_data(data_map, summary_columns, date_col):
    summary_list = []
    for key in data_map:
        summary = {"date": key}
        for col in summary_columns:
            summary[col] = data_map[key].groupby(date_col, as_index=False).sum()[col].values[0]
        summary_list.append(summary)
    return summary_list


def store_df(data_map, output_dir, prefix=""):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    paths = []
    for key in data_map:
        file_path = os.path.join(output_dir, f"{prefix}{'-'if prefix!= '' else ''}{key}.csv")
        data_map[key].to_csv(file_path, index=False, encoding="utf_8_sig")
        paths.append(file_path)
    return paths


def create_response(type_, message, files=None, summary=None):
    if type_ == "error":
        response = dict(type=type_, message=message)
    else:
        response = dict(type=type_, message=message, files=files, summary=summary)
    return json.dumps(response, ensure_ascii=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default="/Users/liuneng/Desktop/银联数据/POS消费交易-11月2.xlsx",
                        help="导入的文件路径")
    parser.add_argument("-od", "--output_dir", type=str, default="test", help="输出文件夹")
    parser.add_argument("-t", "--type", type=str, default="收入", help="数据类型,交易规模数据,还是收入数据")
    args = parser.parse_args()
    file = args.file
    type_ = args.type
    output_dir = args.output_dir
    columns = CONFIG["income"]["columns"]
    target_column = CONFIG["income"]["target_columns"]
    date_column = CONFIG["income"]["date_column"]
    date_format = CONFIG["income"]["date_format"]
    try:
        file_checker = FileChecker(file, columns, target_column, date_column, date_format)
        file_checker.check_columns()
        file_checker.check_date()
        df = file_checker.df
        df_map = separate_df(df, file_checker.date_col)
        paths = store_df(df_map, output_dir, prefix=type_)
    except Exception as e:
        print(create_response("error", str(e)))
        exit(0)
    summary = get_summary_data(df_map, target_column, date_column)
    print(create_response("success", "预处理成功", files=paths, summary=summary))
