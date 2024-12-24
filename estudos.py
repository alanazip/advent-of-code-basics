# Plano de Estudo React Native - 6 meses
import calendar

# Criar um plano de estudo mensal
study_plan = {
    "Mês 1": [
        "Semana 1: Introdução ao React Native - Ambiente de Desenvolvimento (Expo e CLI)",
        "Semana 2: Componentes Básicos - View, Text, StyleSheet",
        "Semana 3: Layout com Flexbox e Estilos",
        "Semana 4: Estados e Props no React Native",
    ],
    "Mês 2": [
        "Semana 1: Navegação com React Navigation (Stack Navigator)",
        "Semana 2: Navegação com React Navigation (Tab Navigator e Drawer Navigator)",
        "Semana 3: Listas e ScrollView (FlatList, SectionList)",
        "Semana 4: Input, Formulários e Eventos",
    ],
    "Mês 3": [
        "Semana 1: Requisições HTTP com Axios/Fetch e integração com APIs",
        "Semana 2: Context API e gerenciamento de estado",
        "Semana 3: Introdução a animações (Animated API)",
        "Semana 4: Animações complexas (Reanimated e Gestures)",
    ],
    "Mês 4": [
        "Semana 1: Gerenciamento de Estado com Redux e Redux Toolkit",
        "Semana 2: Testes unitários e end-to-end (Jest e Detox)",
        "Semana 3: Introdução ao Firebase - Autenticação",
        "Semana 4: Firebase - Banco de Dados (Firestore)",
    ],
    "Mês 5": [
        "Semana 1: Uso de APIs nativas com Expo e módulos personalizados",
        "Semana 2: Configuração de notificações push",
        "Semana 3: Publicação de aplicativos (Android e iOS)",
        "Semana 4: Boas práticas e otimizações de desempenho",
    ],
    "Mês 6": [
        "Semana 1: Revisão de conceitos principais",
        "Semana 2: Projeto final - Planejamento",
        "Semana 3: Projeto final - Desenvolvimento",
        "Semana 4: Projeto final - Finalização e publicação",
    ]
}

# Exibir o plano de estudo
def exibir_plano_estudo(plano):
    for mes, semanas in plano.items():
        print(f"{mes}:")
        for semana in semanas:
            print(f"  - {semana}")
        print("\n")

# Imprimir o plano
exibir_plano_estudo(study_plan)