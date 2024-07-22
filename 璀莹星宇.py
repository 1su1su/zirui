'''我的主页'''
import streamlit as st
#from streamlit_drawable_canvas import st_canvas
from PIL import Image
import pandas as pd
#st(background_image = Image.open("宇宙.gif"))
import datetime
import base64
import streamlit as st


page = st.sidebar.radio('-首页-', ['宇宙的奥秘', '查询信息','时间记录','设置'])
ts_l=[]
tsl=[]
def page_1():
    '''宇宙的奥秘'''
    with open('Ashris、Speed Up Songs - Metamorphosis.mp3','rb') as f:
        mathm=f.read()
    st.audio(mathm,format='mp3',start_time=0)
    st.write("<span style='font-size:30px'>宇宙:</span>", unsafe_allow_html=True)
    st.write('----')
    st.image('宇宙图片2.jpg')
    st.write("<span style='font-size:20px'>简介:</span>", unsafe_allow_html=True)
    st.write('宇宙是广袤空间和其中存在的各种天体以及弥漫物质的总称。宇宙起源是一个极其复杂的问题。现代天文观测证明它处于不断的运动和发展中。千百年来，科学家们一直在探寻宇宙是什么时候、如何形成的。许多科学家认为，宇宙是由大约140亿年前发生的一次大爆炸形成的。')
    st.write("<span style='font-size:20px'>形成:</span>", unsafe_allow_html=True)
    st.write('参见:宇宙大爆炸')
    st.write('宇宙大爆炸是现代宇宙学中最有影响的一种学说。它的主要观点是认为宇宙曾有一段从热到冷的演化史。')
    st.write('在这个时期里，宇宙体系在不断地膨胀，使物质密度从密到稀地演化，如同一次规模巨大的爆炸。起初，无空间、时间，未知原因，空间开始暴涨式出现，振动使得物质诞生，这次大爆炸的反应原理被物理学家们称为量子物理。')
    st.write('大爆炸使空间扩张，宇宙空间不断膨胀，温度也相应下降，后来相继出现宇宙中的所有星系、恒星、行星乃至生命。')
    st.write('该理论的创始人之一是伽莫夫。1946年美国物理学家伽莫夫正式提出大爆炸理论，认为宇宙由大约140亿年前发生的一次大爆炸形成。上世纪末，对Ia超新星的观测显示，宇宙正在加速膨胀，因为宇宙可能大部分由暗能量组成。')
    st.write('最新的研究认为宇宙的直径为1560亿光年，甚至更大。')
    st.write('可观测的宇宙年龄大约为138.2亿年。')
    st.write("<span style='font-size:20px'>宇宙的成分:</span>", unsafe_allow_html=True)
    st.write('宇宙的23%由完全不知道起源的暗物质组成，73%由暗能量构成。')
    st.write('宇宙这一真实的存在表明它必然存在自身的组织成分以及基本面貌，近年国内学者利用数理方法提出了一个体现宇宙成分量及之基本面的表达式:量项维物基，描绘了以空间星分子原子粒子声热光磁电力运动为核心的事物体系在宇宙结构层所起的关建作用，显示以空间星分子原子粒子声热光磁电力运动为体系的产物是形成宇宙物质和时空存在的基本要素。')  
    st.image('宇宙图片1.jpg')
    pass

