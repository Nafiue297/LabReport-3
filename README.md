# Graph Coloring Using Backtracking Algorithm

## Overview
This project implements a graph coloring solution using the backtracking algorithm. The goal is to determine whether a given graph can be colored using a specified number of colors such that no two adjacent vertices share the same color.

## Problem Description
- Given an undirected graph with `N` vertices and `M` edges, the task is to check if the graph can be colored using `K` colors.
- Each vertex is assigned a color, and no two adjacent vertices can have the same color.

## Features
- Takes input for the number of vertices, edges, and available colors.
- Constructs an adjacency matrix to represent the graph.
- Uses backtracking to try and color the graph.
- Outputs whether coloring is possible and displays the color assignment, if valid.

## Requirements
- Python 3.x

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/graph-coloring-backtracking.git
