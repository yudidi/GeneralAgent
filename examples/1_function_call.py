# 函数调用
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    handlers=[logging.StreamHandler()],
)
from GeneralAgent import Agent
from dotenv import load_dotenv

load_dotenv()

# 函数调用时序图
# https://mermaid.live/view#pako:eNqNVmFv2lYU_SvIUitQUmmf-VBpajWpUjtN2rcJCVnwSlCxzYw9KaoqwZYGAklATdJkK0lDYYGlC7Cpayik5c_wns2_2H3v2oCxg5oPiSHn3Hfueeddv-dSQksSKSrlyM8mURPkYVpO6bISU0Pwk5V1I51IZ2XVCD3IpAn8kXMh2n3HStfW-54f9G3KwYiHyahp1bb9qCdE0fRNDrO7fTretroNwNHfO37oI9UgelYn8DsnCO3mtFgGqDXa8qMfP34iBLbadu_K7uRZp0HPKn7cD5vGhqY-gM6_S2egNCfhd1zyecEeF9moJQQh-c6dkJkjejytZk0jxP4rWB2nLNpy7_79NdFydAEXtr8c0Jd_To-703cnEYR_rxkkpP0CSzpwepOn7QptbYED1mEHjEUWwgUIijvguG6qYcQiyqk6E4l-0qsT-mtnUaVbZw2th0qKeIjLyaQjFkmesnOxLo32PSIn41NOK_Xp_jat_stX_3yEXGTAki6Vr6SQXE5OkXBM4i7FpPWQWDvioQDnntOvPT6kb87YxxIr9B49dDcjo2lZUHJq947s_Wtafc2umlaja_0zgs22_tiyRgfsrI5Y1xeBmwzKk0GFvS5ixTliZo_rc4oY8UxGcQXnwhE_2G0Ma6MDy4XnLQV0REvHdqMzBwconsWdVWtWazhHCA-mhT1YlvWqk8HlDDnHLIpdPEeuZKwJJyWc1TUla0S81EWKvwPB5VbW_57TiJoMascf-nKH5Qt2_zd29AG9mB6N6fDCb7K7aLNAdy4RGk6YxmxjfPuykB5Wz1ujEh4XWtuHZLjb43EahgYogVjTV7s81sUhUlbEg0dDVpNxmCk5EtdMQ5x2UQRHTkBc1paHDthQekNHQ9_ICcwDnGZ6U0VloJge7NHhYcAq8D-wC_sJGoPzAyRKOeERbRvaM6J6MwDVfFsfAHNXD2hxNqyKvrR4e3Rz7-aY7n6avtyDPVnejaX43xL828OPhVFSGPcurshGYiPiryBnYNrvfOETTrAgQyvWC8465g-7KfV5BbF0MH15uLDrES2f0_JfbKcC3tPW3tfx6H6Fz-fBB3b8kZ2XVpOWhkO7yc5qq0SunAxIX57BK7XefIKlvlLrbOqOP3NjAg73MtMzlHxfeD44cXcHCO3uspLPifkTTwd__9U7GHy207Ybu0Gt35KKxTtHMNkjzzfhnFl80qO1C848fcvOi3R8jBTBnV8Nipcwdq1R2xpdsWaevXWuGLyJaT1vXxQWEaG7d6F6jSsatmnp_WQw_GbFQMeCKASLOQuJpvxjSkwpeGfb3ZarnsN9O-HpE_HLDnH97n-8NQLeI6iH36JikvYsJkUCnJ49LF6duOl41Zu5Lt4uqEZalxSiK3I6CTfp55wXk4wNopCYFIXHJHkqmxkjJsXUFwCVTUP7cVNNSFFDN8m6pGtmakOKPpUzOfhkZpOy4V7DXQjcWn_SNMUBvfgf_KXxaQ

# 函数: 获取天气信息
def get_weather(city: str) -> str:
    """
    get weather information
    @city: str, city name
    @return: str, weather information
    """
    # return f"{city} weather: sunny"
    weather = "sunny"
    print(f"{city} weather: {weather}")
    return weather


# agent = Agent('你是一个天气小助手', functions=[get_weather], model='deepseek-chat')
agent = Agent("你是一个天气小助手", functions=[get_weather])
agent.user_input("成都天气怎么样？")

# 输出
# ```python
# city = "成都"
# weather_info = get_weather(city)
# weather_info
# ```
# 成都的天气是晴天。
# 请问还有什么我可以帮忙的吗？
