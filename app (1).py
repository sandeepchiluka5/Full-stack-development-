import streamlit as st

st.set_page_config(
    page_title="Responsive Architecture",
    page_icon="📱",
    layout="wide"
)

st.markdown("""
<style>
:root{
    --mocha:#A68B6F;
    --blue:#A0D4E0;
    --grey:#F2F0EA;
}
.main{
    background-color: var(--grey);
}
.hero{
    background: linear-gradient(135deg, var(--grey), var(--blue));
    padding: 3rem;
    border-radius: 20px;
}
.hero h1{
    color:#2f2f2f;
    font-size:3rem;
}
.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,.1);
    height:100%;
}
.section-title{
    color:var(--mocha);
    font-weight:700;
    margin-top:20px;
}
footer{
    text-align:center;
    padding:20px;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>📱 Responsive Frontend Interface</h1>
<p>
Create a responsive frontend interface using HTML, CSS,
and JavaScript principles with accessibility and
mobile-first architecture.
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.markdown('<h2 class="section-title">Pillar 1: Strategy & Blueprint</h2>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="card">
    <h3>Research</h3>
    <ul>
        <li>Understand user pain points</li>
        <li>Create empathy maps</li>
        <li>Gather requirements</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>Wireframing</h3>
    <ul>
        <li>Design layout structure</li>
        <li>Focus on hierarchy</li>
        <li>Mobile-first planning</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Pillar 2: Visual Design</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.color_picker("Mocha Mousse", "#A68B6F")

with col2:
    st.color_picker("Ethereal Blue", "#A0D4E0")

with col3:
    st.color_picker("Moonlit Grey", "#F2F0EA")

st.info("Typography: Inter / Montserrat for headings, Roboto / Open Sans for body text.")

st.markdown('<h2 class="section-title">Pillar 3: Implementation</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["HTML5", "CSS3", "JavaScript"])

with tab1:
    st.code("""
<header>
<nav></nav>
<main>
  <article></article>
</main>
<footer></footer>
""", language="html")

with tab2:
    st.code("""
.container{
    display:grid;
    grid-template-columns:1fr;
}
@media(min-width:768px){
    .container{
        grid-template-columns:1fr 1fr;
    }
}
""", language="css")

with tab3:
    st.code("""
const button=document.querySelector('#btn');
button.addEventListener('click',()=>{
    alert('Responsive UI Ready!');
});
""", language="javascript")

st.markdown('<h2 class="section-title">Frontend Logic Demo</h2>', unsafe_allow_html=True)

count = st.session_state.get("count", 0)

if st.button("Click Me"):
    count += 1
    st.session_state["count"] = count

st.success(f"Button clicked {count} times")

st.markdown('<h2 class="section-title">Execution Roadmap</h2>', unsafe_allow_html=True)

roadmap = [
    "1. Discovery",
    "2. Wireframe",
    "3. Semantic HTML",
    "4. CSS Styling",
    "5. JavaScript Logic",
    "6. Accessibility Audit"
]

for step in roadmap:
    st.write("✅", step)

st.markdown("""
<footer>
Built using Python + Streamlit | Responsive Architecture Project
</footer>
""", unsafe_allow_html=True)
