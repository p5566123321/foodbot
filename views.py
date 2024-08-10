from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from .scraper import IFoodie
from .scraper2 import scrapDelivery
import urllib.parse 


#translator = googletrans.Translator()

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
arr = []

sayhi = [TextSendMessage("你好，很高興為您服務!"),TextSendMessage("按下定位以獲取餐廳資訊~"),TextSendMessage("※在室內的場合，定位可能會有偏差。",quick_reply=QuickReply(items=[
        QuickReplyButton(action=LocationAction("尋找附近餐廳")),
        QuickReplyButton(action=PostbackAction(label="搜尋食物類別", display_text="搜尋食物類別",data="搜尋食物類別"))
    ]))]


iFoodiecat=[#["早午餐",False],
  ["精緻高級",False],
  #["火鍋",False],
  ["甜點",False],
  ["小吃",False],
  #["約會餐廳",False],
  ["蛋糕",False],
  ["咖啡",False],
  ["餐酒館/酒吧",False],
  ["牛排",False],
  ["燒烤",False],
  ["居酒屋",False],
  ["冰品飲料",False],
  ["合菜",False],
  ["宵夜",False],
  ["海鮮",False],
  ["拉麵",False],
  ["牛肉麵",False],
  ["壽司",False],
  ["素食",False],
  ["日本料理",False],
  ["韓式料理",False],
  ["中式料理",False],
  ["美式料理",False],
  ["義式料理",False],
  ["泰式料理",False],
  ["港式料理",False]
]
category=0
count=0
req=0
page=1
lat=0.0
lon=0.0

