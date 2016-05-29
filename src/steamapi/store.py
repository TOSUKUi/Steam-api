import urllib.request as ulr
import json
import time

class Store:

    """
    steamの商品ページの情報を表示するapi
    ["appid":{"success":, "data":{['supported_languages', 'categories', 'packages', 'metacritic', 'mac_requirements', 'steam_appid', 'recommendations', 'required_age', 'linux_requirements', 'is_free', 'background', 'name', 'release_date', 'support_info', 'developers', 'platforms', 'publishers', 'type', 'achievements', 'pc_requirements', 'header_image', 'package_groups', 'about_the_game', 'screenshots', 'price_overview', 'detailed_description', 'website', 'controller_support', 'movies', 'genres']}}]
    """
    def appdetails(self, appid):
        url = 'http://store.steampowered.com/api/appdetails/?appids=' + appid
        try:
            response = ulr.urlopen(url)
        except:
            print("HTTP error")
            return
        try:
            appdetailsJson = json.loads(response.read().decode("utf-8"))
        except:
            print("... may be an args of appid is missed")
            return
        appdetail = None
        for appdetail in appdetailsJson:
            if appdetailsJson[appdetail]['success']:
                appdetail = appdetailsJson[appdetail]['data']
            else:
                appdetail = {}
        return appdetail

    """
    steamの商品ページのうち、価格のみを表示するapi
    これだけ何故かcsv形式でのappidsの指定が可能なので、先にこちらで対象を絞る。
    @:param appids appidをcsv形式で入手するためのもの
    """
    def appprices(self, appids):
        url = 'http://store.steampowered.com/api/appdetails/?appids=' + appids + '&filters=price_overview'
        try:
            response = ulr.urlopen(url)
        except:
            print("http error")
            return

        try:
            apppricesJson = json.loads(response.read().decode("utf-8"))
        except:
            print("json parse error")
        return apppricesJson





