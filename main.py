st.markdown("""
<style>

.stApp{
    background:#0b1426;
    color:#F0E6D2;
}

/* 모든 기본 텍스트 */
html, body, [class*="css"]{
    color:#F0E6D2;
}

/* 제목 */
h1,h2,h3,h4{
    color:#C8AA6E;
    font-weight:bold;
}

/* 문단 */
p{
    color:#F0E6D2;
}

/* 사이드바 */
section[data-testid="stSidebar"]{
    background:#111827;
}

/* 카드 */
div[data-testid="metric-container"]{
    background:#1E2328;
    border:1px solid #C8AA6E;
    border-radius:12px;
    padding:12px;
}

/* Metric 숫자 */
div[data-testid="metric-container"] label{
    color:#FFD166 !important;
}

div[data-testid="metric-container"] div{
    color:#FFFFFF !important;
}

/* 버튼 */
.stButton>button{
    background:#C8AA6E;
    color:#111111;
    font-weight:bold;
    border:none;
    border-radius:10px;
}

.stButton>button:hover{
    background:#F0E6D2;
}

/* 입력창 */
input{
    color:white !important;
}

/* Selectbox */
.stSelectbox div{
    color:white;
}

/* DataFrame */
[data-testid="stDataFrame"]{
    background:#1E2328;
}

/* 링크 */
a{
    color:#FFD166 !important;
}

</style>
""", unsafe_allow_html=True)
