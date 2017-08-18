from os import walk, path
import sys
import csv


def all_files(target_path, file_extension):
  f = []

  for (dirpath, _, filenames) in walk(target_path):
      f.extend(path.abspath(path.join(dirpath, filename)) for filename in filenames if filename.endswith(file_extension))
      break

  return f


def read_csv(files):

  points = []

  for file in files:
    with (open(file, 'rb')) as csvfile:
      point = []
      csvreader = csv.reader(csvfile)
      line_num = csvreader.line_num
      for row in csvreader:
        if csvreader.line_num > 1 : point.extend(row)
      points.append(point)

  return points

def run(path = '../data/areas', extension = '.area'):
  files = all_files(path, extension)

  return read_csv(files)
