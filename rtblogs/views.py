from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from wiktionaryparser import WiktionaryParser
import re
import requests
# Create your views here.
def main_page(request):
    return render(request, 'rtblogs/main_page.html', {})

def bk(request):
    return render(request, 'rtblogs/bk.html', {})

def pf(request):
    return render(request, 'rtblogs/pf.html', {})

def nu(request):
    return render(request, 'rtblogs/nu.html', {})

def idiot(request):
    return render(request, 'rtblogs/idiot.html', {})



def dii(request):
    return render(request, 'rtblogs/dii.html', {})

def ispo(request):
    return render(request, 'rtblogs/ispo.html', {})

def ak(request):
    return render(request, 'rtblogs/ak.html', {})

def nhd(request):
    return render(request, 'rtblogs/nhd.html', {})

def wp(request):
    return render(request, 'rtblogs/wp.html', {})



def demons(request):
    return render(request, 'rtblogs/demons.html', {})

def main_home(request):
    return render(request, 'rtblogs/main_home.html', {})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def rtranslate(request):

    if request.method == 'POST':

        #get wiktionary json data
        data = json.loads(request.body)
        clicked_word = data.get('clicked_word', None)
        #separate for c, y and i
        if clicked_word in ['В','в', 'о','О','К','к','С','с','У','у', 'и', 'И' ]:
            l_clicked_word = clicked_word.lower()
            parser = WiktionaryParser()
            word = parser.fetch(l_clicked_word, 'russian')
            pos = word[1]['definitions'][0]['partOfSpeech']
            definitions = word[1]['definitions'][0]['text'][1:]
            examples = word[1]['definitions'][0]['examples']

            jrespond = {'word':clicked_word,'pos':pos, 'definitions':definitions, 'examples':examples,'ru_word':clicked_word}


            print(pos)
            print(examples)
            print(definitions)

            return JsonResponse(jrespond, status=200, safe=False)

        elif clicked_word in ['под', 'Под', 'бы', 'Бы' ]:
            l_clicked_word = clicked_word.lower()
            parser = WiktionaryParser()
            word = parser.fetch(l_clicked_word, 'russian')
            print(word)
            pos = word[0]['definitions'][0]['partOfSpeech']
            definitions = word[0]['definitions'][0]['text'][1:]
            examples = word[0]['definitions'][0]['examples']

            jrespond = {'word':clicked_word,'pos':pos, 'definitions':definitions, 'examples':examples,'ru_word':clicked_word}


            print(pos)
            print(examples)
            print(definitions)

            return JsonResponse(jrespond, status=200, safe=False)

        print(clicked_word)
        parser = WiktionaryParser()
        word = parser.fetch(str(clicked_word.lower()), 'russian')
        print(clicked_word.lower())
        print(word)
        try:
            declined_check = word[0]['definitions'][0]['text'][1]
        except:
            try:

                parser = WiktionaryParser()
                word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-2]), 'russian')
                declined_check = word[0]['definitions'][0]['text'][1]
            except:
                    try:
                        parser = WiktionaryParser()
                        word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-2] + 'ый'), 'russian')
                        declined_check = word[0]['definitions'][0]['text'][1]
                    except:
                        try:
                            parser = WiktionaryParser()
                            word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-2] + 'ий'), 'russian')
                            declined_check = word[0]['definitions'][0]['text'][1]
                        except:
                            try:
                                parser = WiktionaryParser()
                                word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-2] + 'ой'), 'russian')
                                declined_check = word[0]['definitions'][0]['text'][1]
                            except:
                                try:
                                    parser = WiktionaryParser()
                                    word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-3]), 'russian')
                                    declined_check = word[0]['definitions'][0]['text'][1]
                                except:
                                    try:
                                        parser = WiktionaryParser()
                                        word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-3] + 'ый'), 'russian')
                                        declined_check = word[0]['definitions'][0]['text'][1]
                                    except:
                                        try:
                                            parser = WiktionaryParser()
                                            word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-3] + 'ий'), 'russian')
                                            declined_check = word[0]['definitions'][0]['text'][1]
                                        except:
                                            parser = WiktionaryParser()
                                            word = parser.fetch(str(clicked_word.lower()[:len(clicked_word)-3] + 'ой'), 'russian')
                                            declined_check = word[0]['definitions'][0]['text'][1]


        find_russian_word_declined = re.search(r"\b[А-ЯЁа-яёа́ю́]+\b",declined_check)
        if find_russian_word_declined:
            russian_word_to_search = find_russian_word_declined.group(0)
            print(russian_word_to_search)
            if "а́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"а́","а", russian_word_to_search)

            if "ю́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"ю́","ю", russian_word_to_search)

            if "о́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"о́","о", russian_word_to_search)
            if "е́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"е́","е", russian_word_to_search)
            if "у́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"у́","у", russian_word_to_search)
            if "и́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"и́","и", russian_word_to_search)
            if "ы́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"ы́","ы", russian_word_to_search)
            if "я́" in russian_word_to_search:
                russian_word_to_search = re.sub(r"я́","я", russian_word_to_search)

            print(russian_word_to_search)
            parser = WiktionaryParser()
            word = parser.fetch(russian_word_to_search, 'russian')
            pos = word[0]['definitions'][0]['partOfSpeech']
            definitions = word[0]['definitions'][0]['text'][1:]
            examples = word[0]['definitions'][0]['examples']

            jrespond = {'word':clicked_word,'pos':declined_check, 'definitions':definitions, 'examples':examples, 'ru_word':russian_word_to_search}




            return JsonResponse(jrespond, status=200, safe=False)

        else:
            print(word)
            pos = word[0]['definitions'][0]['partOfSpeech']
            definitions = word[0]['definitions'][0]['text'][1:]
            examples = word[0]['definitions'][0]['examples']

            if examples == [] and not word[0]['definitions'][0]['relatedWords'] == []:
                examples = word[0]['definitions'][0]['relatedWords'][0]['words']


            jrespond = {'word':clicked_word,'pos':pos, 'definitions':definitions, 'examples':examples, 'ru_word':clicked_word}


            print(pos)
            print(examples)
            print(definitions)

            return JsonResponse(jrespond, status=200, safe=False)







        #extract json according to word type



        return JsonResponse(word, status=200, safe=False)


def rtpicture(request):
    if request.method == 'POST':

        #get wiktionary json data
        data = json.loads(request.body)
        clicked_word = data.get('clicked_word', None)
        print("rt picture got clicked_word")

        google_search_url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyD_ciSIUUa-iUZh9kBrR97cpTPqfD5YFN0&cx=7b3da2f3c8e0bc012&searchType=image&exactTerms=" + clicked_word + "&safe=high&q=" + clicked_word


        gi_response = requests.get(google_search_url)
        gi_response.encoding = 'utf-8-sig'
        gi_response_json = gi_response.json()
        print(gi_response_json)

        print(gi_response_json['items'][0]['link'])

        img_list = []

        for search_result in gi_response_json['items']:
            img_list.append(search_result['link'])



    return JsonResponse(img_list, status=200, safe=False)