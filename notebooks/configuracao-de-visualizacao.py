import seaborn as sns
import matplotlib.pyplot as plt

PALETA_OLIST = [
    "#0047bb",
    "#94a3b8",
    "#1e293b",
    "#3b82f6",
    "#e2e8f0"
]

sns.set_theme(style="whitegrid")

plt.rcParams.update({
    'axes.prop_cycle': plt.cycler(color=PALETA_OLIST),
    'figure.figsize': (12, 8),
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold',
    'axes.edgecolor': '#94a3b8'
})