def page_2():
    '''一键查询'''
    global ts_l
    with open('Ashris、Speed Up Songs - Metamorphosis.mp3','rb') as f:
        mathm=f.read()
    st.audio(mathm,format='mp3',start_time=0)
    st.write("<span style='font-size:30px'>一键查询:</span>", unsafe_allow_html=True)
    st.write('----')
    #with open('check_out_times.txt','r',encoding='utf-8') as f:
    #    ts_l=f.read().split('\n')
    #for i in range(len(ts_l)):
    #    ts_l[i]=ts_l[i].split('#')
    #ts_d={}
    #for i in ts_l:
    #    ts_d[i[1]]=[int(i[0]),i[2]]
    word=st.text_input('请输入要查询的信息（目前仅支持恒星、星云、行星、卫星、小行星、彗星、流星、太阳系、类星体、黑洞、中子星）：')
    st.write('----')
    if word =='恒星':
        st.write('恒星：由炽热气体组成并且能够自己发光的球状或类球状天体就是恒星，我们每天肉眼可见的太阳就属于恒星，恒星也是最基本的天体。')
        st.image('太阳.jpg')
        T()
    elif word =='行星':
        st.write('行星：在椭圆轨道上环绕恒星运行的、近似球状的天体就是行星，行星质量比恒星小，自己不会发光，土星就是一颗行星。')
        st.image('行星.jpg')
        T()
    elif word =='卫星':
        st.write('卫星：环绕着行星运转的天体就是卫星，有天然卫星和人造卫星两种，我们常见的月亮就是天然卫星，人造卫星就是人类自己研发然后发射到宇宙中的。')
        T()    
    elif word =='星云':
        st.write('星云：由气体和尘埃组成的呈云雾状外表的天体，它的主要物质是氢，这就是星云，它属于最基本的天体')
        T()
    elif word=='小行星':
        st.write('小行星为微型行星的一种。以太阳系而言，小行星属于太阳系小天体（SSSB），和行星一样环绕太阳运动，但体积和质量比行星小得多。因此“小行星”一词更常被用于专指内太阳系非彗星的小天体。')
        st.write('广义的小行星大小介于流星体和矮行星之间，直径可从数米至1000公里不等，包括在这个尺寸下太阳系里非彗星的所有小天体。')
        st.write('但大部分的小行星都分布于内太阳系，加上外太阳系小天体（如半人马群和海王星外天体）的物理特性和内太阳系小天体有所差异，')
        st.write('因此“小行星”一词更常被用于专指内太阳系非彗星的小天体。')
        T()
    elif word=='彗星':
        st.image('彗星.jpg')
        st.write('彗星，俗称扫把星，是由冰构成的太阳系小天体（SSSB）。')
        st.write('当朝向太阳接近时，会被加热并且开始释气，展示出可见的大气层，也就是彗发，有时也会有彗尾。')
        st.write('这些现象是由太阳辐射和太阳风共同对彗核作用造成的。')
        st.write('彗核是由松散的冰、尘埃和小岩石构成的，大小从P/2007 R5的数百米至海尔博普彗星的数十公里不等，彗尾可能延伸长达一天文单位。')
        T()
    elif word=='流星':
        st.write('流星，是指运行在星际空间的流星体(通常包括宇宙尘粒和固体块等空间物质)在接近地球时由于受到地球引力的摄动而被地球吸引，')
        st.write('从而进入地球大气层，并与大气摩擦燃烧所产生的光迹。')
        st.write('流星体原来是围绕太阳运动的，在经过地球附近时，受地球引力的作用，改变轨道，从而进入地球大气圈。')
        st.write('流星有单个流星、火流星、流星雨几种。在掉到地面之前，大部分都已烧成了灰烬，少部分会变成陨石掉到地面上。')
        st.write('大部分可见的流星体都和沙粒差不多，重量在1克以下。流星进入大气层的速度介于11km/s到72km/s之间。')
        st.image('流星.jpg')   
        T()
    elif word=='太阳系':
        st.write('太阳系是一个受太阳引力约束在一起的天体系统，包括太阳、行星及其卫星、矮行星、小行星、彗星和行星际物质。')
        st.write('太阳位于距银河系中心约2.6万光年、距边缘2.3万光年的地方。而银河系直径约有10万光年，包含1500亿颗恒星，太阳只是其中之一。')
        st.write('太阳以220千米/秒的速度绕银心运动，大约2.5亿年绕行一周，地球气候及整体自然界也因此发生2.5亿年的周期性变化。')
        st.write('太阳运行的方向基本上是朝向织女，靠近武仙座的方向。')
        st.write('截至2019年10月，太阳系包括太阳、8个行星、近500个卫星和至少120万个小行星 ，还有一些矮行星和彗星。')
        st.write('若以海王星轨道作为太阳系边界，则太阳系直径为60个天文单位，即约90亿千米。')
        st.write('若以日球层为界，则太阳距太阳系边界可达100个天文单位(最薄处)。')
        st.write('若以奥尔特云为界，则太阳系直径可能有20万天文单位。')
        st.write('太阳系的形成大约始于46亿年前一个巨型星际分子云的引力坍缩。') 
        st.write('太阳系内大部分的质量都集中于太阳，余下的天体中，质量最大的是木星。八大行星逆时针围绕太阳公转。')
        st.write('此外还有较小的天体位于木星与火星之间的小行星带。柯伊伯带和奥尔特云也存在大量的小天体。')
        st.write('还有很多卫星绕转在行星或者小天体周围。小行星带外侧的每颗行星都有行星环。')
        cc=st.image('太阳系.jpg')
        d={'名字':['太阳','水星','金星','地球','火星','木星','土星','天王星','海王星'],
          '直径':['1392700km','4878km','12104km','12742km','6787km','139822km','116460km','50724km','49244km'],
          '离太阳的距离':['-','57910000km','108200000km','149600000km','227940000km','778330000km','1429400000km','2870990000km','4504000000km']}        
        d=pd.DataFrame(d)
        D=st.write(d)
        cc,D=st.columns([1, 1])
        T()
    elif word=='黑洞':
        st.write('黑洞(英文：Black Hole，简称BH)是由广义相对论所预言的，存在于宇宙空间中的一种致密天体。')
        st.image('黑洞.jpg')
        st.write('黑洞的引力极其强大，使得视界内的逃逸速度大于光速。故而，黑洞是时空曲率大到光都无法从其事件视界逃脱的天体。')
        T()
    elif word=='类星体':
        st.write('类星体是类似恒星天体的简称，又称为似星体、魁霎或类星射电源，')
        st.write('与脉冲星、微波背景辐射和星际有机分子一道并称为20世纪60年代天文学"四大发现"。长期以来，它总是让天文学家感到困惑不解。')
        st.image('类星体.png')
        T()
    elif word=='中子星':
        st.write('中子星是除黑洞外密度最大的星体，恒星演化到末期，经由重力崩溃发生超新星爆炸之后，可能成为的  少数终点之一，质量没有达到可以形成黑洞的恒星在寿命终结时塌缩形成的一种介于白矮星和黑洞之间的星体，其密度比  地球上任何物质密度大相当多倍。')
        st.image('中子星.png')
    else:
        st.write('抱歉，目前并不支持查询此信息。')
        T()
    pass
