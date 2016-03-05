from django.views.generic import View
from django.shortcuts import render_to_response

# from api.models import *
# from api.models import Users
# import requests as rq
# import json

class WebView(View):
    """
    Main View.
    """

    def get(self, r, *arg, **args):
        #return HttpResponse(os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'))

        # _l = Levels(name="第一等级", counts="2000", description="这是第一个等级的描述!")
        # _l.save()

        # _d = json.loads(open('./f.txt').read())
        # _r = _d['data']['reviews']

        # cookies = {"sessionid": "jrycyrr2jzqfojailukzhr7xuilg6yih"}
        # _l = Levels.objects.get(lid=1)
        # for r in _r:
        #     _w = r['content']
        #     _pr = r['pronunciations']
        #     #_st = _r['']
        #     _cn = r['cn_definition']['defn']
        #     _en = r['en_definitions']
        #     params = {'ids': ','.join(map(lambda x: str(x), r['sys_example_ids']))}
        #     req = rq.get('http://www.shanbay.com/api/v1/bdc/example/', params=params, cookies=cookies)
        #     _jd = json.loads(req.text)
        #     #return HttpResponse(json.dumps(_jd))

        #     w, _created = Words.objects.get_or_create(level=_l, word=_w)
        #     w.save()

        #     for _js in _jd['data']:
        #         _jss = _js['annotation'].replace('<vocab>', '').replace('</vocab>', '')
        #         sss, _ = Sentences.objects.get_or_create(sentence=_jss, is_offical=True)
        #         sss.save()
        #         _jst = _js['translation'].replace('“', '').replace('”', '')
        #         ttt, _ = Translations.objects.get_or_create(translation=_jst)
        #         ttt.save()
        #         sss.translation.add(ttt)
        #         sss.save()
        #         w.sentence.add(sss)
        #     w.save()


        #     for i in ['us', 'uk']:
        #         p, _created = Pronuncations.objects.get_or_create(pronuncation=_pr[i], ptype=i)
        #         p.save()
        #         w.pronuncation.add(p)
        #     for i in _en.keys():
        #         for j in _en[i]:
        #             _m = j.split(';')
        #             for _k in _m:
        #                 d, _created = Definitions.objects.get_or_create(pos=i, definition=_k.strip(), language='us')
        #                 d.save()
        #                 w.definition.add(d)
        #     _cns = _cn.split('\n')
        #     for i in _cns:
        #         _cno = i.split('.')
        #         if len(_cno)>1:
        #             _cn_p = _cno[0]
        #             _cn_ds = _cno[1].split(',')
        #         else:
        #             _cn_p = '-'
        #             _cn_ds = _cno[0].split(',')
        #         for j in _cn_ds:
        #             d, _created = Definitions.objects.get_or_create(pos=_cn_p, definition=j.strip(), language='zh_cn')
        #             d.save()
        #             w.definition.add(d)
        #     w.save()
        return render_to_response('index.html', {})

