from pathlib import Path
import streamlit as st
from PIL import Image

#--- PATH SETTINGS ---
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file_pt = current_dir / 'assets' / 'CV_LuanSantos(PT).pdf'
resume_file_en = current_dir / 'assets' / 'CV_LuanSantos(EN).pdf'
profile_pic = current_dir / 'assets' / 'profile-pic.png'



#--- GENERAL SETTINGS ---
PAGE_TITLE = 'Digital CV | Luan Santos'
PAGE_ICON = '👨‍💻'
NAME = 'Luan Santos'
DESCRIPTION_EN = '''
Data Scientist
'''
DESCRIPTION_PT = '''
Cientista de Dados
'''
EMAIL = 'luann.405963@gmail.com'
SOCIAL_MEDIA = {
    'LinkedIn': 'https://www.linkedin.com/in/luan-santos-11254714b/',
    'GitHub': 'https://github.com/LuannSantoss',
}
PROJECTS_EN = {
    '📈 Sales Dashboard - Comparing sales across three stores': 'https://luansantos-salesdash.streamlit.app/',
    '📬 Contact Form - Web app to send message direct to my email' : 'https://luansantos-contact-form.streamlit.app/',
    '💸 Personal Expenses - Web app with NoSQL database' : 'https://luansantos-personal-expenses.streamlit.app/',
    '🐱🔍🐶 Cats & Dogs Classifier - Image classification of cats and dogs using Convolutional Neural Networks' : 'https://github.com/LuannSantoss/Cats-Dogs-Classification-with-CNN',
    '👨🔍👩Photo Rater - Have your photos rated (quality, hotness, trustworthiness and so on) by CLIP' : 'https://github.com/LuannSantoss/Photo-Rater',
    '📦 Optimizing the Flows in an Ecommerce Warehouse - Using Reinforcement Learning to automatically generate the best route between to locations in a Warehouse' : 'https://github.com/LuannSantoss/Case-of-Study-Optimizing-the-Flows-in-an-ECommerce-Warehouse',
    '⬆️💲⬇️ LSTM for Stocks - Use Long short-term memory (Deep Learning) to predict the next 30 days of stocks variation' : 'https://github.com/LuannSantoss/LSTM-for-Brazilian-Stocks',
    '🕳️ Stocks Gap Analysis - An algorithm that analyzes Ibovespa stocks, filtered by several parameters, and returns the up gaps of these stocks' : 'https://github.com/LuannSantoss/Stocks-Gap-Finder',
    '🧠📊🏦 Churn Analysis - Using Artificial Neural Networks (Deep Learning) to analyse the probability of a customer leaves the bank' : 'https://github.com/LuannSantoss/Churn-Analysis-with-Deep-Learning-ANN-'
}

PROJECTS_PT = {
    '📈 Painel de Vendas - Comparando vendas em três lojas': 'https://luansantos-salesdash.streamlit.app/',
    '📬 Formulário de contato - Web app para enviar mensagem direto para meu e-mail': 'https://luansantos-contact-form.streamlit.app/',
    '💸 Despesas pessoais - Aplicativo web com banco de dados NoSQL': 'https://luansantos-personal-expenses.streamlit.app/',
    '🐱🔍🐶 Cats & Dogs Classifier - Classificação de imagens de cães e gatos usando Redes Neurais Convolucionais': 'https://github.com/LuannSantoss/Cats-Dogs-Classification-with-CNN',
    '👨🔍👩Photo Rater - Tenha suas fotos avaliadas (qualidade, atratividade, confiabilidade e assim por diante) pelo CLIP': 'https://github.com/LuannSantoss/Photo-Rater',
    '📦 Otimizando os fluxos em um armazém de comércio eletrônico - usando Aprendizado por Reforço para gerar automaticamente a melhor rota entre locais em um armazém': 'https://github.com/LuannSantoss/Case-of-Study-Optimizing-the-Flows- em um armazém de comércio eletrônico',
    '⬆️💲⬇️ LSTM for Stocks - Use Memória de Longo Prazo (Deep Learning) para prever os próximos 30 dias de variação de ações': 'https://github.com/LuannSantoss/LSTM-for-Brazilian-Stocks',
    '🕳️ Stocks Gap Analysis - Algoritmo que analisa as ações do Ibovespa, filtradas por diversos parâmetros, e retorna os gaps de alta dessas ações': 'https://github.com/LuannSantoss/Stocks-Gap-Finder',
    '🧠📊🏦 Análise de Churn - Usando Redes Neurais Artificiais (Deep Learning) para analisar a probabilidade de um cliente sair do banco': 'https://github.com/LuannSantoss/Churn-Analysis-with-Deep-Learning-ANN- '
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)



