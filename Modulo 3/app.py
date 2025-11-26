import streamlit as st

genero = (
    'MPB': {
        'Jorge Ben Jor' : 'https://www.youtube.com/watch?v=Oph9BfH5FgQ&list=RDOph9BfH5FgQ&start_radio=1'
        'Djavan': 'https://www.youtube.com/watch?v=4NrFiP6Fwbg&list=RD4NrFiP6Fwbg&start_radio=1'
        'Bebeto':'https://www.youtube.com/watch?v=YTkSksHTvOA&list=RDYTkSksHTvOA&start_radio=1'
        'Gal Costa': 'https://www.youtube.com/watch?v=P3OZsKIcjdQ&list=RDP3OZsKIcjdQ&start_radio=1'
    },
    'Rap Nacional':{
        'BK': 'https://www.youtube.com/watch?v=oeSefY3yeu0&list=RDoeSefY3yeu0&start_radio=1'
        'Duquesa' : 'https://www.youtube.com/watch?v=IouZkIlWINM&list=OLAK5uy_nGN5XKU1ggxz5Q9LBXhIs_h3DQgtoANU8'
        'Black Alien' : 'https://www.youtube.com/watch?v=VJHbvVMNt0Q&list=RDVJHbvVMNt0Q&start_radio=1'
        'Tasha e Tracie': 'https://www.youtube.com/watch?v=nZfVmuVzJ3I&list=RDnZfVmuVzJ3I&start_radio=1'
    },
    'R&b': { 
        'Brent Fayaz': 'https://www.youtube.com/watch?v=YjCtucn29JQ&list=RDYjCtucn29JQ&start_radio=1'
        'SZA': 'https://www.youtube.com/watch?v=5sc1YvgxlSg&list=RD5sc1YvgxlSg&start_radio=1'
        'PARTYNEXTDOOR':'https://www.youtube.com/watch?v=44cICamRLwk&list=RD44cICamRLwk&start_radio=1'
        'Kehlani': 'https://www.youtube.com/watch?v=i6Tbai-mRHE&list=RDi6Tbai-mRHE&start_radio=1'
    },
    
    'Soul/Jazz': {
    'Nina Simone': 'https://www.youtube.com/watch?v=L5jI9I03q8E&list=RDL5jI9I03q8E&start_radio=1'    
    'Roy Ayrs Ubiquity':'https://www.youtube.com/watch?v=Blg_vkaXSWI&list=RDBlg_vkaXSWI&start_radio=1'
    'Sade':'https://www.youtube.com/watch?v=NYz8xs163YU&list=RDNYz8xs163YU&start_radio=1'
    'Erika Badu': 'https://www.youtube.com/watch?v=OqN0jsSeqPo&list=RDOqN0jsSeqPo&start_radio=1'
    }

)

#--------------------------------------------------------SIDEBAR
st.sidebar.title('Playlist para relaxar')
st.