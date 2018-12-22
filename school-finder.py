#!/usr/bin/python3
# Author: Milosz Ogaza
# Email: miloszogaza@gmail.com

import random
import plotly.plotly as py  
import plotly.graph_objs as go
import numpy as np


def find_optimal_school_location(kids_coordinates):
    aggregated_coordinates = [0, 0]
    for kid_coordinates in kids_coordinates:
      aggregated_coordinates[0] += kid_coordinates[0]
      aggregated_coordinates[1] += kid_coordinates[1]
    return aggregated_coordinates[0]/len(kids_coordinates), aggregated_coordinates[1]/len(kids_coordinates)


def spawn_kids_coordinates(kids_number=3, square_plane_boundaries=[-10, 10]):
    kids_coordinates = []
    for i in range(kids_number):
      rand_x_coordinate = random.randint(square_plane_boundaries[0], square_plane_boundaries[1])
      rand_y_coordinate = random.randint(square_plane_boundaries[0], square_plane_boundaries[1])
      kids_coordinates.append([rand_x_coordinate, rand_y_coordinate])
    return kids_coordinates


def draw_kids_and_school_plot(kids_coordinates, school_coordinates, plot_name='kids-school-plot'):
    trace_kids = go.Scatter(
      x=[kid_coordinates[0] for kid_coordinates in kids_coordinates],
      y=[kid_coordinates[1] for kid_coordinates in kids_coordinates],
      mode='markers'
    )
    trace_school = go.Scatter(
      x=[school_coordinates[0]],
      y=[school_coordinates[1]],
      marker={'color': 'red', 'symbol': 'square', 'size': 20},
      mode='markers'
    )
    data = [trace_kids, trace_school]
    py.plot(data, filename=plot_name)
  

if __name__ == "__main__":
  kids_coordinates = spawn_kids_coordinates(kids_number=500, square_plane_boundaries=[-1000, 1000])
  school_location = find_optimal_school_location(kids_coordinates)
  draw_kids_and_school_plot(kids_coordinates, school_location, 'kids-school-plot-3')


  
