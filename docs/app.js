'use strict';
const projects = [
 {id:'m3',number:'01',category:'SYSTEM / ERP',title:'더존 ERP M3 도입과 운영',summary:'회계·세무·공시 업무를 담당하며 더존 ERP M3의 도입과 운영을 수행했습니다.',employer:'에스와이(주)',period:'2005.10 — 2008.06',role:'대리',sections:[{title:'담당 업무',items:['더존 ERP M3 도입·운영','소프트파워 Top ERP, 더존 NeoPlus2 사용','결산 및 실적분석, 회계전표 점검, 회계감사 수감']},{title:'함께 수행한 업무',text:'국세·지방세 신고, 세무조정 부속명세 작성, 자금일보·신용조사 작성, 전자공시와 대외조사 수감 업무를 담당했습니다.'}]},
 {id:'icube',number:'02',category:'SYSTEM / MANAGEMENT',title:'iCUBE 도입·운영과 경영관리 실무',summary:'회계·인사·총무·기획·자금 등 관리업무 전반을 담당하며 더존 iCUBE를 도입·운영했습니다.',employer:'메가스터디주식회사',period:'2008.12 — 2020.04',role:'차장',sections:[{title:'시스템과 회계 업무',items:['더존 NeoPlus 운영 및 iCUBE 도입·운영','월차결산, 손익분석, 결산, 전표 검토','회계감사, 재무제표·결산보고서 작성']},{title:'경영관리 업무',items:['세무 신고, 세무조정 부속명세 작성, 소명자료 제출','자금일보와 은행 제출 자료 작성, 사업계획·주주총회','내부회계관리제도, 계약서 관리, 채용·퇴직·평가보상','자산·기기 관리 및 사무실 이전']}]},
 {id:'control',number:'03',category:'ACCOUNTING / CONTROL',title:'내부회계관리제도 구축 경험',summary:'에스와이(주) 재직 중 내부회계관리제도 구축 업무를 수행했습니다.',employer:'에스와이(주)',period:'2005.10 — 2008.06',role:'대리',sections:[{title:'이력서에 기재된 경험',items:['내부회계관리제도 구축','전자공시','대외조사 수감']},{title:'관련 회계·세무 실무',text:'결산 및 실적분석, 회계전표 점검, 회계감사 수감과 국세·지방세 신고, 세무조정 부속명세 작성, 소명자료 제출 업무를 담당했습니다.'}]},
 {id:'publishing',number:'04',category:'EDITORIAL / PRODUCTION',title:'기획에서 제작까지, 한 권의 과정',summary:'출판사의 관리업무와 함께 도서 개발·기획·제작을 담당했습니다.',employer:'출판사 · 회사명 비공개',period:'2020.09 — 2026.06',role:'팀장',sections:[{title:'기획과 원고',items:['도서 기획안 작성','저자 섭외 및 미팅','원고 교정 검토']},{title:'제작과 검수',items:['제작 사양에 따른 용지 발주','제작 발주','제작물 검수']},{title:'함께 수행한 업무',text:'회계·자금·세무·인사·총무 등 관리업무 전반을 담당했습니다.'}]}
];
const $ = s => document.querySelector(s);
const menuButton = $('.menu-toggle');
const nav = $('.nav');
function closeMenu(){menuButton.setAttribute('aria-expanded','false');menuButton.setAttribute('aria-label','메뉴 열기');nav.classList.remove('is-open')}
menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));menuButton.setAttribute('aria-label',open?'메뉴 닫기':'메뉴 열기');nav.classList.toggle('is-open',open)});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('click',e=>{if(!$('.header').contains(e.target))closeMenu()});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});
window.matchMedia('(min-width:761px)').addEventListener('change',e=>{if(e.matches)closeMenu()});

