## 简介
>  本程序适用于已经添加的站点批量推送，网站随时在更新。今天能用不一定明天能用
   [神马站长平台]: http://zhanzhang.sm.cn/ 

* token 和 url 添加目录在 /url/token.txt 文件中 

  <code>示例: www.aiezhi.com TI_f3c27b588b703fe9074833dbec925913</code>

* 推送结果还可以通过 /log/my_log.log 查看推送结果 

* 添加了推送频率控制

  <code>
    post_url_path = 'url/token.txt'                 # 推送哪些url<br>
    post_num_every_index = 2000                     # 每次每个目录推送多少条数据，最大值是2000 <br>
    post_frequency = 10                             # 推送延迟每隔离多少分钟推送一次,单位分钟 m <br>
  </code>

* 安装环境需求 python3.6 anaconda3/2

    <code>conda install subprocess</code>
  