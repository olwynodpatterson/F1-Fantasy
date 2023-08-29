import pandas as pd

df_drivers = pd.read_csv('datasets/drivers.csv')
print(df_drivers)

df_races = pd.read_csv('datasets/races.csv')
print(df_races)

df_driverStandings = pd.read_csv('datasets/driver_standings.csv')
print(df_driverStandings)

currentDrivers = ('alonso', 'max_verstappen', 'piastri', 'norris', 'leclerc', 'sainz', 'hamilton', 'russell',
                  'perez', 'ocon', 'gasly', 'tsunoda', 'ricciardo', 'stroll', 'albon', 'sargeant', 'bottas',
                  'zhou', 'kevin_magnussen', 'hulkenberg')

print(currentDrivers)

for i in currentDrivers:
    if (i == df_drivers.loc[:,"driverRef"]).any():
        print(i)