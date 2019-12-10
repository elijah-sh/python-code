import argparse
import os
import logging
import json
import zipfile
import datetime
import time

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser()
# parser.add_argument("-sf", "--scale_file", default="/Users/liuneng/Documents/银联数据/数据格式处理/data_2016_2018.csv",
#                     type=str, help="历史交易规模数据")
parser.add_argument("-fl", "--file_list", type=str, help="历史数据文件列表")
parser.add_argument("-d", "--tmp_dir", default="./tmp", type=str, help="临时文件目录")
parser.add_argument("-o", "--output", default="./output", type=str, help="输出文件夹")
parser.add_argument("-p", "--period", default="15", type=str)
parser.add_argument("-mt", "--min_train", default="25", type=str)
parser.add_argument("-y", "--start_year", default="2016", type=str)
parser.add_argument("-mon", "--start_month", default="1", type=str)
if __name__ == '__main__':
    args = parser.parse_args()
    # scale_file = args.scale_file
    tmp_dir = args.tmp_dir
    output_dir = args.output
    h = args.period
    min_train = args.min_train
    year = args.start_year
    month = args.start_month


    def join_output_path(file):
        return os.path.join(output_dir, file)

    time.sleep(30)
    zipfile_path = join_output_path(f"forecast-{str(datetime.datetime.now())[:19]}.zip")
    f = open(zipfile_path, mode="wb+")
    zip_file = zipfile.ZipFile(f, mode="w", compression=zipfile.ZIP_STORED, allowZip64=True)
    zip_file.close()
    print(json.dumps(dict(type="success", message="success", paths=[zipfile_path])))
