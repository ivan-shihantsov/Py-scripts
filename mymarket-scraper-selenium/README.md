
пока парсим только юзеров
    это ссылки вида
    https://www.mymarket.ge/ka/search/?UserID=752770

условия:
0. через модуль requests - не получилось
1. selenium без --headless, без распараллеливания (в один поток)
    * 0007000 юзеров за 475.5 минут (== 7 ч 56 мин)
    * с тамим темпом на парсинг 10М юзеров уйдет 679286 мин ( == 472 сут == 1 год 3 мес 16 сут 17 ч 26 мин)
2. selenium с --headless + распараллеливание
3. puppeteer без --headless, без распараллеливания (в один поток)
2. puppeteer с --headless + распараллеливание

--------

затем еще буду парсить каналы
* это ссылки вида
* https://www.mymarket.ge/ka/search/?ShopID=11483&Tab=products
