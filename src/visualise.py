import plotly.graph_objects as go
import numpy as np

def plot_uav_path(x, y, z):
    """
    Generates an interactive Plotly 3D plot showing the terrain and UAV path.
    """
    # Create a mock Indian terrain/mountain surface
    X, Y = np.meshgrid(np.linspace(0, 10, 50), np.linspace(0, 10, 50))
    Z = np.sin(X) * np.cos(Y) * 150 + 100  
    
    fig = go.Figure()

    # 1. Plot the terrain surface
    fig.add_trace(go.Surface(z=Z, colorscale='Viridis', opacity=0.8, name='Terrain'))

    # 2. Plot the UAV flight path
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', 
                               line=dict(color='red', width=6), name='UAV Flight Path'))

    fig.update_layout(title='Terrain-Aware UAV Path', autosize=True)
    return fig
