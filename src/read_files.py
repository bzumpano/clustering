from os import walk, path
import sys
import csv


def all_files(target_path):
  f = []

  for (dirpath, _, filenames) in walk(target_path):
      # f.extend(filenames)
      f.extend(path.abspath(path.join(dirpath, filename)) for filename in filenames)
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

def run():

  path = '../data/areas'
  files = all_files(path)

  print read_csv(files)
