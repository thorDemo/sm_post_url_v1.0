## 简介
>  本程序适用于已经添加的站点批量推送，网站随时在更新。今天能用不一定明天能用
   [神马站长平台]: http://zhanzhang.sm.cn/ 

* token 和 url 添加目录在 /url/token.txt 文件中 

  <code>
        示例: 
        
        www.aiezhi.com TI_f3c27b588b703fe9074833dbec925913
        
   </code>

* 泛域名 添加目录在 /url/head.txt 文件中 
  一定要添加 www 在头部
  <code>
      示例: 
      
        www
        feel
        seem
        how
        high
  </code>
  
* 列表页配置目录 /url/index.txt
 <code>
      示例: 
      
        html/
        news/
        show/
        read/
  </code>

* 推送频率固定 一天一次

* 推送日志在 log/my_log.log
    示例：
    <code>
    
        2018-12-21 18:58:50,892 - __main__ - INFO - 提交成功 post = www.mindfuledu.cn
        2018-12-21 18:58:53,702 - __main__ - INFO - 提交成功 post = www.nodigi.cn
        2018-12-21 18:58:56,482 - __main__ - INFO - 提交成功 post = www.openc.cn
        2018-12-21 18:59:01,685 - __main__ - INFO - 提交成功 post = www.ganluwang.cn
    </code>
* 安装环境需求 python3.6 anaconda3/2
    <code>
    
        conda install subprocess
    </code>
  