if('IntersectionObserver' in window){
 const reducedMotion=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
 if(!reducedMotion){document.body.classList.add('motion-ready');const reveals=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');reveals.unobserve(entry.target)}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(el=>reveals.observe(el))}
 const sections=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){nav.querySelectorAll('a').forEach(a=>{if(a.hash==='#'+entry.target.id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})}})},{rootMargin:'-15% 0px -65% 0px',threshold:0});
 document.querySelectorAll('main>section').forEach(section=>sections.observe(section));
}
let progressQueued=false;
function updateProgress(){const max=document.documentElement.scrollHeight-window.innerHeight;$('.scroll-progress').style.transform=`scaleX(${max>0?window.scrollY/max:0})`;progressQueued=false}
window.addEventListener('scroll',()=>{if(!progressQueued){progressQueued=true;requestAnimationFrame(updateProgress)}},{passive:true});window.addEventListener('resize',updateProgress);updateProgress();

let activeProject=0;
const projectDialog=$('#project-dialog');
function renderProject(index){activeProject=index;const p=projects[index];$('#project-eyebrow').textContent=p.category;$('#project-number').textContent=p.number+' / 04';$('#project-title').textContent=p.title;$('#project-summary').textContent=p.summary;$('#project-employer').textContent=p.employer;$('#project-period').textContent=p.period;$('#project-role').textContent=p.role;
 const details=$('#project-details');details.replaceChildren();p.sections.forEach(section=>{const heading=document.createElement('h3');heading.textContent=section.title;details.append(heading);if(section.items){const ul=document.createElement('ul');section.items.forEach(item=>{const li=document.createElement('li');li.textContent=item;ul.append(li)});details.append(ul)}else{const paragraph=document.createElement('p');paragraph.textContent=section.text;details.append(paragraph)}});
 $('#project-prev').disabled=index===0;$('#project-next').disabled=index===projects.length-1;projectDialog.scrollTop=0;
}
document.querySelectorAll('[data-project]').forEach(button=>button.addEventListener('click',()=>{renderProject(projects.findIndex(p=>p.id===button.dataset.project));projectDialog.showModal();document.body.classList.add('modal-open')}));
$('#project-prev').addEventListener('click',()=>{if(activeProject>0)renderProject(activeProject-1)});
$('#project-next').addEventListener('click',()=>{if(activeProject<projects.length-1)renderProject(activeProject+1)});
const contactDialog=$('#contact-dialog');
$('#contact-open').addEventListener('click',()=>{contactDialog.showModal();document.body.classList.add('modal-open')});
document.querySelectorAll('dialog').forEach(dialog=>{
 dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());
 dialog.addEventListener('close',()=>document.body.classList.remove('modal-open'));
 dialog.addEventListener('click',e=>{if(e.target===dialog){const rect=dialog.getBoundingClientRect();if(e.clientX<rect.left||e.clientX>rect.right||e.clientY<rect.top||e.clientY>rect.bottom)dialog.close()}});
});
let toastTimeout;
function toast(message){const el=$('.toast');el.textContent=message;el.classList.add('visible');clearTimeout(toastTimeout);toastTimeout=setTimeout(()=>el.classList.remove('visible'),4000)}
$('#contact-form').addEventListener('submit',async e=>{e.preventDefault();const message=$('#message').value.trim();if(!message){$('#message').setCustomValidity('문의 내용을 입력해주세요.');$('#message').reportValidity();return}$('#message').setCustomValidity('');const draft=`[${$('#subject').value}]\n\n${message}`;try{await navigator.clipboard.writeText(draft);$('.copy-fallback').hidden=true;toast('문의 초안을 복사했습니다.')}catch{const output=$('#draft-output');output.value=draft;$('.copy-fallback').hidden=false;output.focus();output.select();toast('초안을 선택한 뒤 복사해주세요.')}});
$('#message').addEventListener('input',()=>$('#message').setCustomValidity(''));
document.querySelectorAll('[data-pdf]').forEach(link=>link.addEventListener('click',()=>toast('개인정보를 제외한 PDF를 저장합니다.')));
