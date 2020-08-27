import pandas as pd 
from fbprophet import Prophet
import matplotlib.pyplot as plt  # Matlab-style plotting
import seaborn as sns
import statsmodels.api as sm

color = sns.color_palette()
sns.set_style('darkgrid')
#Leemos datos. Separador es punto y coma
df = pd.read_csv("datos_bcn.csv", sep=';')
print(df.head())
print (len(df["Fecha"]))
#Cambiamos formato de datos que estan como cadenas
df["Precio"] = df["Precio"].str.replace(",", ".").astype(float)
df["Inflacion"] = df["Inflacion"].str.replace(",", ".").astype(float)
#Creamos variable Aeronaves por si es mas util una suma
df["Aeronaves"] = df["AeronavesUE"] + df["AeronavesMundo"]
print(df.columns)
#Comprobamos su tipo
df.info()
print(df.describe())
#df.hist(figsize=(4, 2), bins=50, xlabelsize=8, ylabelsize=8);
#sns.pairplot(df)
gr = sm.tsa.seasonal_decompose(df["Precio"],period=12, model='additive')
fig1 = gr.plot()
fig1.set_figheight(8)
fig1.set_figwidth(15)
plt.show()
corr = df.corr()
ax4 = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    annot=True,
    square=True
)
ax4.set_xticklabels(
    ax4.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
plt.show()
date = pd.date_range('2008-07-31', periods=142, freq='M')
prophet_df = pd.DataFrame({"ds": date, "y": df["Precio"], "paro": df["Paro"]})
print(prophet_df)
m = Prophet()
m.add_regressor("paro")
m.fit(prophet_df)
future = m.make_future_dataframe(periods=20, freq="M")
esc_neutro_data = [92616, 94358, 94438, 92312,
96091, 99595, 101062, 102608, 105787, 107122,
110326,112309, 108345, 100037,95478, 98663,
99405,100200,103465,99030]
esc_pesimismo_data = [i * 1.5 for i in esc_neutro_data]
esc_index = range(142,162)
paro_esc_neutro = pd.Series(esc_neutro_data, index = esc_index)
future["paro"] = df["Paro"].append(paro_esc_neutro)
print (future)

forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12))
fig = m.plot_components(forecast)
plt.show()