import streamlit as st

# Center the title using markdown
st.markdown("<h1 style='text-align: center;'>LernRadar</h1>", unsafe_allow_html=True)

# Center and resize the image using Streamlit's columns for layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("Fack2.png", width=250)

# Create form for Dimension A
st.header('Dimension A: Bedeutung des Fehlers')
dim_a1 = st.slider('Wie sehr beeinflusst der Prozess, wie uns außenstehende wahrnehmen?', 1, 10, 5)
dim_a2 = st.slider('Wie sehr beeinflusst der Prozess, was ihr in eurem Team zukünftig machen wollt?', 1, 10, 5)
dim_a3 = st.slider('Wie sehr beeinflusst der Prozess, ob junge Menschen zukünftig an FACK teilhaben wollen oder können?', 1, 10, 5)

# Create form for Dimension B
st.header('Dimension B: Ressourcen für Learning')
dim_b1 = st.slider('Steht genügend Zeit bei den Handelnden für eine Reflexion zur Verfügung?', 1, 10, 5)
dim_b2 = st.slider('Können die Handelnden selbst ihre Arbeit reflektieren oder haben sie jemanden der ihnen dabei helfen kann?', 1, 10, 5)
dim_b3 = st.slider('Ist die Arbeitsaufgabe so, dass daraus direkt ableitbar ist was gut und was nicht gut lief?', 1, 10, 5)

# Calculate results
dim_a_total = dim_a1 + dim_a2 + dim_a3
dim_b_total = dim_b1 + dim_b2 + dim_b3

# Display results
if dim_a_total <= 16 and dim_b_total <= 16:
    result = 'Antwort 1'
    advice = 'Entspann Dich! Hier kann fast nix passieren. Du musst keine extra Zeit einplanen um rettend einzuspringen oder ein Learning zu begleiten!'
elif dim_a_total <= 16 and dim_b_total > 16:
    result = 'Antwort 2'
    advice = 'Bereite dich auf Reflexion vor! Hier besteht die Möglichkeit zu lernen! Bereite dich darauf vor das Learning de Handelnden Personen zu begleiten. Plane einen Ablauf für die Reflexion und nimm dir Zeit dafür!'
elif dim_a_total > 16 and dim_b_total <= 16:
    result = 'Antwort 3'
    advice = 'Schmeiß dich in die Breche! Es darf nichts schief gehen! Hier musst Du reinspringen und mit viel Kraft dafür sorgen, dass kein Fehler passiert! Der Erfolg hängt von Dir ab!'
else:
    result = 'Antwort 4'
    advice = 'Macht es gemeinsam! Jetzt wird es spannend! Hier darf nichts schief gehen, aber es gibt hier auch viel zu lernen! Nimm deinen Partner an die Hand und geh mit ihm jeden Schritt gemeinsam. Lass ihn nicht allein und führe euer gemeinsames Handeln so, dass er aus jedem Schritt was lernt!'

st.header('Ergebnis')
st.subheader(result)
st.write(advice)