#--- LANGUAGE SWITCH ---


if st.checkbox("EN / PT"):
    st.write("Linguagem: português")

    #--- UPLOADING ---

    with open(css_file) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    with open(resume_file_pt, 'rb') as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    #--- HERO SECTION ---
    col1, col2 = st.columns(2, gap='small')
    with col1:
        st.image(profile_pic, width = 230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION_PT)
        st.download_button(
            label = '📄 Download Currículo',
            data = PDFbyte,
            file_name = resume_file_pt.name,
            mime = 'application/octet-stream',
        )
        st.write('📬', EMAIL)


    #--- SOCIAL LINKS ---
    st.write('#')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f'[{platform}]({link})')

    st.write('---')

    #--- ABOUT ME ---
    st.write('#')
    st.subheader('Sobre mim')
    st.write(
        """
        - ✔️3 anos de experiência na área de Ciência de Dados, descobrindo insights valiosos a partir de dados
        - ✔️Forte experiência prática e conhecimento em Python, Power BI e Excel
        - ✔️Boa compreensão dos princípios estatísticos e suas respectivas aplicações
        - ✔️Excelente senso de trabalho em equipe e com forte senso de iniciativa nas tarefas
        - ✔️Forte senso de auto-aperfeiçoamento e aprendizado contínuo
        - ✔️Mentalidade orientada a dados para resolver de problemas simples a complexos.
        """
    )

    #--- SKILLS ---
    st.write('#')
    st.subheader('Habilidades Técnicas')
    st.write(
        """
        - Programação: Python | R | SQL

        - Frameworks: TensorFlow | Keras | PyTorch | Scikit-Learn | PySpark | Pandas | Numpy | Pycaret | Streamlit | PyAutogui | Selenium | Botcity

        - IDE: Jupyter Notebook | Jupyter Lab | VS Code | Google Colab

        - Visualização de Dados: Power BI | Matplotlib | Seaborn | Plotly | MS Excel

        - Machine Learning: Regressão (Linear Regression, Decision Tree and Random Forest) | Classificação (Logistic Regression, K-NN, Decision Tree and Random Forest) | Clusterização (K-Means) | Aprendizado por Reforço (Thompson Sampling and UCB) | Aprendizagem de Regras de Associação (Apriori and Eclat) | Processamento de Linguagem Natural

        - Deep Learning: Artificial Neural Networks | Convolutional Neural Networks | Recurrent Neural Networks

        - Bases de Dados: SQLite | Deta
        """
    )

    #--- WORK HISTORY ---
    st.write('#')
    st.subheader('Histórico de Trabalho')
    st.write('---')

    #--- JOB 1
    st.write('**Cientista de Dados | Construções Gabriel A.S. Couto, SA.**')
    st.write('09/2022 - 03/2023')
    st.write(
        """
        - ✔️Utilizei técnicas de modelagem estatística para extrair insights dos dados.
        - ✔️Desenvolvimento de modelos de aprendizado de máquina para prever resultados.
        - ✔️Utilizei técnicas de visualização de dados para explicar e comunicar resultados.
        - ✔️Criação de dashboards e relatórios em Power BI para acompanhamento de métricas.
        - ✔️Suporte às equipes de planejamento e equipamentos na tomada de decisão.
        - ✔️Participei de um projeto inovador de criação de um dashboard para a equipe de equipamentos da empresa. Informações extraídas de dispositivos GPS de máquinas com a ajuda de Python para acessar a API do GPS. Criei um painel intuitivo com informações em tempo real, como localização, produtividade e custos. Todo o processo foi construído com código que permite a visualização dos dados desde o início do uso do GPS.
        - ✔️Além disso, tive a oportunidade de apoiar as equipes de planejamento criando um painel que automatizava tarefas repetitivas, reduzindo o tempo de trabalho em questões que antes levavam **2 dias** para serem concluídas **para apenas alguns minutos**. Esse avanço permitiu a otimização da eficiência e eficácia nos processos, aumentando a produtividade da equipe.
        """
    )

    #--- PROJECTS & ACCOMPLISHMENTS ---
    st.write('#')
    st.subheader('Projetos & Realizações')
    st.write('---')
    for project, link in PROJECTS_PT.items():
        st.write(f'[{project}]({link})')


    #--- CERTIFICATES ---
    st.write('#')
    st.subheader('Certificados')
    st.write('---')



    #--- CERTIFICATE 1
    st.write('**IBM Data Science | Coursera**')
    st.markdown('Link: [professional-cert/4NMQNSRAYPDU](https://www.coursera.org/account/accomplishments/professional-cert/4NMQNSRAYPDU)')
    st.write('06/2022')
    st.write(
        """
        - Um programa de certificação profissional que ensina os fundamentos da ciência de dados e desenvolve habilidades práticas usando as ferramentas, linguagens e bibliotecas usadas por cientistas de dados profissionais.
        - Aprendeu a usar Python, SQL, bancos de dados, visualização de dados, análise de dados, análise estatística, modelagem preditiva e algoritmos de aprendizado de máquina para resolver problemas de ciência de dados do mundo real.
        - Realizou projetos práticos na nuvem IBM usando ferramentas e conjuntos de dados reais de ciência de dados.
        - Construí um portfólio de projetos de ciência de dados para demonstrar minha competência e confiança como cientista de dados iniciante.
        """
    )
    st.write('#')

    #--- CERTIFICATE 2
    st.write('**Introduction to Cybersecurity | Cisco Networking Academy**')
    st.markdown('Link: [badge/230f41cb-15ca-4b38-9824-db25a11d8b68](https://www.credly.com/earner/earned/badge/230f41cb-15ca-4b38-9824-db25a11d8b68)')
    st.write('01/2022')
    st.write(
        """
        - Um curso introdutório que explora o novo mundo da segurança cibernética como profissional ou como interesse pessoal. Abrange as ameaças e tendências cibernéticas, juntamente com o tópico mais amplo de segurança cibernética de uma forma que seja importante para VOCÊ.
        - Aprendi como me proteger online e nas mídias sociais, como reconhecer ataques cibernéticos comuns e como responder a eles e como seguir uma carreira em segurança cibernética.
        """
    )
    st.write('#')

    #--- CERTIFICATE 3
    st.write('**Semana do Power BI | DATAB**')
    st.write('10/2021')
    st.write(
        """
        - Um curso que apresenta os fundamentos do Power BI, uma ferramenta poderosa para análise e visualização de dados. Abrange os conceitos e recursos do Power BI, como fontes de dados, modelos de dados, consultas, relatórios, painéis e publicação.
        - Aprendi a usar o Power BI Desktop e o Power BI Service para se conectar a várias fontes de dados, transformar e modelar dados, criar relatórios e painéis interativos e compartilhá-los com outras pessoas. Também aprendi a usar o Power BI Mobile para acessar meus dados em qualquer lugar.
        - Realizei exercícios práticos usando conjuntos de dados e cenários do mundo real para entender os aplicativos e desafios do Power BI. Também aprendi a usar diferentes visualizações, filtros, segmentações, detalhamentos e personalizações no Power BI.
        """
    )
    st.write('#')

    #--- CERTIFICATE 4
    st.write('**Big Data Fundamentos 3.0 | Data Science Academy**')
    st.markdown('Link: [duLkQQxxBvXDwFuNA](https://mycourse.app/duLkQQxxBvXDwFuNA)')
    st.write('09/2021')
    st.write(
        """
        - Um curso que apresenta os conceitos e tecnologias de Big Data, principal plataforma de análise e processamento de dados do mundo.
        - Aprendi a usar ferramentas como Hadoop e Spark para trabalhar com grandes volumes de dados estruturados e não estruturados.
        - Realizei exercícios práticos usando conjuntos de dados e cenários reais para entender os desafios e oportunidades do Big Data.
        """
    )
    st.write('#')

    #--- CERTIFICATE 5
    st.write('**Blockchain Essentials | Cognitive Class**')
    st.markdown('Link: [certificates/e878ce30defc463d9132eff2243e8e32](https://courses.cognitiveclass.ai/certificates/e878ce30defc463d9132eff2243e8e32)')
    st.write('09/2021')
    st.write(
        """
        - Um curso que apresenta os conceitos e tecnologias de blockchain, a tecnologia de contabilidade distribuída que alimenta as criptomoedas e outras aplicações.
        - Aprendi como o blockchain funciona, quais são seus benefícios e desafios e como ele pode ser usado em vários domínios, como finanças, cadeia de suprimentos, saúde e muito mais.
        - Explorei exemplos do mundo real de aplicativos e casos de uso de blockchain e aprendi a criar minha própria rede de blockchain usando o IBM Blockchain Platform.
        """
    )
    st.write('#')

    #--- CERTIFICATE 6
    st.write('**Time Series in Manufacturing Industry | Great Learning**')
    st.markdown('Link: [greatlearning/WIIRFCKZ](https://verify.greatlearning.in/WIIRFCKZ)')
    st.write('09/2021')
    st.write(
        """
        - Um curso que introduz os princípios e técnicas de previsão de séries temporais, que é a prática de prever valores futuros de um conjunto de dados com base em valores passados. Abrange os conceitos e métodos de análise de séries temporais, como decomposição, estacionaridade, autocorrelação e diferenciação.
        - Aprendi a usar vários modelos de previsão, como ARIMA, SARIMA, Alisamento Exponencial e Profeta, para ajustar e avaliar dados de séries temporais. Também aprendi a usar o Python e suas bibliotecas, como Statsmodels, Scikit-learn e FBProphet, para realizar previsões de séries temporais.
        - Realizei exercícios práticos usando conjuntos de dados e cenários do mundo real para entender as aplicações e os desafios da previsão de séries temporais. Também aprendi como lidar com valores ausentes, valores discrepantes, sazonalidade e problemas de tendência em dados de séries temporais.
        """
    )
    st.write('#')

    #--- CERTIFICATE 7
    st.write('**Spark Basics and Streaming | Great Learning**')
    st.markdown('Link: [greatlearning/MRULVUIM](verify.greatlearning.in/MRULVUIM)')
    st.write('08/2021')
    st.write(
        """
        - Um curso que apresenta os fundamentos do Spark, um mecanismo rápido e geral para processamento de dados em larga escala. Abrange os conceitos e a arquitetura do Spark, bem como seus principais componentes, como RDDs, DataFrames e Spark SQL.
        - Aprendi a usar o Spark para executar várias tarefas, como ingestão de dados, transformação de dados, análise de dados e visualização de dados. Também aprendi a usar o PySpark, a API Python para Spark, para escrever aplicativos Spark usando Python.
        - Realizei exercícios práticos usando conjuntos de dados e cenários do mundo real para entender as aplicações e desafios do Spark. Também aprendi a usar o Jupyter Notebook e o IBM Watson Studio para executar o código Spark na nuvem.
        """
    )
    st.write('#')

    #--- CERTIFICATE 8
    st.write('**Inteligência Artificial Fundamentos 2.0 | Data Science Academy**')
    st.markdown('Link: [mycourse/wSv5XopYMAsT4kea7](https://mycourse.app/wSv5XopYMAsT4kea7)')
    st.write('07/2021')
    st.write(
        """
        - Um curso que visa democratizar os fundamentos da inteligência artificial, levando seus principais conceitos para pessoas de todos os níveis e idades, em todos os cantos do Brasil e do mundo. Abrange a definição e a história da inteligência artificial, suas aplicações e desafios e suas implicações éticas e sociais.
        - Aprendi como funciona a inteligência artificial, quais são seus benefícios e limitações, e como ela pode ser utilizada em diversos domínios como saúde, educação, negócios e entretenimento. Também aprendi sobre os principais ramos da inteligência artificial, como aprendizado de máquina, visão computacional, processamento de linguagem natural e robótica.
        - Realizei exercícios práticos usando conjuntos de dados e cenários do mundo real para entender os problemas e soluções da inteligência artificial. Também aprendi a usar Python e suas bibliotecas como TensorFlow, Keras, Scikit-learn e NLTK para criar projetos de inteligência artificial.
        """
    )
    st.write('#')

    #--- CERTIFICATE 9
    st.write('**Introdução à Ciência de Dados 2.0 | Data Science Academy**')
    st.markdown('Link: [mycourse/HuiMWzhshivzgRtT7](https://mycourse.app/HuiMWzhshivzgRtT7)')
    st.write('07/2021')
    st.write(
        """
        - Um curso que apresenta os fundamentos da ciência de dados, como tipos de dados, estruturas de dados, manipulação de dados, visualização de dados e análise de dados. Abrange a definição e a história da ciência de dados, suas aplicações e desafios e suas implicações éticas e sociais.
        - Aprendi a usar Python e suas bibliotecas como NumPy, Pandas, Matplotlib e Seaborn para trabalhar com diferentes tipos de dados e criar visualizações perspicazes.
        - Realizei exercícios práticos usando conjuntos de dados e cenários do mundo real para entender os problemas e soluções da ciência de dados. Também aprendi a usar o Jupyter Notebook e o Google Colab para executar código de ciência de dados na nuvem.
        """
    )
    st.write('#')

    #--- CERTIFICATE 10
    st.write('**Aprenda SQL do Zero | Udemy**')
    st.markdown('Link: [ude.my/UC-efe1b2f9-bc1a-41d4-899f-e9a1439df6ee](https://ude.my/UC-efe1b2f9-bc1a-41d4-899f-e9a1439df6ee)')
    st.write('06/2021')
    st.write(
        """
        - Um curso que ensina SQL do zero, utilizando o banco de dados SQLite e a ferramenta DB Browser. Abrange os comandos e conceitos básicos de SQL, como inserir, excluir, atualizar, criar tabela, selecionar, onde, juntar, agrupar por, ordenar por e muito mais.
        - Aprendi como se conectar ao banco de dados SQLite usando o navegador de banco de dados, como manipular dados usando comandos SQL, como criar tabelas e campos usando comandos SQL ou navegador de banco de dados e como recuperar dados de uma ou mais tabelas usando consultas SQL.
        - Realizei exercícios práticos usando conjuntos de dados e cenários do mundo real para entender as aplicações e os desafios do SQL. Também aprendi a usar funções, subconsultas, aliases e operadores em SQL.
        """
    )

    #--- EDUCATION ---
    st.write('#')
    st.subheader('Educação')
    st.write('---')

    #--- EDUCATION 1
    st.write('**Pós-graduação em Data Science for Business | Universidade Europeia**')
    st.write('10/2022 - 06/2023')
    st.write('#')

    #--- EDUCATION 2
    st.write("**Mestrado em Engenharia | Faculdade de Engenharia da Universidade do Porto**")
    st.write('09/2020 - 02/2022')
    st.write('#')

    #--- EDUCATION 3
    st.write("**Licenciatura em Engenharia | Faculdade de Engenharia da Universidade do Porto**")
    st.write('09/2017 - 09/2020')
    st.write('#')




