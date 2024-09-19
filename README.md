# dynamic-multilevel-caching-system

## Overview
This project implements a dynamic multilevel caching system with support for multiple cache levels, eviction policies, and dynamic level management. The caching system supports both Least Recently Used (LRU) and Least Frequently Used (LFU) eviction policies.

## Features
- **Multiple Cache Levels**: Supports multiple levels with configurable sizes and eviction policies.
- **Eviction Policies**: Implements LRU and LFU policies.
- **Dynamic Management**: Allows adding and removing cache levels dynamically.
- **Thread Safety**: Ensures thread-safe operations using locking.

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>


   2. Navigate to the project directory:

cd dynamic-multilevel-caching-system
   3.Run the tests to ensure everything is working:

python -m unittest discover tests