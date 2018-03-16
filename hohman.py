import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import astropy.units as u
from astropy import time

from poliastro import iod
from poliastro.bodies import Sun
from poliastro.twobody import Orbit
from astropy.coordinates import solar_system_ephemeris
from poliastro.ephem import get_body_ephem

solar_system_ephemeris.set("jpl")


def go_to_mars(offset=0., tof_=6000.):
    # Initial data
    N = 50

    date_launch = time.Time('2011-11-26 15:02', scale='utc') + offset * u.day
    #date_arrival = time.Time('2012-08-06 05:17', scale='utc')
    tof = tof_ * u.h

    # Calculate vector of times from launch and arrival
    date_arrival = date_launch + tof
    dt = (date_arrival - date_launch) / N

    # Idea from http://docs.astropy.org/en/stable/time/#getting-started
    times_vector = date_launch + dt * np.arange(N + 1)

    rr_earth, vv_earth = get_body_ephem("earth", times_vector)
    rr_mars, vv_mars = get_body_ephem("mars", times_vector)

    # Compute the transfer orbit!
    r0 = rr_earth[:, 0]
    rf = rr_mars[:, -1]

    (va, vb), = iod.lambert(Sun.k, r0, rf, tof)

    ss0_trans = Orbit.from_vectors(Sun, r0, va, date_launch)
    ssf_trans = Orbit.from_vectors(Sun, rf, vb, date_arrival)

    # Extract whole orbit of Earth, Mars and transfer (for plotting)
    rr_trans = np.zeros_like(rr_earth)
    rr_trans[:, 0] = r0
    for ii in range(1, len(times_vector)):
        tof = (times_vector[ii] - times_vector[0]).to(u.day)
        rr_trans[:, ii] = ss0_trans.propagate(tof).r

    # Better compute backwards
    date_final = date_arrival - 1 * u.year
    dt2 = (date_final - date_launch) / N

    times_rest_vector = date_launch + dt2 * np.arange(N + 1)
    rr_earth_rest, _ = get_body_ephem("earth", times_rest_vector)
    rr_mars_rest, _ = get_body_ephem("mars", times_rest_vector)

    # Plot figure
    fig = plt.gcf()
    ax = plt.gca()
    ax.cla()

    def plot_body(ax, r, color, size, border=False, **kwargs):
        """Plots body in axes object.

        """
        return ax.plot(*r[:, None], marker='o', color=color, ms=size, mew=int(border), **kwargs)

    # I like color
    color_earth0 = '#3d4cd5'
    color_earthf = '#525fd5'
    color_mars0 = '#ec3941'
    color_marsf = '#ec1f28'
    color_sun = '#ffcc00'
    color_orbit = '#888888'
    color_trans = '#444444'

    # Plotting orbits is easy!
    ax.plot(*rr_earth.to(u.km).value, color=color_earth0)
    ax.plot(*rr_mars.to(u.km).value, color=color_mars0)

    ax.plot(*rr_trans.to(u.km).value, color=color_trans)
    ax.plot(*rr_earth_rest.to(u.km).value, ls='--', color=color_orbit)
    ax.plot(*rr_mars_rest.to(u.km).value, ls='--', color=color_orbit)

    # But plotting planets feels even magical!
    plot_body(ax, np.zeros(3), color_sun, 16)

    plot_body(ax, r0.to(u.km).value, color_earth0, 8)
    plot_body(ax, rr_earth[:, -1].to(u.km).value, color_earthf, 8)

    plot_body(ax, rr_mars[:, 0].to(u.km).value, color_mars0, 8)
    plot_body(ax, rf.to(u.km).value, color_marsf, 8)

    # Add some text
    #ax.text(-0.75e8, -3.5e8, -1.5e8, "MSL mission:\nfrom Earth to Mars", size=20, ha='center', va='center', bbox={"pad": 30, "lw": 0, "fc": "w"})
    ax.text(r0[0].to(u.km).value * 1.4, r0[1].to(u.km).value * 0.4, r0[2].to(u.km).value * 1.25,
            f"Earth at launch\n({date_launch.datetime:%b %d})",
            ha="left", va="bottom", backgroundcolor='#ffffff')
    ax.text(rf[0].to(u.km).value * 0.7, rf[1].to(u.km).value * 1.1, rf[2].to(u.km).value,
            f"Mars at arrival\n({date_arrival.datetime:%b %d})",
            ha="left", va="top", backgroundcolor='#ffffff')
    ax.text(-1.9e8, 8e7, 0, "Transfer\norbit", ha="right", va="center", backgroundcolor='#ffffff')

    # Tune axes
    ax.set_xlim(-3e8, 3e8)
    ax.set_ylim(-3e8, 3e8)
    ax.set_zlim(-3e8, 3e8)
    ax.view_init(30, 260)

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

_ = go_to_mars()
interact(go_to_mars, offset=(-100., 300.), tof_=(100., 12000.))

