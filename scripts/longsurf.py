import matplotlib
matplotlib.use("Agg")

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# === 1. Charger le fichier ===
ds = xr.open_dataset("long_radiation.nc")
data = ds["avg_sdlwrf"].isel(valid_time=0)
#data = np.abs(ds["avg_tnswrf"].isel(valid_time=0))

lon = ds["longitude"].values
lat = ds["latitude"].values

# === 2. Figure et projection centrée sur le Pacifique ===
fig = plt.figure(figsize=(12,6))
ax = plt.axes(projection=ccrs.Robinson(central_longitude=180))
ax.set_global()

# === 3. Tracer les données ===
#levels = np.linspace(120, 310, 30)  # 20 intervalles exacts
levels = np.arange(80, 450+10, 10)
#levels = np.round(levels).astype(int)
im = ax.contourf(
    lon,
    lat,
    data.values,
    levels=levels,
    transform=ccrs.PlateCarree(),
    cmap="turbo"  # <- palette plus adaptée pour radiation
)

#plt.colorbar(im, orientation="horizontal", pad=0.05, shrink=0.7)  # shrink <1 réduit la barre
# === 4. Ajouter terre et côtes ===
ax.add_feature(cfeature.LAND, facecolor="lightgray")
ax.add_feature(cfeature.COASTLINE, linewidth=0.6)

# === 5. Ajouter grilles avec tirets ===
gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.7, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xlocator = plt.FixedLocator(range(-180,181,60))  # méridiens tous les 60°
gl.ylocator = plt.FixedLocator(range(-90,91,30))    # parallèles tous les 30°
gl.xlabel_style = {'size':10}
gl.ylabel_style = {'size':10}

# === 6. Colorbar et titre ===
#cbar = ax.figure.colorbar(im, orientation="horizontal", fraction=0.02, pad=0.05)
cbar=plt.colorbar(im, orientation="horizontal", pad=0.05, label="W/m²" )
#cbar.set_ticks(levels)  # mêmes valeurs que les couleurs
cbar.set_ticks(levels[::2])  # <-- saute un niveau sur deux
# ticks=np.arange(120, 310, 10)  )
plt.title("Surface : Annual Mean Net Longwave Radiation (1991-2020)", fontsize=14)

# === 7. Sauvegarder et fermer ===
plt.savefig("map_surf_longwave.png", dpi=300, bbox_inches="tight")
plt.close()
print("Min =", data.min().item())
print("Max =", data.max().item())
print("Saved as map_pacific.png")
