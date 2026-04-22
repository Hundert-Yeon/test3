import random
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="AI 지역분석시스템 | 연효성", #
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');
html,body,[class*="css"]{font-family:'Noto Sans KR',sans-serif}
[data-testid="stSidebar"]{background:#0f2d52!important}
[data-testid="stSidebar"] *{color:rgba(255,255,255,.85)!important}
[data-testid="stSidebarContent"] hr{border-color:rgba(255,255,255,.1)!important}
[data-testid="metric-container"]{background:#f0f6ff;border:1px solid #dde5f0;border-radius:10px;padding:14px 16px}
[data-testid="metric-container"] [data-testid="stMetricLabel"]{font-size:12px;color:#64748b}
[data-testid="metric-container"] [data-testid="stMetricValue"]{font-size:22px;font-weight:700;color:#0f2d52}
.cover{background:linear-gradient(135deg,#0f2d52,#1a4a8a);border-radius:14px;padding:36px 40px;margin-bottom:24px}
.cover h1{font-size:28px;font-weight:700;color:#fff;margin:0 0 8px}
.cover p{font-size:14px;color:rgba(255,255,255,.6);margin:0 0 20px}
.cmeta{display:flex;gap:28px;flex-wrap:wrap}
.cml{font-size:10px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:.08em}
.cmv{font-size:13px;color:rgba(255,255,255,.9);font-weight:500;margin-top:2px}
.snum{font-size:11px;font-weight:700;color:#2e7dd4;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px}
.stitle{font-size:22px;font-weight:700;color:#0f2d52;margin:0 0 4px}
.sline{width:36px;height:3px;background:#2e7dd4;border-radius:2px;margin-bottom:20px}
.card{background:#fff;border:1px solid #dde5f0;border-radius:12px;padding:18px;margin-bottom:10px}
.cb{border-left:4px solid #2e7dd4;background:#f4f8fe}
.cg{border-left:4px solid #1b6e3a;background:#f0faf5}
.ca{border-left:4px solid #c47a00;background:#fffbf0}
.cr{border-left:4px solid #9b1c1c;background:#fff5f5}
.tag{display:inline-block;font-size:11px;font-weight:500;padding:3px 9px;border-radius:20px;margin:2px}
.tb{background:#e8f2fd;color:#1a56a0}
.tg{background:#e6f4ec;color:#1b6e3a}
.ta{background:#fff4e0;color:#7c4a00}
.tr{background:#fdecea;color:#9b1c1c}
.rr{display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0f4f8}
.rr:last-child{border:none}
.rk{font-size:11px;font-weight:700;color:#cbd5e1;width:16px;text-align:center}
.rn{font-size:13px;color:#1a2332;flex:1}
.rb{font-size:10px;padding:2px 6px;border-radius:20px;font-weight:600}
.rh{background:#fff4e0;color:#c45900}
.rw{background:#fdecea;color:#9b1c1c}
.ru{background:#e6f4ec;color:#1b6e3a}
.rs{background:#e8f2fd;color:#1a56a0}
.hl{background:#e8f2fd;border-left:4px solid #2e7dd4;border-radius:0 8px 8px 0;padding:12px 16px;font-size:13px;color:#1a56a0;margin:16px 0;font-style:italic}
.flow{display:flex;margin:16px 0}
.fs{flex:1;padding:16px 12px;border:1px solid #dde5f0}
.fs:first-child{border-radius:10px 0 0 10px;background:#f0f7ff}
.fs:nth-child(3){background:#f0faf5;border-left:none}
.fs:nth-child(5){background:#fffbf0;border-left:none}
.fs:last-child{border-radius:0 10px 10px 0;background:#f5f0ff;border-left:none}
.ftag{font-size:10px;font-weight:700;color:#2e7dd4;letter-spacing:.08em;text-transform:uppercase;margin-bottom:5px}
.ftitle{font-size:14px;font-weight:700;color:#0f2d52;margin-bottom:4px}
.fdesc{font-size:11px;color:#64748b;line-height:1.5}
.fa{display:flex;align-items:center;padding:0 2px;font-size:16px;color:#2e7dd4}
.ktbl{width:100%;border-collapse:collapse;border:1px solid #dde5f0;border-radius:10px;overflow:hidden}
.ktbl th{background:#0f2d52;color:#fff;font-size:12px;font-weight:600;padding:11px 13px;text-align:left}
.ktbl td{padding:10px 13px;font-size:13px;border-bottom:1px solid #f0f4f8}
.ktbl tr:nth-child(even) td{background:#f7f9fc}
.ktbl tr:last-child td{border-bottom:none}
.kn{font-weight:700;color:#1b6e3a}
.kl{font-weight:600;color:#0f2d52}
.rnum{font-size:36px;font-weight:700;color:#e2e8f0;line-height:1;margin-bottom:8px}
.rtitle{font-size:14px;font-weight:700;color:#0f2d52;margin-bottom:6px}
.rtag{font-size:11px;padding:3px 8px;border-radius:4px;background:#fdecea;color:#9b1c1c;display:inline-block;margin-bottom:8px}
.rdesc{font-size:12px;color:#64748b;line-height:1.6}
.dbar{background:#0f2d52;border-radius:10px 10px 0 0;padding:11px 18px;display:flex;justify-content:space-between;align-items:center}
.dtitle{font-size:14px;font-weight:600;color:#fff}
.dupd{font-size:11px;color:rgba(255,255,255,.4);background:rgba(255,255,255,.07);padding:3px 10px;border-radius:20px}
.bc{font-size:12px;color:#94a3b8;margin-bottom:8px}
.bcl{color:#2e7dd4;font-weight:500}
.bcc{color:#0f2d52;font-weight:600}
.bcs{color:#dde5f0;margin:0 3px}
.lvbar{display:flex;gap:6px;align-items:center;margin-bottom:12px;flex-wrap:wrap}
.lv{font-size:11px;font-weight:600;padding:4px 12px;border-radius:20px}
.lva{background:#e8f2fd;color:#1a56a0}
.lvd{background:#e6f4ec;color:#1b6e3a}
.lvn{background:#f0f0f4;color:#aaa}
.lvs{color:#dde5f0;font-size:12px}
.irow{display:flex;gap:10px;align-items:flex-start;padding:8px 0;border-bottom:1px solid #f0f4f8}
.irow:last-child{border:none}
.iicon{width:26px;height:26px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0}
.ib{background:#e8f2fd;color:#1a56a0}
.ig{background:#e6f4ec;color:#1b6e3a}
.iamb{background:#fff4e0;color:#c45900}
.ir{background:#fdecea;color:#9b1c1c}
.ih{font-size:13px;font-weight:600;color:#0f2d52;margin-bottom:2px}
.id{font-size:12px;color:#64748b;line-height:1.5}
</style>
""", unsafe_allow_html=True)


# ── 데이터 ────────────────────────────────────────────────────────────────────
@st.cache_data
def get_db():
    return {
        "인천": {
            "pop": "299만", "grdp": "89.2조", "retail": 112.4, "spend": "198만원",
            "popT": "+0.8%", "retailT": "+2.1%",
            "tags": [("크루즈 관광객","tb"),("인천공항 면세","tb"),("송도 팝업","tg"),
                     ("외국인 소비↑","ta"),("청라 개발호재","ta")],
            "food":  [("송도 오마카세 급부상","rh"),("차이나타운 재방문↑","ru"),
                      ("부평 로컬카페 확산","ru"),("연수구 브런치 맛집↑","rs")],
            "trend": [("인천 크루즈 일정","rh"),("송도 신규 맛집","ru"),("인천 팝업스토어","rw")],
            "districts": {
                "연수구": {
                    "pop":"36.2만","popT":"+1.4%","retail":118.0,"spend":"212만원",
                    "retailT":"+2.8%","grdp":"18.4%",
                    "tags":[("송도 팝업","tb"),("국제도시 개발","tg"),("글로벌캠퍼스","tb"),("고급주거 수요","ta")],
                    "food":[("오마카세 급부상","rh"),("센트럴파크 카페↑","ru"),("글로벌 브런치","rw"),("CGV 주변 맛집","rs")],
                    "trend":[("송도동 맛집","rh"),("연수구 아파트","ru"),("국제병원","rs")],
                    "dongs":[
                        {"n":"송도1동","pop":"2.8만","hot":True, "rise":False,"badge":"검색 1위"},
                        {"n":"송도2동","pop":"2.6만","hot":True, "rise":False,"badge":"소비 급등"},
                        {"n":"송도3동","pop":"2.1만","hot":False,"rise":True, "badge":"개발 활성"},
                        {"n":"연수1동","pop":"2.4만","hot":False,"rise":False,"badge":None},
                        {"n":"연수2동","pop":"2.2만","hot":False,"rise":False,"badge":None},
                        {"n":"연수3동","pop":"1.9만","hot":False,"rise":False,"badge":None},
                        {"n":"청학동",  "pop":"1.8만","hot":False,"rise":True, "badge":"재개발↑"},
                        {"n":"선학동",  "pop":"1.7만","hot":False,"rise":False,"badge":None},
                        {"n":"옥련1동","pop":"2.0만","hot":False,"rise":False,"badge":None},
                        {"n":"옥련2동","pop":"1.6만","hot":False,"rise":False,"badge":None},
                        {"n":"동춘1동","pop":"2.3만","hot":False,"rise":True, "badge":"소비↑"},
                        {"n":"동춘2동","pop":"2.1만","hot":False,"rise":False,"badge":None},
                        {"n":"동춘3동","pop":"1.9만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {
                        "송도1동": {
                            "pop":"2.8만","popT":"+2.3%","spend":"241만원",
                            "retail":124.8,"foreign":"6.4%",
                            "age":[18,14,34,22,12],
                            "ageLbl":["10대이하","20대","30대","40대","50대+"],
                            "tags":[("국제업무지구","tb"),("외국인 거주↑","tb"),
                                    ("오마카세 급부상","tg"),("센트럴파크 인근","tg"),("프리미엄 소비","ta")],
                            "trend":[("송도1동 오마카세","rh"),("센트럴파크 카페","ru"),
                                     ("송도 파인다이닝","rw"),("외국인 맛집","ru"),("루프탑 레스토랑","rw")],
                            "food":[("오마카세·파인다이닝","rh"),("스페셜티 커피 카페","ru"),
                                    ("글로벌 브런치","rw"),("와인바·비스트로","ru"),("프리미엄 베이커리","rs")],
                            "insights":[
                                ("ib","↑","프리미엄 F&amp;B 수요 급증",
                                 "외국인 거주자 증가(+0.9%p)와 국제업무지구 직장인 유입으로 오마카세·파인다이닝 검색 전월 대비 38% 급등."),
                                ("ig","+","30대 핵심 소비층 집중",
                                 "평균 연령 36.2세로 연수구 내 최연소 동. 30대 비중 34%로 트렌디한 MD 구성 우위."),
                                ("iamb","!","센트럴파크 집객 효과 활용",
                                 "센트럴파크 주변 카페·브런치 검색 지속 상위권. 주말 10~14시 팝업 이벤트 연계 권장."),
                                ("ir","↓","가성비보다 프리미엄 적합",
                                 "20대 비중 14%로 낮음. 품질·경험 중심 프리미엄 포지셔닝이 이 상권에 더 적합."),
                            ],
                        },
                        "송도2동": {
                            "pop":"2.6만","popT":"+1.9%","spend":"228만원",
                            "retail":121.3,"foreign":"4.8%",
                            "age":[16,15,30,26,13],
                            "ageLbl":["10대이하","20대","30대","40대","50대+"],
                            "tags":[("주거 밀집","tb"),("소비 급증","ta"),("신규 상권 형성","tg")],
                            "trend":[("송도2동 카페","rh"),("송도2동 맛집","ru"),("신규 상가","ru")],
                            "food":[("카페형 베이커리↑","rh"),("가족 레스토랑","ru"),("편의식 전문점","rs")],
                            "insights":[
                                ("ib","↑","소비 급증 중인 신흥 상권",
                                 "신규 입주세대 증가로 소비지출 전년 대비 5.2% 급증. 생활밀착형 상권 육성 시점."),
                                ("ig","+","40대 가족 소비층 강세",
                                 "40대 비중 26%로 가족 외식·교육 관련 소비 강세. 키즈 친화 MD 검토 가능."),
                            ],
                        },
                    },
                },
                "남동구": {
                    "pop":"52.1만","popT":"+0.3%","retail":110.0,"spend":"185만원",
                    "retailT":"+0.8%","grdp":"12.1%",
                    "tags":[("구월상권","tb"),("소래포구 관광","tg"),("남동공단","ta")],
                    "food":[("소래포구 해산물↑","rh"),("구월동 음식거리","ru"),("간석오거리 카페","rs")],
                    "trend":[("구월동 쇼핑","rh"),("남동공단 채용","rs"),("소래포구 주차","ru")],
                    "dongs":[
                        {"n":"구월1동","pop":"4.1만","hot":True, "rise":False,"badge":"검색 1위"},
                        {"n":"구월2동","pop":"3.8만","hot":False,"rise":True, "badge":"소비↑"},
                        {"n":"구월3동","pop":"3.2만","hot":False,"rise":False,"badge":None},
                        {"n":"간석1동","pop":"2.9만","hot":False,"rise":False,"badge":None},
                        {"n":"만수1동","pop":"2.4만","hot":False,"rise":True, "badge":"재개발"},
                        {"n":"서창동",  "pop":"3.1만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {},
                },
                "부평구": {
                    "pop":"50.8만","popT":"-0.5%","retail":106.0,"spend":"176만원",
                    "retailT":"-0.3%","grdp":"10.8%",
                    "tags":[("부평역 상권","tb"),("문화특구","tg"),("재개발 이슈","ta")],
                    "food":[("부평 먹자골목↑","rh"),("삼산동 카페거리","ru"),("갈산동 브런치","rs")],
                    "trend":[("부평역 맛집","rh"),("부평 재개발","ru"),("문화특구 행사","rs")],
                    "dongs":[
                        {"n":"부평1동","pop":"4.2만","hot":True, "rise":False,"badge":"검색 상위"},
                        {"n":"부평2동","pop":"3.9만","hot":False,"rise":False,"badge":None},
                        {"n":"부평3동","pop":"3.4만","hot":False,"rise":True, "badge":"소비↑"},
                        {"n":"십정1동","pop":"2.8만","hot":False,"rise":False,"badge":None},
                        {"n":"갈산1동","pop":"2.4만","hot":False,"rise":True, "badge":"카페↑"},
                    ],
                    "dong_detail": {},
                },
            },
        },
        "서울": {
            "pop": "941만", "grdp": "480조", "retail": 118.7, "spend": "234만원",
            "popT": "-0.4%", "retailT": "+1.5%",
            "tags":[("성수 팝업 열풍","tb"),("강남 명품↑","ta"),("2030 소비회복","tg"),("외국인 관광객","tb")],
            "food":[("성수 빈티지샵 핫플","rh"),("한남동 카페거리↑","ru"),("강남 오마카세 대기↑","rh")],
            "trend":[("성수동 팝업스토어","rh"),("강남 명품 세일","ru"),("한남동 맛집","ru")],
            "districts": {
                "강남구": {
                    "pop":"55.3만","popT":"+0.2%","retail":132.0,"spend":"312만원",
                    "retailT":"+2.1%","grdp":"9.8%",
                    "tags":[("명품 소비↑","ta"),("청담 플래그십","tb"),("압구정 재개발","ta")],
                    "food":[("오마카세 대기↑","rh"),("청담 파인다이닝","ru"),("압구정 카페거리","rs")],
                    "trend":[("강남 명품 세일","rh"),("압구정 재개발","ru"),("청담 레스토랑","rs")],
                    "dongs":[
                        {"n":"압구정동","pop":"2.1만","hot":True, "rise":False,"badge":"명품 1위"},
                        {"n":"신사동",  "pop":"2.8만","hot":True, "rise":False,"badge":"팝업↑"},
                        {"n":"청담동",  "pop":"1.9만","hot":False,"rise":True, "badge":"플래그십"},
                        {"n":"역삼1동","pop":"4.2만","hot":False,"rise":False,"badge":None},
                        {"n":"삼성1동","pop":"3.1만","hot":False,"rise":True, "badge":"소비↑"},
                    ],
                    "dong_detail": {},
                },
                "성동구": {
                    "pop":"30.1만","popT":"+1.2%","retail":124.0,"spend":"245만원",
                    "retailT":"+3.4%","grdp":"4.2%",
                    "tags":[("성수 팝업 성지","tb"),("MZ 핫플","tg"),("젠트리피케이션","ta")],
                    "food":[("성수 팝업 줄서기","rh"),("뚝도시장 카페↑","ru"),("왕십리 먹자골목","rs")],
                    "trend":[("성수동 팝업","rh"),("성수 카페","ru"),("뚝섬역 맛집","ru")],
                    "dongs":[
                        {"n":"성수1가1동","pop":"1.8만","hot":True, "rise":False,"badge":"팝업 1위"},
                        {"n":"성수1가2동","pop":"1.6만","hot":True, "rise":False,"badge":"급등"},
                        {"n":"성수2가1동","pop":"2.1만","hot":False,"rise":True, "badge":"상권↑"},
                        {"n":"왕십리2동", "pop":"2.8만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {},
                },
                "마포구": {
                    "pop":"37.8만","popT":"-0.2%","retail":119.0,"spend":"228만원",
                    "retailT":"+1.2%","grdp":"5.1%",
                    "tags":[("홍대 상권","tb"),("망원 로컬","tg"),("연남 카페거리","tg")],
                    "food":[("망원동 브런치↑","rh"),("연남동 카페거리","ru"),("홍대 클럽거리","rs")],
                    "trend":[("홍대 맛집","rh"),("망원동 카페","ru"),("연남동 팝업","rw")],
                    "dongs":[
                        {"n":"서교동","pop":"2.6만","hot":True, "rise":False,"badge":"홍대 핫플"},
                        {"n":"연남동","pop":"2.2만","hot":True, "rise":False,"badge":"급상승"},
                        {"n":"망원1동","pop":"2.4만","hot":False,"rise":True, "badge":"브런치↑"},
                        {"n":"합정동","pop":"2.1만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {},
                },
            },
        },
        "부산": {
            "pop": "332만", "grdp": "98.5조", "retail": 108.3, "spend": "186만원",
            "popT": "-0.6%", "retailT": "-0.8%",
            "tags":[("해운대 관광시즌","tb"),("북항 재개발","ta"),("서면 상권 회복","tg")],
            "food":[("해운대 씨푸드↑","rh"),("서면 로컬카페↑","ru"),("광안리 루프탑 바","rw")],
            "trend":[("부산 해수욕장","rh"),("해운대 맛집","ru"),("북항 개발","rs")],
            "districts": {
                "해운대구": {
                    "pop":"41.8만","popT":"-0.3%","retail":114.0,"spend":"198만원",
                    "retailT":"+0.8%","grdp":"8.4%",
                    "tags":[("해변 관광","tb"),("마린시티 부촌","ta"),("센텀 쇼핑","tb")],
                    "food":[("해수욕장 씨푸드↑","rh"),("센텀 레스토랑","ru"),("마린시티 와인바","rw")],
                    "trend":[("해운대 해수욕장","rh"),("센텀시티 쇼핑","ru"),("마린시티 맛집","rs")],
                    "dongs":[
                        {"n":"우1동",  "pop":"3.8만","hot":True, "rise":False,"badge":"관광 1위"},
                        {"n":"중1동",  "pop":"3.2만","hot":True, "rise":False,"badge":"소비↑"},
                        {"n":"재송1동","pop":"4.1만","hot":False,"rise":True, "badge":"개발↑"},
                        {"n":"반여1동","pop":"2.9만","hot":False,"rise":False,"badge":None},
                        {"n":"송정동", "pop":"1.8만","hot":False,"rise":True, "badge":"서핑↑"},
                    ],
                    "dong_detail": {},
                },
                "부산진구": {
                    "pop":"37.1만","popT":"-0.7%","retail":109.0,"spend":"182만원",
                    "retailT":"-0.2%","grdp":"6.2%",
                    "tags":[("서면 중심상권","tb"),("전포카페거리","tg"),("부전시장","ta")],
                    "food":[("서면 먹자골목↑","rh"),("전포카페거리 MZ↑","rh"),("부전시장 먹거리","rs")],
                    "trend":[("서면 맛집","rh"),("전포 카페","ru"),("부산진 쇼핑","rs")],
                    "dongs":[
                        {"n":"부전1동","pop":"3.6만","hot":True, "rise":False,"badge":"검색 1위"},
                        {"n":"전포1동","pop":"2.4만","hot":True, "rise":False,"badge":"MZ 급등"},
                        {"n":"전포2동","pop":"2.2만","hot":False,"rise":True, "badge":"카페↑"},
                        {"n":"당감1동","pop":"2.8만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {},
                },
            },
        },
        "대구": {
            "pop": "236만", "grdp": "56.2조", "retail": 104.1, "spend": "172만원",
            "popT": "-0.9%", "retailT": "+0.5%",
            "tags":[("동성로 상권 부활","tb"),("섬유산업 침체","tr"),("청년 창업↑","tg")],
            "food":[("동성로 MZ 맛집↑","rh"),("수성못 카페투어↑","ru"),("서문시장 먹거리","rs")],
            "trend":[("동성로 팝업","rh"),("수성못 카페","ru"),("청년 창업","rw")],
            "districts": {
                "수성구": {
                    "pop":"43.2만","popT":"-0.4%","retail":112.0,"spend":"224만원",
                    "retailT":"+1.4%","grdp":"7.8%",
                    "tags":[("수성못 관광","tg"),("학군 수요↑","tb"),("범어 부촌","ta")],
                    "food":[("수성못 카페투어↑","rh"),("범어동 파인다이닝","ru"),("황금동 음식거리","rs")],
                    "trend":[("수성못 카페","rh"),("범어동 맛집","ru"),("수성구 학원","rs")],
                    "dongs":[
                        {"n":"수성1가동","pop":"2.4만","hot":True, "rise":False,"badge":"카페 1위"},
                        {"n":"황금1동",  "pop":"3.8만","hot":False,"rise":True, "badge":"소비↑"},
                        {"n":"범어1동",  "pop":"3.2만","hot":True, "rise":False,"badge":"파인다이닝"},
                        {"n":"만촌1동",  "pop":"3.6만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {},
                },
                "중구": {
                    "pop":"7.8만","popT":"-1.2%","retail":116.0,"spend":"208만원",
                    "retailT":"+0.9%","grdp":"3.1%",
                    "tags":[("동성로 핵심","tb"),("근대골목 관광","tg"),("이월드 인근","tb")],
                    "food":[("동성로 팝업↑","rh"),("서문시장 야시장","ru"),("근대골목 카페","rs")],
                    "trend":[("동성로 맛집","rh"),("서문시장 야시장","ru"),("근대골목 투어","rs")],
                    "dongs":[
                        {"n":"성내1동","pop":"1.2만","hot":True, "rise":False,"badge":"팝업 1위"},
                        {"n":"남산1동","pop":"1.4만","hot":False,"rise":True, "badge":"트렌드↑"},
                        {"n":"대봉1동","pop":"1.6만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {},
                },
            },
        },
        "광주": {
            "pop": "143만", "grdp": "38.7조", "retail": 106.8, "spend": "168만원",
            "popT": "-0.3%", "retailT": "+1.2%",
            "tags":[("비엔날레 시즌","tb"),("친환경 소비↑","tg"),("문화예술 행사","ta")],
            "food":[("양림동 역사카페↑","rh"),("충장로 로컬맛집","ru"),("상무지구 브런치↑","ru")],
            "trend":[("광주 비엔날레","rh"),("양림동 카페거리","ru"),("상무지구 맛집","ru")],
            "districts": {
                "서구": {
                    "pop":"28.4만","popT":"-0.5%","retail":108.0,"spend":"172만원",
                    "retailT":"+0.6%","grdp":"6.2%",
                    "tags":[("상무지구 중심","tb"),("치평동 상권","tg"),("금호지구","tb")],
                    "food":[("상무지구 브런치↑","rh"),("치평동 카페거리","ru"),("금호동 맛집","rs")],
                    "trend":[("상무지구 맛집","rh"),("치평 카페","ru"),("서구 아파트","rs")],
                    "dongs":[
                        {"n":"치평동","pop":"4.2만","hot":True, "rise":False,"badge":"브런치 1위"},
                        {"n":"상무1동","pop":"3.8만","hot":False,"rise":True, "badge":"소비↑"},
                        {"n":"화정1동","pop":"3.4만","hot":False,"rise":False,"badge":None},
                        {"n":"풍암동", "pop":"3.6만","hot":False,"rise":False,"badge":None},
                    ],
                    "dong_detail": {},
                },
                "동구": {
                    "pop":"9.5만","popT":"-1.1%","retail":112.0,"spend":"188만원",
                    "retailT":"+1.8%","grdp":"2.8%",
                    "tags":[("충장로 문화거리","tb"),("양림동 역사마을","tg"),("5·18 성지","tb")],
                    "food":[("양림동 카페↑","rh"),("충장로 맛집","ru"),("동명동 감성카페","rw")],
                    "trend":[("양림동 카페","rh"),("충장로 쇼핑","ru"),("동구 문화행사","rs")],
                    "dongs":[
                        {"n":"양림동","pop":"0.9만","hot":True, "rise":False,"badge":"역사카페 1위"},
                        {"n":"충장1동","pop":"1.8만","hot":True, "rise":False,"badge":"검색↑"},
                        {"n":"계림1동","pop":"1.4만","hot":False,"rise":True, "badge":"상권↑"},
                    ],
                    "dong_detail": {},
                },
            },
        },
    }

DB = get_db()


# ── 헬퍼 ──────────────────────────────────────────────────────────────────────
BADGE_LBL = {"rh": "급등", "rw": "신규", "ru": "상승", "rs": "유지"}

def render_tags(lst):
    h = '<div style="display:flex;flex-wrap:wrap;gap:4px;margin:8px 0">'
    for text, cls in lst:
        h += '<span class="tag {}">{}</span>'.format(cls, text)
    h += "</div>"
    st.markdown(h, unsafe_allow_html=True)

def render_rank(items, title):
    rows = ""
    for text, cls in items:
        lbl = BADGE_LBL.get(cls, "")
        rows += (
            '<div class="rr">'
            '<span class="rk">·</span>'
            '<span class="rn">{}</span>'
            '<span class="rb {}">{}</span>'
            "</div>"
        ).format(text, cls, lbl)
    st.markdown(
        '<div class="card" style="padding:12px 14px">'
        '<div style="font-size:11px;font-weight:600;color:#64748b;margin-bottom:6px">{}</div>'
        "{}</div>".format(title, rows),
        unsafe_allow_html=True,
    )

def render_metrics(d):
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("인구수", d["pop"], d["popT"])
    with c2: st.metric("소매판매지수", str(d["retail"]), d.get("retailT", "—"))
    with c3: st.metric("1인당 소비지출", d["spend"])
    with c4: st.metric("GRDP / 기여도", d.get("grdp", "—"))

def render_retail_chart(base_val, seed_key):
    rng = random.Random(seed_key)
    months = ["10월","11월","12월","1월","2월","3월","4월"]
    vals = [round(base_val - 4 + i * 0.9 + (rng.random() - 0.5) * 0.8, 1) for i in range(7)]
    df = pd.DataFrame({"월": months, "소매판매지수": vals}).set_index("월")
    st.line_chart(df, height=160, use_container_width=True)

def render_age_chart(vals, lbls):
    df = pd.DataFrame({"연령대": lbls, "비율(%)": vals}).set_index("연령대")
    st.bar_chart(df, height=150, use_container_width=True)

def render_gu_bar(sido_name):
    gd = DB[sido_name]["districts"]
    names = list(gd.keys())
    retail_vals = [gd[g]["retail"] for g in names]
    df = pd.DataFrame({"구": names, "소매판매지수": retail_vals}).set_index("구")
    st.bar_chart(df, height=180, use_container_width=True)

def sec_header(num, title):
    st.markdown(
        '<div class="snum">{}</div><div class="stitle">{}</div><div class="sline"></div>'.format(num, title),
        unsafe_allow_html=True,
    )


# ── 사이드바 ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<div style="padding:14px 0 10px">'
        '<div style="font-size:17px;font-weight:700;color:#fff">📊 AI 지역분석</div>'
        '<div style="font-size:11px;color:rgba(255,255,255,.4);margin-top:3px">영업기획팀 · 2026.04</div>'
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    page = st.radio(
        "메뉴",
        [
            "📋 기획서 전문",
            "01 요약",
            "02 현황 및 문제 정의",
            "03 AI 솔루션 설계",
            "04 기대 효과 / KPI",
            "05 리스크 및 대응",
            "06 실행 계획",
            "🗺 대시보드 라이브 데모",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(
        '<div style="font-size:11px;color:rgba(255,255,255,.3)">수치는 추정치이며<br>도입 전 검증이 필요합니다</div>',
        unsafe_allow_html=True,
    )


# ════════════════════════════════════════════════════════════════════════════
# 기획서 전문
# ════════════════════════════════════════════════════════════════════════════
if "기획서" in page:
    st.markdown(
        '<div class="cover">'
        "<h1>AI 지역 거시환경 자동 분석 시스템 구축</h1>"
        "<p>Regional Intelligence Dashboard — 영업기획팀 효율화 프로젝트</p>"
        '<div class="cmeta">'
        '<div><div class="cml">제안팀</div><div class="cmv">영업기획팀</div></div>'
        '<div><div class="cml">대상</div><div class="cmv">9명 전체 구성원</div></div>'
        '<div><div class="cml">기간</div><div class="cmv">총 8주 (4단계)</div></div>'
        '<div><div class="cml">작성일</div><div class="cmv">2026. 04</div></div>'
        "</div></div>",
        unsafe_allow_html=True,
    )
    st.info("좌측 사이드바에서 각 섹션(01~06) 또는 대시보드를 선택하세요.")
    sections = [
        ("cb", "01 요약", "문제 / 솔루션 / 기대효과"),
        ("cr", "04 KPI", "5가지 정량 목표"),
        ("cb", "02 현황", "문제 정의 및 수치 근거"),
        ("cr", "05 리스크", "3가지 리스크 및 대응"),
        ("cg", "03 솔루션", "AI 설계 및 역할 분담"),
        ("ca", "06 실행계획", "8주 마일스톤"),
    ]
    cols = st.columns(3)
    for idx, (cls, title, sub) in enumerate(sections):
        with cols[idx % 3]:
            st.markdown(
                '<div class="card {}">'
                '<b>{}</b><br>'
                '<small style="color:#64748b">{}</small>'
                "</div>".format(cls, title, sub),
                unsafe_allow_html=True,
            )


# ════════════════════════════════════════════════════════════════════════════
# 01 요약
# ════════════════════════════════════════════════════════════════════════════
if "01" in page:
    sec_header("01", "요약")
    c1, c2, c3 = st.columns(3)
    summary_items = [
        ("cr", "문제", "36h", "#9b1c1c",
         "지역별 거시경제·트렌드 데이터를 <b>1인당 주 4시간 이상</b> 수작업 수집·분석. "
         "팀 전체 주 36시간 낭비로 전략 기획 본연의 업무 투입 구조적 제한."),
        ("cb", "솔루션", "3단계", "#1a56a0",
         "AI가 통계청·검색트렌드·뉴스를 실시간 수집·분석. "
         "<b>시·도→행정구→행정동</b> 3단계 드릴다운 대시보드로 클릭 한 번에 인사이트 제공."),
        ("cg", "기대효과", "↓90%", "#1b6e3a",
         "분석 소요시간 <b>90% 단축</b> (4시간→24분), 데이터 정확도 향상, MD 의사결정 속도 2배 이상 향상."),
    ]
    for col, (cls, lbl, num, color, txt) in zip([c1, c2, c3], summary_items):
        with col:
            st.markdown(
                '<div class="card {}">'
                '<div style="font-size:10px;font-weight:700;color:{};text-transform:uppercase;'
                'letter-spacing:.08em;margin-bottom:8px">{}</div>'
                '<div style="font-size:36px;font-weight:700;color:{};line-height:1;margin-bottom:10px">{}</div>'
                '<div style="font-size:13px;color:#1a2332;line-height:1.7">{}</div>'
                "</div>".format(cls, color, lbl, color, num, txt),
                unsafe_allow_html=True,
            )


# ════════════════════════════════════════════════════════════════════════════
# 02 현황
# ════════════════════════════════════════════════════════════════════════════
if "02" in page:
    sec_header("02", "현황 및 문제 정의")
    st.markdown(
        "현재 영업기획팀 9명은 매주 지역별 거시경제 분석 자료를 통계청 KOSIS, "
        "네이버·구글 트렌드, 뉴스 검색 등 다수의 사이트에 개별 접속하여 데이터를 직접 수집하고 있다. "
        "이 과정에서 1인당 최소 4시간, 팀 전체로는 **주 36시간 이상**의 시간이 단순 수집 작업에 소비되어 "
        "전략 기획 본연의 업무 투입이 구조적으로 제한된다.\n\n"
        "데이터 수집 방식의 파편화로 인해 담당자별 분석 기준과 수집 범위가 달라 동일 지역에 대한 "
        "해석이 팀원 간 불일치하는 사례가 발생한다. "
        "또한 트렌드·이슈 데이터는 실시간성이 중요함에도 수작업 특성상 **주 1~2회 업데이트**가 한계로, "
        "시의성 있는 의사결정에 걸림돌이 된다.\n\n"
        "MD 전략 수립에 필요한 정보는 거시지표를 넘어 지역별 실시간 소비 이슈, 검색 트렌드 키워드, "
        "맛집·라이프스타일 변화까지 포함한다. "
        "이를 개인이 모두 탐색하는 현재 구조는 인력 효율 측면의 명백한 비효율이며 AI 자동화가 시급하다."
    )
    st.markdown(
        '<div class="hl">※ 수치 근거: 팀원 인터뷰 기반 평균 소요시간 추정 (1인 4시간 × 9명). '
        "도입 전 2주간 실제 측정으로 검증 권장.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("#### 주간 소요시간 비교 (수작업 vs AI 도입 후)")
    df_time = pd.DataFrame(
        {
            "항목": ["데이터 수집", "분석·정리", "보고서 작성"],
            "수작업(현재)": [18, 12, 6],
            "AI 도입 후": [0.5, 1.5, 1.6],
        }
    ).set_index("항목")
    st.bar_chart(df_time, height=260, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# 03 솔루션
# ════════════════════════════════════════════════════════════════════════════
if "03" in page:
    sec_header("03", "AI 솔루션 설계")
    st.markdown(
        '<div class="flow">'
        '<div class="fs"><div class="ftag">Problem</div><div class="ftitle">분산 데이터</div>'
        '<div class="fdesc">통계청, 검색포털, 뉴스 등 소스별 수작업 수집</div></div>'
        '<div class="fa">→</div>'
        '<div class="fs"><div class="ftag">Data</div><div class="ftitle">자동 수집</div>'
        '<div class="fdesc">API·크롤링으로 지역별 데이터 실시간 통합</div></div>'
        '<div class="fa">→</div>'
        '<div class="fs"><div class="ftag">Insight</div><div class="ftitle">AI 분석</div>'
        '<div class="fdesc">LLM이 트렌드 요약·이슈 추출·소비지표 해석</div></div>'
        '<div class="fa">→</div>'
        '<div class="fs"><div class="ftag">Action</div><div class="ftitle">MD 의사결정</div>'
        '<div class="fdesc">대시보드 클릭 → 인사이트 즉시 활용</div></div>'
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("#### AI 활용 방식 — 3개 레이어")
    layer_data = [
        ("cb", "🔗 데이터 수집 레이어",
         "통계청 KOSIS Open API, 네이버·구글 트렌드 API, 뉴스 RSS 자동 호출. 매일 새벽 스케줄러로 전국 지역별 갱신."),
        ("cg", "🤖 AI 분석 레이어",
         "LLM(Claude/GPT)이 핵심 이슈 키워드·소비 트렌드·맛집 버즈 순위를 자동 추출·요약."),
        ("ca", "📊 시각화 레이어",
         "시·도→행정구→행정동 3단계 드릴다운. 클릭 시 인구·소비 지표 차트와 이슈 태그 즉시 렌더링."),
    ]
    for col, (cls, title, desc) in zip(st.columns(3), layer_data):
        with col:
            st.markdown(
                '<div class="card {}">'
                "<b>{}</b><br><br>"
                '<span style="font-size:13px;color:#4a5568;line-height:1.7">{}</span>'
                "</div>".format(cls, title, desc),
                unsafe_allow_html=True,
            )
    st.markdown("#### 사람 vs AI 역할 분담")
    rc1, rc2 = st.columns(2)
    with rc1:
        st.markdown(
            '<div class="card cg">'
            '<b style="color:#1b6e3a">🤖 AI 담당 역할</b>'
            '<ul style="font-size:13px;color:#4a5568;line-height:2.1;margin-top:10px;padding-left:16px">'
            "<li>공공 API·뉴스 데이터 자동 수집 및 정제</li>"
            "<li>지역별 이슈 키워드 추출 및 요약</li>"
            "<li>소비 트렌드 변화 감지 및 알림</li>"
            "<li>지표 간 상관관계 1차 해석</li>"
            "<li>차트·표·태그 자동 생성</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )
    with rc2:
        st.markdown(
            '<div class="card ca">'
            '<b style="color:#7c4a00">👤 사람 담당 역할</b>'
            '<ul style="font-size:13px;color:#4a5568;line-height:2.1;margin-top:10px;padding-left:16px">'
            "<li>MD 전략 방향성 및 기획 판단</li>"
            "<li>AI 분석 결과의 맥락적 해석</li>"
            "<li>이상 데이터 검증 및 보정</li>"
            "<li>임원 보고 자료 편집·커뮤니케이션</li>"
            "<li>신규 분석 어젠다 설정</li>"
            "</ul></div>",
            unsafe_allow_html=True,
        )


# ════════════════════════════════════════════════════════════════════════════
# 04 기대효과
# ════════════════════════════════════════════════════════════════════════════
if "04" in page:
    sec_header("04", "기대 효과 — KPI 5가지")
    kpi_rows = [
        ("분석 소요시간 절감", "1인 주 4시간", "1인 주 24분 (↓90%)", "팀원 작업일지 월 측정"),
        ("팀 전체 절감 시간", "주 36시간", "주 3.6시간 (32.4h 절감)", "시스템 접속 로그"),
        ("데이터 업데이트 주기", "주 1~2회 수작업", "매일 자동 갱신", "스케줄러 실행 로그"),
        ("분석 커버 지역 수", "2~3개 지역/담당", "전국 17개 광역시도 100%", "대시보드 지역 탭 수"),
        ("MD 보고서 작성 시간", "보고서당 평균 3시간", "보고서당 1시간 이내 (↓67%)", "착수~완료 시간 측정"),
    ]
    rows_html = ""
    for r in kpi_rows:
        rows_html += (
            "<tr>"
            '<td class="kl">{}</td><td>{}</td>'
            '<td class="kn">{}</td>'
            '<td style="font-size:12px;color:#64748b">{}</td>'
            "</tr>"
        ).format(r[0], r[1], r[2], r[3])
    st.markdown(
        '<table class="ktbl"><thead><tr>'
        "<th>KPI</th><th>현재 (Before)</th><th>목표 (After)</th><th>측정 방식</th>"
        "</tr></thead><tbody>{}</tbody></table>".format(rows_html),
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hl">※ 목표 수치는 유사 사례(유통사 데이터팀 AI 도입) 기반 추정치. '
        "도입 후 4주 시점 중간 측정으로 재조정 권장.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("#### KPI 목표 달성률 (현재=100 기준)")
    df_kpi = pd.DataFrame(
        {
            "KPI": ["분석시간", "팀절감시간", "업데이트주기", "커버지역수", "보고서작성"],
            "현재": [100, 100, 100, 100, 100],
            "목표": [10, 10, 14, 100, 33],
        }
    ).set_index("KPI")
    st.bar_chart(df_kpi, height=240, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# 05 리스크
# ════════════════════════════════════════════════════════════════════════════
if "05" in page:
    sec_header("05", "리스크 및 대응 방안")
    risk_data = [
        ("01", "데이터 정확도·신뢰성", "공공 API 오류·결측, AI 요약 오류 가능성",
         "원본 소스 링크 동시 노출, 월 1회 샘플 검증 프로세스 수립, AI 요약에 검토 필요 플래그 기능 추가."),
        ("02", "초기 구축 비용·일정", "개발 인력 부재, 일정 지연, 예산 초과",
         "무료 공공 API로 MVP 먼저 구축, 단계별 검수 계약, 8주 타임박스 내 최소 기능 우선 완성."),
        ("03", "구성원 활용도 저하", "새 시스템 학습 저항, 기존 습관 유지",
         "파일럿 2명 설계 참여, 1페이지 가이드 제작, 4주 기존 방식 병행 후 전환."),
    ]
    for col, (num, title, tag, desc) in zip(st.columns(3), risk_data):
        with col:
            st.markdown(
                '<div class="card">'
                '<div class="rnum">{}</div>'
                '<div class="rtitle">{}</div>'
                '<div class="rtag">{}</div>'
                '<div class="rdesc">{}</div>'
                "</div>".format(num, title, tag, desc),
                unsafe_allow_html=True,
            )


# ════════════════════════════════════════════════════════════════════════════
# 06 실행계획
# ════════════════════════════════════════════════════════════════════════════
if "06" in page:
    sec_header("06", "실행 계획 — 8주 마일스톤")
    st.markdown(
        "전체 프로젝트는 4단계 8주로 운영된다. "
        "1~2주차 기반 설계에서 확정된 소스와 화면 구조를 바탕으로 "
        "3~4주차 MVP를 신속 개발하고, 5~6주차 행정동 드릴다운까지 고도화한 뒤, "
        "7~8주차 팀 전환 및 KPI 측정을 완료한다."
    )
    ms_data = [
        ("1–2주차", "기반 설계", "#2e7dd4",
         ["요구사항 정의 (팀 인터뷰)", "활용 데이터 소스 확정", "API 연결 가능 여부 검증", "화면 와이어프레임 작성"]),
        ("3–4주차", "MVP 개발", "#1b6e3a",
         ["통계청 API 자동 수집 구축", "AI 키워드 추출 연동", "지역 클릭 대시보드 프로토타입", "2개 지역 파일럿 테스트"]),
        ("5–6주차", "고도화·검증", "#c47a00",
         ["전국 17개 지역 확대", "맛집·트렌드 데이터 연동", "행정동 드릴다운 완성", "데이터 정확도 1차 검증"]),
        ("7–8주차", "운영 전환", "#7c3aed",
         ["팀 전체 사용법 교육", "기존 방식 병행 후 전환", "KPI 초기값 측정", "개선사항 수집·반영"]),
    ]
    for col, (week, title, color, items) in zip(st.columns(4), ms_data):
        with col:
            li_html = ""
            for item in items:
                li_html += (
                    '<li style="padding:4px 0;border-bottom:1px solid #f0f4f8;'
                    'font-size:12px;color:#64748b">{}</li>'.format(item)
                )
            st.markdown(
                '<div class="card" style="border-top:3px solid {}">'
                '<div style="font-size:11px;font-weight:700;color:{};text-transform:uppercase;'
                'letter-spacing:.06em;margin-bottom:5px">{}</div>'
                '<div style="font-size:14px;font-weight:700;color:#0f2d52;margin-bottom:8px">{}</div>'
                '<ul style="list-style:none;padding:0;margin:0">{}</ul>'
                "</div>".format(color, color, week, title, li_html),
                unsafe_allow_html=True,
            )
    st.markdown("#### 8주 타임라인")
    df_gantt = pd.DataFrame(
        {
            "주차": list(range(1, 9)),
            "기반 설계":   [1, 1, 0, 0, 0, 0, 0, 0],
            "MVP 개발":    [0, 0, 1, 1, 0, 0, 0, 0],
            "고도화·검증": [0, 0, 0, 0, 1, 1, 0, 0],
            "운영 전환":   [0, 0, 0, 0, 0, 0, 1, 1],
        }
    ).set_index("주차")
    st.bar_chart(df_gantt, height=200, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# 대시보드
# ════════════════════════════════════════════════════════════════════════════
if "대시보드" in page:
    sec_header("부록", "대시보드 — 라이브 데모")

    # session state 초기화
    if "sido" not in st.session_state:
        st.session_state["sido"] = None
    if "gu" not in st.session_state:
        st.session_state["gu"] = None
    if "dong" not in st.session_state:
        st.session_state["dong"] = None

    # 상태 변경 함수
    def set_sido(name):
        st.session_state["sido"] = name
        st.session_state["gu"] = None
        st.session_state["dong"] = None

    def set_gu(name):
        st.session_state["gu"] = name
        st.session_state["dong"] = None

    def set_dong(name):
        st.session_state["dong"] = name

    sido = st.session_state["sido"]
    gu   = st.session_state["gu"]
    dong = st.session_state["dong"]

    # 상단바
    st.markdown(
        '<div class="dbar">'
        '<span class="dtitle">🟢 지역 거시환경 AI 분석 대시보드</span>'
        '<span class="dupd">기준 2026.04 · 자동 갱신</span>'
        "</div>",
        unsafe_allow_html=True,
    )

    # 브레드크럼
    bc_html = '<div class="bc"><span class="bcl">전국</span>'
    if sido:
        bc_html += '<span class="bcs"> › </span>'
        bc_html += '<span class="{}">{}</span>'.format("bcc" if not gu else "bcl", sido)
    if gu:
        bc_html += '<span class="bcs"> › </span>'
        bc_html += '<span class="{}">{}</span>'.format("bcc" if not dong else "bcl", gu)
    if dong:
        bc_html += '<span class="bcs"> › </span><span class="bcc">{}</span>'.format(dong)
    bc_html += "</div>"
    st.markdown(bc_html, unsafe_allow_html=True)

    # 레벨 바
    lv1 = "lvd" if sido else "lva"
    lv2 = "lvd" if gu else ("lva" if sido else "lvn")
    lv3 = "lva" if dong else ("lva" if gu else "lvn")
    st.markdown(
        '<div class="lvbar">'
        '<span class="lv {lv1}">시·도{done1}</span>'
        '<span class="lvs">›</span>'
        '<span class="lv {lv2}">행정구{done2}</span>'
        '<span class="lvs">›</span>'
        '<span class="lv {lv3}">행정동 상세</span>'
        "</div>".format(
            lv1=lv1, done1="  ✓" if sido else "",
            lv2=lv2, done2="  ✓" if gu else "",
            lv3=lv3,
        ),
        unsafe_allow_html=True,
    )

    # 검색
    sq = st.text_input(
        "지역 검색",
        placeholder="연수구, 송도1동, 강남구...",
        label_visibility="collapsed",
        key="search_q",
    )
    if sq:
        results = []
        for sn, sd in DB.items():
            if sq in sn:
                results.append(("시·도", sn, None, None))
            for gn, gd in sd["districts"].items():
                if sq in gn:
                    results.append(("행정구", sn, gn, None))
                for dk in gd["dongs"]:
                    if sq in dk["n"]:
                        results.append(("행정동", sn, gn, dk["n"]))
        if results:
            st.caption("검색 결과 {}건".format(len(results)))
            rcols = st.columns(min(len(results), 4))
            for i, (typ, sn, gn, dn) in enumerate(results[:4]):
                lbl = sn
                if gn:
                    lbl += " " + gn
                if dn:
                    lbl += " " + dn
                with rcols[i]:
                    btn_key = "sr_{}".format(i)
                    if st.button("📍 {}\n({})".format(lbl, typ), key=btn_key, use_container_width=True):
                        st.session_state["sido"] = sn
                        if gn:
                            st.session_state["gu"] = gn
                        if dn:
                            st.session_state["dong"] = dn
                        st.rerun()
        else:
            st.caption("검색 결과 없음")
        st.divider()
        sido = st.session_state["sido"]
        gu   = st.session_state["gu"]
        dong = st.session_state["dong"]

    # ── LEVEL 1 : 시·도 ──────────────────────────────────────────────────────
    st.markdown(
        '<div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:8px">'
        "시·도를 선택하세요</div>",
        unsafe_allow_html=True,
    )
    sido_list = list(DB.keys())
    sido_cols = st.columns(len(sido_list))
    for col, sn in zip(sido_cols, sido_list):
        sd = DB[sn]
        is_sel = sido == sn
        bg  = "#0f2d52" if is_sel else "#fff"
        bdr = "1.5px solid #1a56a0" if is_sel else "1px solid #dde5f0"
        tc  = "#fff" if is_sel else "#0f2d52"
        sc  = "rgba(255,255,255,.6)" if is_sel else "#94a3b8"
        trc = "#a5f3c0" if is_sel else ("#2E7D32" if sd["popT"].startswith("+") else "#C62828")
        with col:
            st.markdown(
                '<div style="background:{bg};border:{bdr};border-radius:8px;'
                'padding:11px 8px;text-align:center;margin-bottom:4px">'
                '<div style="font-size:14px;font-weight:700;color:{tc}">{sn}</div>'
                '<div style="font-size:11px;color:{sc};margin-top:2px">인구 {pop}</div>'
                '<div style="font-size:11px;color:{trc};margin-top:3px">{popT}</div>'
                "</div>".format(
                    bg=bg, bdr=bdr, tc=tc, sn=sn,
                    sc=sc, pop=sd["pop"], trc=trc, popT=sd["popT"]
                ),
                unsafe_allow_html=True,
            )
            btn_key = "sido_btn_{}".format(sn)
            btn_type = "primary" if is_sel else "secondary"
            if st.button("✓" if is_sel else "선택", key=btn_key,
                         use_container_width=True, type=btn_type):
                set_sido(sn)
                st.rerun()

    if not sido:
        st.stop()

    # 시·도 상세
    st.divider()
    sd = DB[sido]
    render_metrics({
        "pop": sd["pop"], "popT": sd["popT"],
        "retail": sd["retail"], "retailT": sd["retailT"],
        "spend": sd["spend"], "grdp": sd.get("grdp", "—"),
    })
    render_tags(sd["tags"])
    fc1, fc2 = st.columns(2)
    with fc1:
        render_rank(sd["food"], "인기 맛집·소비 트렌드")
    with fc2:
        render_rank(sd["trend"], "급상승 검색어")
    st.markdown("**행정구별 소매판매지수**")
    render_gu_bar(sido)
    st.divider()

    # ── LEVEL 2 : 행정구 ─────────────────────────────────────────────────────
    st.markdown(
        '<div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:8px">'
        "행정구·군을 선택하세요</div>",
        unsafe_allow_html=True,
    )
    gu_list = list(sd["districts"].keys())
    gu_cols = st.columns(len(gu_list))
    for col, gn in zip(gu_cols, gu_list):
        gd = sd["districts"][gn]
        is_sel = gu == gn
        bg  = "#1a4a8a" if is_sel else "#f7f9fc"
        bdr = "1.5px solid #2e7dd4" if is_sel else "1px solid #dde5f0"
        tc  = "#fff" if is_sel else "#0f2d52"
        sc  = "rgba(255,255,255,.6)" if is_sel else "#94a3b8"
        trc = "#a5f3c0" if is_sel else ("#2E7D32" if gd["popT"].startswith("+") else "#C62828")
        with col:
            st.markdown(
                '<div style="background:{bg};border:{bdr};border-radius:8px;'
                'padding:10px 8px;text-align:center;margin-bottom:4px">'
                '<div style="font-size:13px;font-weight:700;color:{tc}">{gn}</div>'
                '<div style="font-size:11px;color:{sc}">인구 {pop}</div>'
                '<div style="font-size:11px;color:{trc};margin-top:2px">{popT}</div>'
                "</div>".format(
                    bg=bg, bdr=bdr, tc=tc, gn=gn,
                    sc=sc, pop=gd["pop"], trc=trc, popT=gd["popT"]
                ),
                unsafe_allow_html=True,
            )
            btn_key = "gu_btn_{}".format(gn)
            btn_type = "primary" if is_sel else "secondary"
            if st.button("✓" if is_sel else "선택", key=btn_key,
                         use_container_width=True, type=btn_type):
                set_gu(gn)
                st.rerun()

    if not gu:
        st.stop()

    # 행정구 상세
    st.divider()
    gd = sd["districts"][gu]
    hc1, hc2 = st.columns([8, 1])
    with hc1:
        st.markdown("#### {} 상세 현황".format(gu))
    with hc2:
        if st.button("← 뒤로", key="bk_gu"):
            st.session_state["gu"] = None
            st.session_state["dong"] = None
            st.rerun()
    render_metrics({
        "pop": gd["pop"], "popT": gd["popT"],
        "retail": gd["retail"], "retailT": gd["retailT"],
        "spend": gd["spend"], "grdp": gd.get("grdp", "—"),
    })
    render_tags(gd["tags"])
    fc1, fc2 = st.columns(2)
    with fc1:
        render_rank(gd["food"], "인기 맛집·소비 트렌드")
    with fc2:
        render_rank(gd["trend"], "급상승 검색어")
    st.markdown("**소매판매지수 추이**")
    render_retail_chart(gd["retail"], hash(gu))
    st.divider()

    # ── LEVEL 3 : 행정동 ─────────────────────────────────────────────────────
    dong_list = gd["dongs"]
    st.markdown(
        '<div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:8px">'
        "행정동 목록 — {} ({}개동) · ▶ 클릭하여 상세 분석</div>".format(gu, len(dong_list)),
        unsafe_allow_html=True,
    )
    cols_per_row = 5
    for row_start in range(0, len(dong_list), cols_per_row):
        row_items = dong_list[row_start: row_start + cols_per_row]
        dcols = st.columns(cols_per_row)
        for col, dk in zip(dcols, row_items):
            dong_name = dk["n"]
            is_sel = dong == dong_name
            if is_sel:
                bg, bdr = "#e8f2fd", "#1a56a0"
            elif dk["hot"]:
                bg, bdr = "#fff8ed", "#e08020"
            elif dk["rise"]:
                bg, bdr = "#e6f4ec", "#1b6e3a"
            else:
                bg, bdr = "#f7f9fc", "#dde5f0"
            badge_html = ""
            if dk.get("badge"):
                badge_bg = "#fff4e0" if dk["hot"] else "#e6f4ec"
                badge_color = "#c45900" if dk["hot"] else "#1b6e3a"
                badge_html = (
                    '<br><span style="font-size:10px;padding:1px 6px;border-radius:20px;'
                    'background:{};color:{};font-weight:600">{}</span>'
                ).format(badge_bg, badge_color, dk["badge"])
            with col:
                st.markdown(
                    '<div style="background:{bg};border:1.5px solid {bdr};border-radius:8px;'
                    'padding:9px 6px;text-align:center;margin-bottom:4px">'
                    '<div style="font-size:12px;font-weight:{fw};color:#0f2d52">{name}</div>'
                    '<div style="font-size:10px;color:#94a3b8;margin-top:2px">{pop}</div>'
                    "{badge}</div>".format(
                        bg=bg, bdr=bdr,
                        fw="700" if is_sel else "600",
                        name=dong_name,
                        pop=dk["pop"],
                        badge=badge_html,
                    ),
                    unsafe_allow_html=True,
                )
                btn_key = "dk_btn_{}".format(dong_name)
                btn_type = "primary" if is_sel else "secondary"
                if st.button("▶", key=btn_key, use_container_width=True, type=btn_type):
                    set_dong(dong_name)
                    st.rerun()

    if not dong:
        st.stop()

    # 행정동 상세
    st.divider()
    dd = gd.get("dong_detail", {}).get(dong)
    dh1, dh2 = st.columns([8, 1])
    with dh1:
        st.markdown("#### {} 상세 분석".format(dong))
    with dh2:
        if st.button("← 뒤로", key="bk_dong"):
            st.session_state["dong"] = None
            st.rerun()

    if dd:
        mc1, mc2, mc3, mc4 = st.columns(4)
        with mc1: st.metric("총 인구", dd["pop"], dd["popT"])
        with mc2: st.metric("1인당 월 소비지출", dd["spend"])
        with mc3: st.metric("외국인 비율", dd["foreign"])
        with mc4: st.metric("소매판매지수", str(dd["retail"]))
        render_tags(dd["tags"])
        ac1, ac2 = st.columns(2)
        with ac1:
            st.markdown("**연령대별 인구 분포**")
            render_age_chart(dd["age"], dd["ageLbl"])
        with ac2:
            st.markdown("**소매판매지수 추이**")
            render_retail_chart(dd["retail"], hash(dong))
        fc1, fc2 = st.columns(2)
        with fc1:
            render_rank(dd["trend"], "급상승 검색 키워드")
        with fc2:
            render_rank(dd["food"], "인기 맛집·소비 업종")
        st.markdown("**AI 종합 인사이트**")
        card_map = {"ib": "cb", "ig": "cg", "iamb": "ca", "ir": "cr"}
        for ic, icon, head, desc in dd["insights"]:
            card_cls = card_map.get(ic, "card")
            st.markdown(
                '<div class="card {}" style="padding:14px;margin-bottom:8px">'
                '<div class="irow">'
                '<div class="iicon {}">{}</div>'
                "<div>"
                '<div class="ih">{}</div>'
                '<div class="id">{}</div>'
                "</div></div></div>".format(card_cls, ic, icon, head, desc),
                unsafe_allow_html=True,
            )
    else:
        dk_info = next((d for d in dong_list if d["n"] == dong), {})
        st.metric("추정 인구", dk_info.get("pop", "—"))
        st.info(
            "이 행정동의 상세 데이터는 실제 시스템 구축 후 "
            "통계청 KOSIS API와 연동하여 자동 수집됩니다."
        )
