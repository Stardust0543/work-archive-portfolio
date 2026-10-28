"""Generate the anonymized portfolio. Requires reportlab and the bundled OFL font."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

ROOT = Path(__file__).resolve().parent.parent
pdfmetrics.registerFont(TTFont('KR', str(ROOT/'scripts/fonts/NotoSansKR-Regular.ttf')))
OUT = ROOT/'dist/assets/work-archive.pdf'
pdfmetrics.registerFont(TTFont('SerifItalic', str(ROOT/'scripts/fonts/DejaVuSerif-Italic.ttf')))
C = canvas.Canvas(str(OUT), pagesize=(595.28,841.89))
C.setTitle('Work Archive - 경영관리 포트폴리오')
C.setAuthor('Work Archive')
C.setSubject('개인정보를 제외한 이력서 기반 포트폴리오')
INK=HexColor('#20211e'); MUTED=HexColor('#65685e'); LINE=HexColor('#cecec6'); PEACH=HexColor('#f4c8a8')
W,H=595.28,841.89
def text(x,y,s,size=10,font='KR',color=INK):
 font = {'Helvetica':'KR','Helvetica-Bold':'KR','Times-Italic':'SerifItalic'}.get(font,font)
 C.setFillColor(color);C.setFont(font,size);C.drawString(x,y,s)
def para(s,x,y,width=475,size=10,leading=18,color=MUTED):
 st=ParagraphStyle('body',fontName='KR',fontSize=size,leading=leading,textColor=color,wordWrap='CJK')
 p=Paragraph(s,st);w,h=p.wrap(width,700);p.drawOn(C,x,y-h);return y-h
def line(y):
 C.setStrokeColor(LINE);C.setLineWidth(.5);C.line(50,y,W-50,y)
def page(n,label):
 C.setFillColor(HexColor('#f7f7f2'));C.rect(0,0,W,H,fill=1,stroke=0)
 text(50,796,'work archive.',15,'Helvetica-Bold')
 text(387,797,'RESUME-BASED PORTFOLIO',7,'Helvetica',MUTED)
 line(776);text(50,749,label,8,'Helvetica');
 line(45);text(50,29,'개인정보 비공개 | 이력서 기준 2026.08.21',7,color=MUTED)
 text(501,29,f'{n:02d} / 03',7,'Helvetica',MUTED)
def heading(y,tag,title):
 text(50,y,tag,8,'Helvetica',MUTED);text(50,y-29,title,18);return y-51

page(1,'01 / PROFILE, ABOUT & SKILLS')
C.setFillColor(PEACH);C.circle(465,662,63,fill=1,stroke=0)
C.setStrokeColor(LINE);C.circle(493,641,55,fill=0,stroke=1)
text(47,667,'Behind',66,'Helvetica')
text(48,601,'the work.',72,'Times-Italic')
text(50,548,'숫자로 정리하고, 일의 흐름을 잇다.',21)
y=para('회계·세무에서 인사·총무, 도서 기획·제작까지.<br/>기업의 경영관리와 출판의 기획·제작을 경험했습니다.',50,518,size=10.5,leading=19)
text(50,425,'23',56,'Helvetica');text(118,427,'년',13);text(146,425,'8',56,'Helvetica');text(181,427,'개월',13)
text(50,401,'이력서에 기재된 총 경력',8,color=MUTED)
text(330,445,'EDUCATION',8,'Helvetica',MUTED);text(330,424,'회계학 전공 · 학사',11)
line(377)
y=heading(354,'PRACTICAL SKILLS','실무와 도구의 경험')
skills=[('회계·세무','월차·연차 결산, 손익분석, 전표 검토, 회계감사 대응, 세무 신고, 세무조정 부속명세 작성'),('경영관리','자금일보, 사업계획, 예산 수립 업무 참여, 주주총회, 전자공시, 내부회계관리제도, 계약서 관리'),('인사·총무','채용·퇴직, 평가보상, 자산·기기·이전 관리, 인사평가시스템 도입 TF 참여'),('도서 기획·제작','기획안 작성, 저자 섭외·미팅, 원고 교정 검토, 용지·제작 발주, 제작물 검수')]
for title,body in skills:
 text(50,y,title,10);end=para(body,166,y+3,width=378,size=8.5,leading=15);y=min(y-44,end-14)
line(y+6)
y=para('OneWorld / Top ERP / 더존 NeoPlus·NeoPlus2 / ERP M3 / iCUBE<br/>문서작성 · 스프레드시트 · 프레젠테이션 · AI를 활용한 업무 능력 확장',50,y-8,size=8,leading=16)
C.showPage()

page(2,'02 / CAREER')
text(50,682,'Different fields.',43,'Helvetica')
text(50,632,'One thread.',48,'Times-Italic')
text(50,591,'회계에서 경영관리로, 그리고 출판으로.',13)
careers=[('2020.09 - 2026.06','출판사 · 회사명 비공개','팀장','회계·자금·세무·인사·총무 등 관리업무 전반, 도서 개발·제작','도서 기획안 작성, 저자 섭외·미팅, 원고 교정 검토<br/>제작 사양에 따른 용지·제작 발주와 검수'),('2008.12 - 2020.04','메가스터디주식회사','차장','회계·인사·총무·기획·자금 등 관리업무 전반','결산·손익분석·회계감사·세무 신고·자금 관리<br/>사업계획·주주총회, iCUBE 도입·운영, 내부회계관리제도<br/>계약서 관리, 채용·퇴직·평가보상, 자산·기기·이전 관리'),('2005.10 - 2008.06','에스와이(주)','대리','회계·세무·공시·ERP','결산·실적분석·회계감사, 세무 신고·소명자료 제출<br/>ERP M3 도입·운영, 내부회계관리제도 구축<br/>자금일보·신용조사 작성, 전자공시, 대외조사 수감'),('2001.01 - 2004.08','(주)두산','사원','회계·세무, 실적분석·예산 수립 업무 참여','결산·전표 점검·회계감사, 국세·지방세 신고<br/>OneWorld 사용, 인사평가시스템 도입 TF 참여<br/>대외조사 수감, 매출채권관리')]
y=551
for period,company,role,summary,body in careers:
 line(y);text(50,y-21,period,8,'Helvetica',MUTED)
 text(205,y-24,company,14);text(508,y-23,role,8,color=MUTED)
 end=para(summary+'<br/>'+body,205,y-38,width=340,size=8.5,leading=15)
 y=end-22
C.showPage()

page(3,'03 / SELECTED EXPERIENCE & CONTACT')
text(50,684,'Selected',45,'Helvetica')
text(50,634,'experience.',50,'Times-Italic')
para('이력서에 기재된 업무 경험을 프로젝트 형식으로 정리했습니다.<br/>아래 기간은 프로젝트 진행기간이 아닌 재직기간입니다.',50,601,size=9,leading=17)
projects=[('01','더존 ERP M3 도입과 운영','에스와이(주) / 2005.10 - 2008.06 / 대리','더존 ERP M3 도입·운영. 소프트파워 Top ERP, 더존 NeoPlus2 사용. 결산·실적분석·회계전표 점검·회계감사 수감.'),('02','iCUBE 도입·운영과 경영관리 실무','메가스터디주식회사 / 2008.12 - 2020.04 / 차장','더존 NeoPlus 운영, iCUBE 도입·운영. 결산·회계감사·세무·자금 실무와 사업계획·주주총회, 인사·총무·계약서 관리.'),('03','내부회계관리제도 구축 경험','에스와이(주) / 2005.10 - 2008.06 / 대리','내부회계관리제도 구축, 전자공시, 대외조사 수감. 관련 업무로 결산·실적분석·회계감사, 세무 신고와 소명자료 제출 수행.'),('04','기획에서 제작까지, 한 권의 과정','출판사 · 회사명 비공개 / 2020.09 - 2026.06 / 팀장','기획안 작성, 저자 섭외·미팅, 원고 교정 검토. 제작 사양에 따른 용지·제작 발주와 검수. 회계·자금·세무·인사·총무 관리업무 병행.')]
y=545
for number,title,meta,body in projects:
 line(y);text(50,y-24,number,10,'Helvetica',MUTED);text(87,y-24,title,14)
 text(87,y-44,meta,8,color=MUTED)
 end=para(body,87,y-57,width=458,size=8.5,leading=15);y=end-21
line(y)
text(50,y-26,'CONTACT',8,'Helvetica',MUTED)
para('연락처 비공개<br/>이름·사진·생년·주소·전화·이메일을 포함하지 않았습니다.',50,y-40,size=9,leading=17)
C.save()
print(f'Created {OUT}')
