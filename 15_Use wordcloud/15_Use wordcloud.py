from wordcloud import WordCloud  
import jieba  
import PIL  
import matplotlib.pyplot as plt  
import numpy as np  
  
  
def wordcloudplot(txt):  
    path = r'e:/test/msyh.ttf'  
    alice_mask = np.array(PIL.Image.open('e:/test/22.png'))  
    wordcloud = WordCloud(font_path=path,  
                          background_color="white",  
                          margin=5, width=1800, height=800, mask=alice_mask, max_words=2000, max_font_size=60,  
                          random_state=42)  
    wordcloud = wordcloud.generate(txt)  
    wordcloud.to_file('e:/test/4.jpg')  
    plt.imshow(wordcloud)  
    plt.axis("off")  
    plt.show()  
  
  
def main():  
    a = []  
    f = open(r'e:/test/23.txt', 'r',encoding='utf-8').read()  
    words = list(jieba.cut(f))  
    for word in words:  
        if len(word) > 1:  
            a.append(word)  
    txt = r' '.join(a)  
    wordcloudplot(txt)  
  
  
if __name__ == '__main__':  
    main()  
