import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LoL 챔피언 도감",
    page_icon="⚔️",
    layout="wide"
)

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("LoL_________.csv")

df = load_data()

st.title("⚔️ League of Legends 챔피언 도감")

st.write("원하는 챔피언을 검색하거나 역할군별로 찾아볼 수 있습니다.")

# ======================
# 사이드바
# ======================

st.sidebar.header("검색")

search = st.sidebar.text_input("챔피언 이름")

roles = ["전체"] + sorted(df["역할1"].dropna().unique().tolist())

selected_role = st.sidebar.selectbox(
    "역할군",
    roles
)

filtered = df.copy()

if search:
    filtered = filtered[
        filtered["챔피언"].str.contains(search, case=False, na=False)
    ]

if selected_role != "전체":
    filtered = filtered[
        filtered["역할1"] == selected_role
    ]

st.subheader(f"검색 결과 : {len(filtered)}명")

if len(filtered) == 0:
    st.warning("검색 결과가 없습니다.")

else:

    champion = st.selectbox(
        "챔피언 선택",
        filtered["챔피언"]
    )

    info = filtered[
        filtered["챔피언"] == champion
    ].iloc[0]

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(info["챔피언"])
        st.write(f"**영문 이름** : {info['영문이름']}")
        st.write(f"**주 역할** : {info['역할1']}")

        if pd.notna(info["역할2"]):
            st.write(f"**보조 역할** : {info['역할2']}")

    with col2:

        st.metric("체력", info["체력"])
        st.metric("마나", info["마나"])
        st.metric("공격력", info["공격력"])
        st.metric("방어력", info["방어력"])
        st.metric("마법 저항력", info["마법저항력"])
        st.metric("이동속도", info["이동속도"])

    st.divider()

    st.subheader("능력치")

    st.progress(min(info["체력"]/1000,1.0))
    st.write(f"체력 : {info['체력']}")

    st.progress(min(info["공격력"]/100,1.0))
    st.write(f"공격력 : {info['공격력']}")

    st.progress(min(info["방어력"]/100,1.0))
    st.write(f"방어력 : {info['방어력']}")

    st.progress(min(info["마법저항력"]/100,1.0))
    st.write(f"마법 저항력 : {info['마법저항력']}")

    st.divider()

    st.subheader("성장 능력치")

    st.write(f"체력 성장 : {info['체력성장']}")
    st.write(f"마나 성장 : {info['마나성장']}")
    st.write(f"공격력 성장 : {info['공격력성장']}")
    st.write(f"공격속도 성장 : {info['공격속도성장(%)']}%")

st.divider()

st.subheader("전체 챔피언 데이터")

st.dataframe(filtered, use_container_width=True)
