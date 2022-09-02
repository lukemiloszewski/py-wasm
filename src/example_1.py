import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

fig, ax = plt.subplots(figsize = (5,4), dpi = 200)

data_1 = pd.Series([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5])
data_2 = pd.Series([5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0])

x_fill = pd.Series(range(len(data_1)))

x_fill_aux = x_fill.copy()
x_fill_aux.index = x_fill_aux.index * 10
last_idx = x_fill_aux.index[-1] + 1
x_fill_aux = x_fill_aux.reindex(range(last_idx))
x_fill_aux = x_fill_aux.interpolate()

data_1_aux = data_1.copy()
data_1_aux.index = data_1_aux.index * 10
last_idx = data_1_aux.index[-1] + 1
data_1_aux = data_1_aux.reindex(range(last_idx))
data_1_aux = data_1_aux.interpolate()

data_2_aux = data_2.copy()
data_2_aux.index = data_2_aux.index * 10
last_idx = data_2_aux.index[-1] + 1
data_2_aux = data_2_aux.reindex(range(last_idx))
data_2_aux = data_2_aux.interpolate()

plot_1 = ax.plot(x_fill, data_1, marker="o", mfc="white", ms=4, color="#87D8F7")
plot_2 = ax.plot(x_fill, data_2, marker="o", mfc="white", ms=4, color="#15366F")

for index in range(len(x_fill_aux) - 1):
    if data_1_aux.iloc[index + 1] > data_2_aux.iloc[index + 1]:
        color = plot_1[0].get_color()
    else:
        color = plot_2[0].get_color()

    ax.fill_between(
        [x_fill_aux[index], x_fill_aux[index + 1]],
        [data_1_aux.iloc[index], data_1_aux.iloc[index + 1]],
        [data_2_aux.iloc[index], data_2_aux.iloc[index + 1]],
        color=color,
        zorder=2,
        alpha=0.2,
        ec=None,
    )

ax.grid(ls="--", lw=0.25, color="#4E616C")

ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_edgecolor("#4E616C")
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_ylim(0)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_tick_params(length=2, color="#4E616C", labelcolor="#4E616C", labelsize=6)
ax.yaxis.set_tick_params(length=2, color="#4E616C", labelcolor="#4E616C", labelsize=6)

plt.tight_layout()
fig