def countstar():
  global arr
  global req
  bubbles=[]


  for i in range (req,req+10):
            
            
            addr="https://www.google.com/maps/search/?api=1&query="+urllib.parse.quote(arr[i][0])
            if (arr[i][1])[0]=="5":
              bubble={
                "type": "bubble",
                "size": "kilo",
                "hero": {
                  "type": "image",
                  "url": arr[i][3],
                  "size": "full",
                  "aspectMode": "cover",
                  "aspectRatio": "320:213"
                },
                "body": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "text",
                      "text": arr[i][0],
                      "weight": "bold",
                      "size": "sm",
                      "wrap": True
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "contents": [
                        {
                          "type": "icon",
                          "size": "xs",
                          "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                          "type": "icon",
                          "size": "xs",
                          "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                          "type": "icon",
                          "size": "xs",
                          "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                          "type": "icon",
                          "size": "xs",
                          "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                          "type": "icon",
                          "size": "xs",
                          "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                          "type": "text",
                          "text": arr[i][1],
                          "size": "xs",
                          "color": "#8c8c8c",
                          "margin": "md",
                          "flex": 0
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "baseline",
                          "spacing": "sm",
                          "contents": [
                            {
                              "type": "text",
                              "text": arr[i][5],
                              "wrap": True,
                              "color": "#8c8c8c",
                              "size": "xs",
                              "flex": 5
                            }
                          ]
                        }
                      ]
                    }
                  ],
                  "spacing": "sm",
                  "paddingAll": "13px"
                },
                "footer": {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                      "type": "uri",
                      "label": "Google Map",
                      "uri": addr
                      }
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "foodpanda",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"foodpanda"
                      }
                    },
                    {
                      "type": "button",
                      "action": {
                        "type": "postback",
                        "label": "Uber Eats",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"Uber Eats"
                      }
                    }
                  ]
                }
              }
            elif (arr[i][1])[0]=="4":
              bubble={
                  "type": "bubble",
                  "size": "kilo",
                  "hero": {
                    "type": "image",
                    "url": arr[i][3],
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": arr[i][0],
                        "weight": "bold",
                        "size": "sm",
                        "wrap": True
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                          },
                          {
                            "type": "text",
                            "text": arr[i][1],
                            "size": "xs",
                            "color": "#8c8c8c",
                            "margin": "md",
                            "flex": 0
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                              {
                                "type": "text",
                                "text": arr[i][5],
                                "wrap": True,
                                "color": "#8c8c8c",
                                "size": "xs",
                                "flex": 5
                              }
                            ]
                          }
                        ]
                      }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "Google Map",
                        "uri": addr
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                        "type": "postback",
                        "label": "foodpanda",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"foodpanda"
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                        "type": "postback",
                        "label": "Uber Eats",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"Uber Eats"
                        }
                      }
                    ]
                  }
                }
            elif (arr[i][1])[0]=="3":
              print("T")
              bubble={
                  "type": "bubble",
                  "size": "kilo",
                  "hero": {
                    "type": "image",
                    "url": arr[i][3],
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": arr[i][0],
                        "weight": "bold",
                        "size": "sm",
                        "wrap": True
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                          },
                          {
                            "type": "text",
                            "text": arr[i][1],
                            "size": "xs",
                            "color": "#8c8c8c",
                            "margin": "md",
                            "flex": 0
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                              {
                                "type": "text",
                                "text": arr[i][5],
                                "wrap": True,
                                "color": "#8c8c8c",
                                "size": "xs",
                                "flex": 5
                              }
                            ]
                          }
                        ]
                      }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "Google Map",
                        "uri": addr
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                        "type": "postback",
                        "label": "foodpanda",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"foodpanda"
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                        "type": "postback",
                        "label": "Uber Eats",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"Uber Eats"
                        }
                      }
                    ]
                  }
                }
            elif (arr[i][1])[0]=="2":
              print("T")
              bubble={
                    "type": "kilo",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": arr[i][3],
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": arr[i][0],
                          "weight": "bold",
                          "size": "sm",
                          "wrap": True
                        },
                        {
                          "type": "box",
                          "layout": "baseline",
                          "contents": [
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                              "type": "text",
                              "text": arr[i][1],
                              "size": "xs",
                              "color": "#8c8c8c",
                              "margin": "md",
                              "flex": 0
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "spacing": "sm",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": arr[i][5],
                                  "wrap": True,
                                  "color": "#8c8c8c",
                                  "size": "xs",
                                  "flex": 5
                                }
                              ]
                            }
                          ]
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                          "type": "uri",
                          "label": "Google Map",
                          "uri": addr
                          }
                        },
                        {
                          "type": "button",
                          "action": {
                          "type": "postback",
                          "label": "foodpanda",
                          "data": arr[i][0]+" "+arr[i][2]+" "+"foodpanda"
                          }
                        },
                        {
                          "type": "button",
                          "action": {
                        "type": "postback",
                        "label": "Uber Eats",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"Uber Eats"
                          }
                        }
                      ]
                    }
                  }
            elif (arr[i][1])[0]=="1":
              print("T")
              bubble={
                    "type": "kilo",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": arr[i][3],
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": arr[i][0],
                          "weight": "bold",
                          "size": "sm",
                          "wrap": True
                        },
                        {
                          "type": "box",
                          "layout": "baseline",
                          "contents": [
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                              "type": "icon",
                              "size": "xs",
                              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                            },
                            {
                              "type": "text",
                              "text": arr[i][1],
                              "size": "xs",
                              "color": "#8c8c8c",
                              "margin": "md",
                              "flex": 0
                            }
                          ]
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "spacing": "sm",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": arr[i][5],
                                  "wrap": True,
                                  "color": "#8c8c8c",
                                  "size": "xs",
                                  "flex": 5
                                }
                              ]
                            }
                          ]
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    },
                    "footer": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "button",
                          "action": {
                          "type": "uri",
                          "label": "Google Map",
                          "uri": addr
                          }
                        },
                        {
                          "type": "button",
                          "action": {
                          "type": "postback",
                          "label": "foodpanda",
                          "data": arr[i][0]+" "+arr[i][2]+" "+"foodpanda"
                          }
                        },
                        {
                          "type": "button",
                          "action": {
                        "type": "postback",
                        "label": "Uber Eats",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"Uber Eats"
                          }
                        }
                      ]
                    }
                  }
            else:
              print("T")
              bubble={
                        "type": "kilo",
                        "size": "micro",
                        "hero": {
                          "type": "image",
                          "url": arr[i][3],
                          "size": "full",
                          "aspectMode": "cover",
                          "aspectRatio": "320:213"
                        },
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": arr[i][0],
                              "weight": "bold",
                              "size": "sm",
                              "wrap": True
                            },
                            {
                              "type": "box",
                              "layout": "baseline",
                              "contents": [
                                {
                                  "type": "icon",
                                  "size": "xs",
                                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                  "type": "icon",
                                  "size": "xs",
                                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                  "type": "icon",
                                  "size": "xs",
                                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                  "type": "icon",
                                  "size": "xs",
                                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                  "type": "icon",
                                  "size": "xs",
                                  "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                  "type": "text",
                                  "text": arr[i][1],
                                  "size": "xs",
                                  "color": "#8c8c8c",
                                  "margin": "md",
                                  "flex": 0
                                }
                              ]
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "spacing": "sm",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": arr[i][5],
                                      "wrap": True,
                                      "color": "#8c8c8c",
                                      "size": "xs",
                                      "flex": 5
                                    }
                                  ]
                                }
                              ]
                            }
                          ],
                          "spacing": "sm",
                          "paddingAll": "13px"
                        },
                        "footer": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "button",
                              "action": {
                                "type": "uri",
                                "label": "Google Map",
                                "uri": addr
                              }
                            },
                            {
                              "type": "button",
                              "action": {
                            "type": "postback",
                            "label": "foodpanda",
                            "data": arr[i][0]+" "+arr[i][2]+" "+"foodpanda"
                              }
                            },
                            {
                              "type": "button",
                              "action": {
                        "type": "postback",
                        "label": "Uber Eats",
                        "data": arr[i][0]+" "+arr[i][2]+" "+"Uber Eats"
                              }
                            }
                          ]
                        }
                      }
              
            bubbles.append(bubble)
  return bubbles
              


