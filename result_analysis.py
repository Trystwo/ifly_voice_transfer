#提取result.txt文件中的内容，制作云词图
#coding=utf-8
import jieba
import jieba.analyse    
import matplotlib.pyplot as plt 
from wordcloud import WordCloud 
import numpy as np
import PIL.Image as Image

# 读取文件
def get_text():     
    with open("result.txt", "r", encoding="gbk") as f:
        text = f.read()
    return text     

def get_wordcloud(text):
    # 设置停用词
    jieba.analyse.set_stop_words('stopwords.txt')
    # 提取关键词
    tags = jieba.analyse.extract_tags(text, topK=100, withWeight=False)
    text = " ".join(tags)
    # 设置背景图片
    mask = np.array(Image.open("background.png"))
    # 设置词云
    wordcloud = WordCloud(
        background_color="black",
        mask=mask,
        max_words=100,
        font_path="C:\Windows\Fonts\simfang.ttf",
        max_font_size=60,
        random_state=42,
        width=1000, height=860, margin=2,
    ).generate(text)
    # 生成词云
    plt.imshow(wordcloud)   
    plt.axis("off")
    plt.show()
    wordcloud.to_file('wordcloud.jpg')
# 主函数
if __name__ == '__main__':
    text = get_text()
    get_wordcloud(text)






