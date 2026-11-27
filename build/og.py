from PIL import Image, ImageDraw, ImageFont
import math, sys
W,H=1200,630; out=sys.argv[1]
mask=Image.new('L',(W,H),0); d=ImageDraw.Draw(mask)
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
mono='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
lines=['Michelle','Yun']; fs=300
while True:
    f=ImageFont.truetype(bold,fs)
    if max(d.textlength(l,font=f) for l in lines)<=W-140: break
    fs-=5
y=50
for l in lines:
    bb=d.textbbox((0,0),l,font=f); d.text((70-bb[0],y-bb[1]),l,font=f,fill=255); y+=(bb[3]-bb[1])+40
img=Image.new('RGB',(W,H),'#fafaf8'); g=ImageDraw.Draw(img)
cs=13; mf=ImageFont.truetype(mono,cs); cw=mf.getlength('0'); CH=' .,:;-=+*#%@'
cols=int(W//cw); rows=H//cs
for r in range(rows):
    for c in range(cols):
        x=c*cw+cw/2; yy=r*cs+cs/2
        v=mask.getpixel((min(W-1,int(x)),min(H-1,int(yy))))/255
        if v>0.5: ch=CH[9+int(2*(0.5+0.5*math.sin(x*.05+yy*.03)))]; col='#141414'
        else: ch=CH[1+int(1.6*(0.5+0.5*math.sin(x*.02+yy*.04)))]; col='#c4c0b6'
        if ch!=' ': g.text((c*cw,r*cs),ch,font=mf,fill=col)
g.text((W-70,H-48),'Solutions Engineer · Chicago',font=ImageFont.truetype(mono,22),fill='#6b6964',anchor='rs')
img.save(out,optimize=True)
