from pathlib import Path
from html import escape
import math
s=[]
def add(v):s.append(v)
def text(x,y,t,size=20,fill='#14575f',extra=''):
 add(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" {extra}>{escape(t)}</text>')
def palm(x,y,scale=1,flip=1):
 add(f'<g transform="translate({x} {y}) scale({scale*flip} {scale})"><path d="M0 180Q25 75 0 0" fill="none" stroke="#b3794b" stroke-width="16"/><path d="M2 1Q-74-80-140-20Q-64-36 2 1M2 1Q-22-103-83-103Q-35-71 2 1M2 1Q56-103 115-65Q53-64 2 1M2 1Q102-35 136 31Q64-5 2 1M2 1Q-89-19-113 58Q-56 12 2 1M2 1Q44-27 65 57Q26 16 2 1" fill="#278b67"/><circle cx="0" cy="9" r="9" fill="#8b6348"/></g>')
add('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1740" viewBox="0 0 1200 1740" role="img" aria-labelledby="title desc"><title id="title">Aloha, I'm Hawaii — tropical developer profile</title><desc id="desc">One continuous sunny Hawaiian beach poster with an ocean, palms, development skills, and a friendly invitation to connect.</desc><defs><linearGradient id="sky" x2="0" y2="1"><stop stop-color="#b8eef0"/><stop offset="1" stop-color="#e5faf3"/></linearGradient><linearGradient id="sea" x2="0" y2="1"><stop stop-color="#25b6c5"/><stop offset="1" stop-color="#8ee1d1"/></linearGradient><linearGradient id="sand" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="1740"><stop stop-color="#fff6df"/><stop offset="1" stop-color="#f9e5be"/></linearGradient><pattern id="grain" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="3" cy="4" r=".6" fill="#b39162" opacity=".13"/><circle cx="13" cy="12" r=".6" fill="#b39162" opacity=".12"/></pattern><clipPath id="page"><rect width="1200" height="1740" rx="28"/></clipPath></defs><g clip-path="url(#page)" font-family="Arial,Helvetica,sans-serif"><rect width="1200" height="1740" fill="url(#sand)"/><rect width="1200" height="650" fill="url(#sky)"/>
<circle cx="930" cy="163" r="103" fill="#fff5ce" opacity=".5"/><circle cx="930" cy="163" r="77" fill="#ffd37d"/>
<path d="M0 375Q160 330 300 365T600 365T900 359T1200 367V680H0Z" fill="url(#sea)"/>
<path d="M700 375Q830 222 924 361Q1000 280 1100 375" fill="#54a99a"/>
<path d="M700 375Q815 285 861 308L924 361Q1000 304 1100 375" fill="#389c91"/>
<path d="M0 460Q200 420 430 475T870 465T1250 460" fill="none" stroke="#d6fff4" stroke-width="3" opacity=".7"/>
<path d="M-20 562Q200 505 430 565T850 566T1220 542V730H-20Z" fill="#d7f9e9"/>
<path d="M-20 591Q200 534 430 594T850 595T1220 571V750H-20Z" fill="url(#sand)"/>
<path d="M-20 580Q200 523 430 583T850 584T1220 560" fill="none" stroke="#fffdf0" stroke-width="11"/>
<path d="M64 419q18-18 36 0m2 0q18-18 36 0M619 160q13-15 26 0m1 0q13-15 26 0" fill="none" stroke="#227987" stroke-width="3" stroke-linecap="round"/>
<rect width="1200" height="1740" fill="url(#grain)"/>
''')
palm(1120,291,.96,-1)
text(64,61,'THE HAWAII EDITION',13,extra='letter-spacing="4" font-weight="700"')
text(1136,61,'EST. / BUTTERCAT007',12,extra='text-anchor="end" letter-spacing="2"')
text(62,157,"Aloha, I'm",37)
text(53,285,'HAWAII.',139,'#095e69','font-weight="900" letter-spacing="-5"')
text(68,329,'A LITTLE SUNSHINE. A LOT OF CURIOSITY.',17,'#176772','letter-spacing="2" font-weight="700"')
add('<rect x="65" y="365" width="391" height="49" rx="24" fill="#fffaf0"/>')
text(87,396,'CODE  /  CREATE  /  CATCH THE NEXT WAVE',13,'#1c7375','font-weight="700" letter-spacing="1"')
# A small surfboard in the shallows.
add('<g transform="translate(910 492) rotate(22)"><ellipse rx="29" ry="88" fill="#fff4d8" stroke="#e9c79c" stroke-width="2"/><path d="M-10-80V80H10V-80" fill="#ef977c"/><path d="M0-86V86" stroke="#fff7e9" stroke-width="3"/></g>')
text(65,655,'01 / THE ISLAND TOOLKIT',13,'#a3633d','font-weight="700" letter-spacing="3"')
text(62,708,'Good tools. Fresh ideas.',46,'#14575f','font-weight="700" letter-spacing="-1"')
text(65,745,'The languages, frameworks & companions in my creative beach bag.',20,'#627972')
rows=[('01','FRONTEND & INTERFACE',['HTML','CSS','JavaScript','TypeScript','React','Vue','Nuxt','Next.js','Tailwind','Bootstrap','Sass','Vite','Svelte','Astro']),('02','LANGUAGES',['JavaScript','TypeScript','Go','Python','PHP','C#','C','C++','Java','Rust','Dart','Bash','SQL']),('03','BACKEND & INFRASTRUCTURE',['Go','Node.js','Bun','Elysia','Express','NestJS','MySQL','PostgreSQL','Redis','MongoDB','Linux','Docker','Cloudflare']),('04','TOOLS & WORKFLOW',['Git','GitHub','Bitbucket','npm','pnpm','Yarn','VS Code','Atom','Postman','Figma','Vercel','Netlify','Discord'])]
for i,(n,title,items) in enumerate(rows):
 x=64+(i%2)*548;y=788+(i//2)*239
 add(f'<rect x="{x}" y="{y+5}" width="524" height="216" rx="20" fill="#d8bf96" opacity=".24"/><rect x="{x}" y="{y}" width="524" height="216" rx="20" fill="#fffdf3" stroke="#e4d8ba"/>')
 add(f'<circle cx="{x+34}" cy="{y+36}" r="16" fill="#e0f2e6"/>')
 text(x+34,y+40,n,11,'#2c7b6c','text-anchor="middle" font-weight="700"')
 text(x+62,y+41,title,13,'#276969','font-weight="700" letter-spacing="1"')
 xx=x+22;yy=y+68
 for item in items:
  w=max(77,len(item)*9+25)
  if xx+w>x+505:xx=x+22;yy+=47
  assert yy+35 <= y+207, f'Skills overflow: {title}'
  add(f'<rect x="{xx}" y="{yy}" width="{w}" height="35" rx="9" fill="#edf6ef"/>')
  text(xx+w/2,yy+23,item,15,'#306b66','text-anchor="middle"')
  xx+=w+9
text(65,1302,'02 / KEEP EXPLORING',13,'#a3633d','font-weight="700" letter-spacing="3"')
text(62,1354,'Made of code & ocean air.',43,'#14575f','font-weight="700" letter-spacing="-1"')
text(65,1394,'Explore the repos. Share an idea. Say aloha.',22,'#627972')
add('<path d="M0 1580Q200 1510 400 1580T800 1580T1200 1570V1740H0Z" fill="#b9e7d8"/><path d="M0 1610Q200 1540 400 1610T800 1610T1200 1600V1740H0Z" fill="#81ccc1"/>')
palm(1020,1422,.88)
add('<rect x="65" y="1434" width="636" height="70" rx="13" fill="#fffaf0" stroke="#e0cba6"/>')
text(88,1463,'FIND ME ON',11,'#a3633d','letter-spacing="2" font-weight="700"')
text(88,1488,'GitHub / buttercat007     ·     Discord / say aloha',17,'#215f62')
text(65,1686,'STAY CURIOUS. KEEP CREATING.',15,'#155e63','font-weight="700" letter-spacing="3"')
text(1135,1686,'ALOHA / 007',13,'#155e63','text-anchor="end" letter-spacing="3"')
add('</g></svg>')
Path('assets/hawaii-beach.svg').write_text(''.join(s))
