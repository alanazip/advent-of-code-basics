# Importando bibliotecas necessárias
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Gerar um conjunto de dados simples para regressão
# Dados fictícios: Preço de casas baseado na área em m²
np.random.seed(42)
area = np.random.rand(100) * 100  # Área em m² entre 0 e 100
preco = 50 * area + np.random.randn(100) * 10  # Preço em R$1000 com ruído

# Criar DataFrame
data = pd.DataFrame({'Area': area, 'Preco': preco})

# Dividir os dados em treino e teste
X = data[['Area']]
y = data['Preco']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar um modelo de Regressão Linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

mse, r2, model.coef_[0], model.intercept_