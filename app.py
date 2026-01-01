import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

st.set_page_config(page_title="MAT201 Visualizer", layout="wide")
st.title("Interactive Visualizer: Functions of Several Variables")

st.sidebar.header("Settings")
mode = st.sidebar.radio("Select Mode", ["Two Variables (z=f(x,y))", "Three Variables (w=f(x,y,z))"])

if mode == "Two Variables (z=f(x,y))":
    st.subheader("Functions of Two Variables:  z = f(x, y)")
    func_name = st.sidebar.selectbox(
        "Choose an Example Function",
        ["Paraboloid: x^2 + y^2", "Saddle: x^2 - y^2", "Ripple: sin(sqrt(x^2+y^2))"]
    )
    grid_n = st.sidebar.slider("Grid Resolution", 30, 120, 60, 10)
    axis_range = st.sidebar.slider("Axis Range", 2, 10, 5, 1)

    x = np.linspace(-axis_range, axis_range, grid_n)
    y = np.linspace(-axis_range, axis_range, grid_n)
    X, Y = np.meshgrid(x, y)

    if func_name.startswith("Paraboloid"):
        Z = X**2 + Y**2
        st.latex(r"z = x^2 + y^2")
    elif func_name.startswith("Saddle"):
        Z = X**2 - Y**2
        st.latex(r"z = x^2 - y^2")
    else:
        Z = np.sin(np.sqrt(X**2 + Y**2))
        st.latex(r"z = \sin(\sqrt{x^2+y^2})")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 3D Surface Plot")
        fig = plt.figure(figsize=(6, 5))
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0, antialiased=True)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        st.pyplot(fig, clear_figure=True)

    with col2:
        st.markdown("### Contour Plot (Level Curves)")
        fig2, ax2 = plt.subplots(figsize=(6, 5))
        cs = ax2.contourf(X, Y, Z, levels=30, cmap="viridis")
        ax2.contour(X, Y, Z, levels=15, colors="black", linewidths=0.5)
        ax2.set_xlabel("x")
        ax2.set_ylabel("y")
        fig2.colorbar(cs, ax=ax2, label="z value")
        st.pyplot(fig2, clear_figure=True)

else:
    st.subheader("Functions of Three Variables:  w = f(x, y, z)")
    st.write("We visualize 4D functions using **level surfaces**: the set of points where f(x,y,z)=k.")

    k = st.sidebar.slider("Level value k", 1, 25, 9, 1)
    st.latex(r"x^2 + y^2 + z^2 = k")

    # Simple sphere level surface visualization by parametric surface
    u = np.linspace(0, 2*np.pi, 80)
    v = np.linspace(0, np.pi, 80)
    U, V = np.meshgrid(u, v)
    r = np.sqrt(k)
    X = r * np.cos(U) * np.sin(V)
    Y = r * np.sin(U) * np.sin(V)
    Z = r * np.cos(V)

    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="plasma", linewidth=0, antialiased=True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    st.pyplot(fig, clear_figure=True)

    st.caption("As k increases, the radius √k increases, so the sphere grows.")
