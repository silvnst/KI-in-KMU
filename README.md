# KI in KMU
FPV: Künstliche Intelligenz in kleinen und mittleren Betrieben

## Inhalt

### [1_Data Understanding](https://silvnst.github.io/else/1_Data%20Understanding.html)
In diesem File werden verschiedenste Grafiken erstellt, um die Daten zu verstehen. Es werden die Daten aus dem File `Datensatz_Lichtensteiger_(FS23).csv` verwendet. Zudem wird eine ABC-Analyse erstellt, welche im File `abc_analyses.csv` gespeichert wurde.

[2_Data Preparation](https://silvnst.github.io/else/2_Data%20Preparation.html)
Die Daten werden für die weitere Verwendung aufbereitet. Beispielsweise werden NaN-Werte ersetzt, Spalten umbenannt, neue Spalten erstellt, Variabeln logarithmisiert oder Extremwerte entfernt. Die aufbereiteten Daten werden im File `data_constructed.csv` gespeichert.

[3_Add Variables](https://silvnst.github.io/else/3_Add%20Variables.html)
Es werden neue Variabeln erstellt, welche für die weitere Verwendung nützlich sein könnten. Es werden Ferientage, Feiertage, Google Trends oder Covid-19 Daten hinzugefügt. Das neue Datenset wird im File `data_enriched.csv` gespeichert.

[4_Data Modelling](https://silvnst.github.io/else/4_Data%20Modelling.html)

Es werden verschiedene Modelle erstellt, um die Daten zu analysieren. Es werden Modelle die Lineare Regression, ein RandomForestRegressor und ein XGBoostRegressor verwendet. Im folgenden eine Ansicht der RMSE der Modelle nach Artikel.

![RMSE der Modelle](https://github.com/silvnst/KI-in-KMU/blob/main/img/4_rmse.png?raw=true)
<img src="https://github.com/silvnst/KI-in-KMU/blob/main/img/4_rmse.png?raw=true" width="auto" height="400" alt='rmse 4' style='margin:auto;'>

![RMSE der Modelle](https://github.com/silvnst/KI-in-KMU/blob/main/img/4_r2.png?raw=true)


[5_Fine Tuning](https://silvnst.github.io/else/5_Fine%20Tuning.html)
Die Modelle werden optimiert, um die besten Resultate zu erhalten. Die Hyperparameter von RandomForestRegressor und XGBoostRegressor werden optimiert. Zudem wird ein VortingRegressor erstellt, welches den Schnitt der Resultate der besten Modelle nimmt. Im folgenden eine Ansicht der RMSE der Modelle nach Artikel.

![RMSE der Modelle](https://github.com/silvnst/KI-in-KMU/blob/main/img/5_rmse.png?raw=true)

![RMSE der Modelle](https://github.com/silvnst/KI-in-KMU/blob/main/img/5_r2.png?raw=true)


FS2023
