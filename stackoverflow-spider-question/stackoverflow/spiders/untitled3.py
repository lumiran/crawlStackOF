# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:22:06 2019

@author: lumir
"""

from lxml import etree
wb_data = """
<div class="question" data-questionid="2193953"  id="question">

    <style>.everyoneloves__top-leaderboard:empty,.everyoneloves__mid-leaderboard:empty,.everyoneloves__bot-mid-leaderboard:empty{                height:90px;width:728px;box-sizing:border-box;
}</style>
        <div id="dfp-tlb" class="everyonelovesstackoverflow everyoneloves__top-leaderboard"></div>
    <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container grid fd-column ai-stretch gs4 fc-black-200" data-post-id="2193953">
        <button class="js-vote-up-btn grid--cell s-btn s-btn__unset c-pointer" title="This question shows research effort; it is useful and clear" aria-pressed="false" aria-label="up vote" data-selected-classes="fc-theme-primary"><svg aria-hidden="true" class="svg-icon m0 iconArrowUpLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 26h32L18 10 2 26z"/></svg></button>
        <div class="js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center" itemprop="upvoteCount" data-value="2722">2722</div>
        <button class="js-vote-down-btn grid--cell s-btn s-btn__unset c-pointer" title="This question does not show any research effort; it is unclear or not useful" aria-pressed="false" aria-label="down vote" data-selected-classes="fc-theme-primary"><svg aria-hidden="true" class="svg-icon m0 iconArrowDownLg" width="36" height="36" viewBox="0 0 36 36"><path d="M2 10h32L18 26 2 10z"/></svg></button>

        <button class="js-favorite-btn s-btn s-btn__unset c-pointer py8" aria-pressed="false" aria-label="favorite (507)" data-selected-classes="fc-yellow-600">
            <svg aria-hidden="true" class="svg-icon iconStar" width="18" height="18" viewBox="0 0 18 18"><path d="M9 12.65l-5.29 3.63 1.82-6.15L.44 6.22l6.42-.17L9 0l2.14 6.05 6.42.17-5.1 3.9 1.83 6.16L9 12.65z"/></svg>
            <div class="js-favorite-count mt8" data-value="507">507</div>
        </button>


</div>

            </div>

"""
html = etree.HTML(wb_data)
result = etree.tostring(html)
print(result.decode("utf-8"))
html_data = html.xpath('/html/body/div')
for i in html_data:
    print(i)

for index in range(1, 51):
    html_data = html.xpath('/html/body/text()')
    
    for i in html_data:
        print(i)
        print(i.text)
print(html)
#result = etree.tostring(html)
#print(result.decode("utf-8"))


#html = etree.parse('1234.html')
#html_data = html.xpath('//*')#打印是一个列表，需要遍历
#print(html_data)
#for i in html_data:
#    print(i.text)