import html
import re

# html内容
html_str = '''
<div class="f18 mb20">
	<p>英语雯老师过生日，带我们去KTV嗨&hellip;</p>
	<p>大家买了一堆吃的放在桌上，正准备开吃&hellip;</p>
	<p>&ldquo;啪&rdquo;的包厢停电了，霎时一片漆黑，几声尖叫声过后，遂一片寂静&hellip;</p>
	<p>接着一阵阵&ldquo;啪哩叭啦&rdquo;的拆包装袋声音。</p>
	<p>卧槽！都特么偷吃啦！！！</p>
	<p>竟然趁黑偷吃，一个个吃货，真没素质，至于吗？形象呢？一群没出息的货！就特么知道吃！</p>
	<p>不屑于顾的我，果断的把牛仔裤一下褪到脚背，趁黑朝着几个女生挤了过去&hellip;</p>
</div>
'''

# 获取内容包含段落
# p_list = re.findall("<p>(.*?)</p>", html_str)
# print(p_list)

# 保留段落
html_str = re.sub(r"<p>|<br>|<br />", r"\\n", html_str)
print(html_str)

# 替换标签
html_str = re.sub(r"<.*?>|\s|　", "", html_str)
print(html_str)

html_str = re.sub(r"\\n", "\n", html_str)
print(html_str)

# 处理html实体
# html_escape_str = html.escape('<a href="a.html">a link</a>') # 编码
html_str = html.unescape(html_str) # 解码
print(html_str)