def page_3():
    #with open('leave_messages.txt','w',encoding='utf-8') as f:
    #    l_l=f.read().split('\n')
    #for i in range(len(l_l)):
    #   l_l[i]=l_l[i].split('#')
    st.write("<span style='font-size:30px'>时间记录:</span>", unsafe_allow_html=True)
    st.write('----')
    timE()
    
    pass
def page_4():
    global tsl
    st.write("<span style='font-size:30px'>设置:</span>", unsafe_allow_html=True)
    st.write('----')
    ex = st.toggle('背景图片')
    C = st.radio('如果你开启了背景，请选择一个背景：',
    ['选项1', '选项2', '选项3'],
    captions=['这是第一个选项', '这是第二个选项', '这是第三个选项']
    )
    if ex:
        if C=='选项1':
            bar_bg('天象奇景.jpg')
            page_bg('天象奇景.jpg')
        elif C=='选项2':
            bar_bg('宇宙.jpg')
            page_bg('宇宙.jpg')
        elif C=='选项3':
            bar_bg('黑.jpg')
            page_bg('黑.jpg')
        else:
            bar_bg('白.jpg')
            page_bg('白.jpg')
    else:
        bar_bg('白.jpg')
        page_bg('白.jpg')
    pass
def timE():
    with open('time.txt','r',encoding='utf-8') as f:
        ts_l=[]
        ts_l=f.read().split('\n')
    st.write('最近一次查询时间：'+ts_l[0])
    pass
def T():
    with open('time.txt','w',encoding='utf-8') as f:
        mes=datetime.datetime.now()
        f.write(str(mes))
    pass
def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )
if page == '宇宙的奥秘':
    page_1()
elif page == '查询信息':
    page_2()
elif page == '时间记录':
    page_3()
elif page == '设置':
    page_4()
#---------------------------------------------------------
#st.write('一键查询')
#   with open('words_space1.txt','r',encoding='utf-8') as f:
#        words_l=f.read().split('\n')
#    for i in range(len(words_l)):
#        words_l[i]=words_l[i].split('#')
#    words_d={}
#    for i in words_l:
#        words_d[i[1]]=[int(i[0]),i[2]]
#---------------------------------------------
#with open('check_out_times.txt','r',encoding='utf-8') as f:
    #    ts_l=f.read().split('\n')
    #for i in range(len(ts_l)):
    #    ts_l[i]=ts_l[i].split('#')
    #ts_d={}
    #for i in ts_l:
    #    ts_d[i[1]]=[int(i[0]),i[2]]
#with open('check_out_times.txt','w',encoding='utf-8') as f:
#    mes=''
#    for k,v in ts_d.items():
#        mes+=str(k)+'#'+str(v)+'\n'
#    mes=mes[:-1]
#    f.write(mes)
#--------------------------------------
# with open('leave_messages.txt','w',encoding='utf-8') as f:
#         l_l=f.read().split('\n')
#     for i in range(len(l_l)):
#         l_l[i]=l_l[i].split('#')
#--------------------------------------------------
# st.write('宇宙(Universe)，泛指物质和时空。')
    # st.write('现代宇宙学中的主流观点认为宇宙的起源，')
    # st.write('是起源于1次大爆炸，')
    # st.write('是在过去由一个密度极大且温度极高的状态演变而来的，')
    # st.write('并经过不断的膨胀达到的状态，')
    # st.write('这种观点被称为宇宙大爆炸理论或奇点爆炸理论。')
    # st.write('我们不知道什么原因引起了这次大爆炸。')
    # st.write('大爆炸发出的光线，还在向外传播。')
    # st.write('爆炸产生的气体和云团，舞动着，旋转着，聚集成胚胎时期的星系。')