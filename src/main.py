from src.physics import calculate_uav_path
from src.visualise import plot_uav_path

def main():
    print("--- Starting Terrain-Aware UAV Path Planner ---")
    
    # 1. Define mission parameters
    start_point = (0, 0)
    end_point = (45, 45)
    mock_terrain = None  # Will be replaced by your DEM files later
    
    # 2. Run the math
    x, y, z = calculate_uav_path(start_point, end_point, mock_terrain)
    
    # 3. Build the visualization
    fig = plot_uav_path(x, y, z)
    print("Path generated successfully! (Run locally to view interactive 3D map)")

if __name__ == "__main__":
    main()