else:
    st.write("Language: english")

    #--- UPLOADING ---

    with open(css_file) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    with open(resume_file_en, 'rb') as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    #--- HERO SECTION ---
    col1, col2 = st.columns(2, gap='small')
    with col1:
        st.image(profile_pic, width = 230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION_EN)
        st.download_button(
            label = '📄 Download Resume',
            data = PDFbyte,
            file_name = resume_file_en.name,
            mime = 'application/octet-stream',
        )
        st.write('📬', EMAIL)


    #--- SOCIAL LINKS ---
    st.write('#')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f'[{platform}]({link})')

    st.write('---')

    #--- ABOUT ME ---
    st.write('#')
    st.subheader('About me')
    st.write(
        """
        - ✔️3 years of experience in Data Science field, extracting actionable insights from data
        - ✔️Strong hands-on experience and knowledge in Python, Power BI and Excel
        - ✔️Good understanding of statistical principles and their respective applications
        - ✔️Excellent team-player and displaying strong sense of initiative on tasks
        - ✔️Strong sense of self-improvement and continuous learning
        - ✔️Data driven mindset to solve from simple to complex problems.
        """
    )

    #--- SKILLS ---
    st.write('#')
    st.subheader('Hard Skills')
    st.write(
        """
        - Programming: Python | R | SQL

        - Frameworks: TensorFlow | Keras | PyTorch | Scikit-Learn | PySpark | Pandas | Numpy | Pycaret | Streamlit | PyAutogui | Selenium | Botcity

        - IDE: Jupyter Notebook | Jupyter Lab | VS Code | Google Colab

        - Data Visualization: Power BI | Matplotlib | Seaborn | Plotly | MS Excel

        - Machine Learning: Regression (Linear Regression, Decision Tree and Random Forest) | Classification (Logistic Regression, K-NN, Decision Tree and Random Forest) | Clustering (K-Means) | Reinforcement Learning (Thompson Sampling and UCB) | Association Rule Learning (Apriori and Eclat) | Natural Language Processing

        - Deep Learning: Artificial Neural Networks | Convolutional Neural Networks | Recurrent Neural Networks

        - Databases: SQLite | Deta
        """
    )

    #--- WORK HISTORY ---
    st.write('#')
    st.subheader('Work History')
    st.write('---')

    #--- JOB 1
    st.write('**Data Scientist | Construções Gabriel A.S. Couto, SA.**')
    st.write('09/2022 - 03/2023')
    st.write(
        """
        - ✔️Used statistical modeling techniques to extract insights from data. 
        - ✔️Developed machine learning models to predict outcomes. 
        - ✔️Used data visualization techniques to explain and communicate results. 
        - ✔️Created dashboards and reports in Power BI to track metrics. 
        - ✔️Supported planning and equipment teams in decision-making. 
        - ✔️Participated in an innovative project to create a dashboard for the company's equipment team. Extracted information from GPS devices of machinery with the help of Python to access the GPS API. Created an intuitive dashboard with real-time information such as location, productivity, and costs. The entire process was built with code that allows data to be visualized from the beginning of GPS use. 
        - ✔️Furthermore, had the opportunity to support the planning teams by creating a dashboard that automated repetitive tasks, reducing work time on issues that previously took **2 days** to complete **to just a few minutes**. This advancement allowed for optimization of efficiency and effectiveness in processes, increasing the productivity of the team.
        """
    )

    #--- PROJECTS & ACCOMPLISHMENTS ---
    st.write('#')
    st.subheader('Projects & Accomplishments')
    st.write('---')
    for project, link in PROJECTS_EN.items():
        st.write(f'[{project}]({link})')


    #--- CERTIFICATES ---
    st.write('#')
    st.subheader('Certificates')
    st.write('---')



    #--- CERTIFICATE 1
    st.write('**IBM Data Science | Coursera**')
    st.markdown('Link: [professional-cert/4NMQNSRAYPDU](https://www.coursera.org/account/accomplishments/professional-cert/4NMQNSRAYPDU)')
    st.write('06/2022')
    st.write(
        """
        - A professional certificate program that teaches the fundamentals of data science and develops practical skills using the tools, languages and libraries used by professional data scientists.
        - Learned how to use Python, SQL, databases, data visualization, data analysis, statistical analysis, predictive modeling and machine learning algorithms to solve real-world data science problems.
        - Performed hands-on projects in the IBM cloud using real data science tools and data sets.
        - Built a portfolio of data science projects to demonstrate my competence and confidence as a beginner data scientist.
        """
    )
    st.write('#')

    #--- CERTIFICATE 2
    st.write('**Introduction to Cybersecurity | Cisco Networking Academy**')
    st.markdown('Link: [badge/230f41cb-15ca-4b38-9824-db25a11d8b68](https://www.credly.com/earner/earned/badge/230f41cb-15ca-4b38-9824-db25a11d8b68)')
    st.write('01/2022')
    st.write(
        """
        - An introductory course that explores the new world of cybersecurity as a professional or as a personal interest. It covers the cyber threats and trends, along with the broader topic of cybersecurity in a way that matters to YOU.
        - Learned how to protect myself online and on social media, how to recognize common cyberattacks and how to respond to them, and how to pursue a career in cybersecurity.
        """
    )
    st.write('#')

    #--- CERTIFICATE 3
    st.write('**Power BI Week | DATAB**')
    st.write('10/2021')
    st.write(
        """
        - A course that introduces the basics of Power BI, a powerful tool for data analysis and visualization. It covers the concepts and features of Power BI, such as data sources, data models, queries, reports, dashboards, and publishing.
        - Learned how to use Power BI Desktop and Power BI Service to connect to various data sources, transform and model data, create interactive reports and dashboards, and share them with others. I also learned how to use Power BI Mobile to access my data on the go.
        - Performed practical exercises using real-world data sets and scenarios to understand the applications and challenges of Power BI. I also learned how to use different visualizations, filters, slicers, drill-downs, and customizations in Power BI.
        """
    )
    st.write('#')

    #--- CERTIFICATE 4
    st.write('**Big Data Fundamentals 3.0 | Data Science Academy**')
    st.markdown('Link: [duLkQQxxBvXDwFuNA](https://mycourse.app/duLkQQxxBvXDwFuNA)')
    st.write('09/2021')
    st.write(
        """
        - A course that introduces the concepts and technologies of Big Data, the main platform for data analysis and processing in the world.
        - Learned how to use tools such as Hadoop and Spark to work with large volumes of structured and unstructured data.
        - Performed practical exercises using real data sets and scenarios to understand the challenges and opportunities of Big Data.
        """
    )
    st.write('#')

    #--- CERTIFICATE 5
    st.write('**Blockchain Essentials | Cognitive Class**')
    st.markdown('Link: [certificates/e878ce30defc463d9132eff2243e8e32](https://courses.cognitiveclass.ai/certificates/e878ce30defc463d9132eff2243e8e32)')
    st.write('09/2021')
    st.write(
        """
        - A course that introduces the concepts and technologies of blockchain, the distributed ledger technology that powers cryptocurrencies and other applications.
        - Learned how blockchain works, what are its benefits and challenges, and how it can be used in various domains such as finance, supply chain, healthcare and more.
        - Explored real-world examples of blockchain applications and use cases, and learned how to create my own blockchain network using IBM Blockchain Platform.
        """
    )
    st.write('#')

    #--- CERTIFICATE 6
    st.write('**Time Series in Manufacturing Industry | Great Learning**')
    st.markdown('Link: [greatlearning/WIIRFCKZ](https://verify.greatlearning.in/WIIRFCKZ)')
    st.write('09/2021')
    st.write(
        """
        - A course that introduces the principles and techniques of time series forecasting, which is the practice of predicting future values of a data set based on past values. It covers the concepts and methods of time series analysis, such as decomposition, stationarity, autocorrelation, and differencing.
        - Learned how to use various forecasting models, such as ARIMA, SARIMA, Exponential Smoothing, and Prophet, to fit and evaluate time series data. I also learned how to use Python and its libraries such as Statsmodels, Scikit-learn, and FBProphet to perform time series forecasting.
        - Performed practical exercises using real-world data sets and scenarios to understand the applications and challenges of time series forecasting. I also learned how to handle missing values, outliers, seasonality, and trend issues in time series data.
        """
    )
    st.write('#')

    #--- CERTIFICATE 7
    st.write('**Spark Basics and Streaming | Great Learning**')
    st.markdown('Link: [greatlearning/MRULVUIM](verify.greatlearning.in/MRULVUIM)')
    st.write('08/2021')
    st.write(
        """
        - A course that introduces the basics of Spark, a fast and general engine for large-scale data processing. It covers the concepts and architecture of Spark, as well as its core components such as RDDs, DataFrames and Spark SQL.
        - Learned how to use Spark to perform various tasks such as data ingestion, data transformation, data analysis and data visualization. I also learned how to use PySpark, the Python API for Spark, to write Spark applications using Python.
        - Performed practical exercises using real-world data sets and scenarios to understand the applications and challenges of Spark. I also learned how to use Jupyter Notebook and IBM Watson Studio to run Spark code in the cloud.
        """
    )
    st.write('#')

    #--- CERTIFICATE 8
    st.write('**Artificial Intelligence Fundamentals 2.0 | Data Science Academy**')
    st.markdown('Link: [mycourse/wSv5XopYMAsT4kea7](https://mycourse.app/wSv5XopYMAsT4kea7)')
    st.write('07/2021')
    st.write(
        """
        - A course that aims to democratize the fundamentals of artificial intelligence, bringing its main concepts to people of all levels and ages, in all corners of Brazil and the world. It covers the definition and history of artificial intelligence, its applications and challenges, and its ethical and social implications.
        - Learned how artificial intelligence works, what are its benefits and limitations, and how it can be used in various domains such as health, education, business, and entertainment. I also learned about the main branches of artificial intelligence, such as machine learning, computer vision, natural language processing, and robotics.
        - Performed practical exercises using real-world data sets and scenarios to understand the problems and solutions of artificial intelligence. I also learned how to use Python and its libraries such as TensorFlow, Keras, Scikit-learn, and NLTK to create artificial intelligence projects.
        """
    )
    st.write('#')

    #--- CERTIFICATE 9
    st.write('**Introduction to Data Science 2.0 | Data Science Academy**')
    st.markdown('Link: [mycourse/HuiMWzhshivzgRtT7](https://mycourse.app/HuiMWzhshivzgRtT7)')
    st.write('07/2021')
    st.write(
        """
        - A course that introduces the basics of data science, such as data types, data structures, data manipulation, data visualization and data analysis. It covers the definition and history of data science, its applications and challenges, and its ethical and social implications.
        - Learned how to use Python and its libraries such as NumPy, Pandas, Matplotlib and Seaborn to work with different kinds of data and create insightful visualizations.
        - Performed practical exercises using real-world data sets and scenarios to understand the problems and solutions of data science. I also learned how to use Jupyter Notebook and Google Colab to run data science code in the cloud.
        """
    )
    st.write('#')

    #--- CERTIFICATE 10
    st.write('**Learn SQL from Scratch | Udemy**')
    st.markdown('Link: [ude.my/UC-efe1b2f9-bc1a-41d4-899f-e9a1439df6ee](https://ude.my/UC-efe1b2f9-bc1a-41d4-899f-e9a1439df6ee)')
    st.write('06/2021')
    st.write(
        """
        - A course that teaches SQL from scratch, using the SQLite database and the DB Browser tool. It covers the basic commands and concepts of SQL, such as insert, delete, update, create table, select, where, join, group by, order by, and more.
        - Learned how to connect to the SQLite database using DB Browser, how to manipulate data using SQL commands, how to create tables and fields using SQL commands or DB Browser, and how to retrieve data from one or more tables using SQL queries.
        - Performed practical exercises using real-world data sets and scenarios to understand the applications and challenges of SQL. I also learned how to use functions, subqueries, aliases, and operators in SQL.
        """
    )

    #--- EDUCATION ---
    st.write('#')
    st.subheader('Education')
    st.write('---')

    #--- EDUCATION 1
    st.write('**Postdegree in Data Science for Business | Universidade Europeia**')
    st.write('10/2022 - 06/2023')
    st.write('#')

    #--- EDUCATION 2
    st.write("**Master's Degree in Engineering | Faculdade de Engenharia da Universidade do Porto**")
    st.write('09/2020 - 02/2022')
    st.write('#')

    #--- EDUCATION 3
    st.write("**Bachelor's Degree in Engineering | Faculdade de Engenharia da Universidade do Porto**")
    st.write('09/2017 - 09/2020')
    st.write('#')


