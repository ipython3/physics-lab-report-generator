from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, red, blue, green
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('微软雅黑', 'msyh.ttc'))
pdfmetrics.registerFont(TTFont('华文中宋', 'STZHONGS.TTF'))
pdfmetrics.registerFont(TTFont('宋体', 'simsun.ttc'))
c = canvas.Canvas(filename='大物实验.pdf', pagesize=A4)

# 页面的宽度和高度
(width, height) = A4

# 页面被分为三份，从上到下是 头部， 正文， 尾部
# 每个部分用两条虚拟的线来标记上端和下端
head_top = height  # 头部的上线(y坐标)
head_bottom = height - 2 * cm  # 头部的底线(y坐标)

body_top = height - 5 * cm  # 正文的上线(y坐标)
body_bottom = 1 * cm  # 正文的底线(y坐标)

tail_top = 1 * cm  # 尾部的上线(y坐标)
tail_bottom = 0  # 尾部的底线(y坐标)

cursor = body_top  # 光标的位置


# 画出头部
def set_head(c):
    # 将坐标原点移动到此位置
    # c.translate(0, head_bottom)

    # 画出第1、2根线
    c.setLineWidth(2)
    c.line(cm, head_top - 0.5 * cm, width / 2 - 2.5 * cm, head_top - 0.5 * cm)
    c.line(width / 2 + 2.5 * cm, head_top - 0.5 * cm, width - cm, head_top - 0.5 * cm)

    # 画出第3根线
    c.setLineWidth(4)
    c.line(cm, head_bottom, width - cm, head_bottom)

    # 画出第4根线
    c.setLineWidth(1)
    c.line(cm, head_bottom + 0.2 * cm, width - cm, head_bottom + 0.2 * cm)

    # 写出“大物·实验”这几个字
    c.setFont('华文中宋', 23)
    c.drawCentredString(width / 2, head_top - 1 * cm, '实 验 报 告')


# 画出尾部
def set_tail(c):
    # 画出尾部线
    c.setLineWidth(2)
    c.line(cm, tail_top, width - cm, tail_top)


# 填写学生信息
def set_user_info(c, text='未填写姓名，学号，组号，座位号'):
    c.setFont('宋体', 12)
    c.drawString(cm, head_bottom + 0.4 * cm, '学生信息：' + text)


# 填写实验标题
def set_title(c, text='未填写实验标题'):
    c.setFont('宋体', 14)
    c.drawString(cm, height - 3.3 * cm, '实验标题：' + text)


# 填写实验目的
def set_target(c, text='未填写实验目的'):
    c.setFont('宋体', 14)
    c.drawString(cm, height - 3.3 * cm, '实验目的：' + text)


user_info = '张三，PB14111111，211组，9号'
user_title = '光电池伏安特性的研究'
user_target = '''1.了解光电池的工作原理
2.绘制光电池的伏安特性曲线
3.测量光电池在特定条件下的内阻'''

set_head(c)
set_tail(c)
set_user_info(c, user_info)
#set_title(c, user_title)
#set_target(c, user_target)

c.showPage()
c.save()
