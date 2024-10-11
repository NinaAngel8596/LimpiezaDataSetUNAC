import pandas as pd

# Leer el archivo CSV con la codificación ISO-8859-1
df_Unac = pd.read_csv('C:/Users/ADMI/Desktop/E-D-A/data/03 INGRESANTES.csv', encoding='ISO-8859-1')

# Crear una función para reemplazar caracteres con tilde
def quitar_tildes(texto):
    tildes = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
              'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    for tilde, sin_tilde in tildes.items():
        texto = texto.replace(tilde, sin_tilde)
    return texto

# Eliminar la columna 'ALUMNO' si existe
if 'ALUMNO' in df_Unac.columns:
    df_Unac_mod = df_Unac.drop(columns='ALUMNO')
else:
    df_Unac_mod = df_Unac.copy()  # Crear una copia si no se elimina la columna

# Aplicar la función a cada columna de tipo 'object' (texto)
for col in df_Unac_mod.select_dtypes(include='object').columns:
    df_Unac_mod[col] = df_Unac_mod[col].map(lambda x: quitar_tildes(x) if isinstance(x, str) else x)

# Guardar el DataFrame modificado con codificación UTF-8
df_Unac_mod.to_csv('C:/Users/ADMI/Desktop/E-D-A/data/03_INGRESANTES_utf8.csv', index=False, encoding='utf-8')

# Mostrar el DataFrame modificado
print(df_Unac_mod.head())
