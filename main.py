import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LoL Champion Encyclopedia",
    page_icon="⚔️",
    layout="wide"
)

# ==========================
# CSS
# ==========================
st.markdown("""
<style>

.stApp{
    background-color:#0b1426;
    color:white;
}

h1,h2,h3{
    color:#C8AA6E;
}

div[data-testid="metric-container"]{
    background:#1E2328;
    border:1px solid #C8AA6E;
    border-radius:12px;
    padding:10px;
}

.stButton>button{
    background:#C8AA6E;
    color:black;
    border-radius:10px;
}

.stButton>button:hover{
    background:#F0E6D2;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""",unsafe_allow_html=True)

# ==========================
# 데이터
# ==========================

@st.cache_data
def load_data():
    return pd.read_csv("LoL_________.csv")

df=load_data()

# ==========================
# 즐겨찾기
# ==========================

if "favorite" not in st.session_state:
    st.session_state.favorite=[]

# ==========================
# 제목
# ==========================

st.title("⚔️ League of Legends Champion Encyclopedia")

st.caption("모든 챔피언의 능력치를 확인하고 즐겨찾기에 저장하세요.")

# ==========================
# 사이드바
# ==========================

st.sidebar.title("검색")

search=st.sidebar.text_input("챔피언 검색")

roles=["전체"]+sorted(df["역할1"].dropna().unique())

role=st.sidebar.selectbox("역할군",roles)

filtered=df.copy()

if search:
    filtered=filtered[
        filtered["챔피언"].str.contains(search,case=False)
    ]

if role!="전체":
    filtered=filtered[
        filtered["역할1"]==role
    ]

# ==========================
# 챔피언 선택
# ==========================

champion=st.selectbox(
    "챔피언 선택",
    filtered["챔피언"]
)

info=df[df["챔피언"]==champion].iloc[0]

col1,col2=st.columns([1,2])

with col1:

    st.markdown("## 🛡️ 기본 정보")

    st.write(f"### {info['챔피언']}")
    st.write(f"**영문명** : {info['영문이름']}")
    st.write(f"**주 역할** : {info['역할1']}")

    if pd.notna(info["역할2"]):
        st.write(f"**보조 역할** : {info['역할2']}")

    if champion not in st.session_state.favorite:

        if st.button("⭐ 즐겨찾기 추가"):
            st.session_state.favorite.append(champion)

    else:

        if st.button("❌ 즐겨찾기 제거"):
            st.session_state.favorite.remove(champion)

with col2:

    st.markdown("## 📊 능력치")

    st.metric("체력",info["체력"])
    st.progress(min(info["체력"]/1000,1.0))

    st.metric("공격력",info["공격력"])
    st.progress(min(info["공격력"]/100,1.0))

    st.metric("방어력",info["방어력"])
    st.progress(min(info["방어력"]/100,1.0))

    st.metric("마법저항력",info["마법저항력"])
    st.progress(min(info["마법저항력"]/100,1.0))

    st.metric("이동속도",info["이동속도"])

st.divider()

st.subheader("📈 성장 능력치")

c1,c2,c3,c4=st.columns(4)

c1.metric("체력 성장",info["체력성장"])
c2.metric("마나 성장",info["마나성장"])
c3.metric("공격력 성장",info["공격력성장"])
c4.metric("공속 성장",f"{info['공격속도성장(%)']}%")

st.divider()

st.subheader("⭐ 즐겨찾기")

if len(st.session_state.favorite)==0:
    st.info("즐겨찾기한 챔피언이 없습니다.")

else:

    fav=df[df["챔피언"].isin(st.session_state.favorite)]

    st.dataframe(
        fav[["챔피언","역할1","공격력","방어력","체력"]],
        use_container_width=True
    )

st.divider()

st.subheader("📚 전체 챔피언 도감")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)
