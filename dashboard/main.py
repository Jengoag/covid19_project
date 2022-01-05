import streamlit as st
from PIL import Image
import datetime
import graphs



################### title 

title_image = Image.open("dashboard/src/head_covid.jpeg")
st.image(title_image)

st.markdown("<h1 style='text-align: center; color: #942953 '>Visualización de datos Covid-19</h1>", unsafe_allow_html = True)

st.markdown("""
 * Utiliza el menú de la izqierda para seleccionar los parametros que desee
 * Tus datos aparecerán a continuación
""")

###################  SIDEBAR PRINCIPAL
st.sidebar.title('Selecciona tus preferencias ')

###################  SIDEBAR MODE
option=st.sidebar.selectbox('Information',('Confirmed','Deaths', 'Recovered'))

 
###################  SIDEBAR COUNTRY
country_names_list = [d['Country'] for d in graphs.get_countries()]
country_names_list.insert(0,'Worldwide')

option=st.sidebar.selectbox('Country', country_names_list)

####graphs.get_graph_by_country(option) 

""" ###################  SIDEBAR START DATE AND END DATE

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

start_date = st.sidebar.date_input('Fecha inicial', today)
end_date = st.sidebar.date_input('Fecha final', tomorrow)

###################  MAP LOCATION

graphs.get_global_map() """


""" ###################  SUCCESS OR ERROR DATA
if start_date < end_date:
    st.success('Fecha inicial: `%s`\n\nFecha final:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.') """ 