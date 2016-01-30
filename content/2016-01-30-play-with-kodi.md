title: Play with kodi
date: 2016-01-30 06:39:57
category: Blog
tags: kodi, rpi
slug: play-with-kodi
authors: xuhao
summary: write an audio addon of kodi.

先后买过两个Raspberry pi (RPi), 一个当server跑git和caddy, 另一个当media center跑kodi。

有功夫的时候打开，看看片子，跑跑服务还是挺好的。kodi作为老牌开源软件，历久弥新，无论功能还是性能都不逊与任何同类商业产品，甚至更好。玩法也很多，比如作为前端界面，以RPi＋触屏作为硬件平台，变成car pc，可以定制不少功能。

第三方插件十分丰富，但由于各种原因，不少插件在神奇的土地上是无法正常使用的。另外，不少插件也缺少维护，也不能用了。

因此决定自己动手，昨晚对着kodi tutorial做了一个addon。这里要说kdoi不亏是得过open source大奖的，从文档到api设计都很清楚。吃完晚饭，收拾好后，2到3个小时就搞定了。

Todo: add metadata, support cookies, caching and persistence, etc.

就放一张播放的图吧。

<img title="music playing" src="/images/20160129_music_playing_1.jpg" width="640" alt="music playing">

开发环境: pycharm community

<img title="pycharm community" src="/images/20160129_pycharm_edit.png"
width="640" alt="pycharm community">

.