@csrf_exempt
def callback(request):
  global count
  global category
  global req
  global page
  global arr
  global lat
  global lon
  if request.method == 'POST':
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')

    try:
        events = parser.parse(body, signature)  # 傳入的事件
        print(events)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    except LineBotApiError:
        return HttpResponseBadRequest()      
    

    for event in events:
        print("\n\n"+event.type+"\n\n")
        print("\n\n"+str(count)+"\n\n")

        if isinstance(event, FollowEvent): 
          line_bot_api.reply_message(event.reply_token,sayhi)

        if isinstance(event, PostbackEvent):
          print(event.postback.data)
          if event.postback.data=="搜尋食物類別":
              arr=[]
              req=0
              page=1
              line_bot_api.reply_message(
              event.reply_token,
              TemplateSendMessage(
                      alt_text='Buttons template',
                      template=ButtonsTemplate(
                          title='Menu',
                          text='請選擇美食類別',
                          actions=[
                              PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
                                  label='火鍋',
                                  data='火鍋'
                              ),
                              PostbackTemplateAction(
                                  label='早午餐',
                                  data='早午餐'
                              ),
                              PostbackTemplateAction(
                                  label='約會餐廳',
                                  data='約會餐廳'
                              ),
                              PostbackTemplateAction(
                                  label='其他類別',
                                  data='其他類別'
                              )
                          ]
                      )
                  )
              )
          elif event.postback.data=="其他類別":

            if count<len(iFoodiecat):
              line_bot_api.reply_message(
              event.reply_token,
              TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='請選擇美食類別',
                                actions=[
                                    PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
                                        label=iFoodiecat[count][0],
                                        data=iFoodiecat[count][0]
                                    ),
                                    PostbackTemplateAction(
                                        label=iFoodiecat[count+1][0],
                                        data=iFoodiecat[count+1][0]
                                    ),
                                    PostbackTemplateAction(
                                        label=iFoodiecat[count+2][0],
                                        data=iFoodiecat[count+2][0]
                                    ),
                                    PostbackTemplateAction(
                                        label='其他類別',
                                        data='其他類別'
                                    )
                                ]
                            )
                        )
              )
              count=count+3
            else:
              line_bot_api.reply_message(
              event.reply_token,
              TextSendMessage("沒有更多類別了喔!"))
              
          elif "foodpanda" in event.postback.data:
            split_tmp=event.postback.data.split()
            string_url=scrapDelivery(split_tmp[0],split_tmp[1],split_tmp[2])
            if "null" in string_url:
              line_bot_api.reply_message(
              event.reply_token,
              TextSendMessage("此外送未提供喔!",quick_reply=QuickReply(items=[
              QuickReplyButton(action=LocationAction("尋找附近餐廳")),
              QuickReplyButton(action=PostbackAction(label="搜尋食物類別", display_text="搜尋食物類別",data="搜尋食物類別"))
              ])))
            else:
              line_bot_api.reply_message(
              event.reply_token,
              TextSendMessage(string_url,quick_reply=QuickReply(items=[
              QuickReplyButton(action=LocationAction("尋找附近餐廳")),
              QuickReplyButton(action=PostbackAction(label="搜尋食物類別", display_text="搜尋食物類別",data="搜尋食物類別"))
              ])))
          elif "Uber Eats" in event.postback.data: 
            split_tmp=event.postback.data.split()  
            string_url=scrapDelivery(split_tmp[0],split_tmp[1],split_tmp[2])
            if "null" in string_url:
              line_bot_api.reply_message(
              event.reply_token,
              TextSendMessage("此外送未提供喔!",quick_reply=QuickReply(items=[
              QuickReplyButton(action=LocationAction("尋找附近餐廳")),
              QuickReplyButton(action=PostbackAction(label="搜尋食物類別", display_text="搜尋食物類別",data="搜尋食物類別"))
              ])))
            else:
              line_bot_api.reply_message(
              event.reply_token,
              TextSendMessage(string_url,quick_reply=QuickReply(items=[
              QuickReplyButton(action=LocationAction("尋找附近餐廳")),
              QuickReplyButton(action=PostbackAction(label="搜尋食物類別", display_text="搜尋食物類別",data="搜尋食物類別"))
              ])))

              
          else:

            category=event.postback.data
            line_bot_api.reply_message(
              event.reply_token,
              TextSendMessage("請按下定位獲取餐廳資訊!",quick_reply=QuickReply(items=[
                                QuickReplyButton(action=LocationAction("開始定位"))]))
            )
          
        
        
        
        if isinstance(event, MessageEvent):  # 如果有訊息事件
          count=0
          if event.message.type=='location':
            lat=event.message.latitude
            lon=event.message.longitude
            page=1
            print("page")
            print(page)
          elif event.message.type=='text':
            if event.message.text=='更多資訊':
              req=req+10
            if req+10>len(arr):
              page=page+1

          food = IFoodie([lat,lon],category,page)
          arr=arr+food.scrape()
          print("arr len")
          print (len(arr))
          print (arr)
          print("req")
          print(req)
          print("page")
          print(page)
          contents=dict()
          contents['type']='carousel'
          bubbles=[]

            
          bubbles=countstar()
          
          contents['contents']=bubbles
          line_bot_api.reply_message(  # 回復傳入的訊息文字
              event.reply_token,
              FlexSendMessage(
                alt_text='hello',
                contents=contents,quick_reply=QuickReply(items=[
                            QuickReplyButton(action=LocationAction("尋找附近餐廳")),
                            QuickReplyButton(action=MessageAction(label="更多資訊",text="更多資訊")),
                            QuickReplyButton(action=PostbackAction(label="搜尋食物類別", display_text="搜尋食物類別",data="搜尋食物類別"))
                        ]))
            )

          
    return HttpResponse()
  else:
    return HttpResponseBadRequest()


        