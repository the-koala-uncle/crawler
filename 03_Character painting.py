

from PIL import Image
import os

road=os.getcwd()    #获取当前工作目录
os.chdir(road)    #切换目录
WIDTH=80
HEIGHT=80

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

inn=input('放在同一目录下的图片名(如a.jpg),填写：')
im=Image.open(inn)


im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
txt = ""

for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'
print(txt)

with open('output.txt','w') as f:
    f.write(txt)

'''
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                .......  ..       ..'     .                                     
                .    ......     .  ..  ..                                       
                .    ......     .  .......                                      
                .`^ . . '       ...''' ...                      ...             
                .'.<<!<i"..     . .'... .                                       
                u0OQLCL0X-`     ...`vji .                                       
     ... .. ^.udmc. ;`))vhn'`.... '.zM0YLO''.. .  ...      .....                
     .......^w8J|.''''. .xWt`.....[1\Lk" YbZCx}......                           
     .. .'.^kpt ... .   `'|oj..'."Q&op#Zx. vk8#``.` .                           
     .  ."u&Z".......   . 'ud|.'.`^*q nJdQ'.vdpqd'..       .                    
      . 'Ybu . '. .....   '.QZI)nwpap.`'cw0".vJxJp'.       ..                   
     . .?aU?               `jkLd#Lj       .  '  |Zz'.......^^:'`'.'..           
      .'zd,                 tpaO/....       '` ' vm. .' .`}xLO0mm[^..           
     . lw*Y`.              JpC{^ .'..   .. .`  ..'Q`...^jJLxx  vJpzi.           
.    '.Ipkn '         . .fohj` ...  .           '.)C.^lCZj .'....t0k`           
.    .:dZ`..          ..x#J'   '.   .           . .(pcQn   .     '|Zc .'        
.    iZJ         . `  .vbv.                         (*0/  '     . .(Xz.`...     
.  .;CU          . .]'z#n`                          .npU ..       ..\Yx`  .     
. .^QBp   .     ..`<' kc  .                         `'nhr       . ...tQ}...     
. .]aqm,          !``QL'       .''                     qb .       ...'fO.;.     
   .}Qt  .      '~  fkf        .( '                    'h0        ..  \w`..     
  .^QQ  ..      ?".<#u..     . (m.                      jaj     .. ...^{k.'     
...|q/^.       _^. wZ     .'  (hY:'                      wn          ' 1YC^     
...0n'`        l..}#nB@B%o*bqbBpcfv"`         n         .cd          .  jm.     
'.`a'        `}.. CCp$$$$$$$$$$$$$$O.. .      mr`. ..   `fb ~.       ..\Yb.     
 '.k.        ^> .>m $$$$$$$$$$$$$$$M         Qb0" . '   ''d| <'      . X@w`     
'.^h.        .,  /Z^$$$$$$$$$$$$$$$@^       dB@@0       . XX."`.     . :Ob'     
...b'  '. .   ? .v' $$$$$$$$$$$$$$$$aoomn( Z$$$$$8qj   `  'a. +      . .{Oj. .  
. .wL  '      .:lp' $$$$$$$$$$$$$$$$$$$$B$M@$$$$$$$$oUr'".'&,`l      ....mU''.  
. .jaC .. .   .+>q/x$$$$$$$$$$$$$$$BWMW&%8%$@$$$$$$$$$8hCv.w] ''     . ..rk+ .  
.. 'xdm}..    .'uZ. W$@$$$$$$$$$$$%uzkkk#8@$$$$$$$$$$$$$$WUCr  +     . ..O%\'   
.....)mk..   .. 0J  Q$$$$$$$$$$$@$Y:OkkkoWB$$$$$$$$$$$$$$BJ'Y  I      ...OMd'   
   .. `qz.' .. .hv'.)a$$$@$$$$$$@M]xkaaak#B$$$$$$$$$$$$$$$0.m          . Xcn..  
     ..|W  ... ^o`. .fa8$$$$$$$$@drbaaaah*B$$$$$$$$$$$$$$Bc.Z.         ..xz`..  
       ^JoqULQ ^M   .'fC#$$$$$8WBahahaaaaoW@$$$$$$$$$$$$@af Z          ..xJ;.  .
        ^-/nxQ(uh.    .'\c0O0XtkMaaaaaaaa*W@$$$$$$$$$$$$@Y .0  .       .^ ZI.. .
        .. .'tJLO.    .       .W*akhaaaaa*W$*$$$$$$$$@$Bp ..X">        . :OI....
         .'..]Lhu'    .  `   'XWakhaaaaaa*W$co$$$$$$$$8Q|. Cjl .       . .Zl ...
.          ..`wO,            .X*hhaaaaaaao&$'jd$$@BB$Mv    wn"''  ...''.^nJl.   
.          ...br"^           .cMhaoaaahaa#&@. (nOo#dY` " ..kz  .     .  {Jn:    
           ...Or              n#o*haaahaoM&&'             '8    .  . '.jLZ!.   .
           ..`df             '.Z%okkaahaoM%m.           .  8.   . .  .`qCI.     
           ...df              "^m%&akahaoW&u.              k    . . k0J.. '. .. 
            ..qx' . .            uo&&#*W8WY,^           ..CC.Lqx.'`qQ           
           ...Qw ''             ^``JmpqqC\  .           . 0CmmUddZZU^           
           . .^*c'                ..     ''.            ..UMX.'..^..'           
           ..'.Ubf...               . '                  `|*].. '....           
            .'._rZ...            pbkh'^                 '  #?..... ..           
                !Zv  ..   .         rhY"             .....zw. ..                
                .}mn               ' ck              ..  \Zf....                
                .^thj  ..            \j.             ...`Xz^^...                
                .'`\&j'.^ .                          '..Cd_...                  
                 .."fqCbk0n.                         '(jp-.  ..                 
                ...'^0d.  L                          \LCf'.. . .                
                  . ^Q....pt.''            .. .. ''"xkui ..                     
                  .. Z.  ^ac' '.............    '..cav`..                       
           ..     ...w'  .k%hYx. '' `     ..'   jYZp{.   ..                     
                  .. q.   JQM *k0 .^^  . .  vvXLdC... .   .                     
                  .. q .^0u.q   ..apaodqqpq*hhJf).  .  ....                     
     .          . .''p. .Cm. &&^...^"`.. . u.ZC.           ..                   
     .          . ..^0.`".qO.aZ......^. *Mn"..U'                                
     .          . ...v..^'..nO`*... owJYm `. cX                                 
               .. ...^vw.`^.j.,kM.^.w.  .....YC.        .                       
               .. .. '.fk...tO 1*..&\... ..`'aY.        .                       
        .            ...1Z''fQ' W#*kpvxj/'jzbax'.....                           
        .            ...'q.^^Cv #O(^\ChwCCp'.'r" . ..                           
        .            ...^Z.` fd'. ..^L  .`  '.x"   ..                           
        .            ...`L'. .(pL\.Qp^''... .'qt... .        ...       .        
        .            ...`Q'.    '.^^' ''.     QoU....                  .        
        .            ...^m..   ..  . XUXnr. ...U#`'.                   .        
          .          ...'m. .'   QhLY..\jm....' a...                            
          .          ...`L... `xhc`  ' .!Zc....'u. ..                           
          .           ..`L... cJi.  ....;Cu. .`C....              .             
          .          ....nz`'mY' ... .   {CQObJ:. ..              .             
          .          ....'c0L|  . .. .  ..^..'`.  .               .             

'''

