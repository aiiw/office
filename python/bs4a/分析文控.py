# -*- coding: utf-8 -*-
html_doc ="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="zh" type="basic">
  <head>
    <title>测试-文档管理</title>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, user-scalable=yes" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="imagetoolbar" content="no" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="pragma" content="no-cache" />
    <link rel="shortcut icon" type="image/x-icon" href="/__cache__/workonline/1585376646//img/favicon.ico" />
    <link rel="root-url" href="http://192.168.0.38:7089/default" />
    <link rel="cache-url" href="/__cache__/workonline/1585376646/" />
    <link rel="packages-cache-url" href="http://192.168.0.38:7089/default/packages/" />
    <link type="text/css" rel="stylesheet" href="/__cache__/workonline/1585376646//zopen-component.css" media="all" />
    <link type="text/css" rel="stylesheet" href="/__cache__/workonline/1585376646//zopen-template.css" media="all" />
    <base href="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/" />
    <script charset="utf-8" src="/__cache__/workonline/1585376646//zopen.core.js"></script>
    
  </head>
  <body class="view-zopen-docs-view_folder_listing type-folder">
    <div id="visual-wrapper">
      <div id="header">
        <div class="actionMenu">
            <h1 class="site-title"><a href="http://192.168.0.38:7089/default">文档管理</a></h1>
            
    <ul class="topNavTabs" id="site-navbar">
        <li>
            <a href="http://192.168.0.38:7089/default/desks/">工作台</a>
        </li>
        <li class="selected">
            <a href="http://192.168.0.38:7089/default/isodoc/">体系文控</a>
        </li>
        <li>
            <a href="http://192.168.0.38:7089/default/files/">文档</a>
        </li>
        <li>
            <a href="http://192.168.0.38:7089/default/ldap/">LDAP集成</a>
        </li>
        <li>
            <a href="http://192.168.0.38:7089/default/472547/">应用开发</a>
        </li>
        <li>
            <a href="http://192.168.0.38:7089/default/common_flow/">常用流程</a>
        </li>
        <li>
            <a href="http://192.168.0.38:7089/default/542249/">ISO文控</a>
        </li>
        <li>
            <a href="http://192.168.0.38:7089/default/_more_/">更多</a>
        </li>
        
        <li style="display:none;" class="collapsed">
            <dl class="actionMenu">
            <dt class="actionMenuHeader KSSActionMenu">
                <button class="navbar-toggle KSSActionMenu">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
            </dt>
            <dd class="actionMenuContent KSSActionMenuContent hidden" style="right: 0;"></dd>
        </dl></li>
    </ul>
 

        </div>
        <div id="header-right" class="topNavTabs">
    <ul>
        
            <li id="notify-center">
<dl class="actionMenu">
  <dt class="actionMenuHeader KSSActionMenu" id="notify-trigger">
    <a id="current_site" href="javascript:;">
      <span class="current_site_title"></span>
          <i class="icon-bell"></i>
          <span class="site_msg_count unmsg_num">0</span>
    </a>
  </dt>
      <dd class="actionMenuContent hidden KSSActionMenuContent" style="right:-1px;font-size:14px; height:200px;">
      <input type="hidden" id="hidden_wo_site_title" value="    测试-文档管理" />
      <input type="hidden" id="hidden_site_title" value="    文档管理" />
      <input type="hidden" id="hidden_new_msg" value="have new message!" />
      <table class="CustomShowHideArea" style="height: 100%;width: 100%;">
         <tbody>
           <tr>
            <td style="height: 200px;vertical-align: top;width: 15%;">
              <div id="notify-channels" style="overflow-x:hidden;overflow-y:auto;width:180px;"></div>
              <script>var channels = [{"name": "workflow", "title": "\u6d41\u7a0b"}, {"name": "sendme", "title": "\u53d1\u9001\u7ed9\u6211\u7684"}, {"name": "mentioned", "title": "\u63d0\u5230\u6211\u7684"}, {"name": "announcement", "title": "\u516c\u544a"}, {"name": "comment", "title": "\u8bc4\u8bba"}, {"name": "subscribe", "title": "\u8ba2\u9605"}, {"name": "default", "title": "\u5176\u4ed6"}]</script>
            </td>
            <td style="border-left:1px solid #E5ECF9;height:100%;width:580px;vertical-align:top;width: 85%;">
              <div id="msg-history" style="height:200px;"></div>
            </td>
          </tr>
        </tbody>
      </table>
     </dd>
</dl>
<div id="xmpp-sound"></div>
<script>var root_url = $("[rel=root-url]").attr("href");</script>
<script type="text/javascript">
// 关闭飘窗
$('body').on('click', 'a[name="notify"]', function(event) {
    var fadeOutDuration = 500,
        helper = $(this).parents('div.jquery-message');
    helper.animate(
        { opacity: 0 },
        fadeOutDuration,
        function() {
            $(this).hide();
            $(this).remove();
        }
    );
});
</script>
<script type="text/javascript">
  $('body').on('click', '.chatSelectSubmit', function(){
    var data = $(this.form).serialize();
    $(this).kss({
        url: '@@chatAction', params: data });
  });
</script>
</li>


            
            <script>var sites_info = []</script>
            <script>var current_site_info = {"name": "default", "title": ""}</script>
            <script>var other_site = {"title": "\u5176\u4ed6\u7ad9\u70b9"}</script>
        
        <li id="site-menu">
            <dl class="actionMenu">
                <dt class="actionMenuHeader cancelBubble" onclick="showMenu(this, '#site-user-menu');return false;">
                    <a href="javascript:;">简东兴<span class="arr_d"><em class="b1"></em><em class="b2"></em><em class="b3"></em></span></a></dt>
                <ul class="actionMenuContent KSSActionMenuContent hidden" id="site-user-menu">
                    
                        
                        
                        <li>
                            <a href="#" class="kss" style="padding-left:34px;" data-kss="http://192.168.0.38:7089/default/@zopen.desks:my_logs">我的动态</a>
                        </li>
                        <li>
                            <a id="site-menu-my-setting" href="#" class="kss" style="padding-left:34px;" data-kss="http://192.168.0.38:7089/default/@zopen.user_setting:index">个人设置</a>
                        </li>
                        <li>
                            <a href="#" class="kss" style="padding-left:34px;" data-kss="http://192.168.0.38:7089/default/@zopen.assistant:download_assistant">桌面助手</a>
                        </li>
                        <li class="submenu">
                            <a href="javascript:;" class="submenu-hover">
                                <i class="fa fa-language" style="float:none;margin:0;width:16px;"></i>
                                <i class="fa fa-caret-right"></i>
                                
                                    简体中文
                                
                                
                                
                                
                                
                            </a>
                            <ul class="submenu-items actionMenuContent" style="display: none;">
                                <li>
                                    
                                </li>
                                <li>
                                    <a href="#" class="kss" data-lang="zh-tw" data-kss="http://192.168.0.38:7089/default/@zopen.views:switch_lang">繁體中文</a>
                                </li>
                                <li>
                                    <a href="#" class="kss" data-lang="ja" data-kss="http://192.168.0.38:7089/default/@zopen.views:switch_lang">日本語</a>
                                </li>
                                <li>
                                 
                                </li>
                                <li>
                                    <a href="#" class="kss" data-lang="en" data-kss="http://192.168.0.38:7089/default/@zopen.views:switch_lang">English</a>
                                </li>
                            </ul>
                        </li>
                    
                    <li>
                        <a href="http://192.168.0.38:7089/default/ssologout" style="padding-left:34px;" id="site-menu-logout">退出</a>
                    </li>
                </ul>
            </dl>
        </li>
        
        <li style="margin-right:10px;_margin-right:7px"></li>
    </ul>

</div>
        <div id="site-actions">
    <div id="site-new">
        <dl class="actionMenu">
            <dt class="actionMenuHeader KSSActionMenu">
                <i class="fa fa-plus new" title="快捷添加"></i>
                <span class="arr_d"><em class="b1"></em><em class="b2"></em><em class="b3"></em></span>
            </dt>
            <dd class="actionMenuContent KSSActionMenuContent hidden">
                <ul kssattr:url="http://192.168.0.38:7089/default/@@targetContents">
                    <li>
                        <a class="kss" data-param1="uploadFile" href="#" onclick="uploadMode(this);">上传文件</a>
                    </li>
                    <li>
                        <a class="kssattr-param1-newDocument KSSActionServer" href="#">新建文件</a>
                    </li>
                    <li>
                        <a kssattr:url="@@issue_workflow_pop" kssattr:param1="desk" class="KSSActionServer" href="#">提交表单</a>
                    </li>
                </ul>
            </dd>
        </dl>
    </div>
    <div id="site-searchbox">
        <form name="searchform" action="http://192.168.0.38:7089/default/@zopen.views:advanced_search_index">
            <div class="searchBox" id="search-box">
              <input type="text" value="" placeholder="全站搜索" name="text" id="search" title="全站搜索">
              <input type="submit" id="magnifier" value="" title="搜索">
              <i class="fa fa-close hand hidden"></i>
            </div>
        </form>
    </div>

</div>
        <div class="visualClear"><!-- --></div>
      </div>
      <div id="visual-content">
        <div id="top"></div>
        <div id="site-subnav"><div class="subnav" id="sub-navbar">
    <ul class="nav-tabs">
        
        <li class="selected">
            <a href="http://192.168.0.38:7089/default/isodoc/files/">文件库</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/forum/">公告</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/review/">文档审批</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/document_borrow/">借阅</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/perm_delivery/">分发</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/review_comment/">意见处理</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/annul/">废止</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/retrospect/">回顾</a>
        </li>
        <li class="">
            <a href="http://192.168.0.38:7089/default/isodoc/reports/">统计报表</a>
        </li>
        
        <i class="hand nav-config fa fa-gear kss mobile-hide" data-kss="http://192.168.0.38:7089/default/isodoc/@zopen.site_config:nav_settings"></i>
    </ul>
</div>
</div>
        <table id="columns" class=" leftcol rightcol">
          <tbody>
            <tr>
              <td id="left">
                <div class="visualPadding"><dl class="portlet portlet">
    <dt class="portletHeader">
        <div class="portletHeaderContent">目录</div>
    </dt>
    <dd class="portletItem"><div id="nav_02c4bd0bd698535e3b06915807a7eec3" class="navtree" kssattr:templ="templ_02c4bd0bd698535e3b06915807a7eec3">
                  <script type="text/javascript">
                      var templ_02c4bd0bd698535e3b06915807a7eec3 = Handlebars.compile('<a class="KSSActionServer{{#if selected}} selected{{/if}}" kssattr:url="{{url}}/@@single-preview" href="{{url}}/{{view}}" title="{{title}}"><i class="fa fa-{{icon}}"></i> {{title}}</a>');
                      $('#nav_02c4bd0bd698535e3b06915807a7eec3').html(render_navtree("%5B%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/1.0%2520%25E7%25AE%25A1%25E7%2590%2586%25E6%2589%258B%25E5%2586%258C/%40%40simple-content%22%2C%20%22title%22%3A%20%221.0%20%5Cu7ba1%5Cu7406%5Cu624b%5Cu518c%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/1.0%2520%25E7%25AE%25A1%25E7%2590%2586%25E6%2589%258B%25E5%2586%258C%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/1.0%2520%25E7%25AE%25A1%25E7%2590%2586%25E6%2589%258B%25E5%2586%258C%20id%3D%5C%22nodeid-245069989%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/2.0%2520%25E7%25A8%258B%25E5%25BA%258F%25E6%2596%2587%25E4%25BB%25B6/%40%40simple-content%22%2C%20%22title%22%3A%20%222.0%20%5Cu7a0b%5Cu5e8f%5Cu6587%5Cu4ef6%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/2.0%2520%25E7%25A8%258B%25E5%25BA%258F%25E6%2596%2587%25E4%25BB%25B6%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/2.0%2520%25E7%25A8%258B%25E5%25BA%258F%25E6%2596%2587%25E4%25BB%25B6%20id%3D%5C%22nodeid-245069990%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/3.0%2520%25E4%25BD%259C%25E4%25B8%259A%25E6%258C%2587%25E5%25AF%25BC/%40%40simple-content%22%2C%20%22title%22%3A%20%223.0%20%5Cu4f5c%5Cu4e1a%5Cu6307%5Cu5bfc%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/3.0%2520%25E4%25BD%259C%25E4%25B8%259A%25E6%258C%2587%25E5%25AF%25BC%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/3.0%2520%25E4%25BD%259C%25E4%25B8%259A%25E6%258C%2587%25E5%25AF%25BC%20id%3D%5C%22nodeid-245069991%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/4.0%2520%25E8%25A1%25A8%25E5%258D%2595/%40%40simple-content%22%2C%20%22title%22%3A%20%224.0%20%5Cu8868%5Cu5355%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/4.0%2520%25E8%25A1%25A8%25E5%258D%2595%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/4.0%2520%25E8%25A1%25A8%25E5%258D%2595%20id%3D%5C%22nodeid-245069993%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/5.0%2520%25E8%25A1%258C%25E6%2594%25BF%25E5%2585%25AC%25E6%2596%2587/%40%40simple-content%22%2C%20%22title%22%3A%20%225.0%20%5Cu884c%5Cu653f%5Cu516c%5Cu6587%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/5.0%2520%25E8%25A1%258C%25E6%2594%25BF%25E5%2585%25AC%25E6%2596%2587%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/5.0%2520%25E8%25A1%258C%25E6%2594%25BF%25E5%2585%25AC%25E6%2596%2587%20id%3D%5C%22nodeid-245069994%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/6.0%2520%25E5%25B7%25A5%25E8%2589%25BA%25E6%258A%2580%25E6%259C%25AF%25E8%25B5%2584%25E6%2596%2599/%40%40simple-content%22%2C%20%22title%22%3A%20%226.0%20%5Cu5de5%5Cu827a%5Cu6280%5Cu672f%5Cu8d44%5Cu6599%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/6.0%2520%25E5%25B7%25A5%25E8%2589%25BA%25E6%258A%2580%25E6%259C%25AF%25E8%25B5%2584%25E6%2596%2599%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/6.0%2520%25E5%25B7%25A5%25E8%2589%25BA%25E6%258A%2580%25E6%259C%25AF%25E8%25B5%2584%25E6%2596%2599%20id%3D%5C%22nodeid-245069995%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/7.0%2520%25E4%25B8%259A%25E5%258A%25A1%25E7%259B%25B8%25E5%2585%25B3%25E5%258D%258F%25E8%25AE%25AE%25E6%2596%2587%25E4%25BB%25B6/%40%40simple-content%22%2C%20%22title%22%3A%20%227.0%20%5Cu4e1a%5Cu52a1%5Cu76f8%5Cu5173%5Cu534f%5Cu8bae%5Cu6587%5Cu4ef6%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/7.0%2520%25E4%25B8%259A%25E5%258A%25A1%25E7%259B%25B8%25E5%2585%25B3%25E5%258D%258F%25E8%25AE%25AE%25E6%2596%2587%25E4%25BB%25B6%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/7.0%2520%25E4%25B8%259A%25E5%258A%25A1%25E7%259B%25B8%25E5%2585%25B3%25E5%258D%258F%25E8%25AE%25AE%25E6%2596%2587%25E4%25BB%25B6%20id%3D%5C%22nodeid-675379627%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/8.0%2520%25E5%2590%2588%25E5%2590%258C%25E7%25AE%25A1%25E7%2590%2586/%40%40simple-content%22%2C%20%22title%22%3A%20%228.0%20%5Cu5408%5Cu540c%5Cu7ba1%5Cu7406%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/8.0%2520%25E5%2590%2588%25E5%2590%258C%25E7%25AE%25A1%25E7%2590%2586%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/8.0%2520%25E5%2590%2588%25E5%2590%258C%25E7%25AE%25A1%25E7%2590%2586%20id%3D%5C%22nodeid-245071588%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/9.0%2520%25E5%2590%2584%25E9%2583%25A8%25E9%2597%25A8%25E5%2588%2586%25E5%258F%2591%25E5%25AD%2598%25E5%2582%25A8%25E6%2596%2587%25E4%25BB%25B6%25E6%25B1%2587%25E6%2580%25BB/%40%40simple-content%22%2C%20%22title%22%3A%20%229.0%20%5Cu5404%5Cu90e8%5Cu95e8%5Cu5206%5Cu53d1%5Cu5b58%5Cu50a8%5Cu6587%5Cu4ef6%5Cu6c47%5Cu603b%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/9.0%2520%25E5%2590%2584%25E9%2583%25A8%25E9%2597%25A8%25E5%2588%2586%25E5%258F%2591%25E5%25AD%2598%25E5%2582%25A8%25E6%2596%2587%25E4%25BB%25B6%25E6%25B1%2587%25E6%2580%25BB%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/9.0%2520%25E5%2590%2584%25E9%2583%25A8%25E9%2597%25A8%25E5%2588%2586%25E5%258F%2591%25E5%25AD%2598%25E5%2582%25A8%25E6%2596%2587%25E4%25BB%25B6%25E6%25B1%2587%25E6%2580%25BB%20id%3D%5C%22nodeid-966828920%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/10.0%2520%25E5%259F%25B9%25E8%25AE%25AD%25E8%25B5%2584%25E6%2596%2599/%40%40simple-content%22%2C%20%22title%22%3A%20%2210.0%20%5Cu57f9%5Cu8bad%5Cu8d44%5Cu6599%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/10.0%2520%25E5%259F%25B9%25E8%25AE%25AD%25E8%25B5%2584%25E6%2596%2599%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/10.0%2520%25E5%259F%25B9%25E8%25AE%25AD%25E8%25B5%2584%25E6%2596%2599%20id%3D%5C%22nodeid-1215876622%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/11.0%2520%25E5%25BA%259F%25E6%25AD%25A2%25E6%2596%2587%25E4%25BB%25B6/%40%40simple-content%22%2C%20%22title%22%3A%20%2211.0%20%5Cu5e9f%5Cu6b62%5Cu6587%5Cu4ef6%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/11.0%2520%25E5%25BA%259F%25E6%25AD%25A2%25E6%2596%2587%25E4%25BB%25B6%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/11.0%2520%25E5%25BA%259F%25E6%25AD%25A2%25E6%2596%2587%25E4%25BB%25B6%20id%3D%5C%22nodeid-1215876634%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/12.0%2520%25E5%25BE%2585%25E5%25AE%25A1%25E6%2596%2587%25E4%25BB%25B6/%40%40simple-content%22%2C%20%22title%22%3A%20%2212.0%20%5Cu5f85%5Cu5ba1%5Cu6587%5Cu4ef6%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/12.0%2520%25E5%25BE%2585%25E5%25AE%25A1%25E6%2596%2587%25E4%25BB%25B6%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/12.0%2520%25E5%25BE%2585%25E5%25AE%25A1%25E6%2596%2587%25E4%25BB%25B6%20id%3D%5C%22nodeid-1227016044%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/13.0%2520%25E5%25A4%2596%25E6%259D%25A5%25E5%258F%2597%25E6%258E%25A7%25E6%2596%2587%25E4%25BB%25B6/%40%40simple-content%22%2C%20%22title%22%3A%20%2213.0%20%5Cu5916%5Cu6765%5Cu53d7%5Cu63a7%5Cu6587%5Cu4ef6%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/13.0%2520%25E5%25A4%2596%25E6%259D%25A5%25E5%258F%2597%25E6%258E%25A7%25E6%2596%2587%25E4%25BB%25B6%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/13.0%2520%25E5%25A4%2596%25E6%259D%25A5%25E5%258F%2597%25E6%258E%25A7%25E6%2596%2587%25E4%25BB%25B6%20id%3D%5C%22nodeid-1048010609%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/14.0%2520%25E6%25A0%25B7%25E6%259D%25BF%25E5%258D%2595/%40%40simple-content%22%2C%20%22title%22%3A%20%2214.0%20%5Cu6837%5Cu677f%5Cu5355%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/14.0%2520%25E6%25A0%25B7%25E6%259D%25BF%25E5%258D%2595%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/14.0%2520%25E6%25A0%25B7%25E6%259D%25BF%25E5%258D%2595%20id%3D%5C%22nodeid-1517612122%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/15.0%2520%25E7%25AB%258B%25E9%25A1%25B9%25E6%2596%2587%25E4%25BB%25B6/%40%40simple-content%22%2C%20%22title%22%3A%20%2215.0%20%5Cu7acb%5Cu9879%5Cu6587%5Cu4ef6%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/15.0%2520%25E7%25AB%258B%25E9%25A1%25B9%25E6%2596%2587%25E4%25BB%25B6%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/15.0%2520%25E7%25AB%258B%25E9%25A1%25B9%25E6%2596%2587%25E4%25BB%25B6%20id%3D%5C%22nodeid-1366226172%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20null%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/16.0%2520%25E5%2585%25B6%25E5%25AE%2583/%40%40simple-content%22%2C%20%22title%22%3A%20%2216.0%20%5Cu5176%5Cu5b83%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/16.0%2520%25E5%2585%25B6%25E5%25AE%2583%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/16.0%2520%25E5%2585%25B6%25E5%25AE%2583%20id%3D%5C%22nodeid-816644877%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20true%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/%25E6%25B5%258B%25E8%25AF%2595/%40%40simple-content%22%2C%20%22title%22%3A%20%22%5Cu6d4b%5Cu8bd5%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/%25E6%25B5%258B%25E8%25AF%2595%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/%25E6%25B5%258B%25E8%25AF%2595%20id%3D%5C%22nodeid-186395102%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%2C%20%7B%22classes%22%3A%20%22navTreeItem%22%2C%20%22selected%22%3A%20false%2C%20%22kss%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/%25E6%25AC%25A7%25E5%25BE%25B7%25E7%25BD%2597%25E5%2585%25AC%25E5%258F%25B8%25E6%2596%2587%25E4%25BB%25B6/%40%40simple-content%22%2C%20%22title%22%3A%20%22%5Cu6b27%5Cu5fb7%5Cu7f57%5Cu516c%5Cu53f8%5Cu6587%5Cu4ef6%22%2C%20%22url%22%3A%20%22http%3A//192.168.0.38%3A7089/default/isodoc/files/%25E6%25AC%25A7%25E5%25BE%25B7%25E7%25BD%2597%25E5%2585%25AC%25E5%258F%25B8%25E6%2596%2587%25E4%25BB%25B6%22%2C%20%22attributes%22%3A%20%22kssattr%3Anodeurl%3Dhttp%3A//192.168.0.38%3A7089/default/isodoc/files/%25E6%25AC%25A7%25E5%25BE%25B7%25E7%25BD%2597%25E5%2585%25AC%25E5%258F%25B8%25E6%2596%2587%25E4%25BB%25B6%20id%3D%5C%22nodeid-1860001380%5C%22%22%2C%20%22icon%22%3A%20%22folder%22%2C%20%22view%22%3A%20%22%40zopen.docs%3Aview_folder_listing%22%7D%5D", templ_02c4bd0bd698535e3b06915807a7eec3, false));
                  </script>
              </div>
           </dd>
</dl>
</div>
              </td>
              <td id="main">
                <div id="viewlet-above-content"></div>
                <div id="region-content" class="documentContent">
                  <span id="portal-message"></span>
                  <div id="content"><div id="above-content-bar" class="KSSTabArea">
    <div class="contentbar_content contentbarcontent">
        <div class="contentbar_right">
            <div class="button-group mini">
    <dl class="actionMenu" style="display: inline;float: left;">
    <dt class="actionMenuHeader KSSActionMenu">
        
            <button class="button">查看方式 <i class="fa fa-caret-down"></i></button>
        
        
    </dt>
    <dd class="actionMenuContent hidden KSSActionMenuContent barActionMenuContent">
        <ul>
            
                <li>
                    <div class="plain">内容列表</div>
                    
                    
                </li>
            
            
                <li>
                    
                    
                    <a class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@switch_view?name=zopen.docs:view_folder_thumbnail">缩略图</a>
                </li>
            
            
                <li class="seperator">
                    
                    <a href=""></a>
                    
                </li>
            
            
                <li>
                    
                    
                    <a class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.views:menu_item_setting">设置...</a>
                </li>
            
        </ul>
    </dd>
</dl>

    <span class="actionMenu" style="float: left;">
    <button class="button cancelBubble" onclick="showMenu(this, '#folder-more-actions');return false;">
        操作
        <i class="fa fa-caret-down"></i>
    </button>
    <ul class="actionMenuContent KSSActionMenuContent hidden" id="folder-more-actions">
        <li>
            <a href="#" class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@addSub">分享</a>
        </li>
        <li class="submenu mobile-hide">
            <a href="javascript:;" class="submenu-hover">
                <i class="fa fa-caret-right"></i>
                桌面
            </a>
            <ul class="submenu-items actionMenuContent" style="display: none;">
                <li>
                    <a href="#" class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.assistant:assistant_webfolder">映射盘</a>
                </li>
                <li>
                    <a href="#" class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.assistant:assistant_sync">文件同步</a>
                </li>
            <ul>
        </ul></ul></li>
        <li>
            <a href="#" class="kss" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.logs:recycle?domain:list=zopen.docs">回收站</a>
        </li>
        <li>
            <a href="#" class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@popTitleForm">重命名</a>
        </li>
        <li>
            <a href="#" class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.views:permission">权限</a>
        </li>
        <li class="submenu">
            <a href="javascript:;" class="submenu-hover">
                <i class="fa fa-caret-right"></i>
                属性
            </a>
            <ul class="submenu-items actionMenuContent" style="display: none;">
                <li>
                    <a href="#" class="KSSActionServer" data-param1="folder" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@gochworkflowState">受控</a>
                </li>
                <li>
                    <a href="#" class="KSSActionServer" data-only_edit="true" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@show_metadata">扩展属性</a>
                </li>
            <ul>
        </ul></ul></li>
        <li>
            <a href="#" class="KSSActionServer" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.logs:history?domain:list=zopen.docs">操作历史</a>
        </li>
        <li>
            <a href="#" class="kss" data-redirect="true" kssattr:url="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@kss_obj_delete_pulldown">删除</a>
        </li>
        <li><a href="#" onclick="$('#_portlets_docs_folder_right').trigger('customize');return false;" class="kss-com link" >右侧列布局</a></li>
    </ul>
</span>

</div>

            <button class="button mini toggle_right_visible mobile-hide">
                <i class="fa fa-angle-double-right"></i>
            </button>
        </div>
        <div class="contentbar_left"><span class="path">
    
        
            <a class="kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/@@single-preview" data-param1="http://192.168.0.38:7089/default/isodoc/files/@zopen.docs:view_folder_listing" href="http://192.168.0.38:7089/default/isodoc/files/@zopen.docs:view_folder_listing">文件库</a>
            
        
        
        &gt;
    
    
        
            <a class="kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@single-preview" data-param1="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:view_folder_listing" href="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:view_folder_listing">测试</a>
            
        
        
        
    
    <span style="background: #dd0000; color:#fff; padding: 0 2px;" title="这是一个受控文件夹，文件存档后才可见">受控</span>
</span>
</div>
        <div class="visualClear"><!-- --></div>
    </div>
    <div class="KSSTabPageContentContainer"></div>
</div>
<div class="kss-com html" ><div id="folder_listing_content_6113" class="kss-com layout row-fluid" ><div class="" ><div class="kss-com html" ><form style="height: 0;" class="kss-com kss" action="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:folder_listing" id="folder_listing_form" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:folder_listing" method="post"><input type="hidden" name="form.submitted" value="1" /><input type="hidden" name="sort" value="" /><input type="hidden" name="old_sort" value="" /><input type="hidden" name="reverse" value="" /><input type="hidden" name="init_query_json" value="&quot;&quot;" /><input type="hidden" name="update:boolean" value="1" /><input type="hidden" name="page_size:int" value="20" /><input type="hidden" name="start:int" value="0" /><input type="hidden" name="widgets:json" value="[&quot;export&quot;, &quot;setting&quot;, &quot;select&quot;, &quot;item_menu&quot;, &quot;stat&quot;, &quot;description&quot;]" /><input type="hidden" name="sorts:json" value="[]" /><input type="hidden" name="old_reverse" value="" /><input type="hidden" name="result_id" value="folder_listing_content_6113" /><input type="hidden" name="columns:json" value="[]" /><input type="hidden" name="form_id" value="folder_listing_form" /><table class="vertical listing"></table><div></div></form>
<div id="file_list" class="kss-com" ><div style="margin-bottom:5px;" class="kss-com" ><a style="float:right;" href="#" class="kss-com link discreet black kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@import_export_pop?sort=-_drag_&total_condition=%5B%7B%22operator%22%3A%20%22exclude_anyof%22%2C%20%22stati%22%3A%20%5B%22attach.attachment%22%5D%7D%2C%20%7B%22operator%22%3A%20%22anyof%22%2C%20%22parent%22%3A%20%5B186395102%5D%7D%5D"><i class="fa fa-file-excel-o" ></i> 导入(导出)</a><span class="kss-com discreet" >共有 1 项内容有权限查看</span></div><div class="scroll-auto">
    <table class="listing querySelectArea colResizable batchAction" data-batch="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@batchActions" id="colResizable-186395102">
        <thead>
            <tr class="nodrop nodrag actionMenu">
                <th style="width: 15px;">
                    <span class="fa-stack icon-chbactions mobile-hide">
                        <i class="fa fa-square-o fa-stack-2x"></i>
                        <i class="fa fa-check fa-stack-1x hidden"></i>
                    </span>
                    <input type="checkbox" class="querySelect chbactions hidden" />
                </th>
                <th>
                    <a href="#" class="KSSSortListingBar underline" title="按此列排序" data-reverse="" data-sort="title">
                        标题
                        
                    </a>
                    
                </th>
                <th>
                    <a href="#" class="KSSSortListingBar underline" title="按此列排序" data-reverse="" data-sort="zopen.archive:archive.archival_number">
                        档号
                        
                    </a>
                    
                </th>
                <th>
                    <a href="#" class="KSSSortListingBar underline" title="按此列排序" data-reverse="" data-sort="zopen.archive:archive.archive_id">
                        案卷号
                        
                    </a>
                    
                </th>
                <th>
                    <a href="#" class="KSSSortListingBar underline" title="按此列排序" data-reverse="" data-sort="zopen.archive:archive.qzh">
                        全宗号
                        
                    </a>
                    
                </th>
                <th>
                    <a href="#" class="KSSSortListingBar underline" title="按此列排序" data-reverse="" data-sort="zopen.archive:archive.retention_period">
                        保存期限
                        
                    </a>
                    
                </th>
                <th>
                    <a href="#" class="KSSSortListingBar underline" title="按此列排序" data-reverse="" data-sort="zopen.archive:archive.confidentiality">
                        密级
                        
                    </a>
                    
                </th>
                <th>
                    <a href="#" class="KSSSortListingBar underline" title="按此列排序" data-reverse="" data-sort="size">
                        大小
                        
                    </a>
                    
                </th>
                <th style="width: 25px;" class="hand cancelBubble" onclick="showMenu(this, '#colums-settings');">
                    
                        <i class="fa fa-ellipsis-v"></i>
                        <ul class="actionMenuContent KSSActionMenuContent hidden" id="colums-settings">
                            <li>
                                <a href="#" class="kss" data-param1="tabular" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.views:columns_setting">调整表头</a>
                            </li>
                            <li>
                                <a href="#" class="kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:drag_sort">
                                    拖动排序
                                    
                                </a>
                            </li>
                        </ul>
                    
                </th>
            </tr>
        </thead>
        <tbody>
            
            <tr class="folderRow" id="row-901032512">
                <td>
                    <span class="fa-stack icon-chbactions mobile-hide">
                        <i class="fa fa-square-o fa-stack-2x"></i>
                        <i class="fa fa-check fa-stack-1x hidden"></i>
                    </span>
                    <input type="checkbox" class="chbitem chbactions hidden" value="901032512" />
                </td>
                
                <td>
                    
                        <a class="kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/%28%E4%B8%87%E4%BA%8B%E6%B3%B0%29T100%E4%B8%8A%E7%BA%BF%E9%97%AE%E9%A2%98%E7%AE%A1%E5%88%B6%E8%A1%A8190909%20%281%29.xlsx/@@simple-preview?toggle=1" href="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/%28%E4%B8%87%E4%BA%8B%E6%B3%B0%29T100%E4%B8%8A%E7%BA%BF%E9%97%AE%E9%A2%98%E7%AE%A1%E5%88%B6%E8%A1%A8190909%20%281%29.xlsx/@@view.html">
                            <i class="fa fa-external-link-square fa-lg" style="color:#4E6D86"></i>
                            
                            (万事泰)T100上线问题管制表190909 (1).xlsx
                            <span class="KSSShowHideArea">
    
    
    <img class="hidden KSSShowHideTarget" src="/__cache__/workonline/1585376646/img/waiting.gif" />
</span>

                        </a>
                        <span class="visible_default">非保密</span>
                        <span class="modify_published">发布</span>
                        

                        
                     
                     
                </td>
                
                
                <td>
                    
                      
                </td>
                
                
                <td>
                    
                      
                </td>
                
                
                <td>
                    
                      
                </td>
                
                
                <td>
                    
                     
                </td>
                
                
                <td>
                    
                      
                </td>
                
                
                <td>
                    
                     3.58 M
                </td>
                
                <td class="actionMenu dragHandle">
                    <span class="menu mobile-hide">
                        <i class="fa fa-sort icon-actions sort hidden" style="cursor: move;float: right;"></i>
                        <i class="fa fa-chevron-circle-down icon-actions hand kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/%28%E4%B8%87%E4%BA%8B%E6%B3%B0%29T100%E4%B8%8A%E7%BA%BF%E9%97%AE%E9%A2%98%E7%AE%A1%E5%88%B6%E8%A1%A8190909%20%281%29.xlsx/@@show_menu"></i>
                    </span>
                </td>
            </tr>
            
            
        </tbody>
    </table>
</div>

<input type="hidden" name="files_filter_json" value="{&quot;sort&quot;: [{&quot;fields._drag_&quot;: {&quot;order&quot;: &quot;desc&quot;, &quot;ignore_unmapped&quot;: true, &quot;mode&quot;: &quot;max&quot;}}], &quot;query&quot;: {&quot;filtered&quot;: {&quot;filter&quot;: {&quot;and&quot;: [{&quot;terms&quot;: {&quot;allowed_principals&quot;: [&quot;users.11608&quot;, &quot;zope.Everybody&quot;, &quot;zope.Authenticated&quot;, &quot;groups.tree.default&quot;, &quot;groups.tree.0b6364b245b52b498f87197dbc2a0f5f&quot;, &quot;groups.tree.66751b116efd8e449a1f0f5e29bd9c03&quot;, &quot;groups.tree.46894b8f998f5945bc018b1e92521675&quot;, &quot;groups.tree.4497811e37475a4483509ddfb1febf31&quot;, &quot;groups.jobs.3b1415731ee3dc4c9fbc4cb4a8c5610a&quot;, &quot;groups.jobs.883026&quot;, &quot;groups.teams.0-9&quot;, &quot;groups.teams.0&quot;, &quot;groups.teams.0-managers&quot;]}}, {&quot;not&quot;: {&quot;terms&quot;: {&quot;disallowed_principals&quot;: [&quot;users.11608&quot;]}}}, {&quot;not&quot;: {&quot;terms&quot;: {&quot;stati&quot;: [&quot;modify.history_archived&quot;, &quot;modify.history_default&quot;, &quot;modify.history_temp&quot;, &quot;modify.history_abandoned&quot;]}}}, {&quot;not&quot;: {&quot;terms&quot;: {&quot;stati&quot;: [&quot;attach.attachment&quot;]}}}, {&quot;terms&quot;: {&quot;parent&quot;: [186395102]}}, {&quot;terms&quot;: {&quot;object_types&quot;: [&quot;File&quot;, &quot;FileShortCut&quot;, &quot;FolderShortCut&quot;]}}]}}}, &quot;_source&quot;: false}" form="exportResult" /><input type="hidden" name="folders_filter_json" value="{&quot;sort&quot;: [{&quot;fields._drag_&quot;: {&quot;order&quot;: &quot;desc&quot;, &quot;ignore_unmapped&quot;: true, &quot;mode&quot;: &quot;max&quot;}}], &quot;query&quot;: {&quot;filtered&quot;: {&quot;filter&quot;: {&quot;and&quot;: [{&quot;terms&quot;: {&quot;allowed_principals&quot;: [&quot;users.11608&quot;, &quot;zope.Everybody&quot;, &quot;zope.Authenticated&quot;, &quot;groups.tree.default&quot;, &quot;groups.tree.0b6364b245b52b498f87197dbc2a0f5f&quot;, &quot;groups.tree.66751b116efd8e449a1f0f5e29bd9c03&quot;, &quot;groups.tree.46894b8f998f5945bc018b1e92521675&quot;, &quot;groups.tree.4497811e37475a4483509ddfb1febf31&quot;, &quot;groups.jobs.3b1415731ee3dc4c9fbc4cb4a8c5610a&quot;, &quot;groups.jobs.883026&quot;, &quot;groups.teams.0-9&quot;, &quot;groups.teams.0&quot;, &quot;groups.teams.0-managers&quot;]}}, {&quot;not&quot;: {&quot;terms&quot;: {&quot;disallowed_principals&quot;: [&quot;users.11608&quot;]}}}, {&quot;not&quot;: {&quot;terms&quot;: {&quot;stati&quot;: [&quot;modify.history_archived&quot;, &quot;modify.history_default&quot;, &quot;modify.history_temp&quot;, &quot;modify.history_abandoned&quot;]}}}, {&quot;not&quot;: {&quot;terms&quot;: {&quot;stati&quot;: [&quot;attach.attachment&quot;]}}}, {&quot;terms&quot;: {&quot;parent&quot;: [186395102]}}, {&quot;terms&quot;: {&quot;object_types&quot;: [&quot;Folder&quot;]}}]}}}, &quot;_source&quot;: false}" form="exportResult" />
</div>
<div class="kss-com html" >
<script type="text/javascript">
    $(function(){
        $('#folder_listing_content_6113').off('click').one('click', '#folder_listing_content_6113 a.KSSSortListingBar', function(e) {
            e.preventDefault();
            $('form#folder_listing_form input[name="sort"]').val($(this).data('sort'));
            $('form#folder_listing_form input[name="reverse"]').val($(this).data('reverse'));
            $('form#folder_listing_form').submit();
        });
    })
</script>
</div>
</div></div></div></div></div>
                </div>
              </td>
              <td id="right">
                <div class="visualPadding"><div id="_portlets_docs_folder_right" class="kss-com custom-view" ><div class="kss-com html" ><div style="" class="kss-com" ><div id="" class="kss-com layout layout-vertical" ><div class="layout-block" ><span class="actionMenu"><button style="margin:0 10px 10px 0" class="button cancelBubble"  onclick="showMenu(this, '#drop-menu-2184', '');return false;"><i class="fa fa-plus" ></i> 新建 <i class="fa fa-caret-down"></i></button><div class="actionMenuContent KSSActionMenuContent hidden" id="drop-menu-2184"><ul id="" class="kss-com"><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_folder" data-param1="newFolder" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_folder"><i class="fa fa-folder-o" style="width:15px;color:#FFB74D"></i> 文件夹</a></li><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file" data-ext="docx" data-param1="newDocument" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file"><i class="fa fa-file-word-o" style="width:15px;color:#5C6BC0"></i> Word 文档(.docx)</a></li><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file" data-ext="pptx" data-param1="newDocument" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file"><i class="fa fa-file-powerpoint-o" style="width:15px;color:#FF6E40"></i> PowerPoint 文档(.pptx)</a></li><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file" data-ext="xlsx" data-param1="newDocument" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file"><i class="fa fa-file-excel-o" style="width:15px;color:#43A047"></i> Excel 文档(.xlsx)</a></li><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file" data-ext="html" data-param1="newDocument" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file"><i class="fa fa-file-text-o" style="width:15px;color:#BDBDBD"></i> 页面(.html)</a></li><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file" data-ext="md" data-param1="newDocument" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file"><i class="fa fa-file-code-o" style="width:15px;color:#BDBDBD"></i> 标记文本(.md)</a></li><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file" data-ext="template" data-param1="newDocument" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:new_file"><i class="fa fa-copy" style="width:15px;color:"></i> 根据模板创建</a></li></ul></div></span>
<span class="actionMenu"><button style="margin:0 0 10px 0" class="button cancelBubble"  onclick="showMenu(this, '#drop-menu-8156', '');return false;"><i class="fa fa-upload" ></i> 上传 <i class="fa fa-caret-down"></i></button><div class="actionMenuContent KSSActionMenuContent hidden" id="drop-menu-8156"><ul id="" class="kss-com"><li><a href="#" onclick="uploadMode(this)" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@ajax_content_actions" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@ajax_content_actions">网页上传</a></li><li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.assistant:assistant_upload?param1=client" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.assistant:assistant_upload?param1=client">桌面助手上传</a></li></ul></div></span>
</div><div class="layout-block" ><div id="docs_search_panel" class="kss-com" ><form style="white-space: nowrap;" class="kss-com kss" action="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_search?update%3Aboolean=1&addon_option%3Ajson=%7B%22query_condition%22%3A%20%22%22%2C%20%22view_name%22%3A%20%22zopen.docs%3Aview_folder_listing%22%7D" id="docs_simple_search_form" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_search?update%3Aboolean=1&addon_option%3Ajson=%7B%22query_condition%22%3A%20%22%22%2C%20%22view_name%22%3A%20%22zopen.docs%3Aview_folder_listing%22%7D" method="post"><input type="hidden" name="form.submitted" value="1" /><div style="float: left; border: 1px solid #ccc; width: 70% ;"> <input style="border: none; width: 77%;" placeholder="搜索" autocomplete="off" type="text" name="text" class="kss-com cancelBubble text-line controls"  /> <button type="submit" type="submit" name="form.button.search" id="folder_simple_search_button" name="search" class="hidden submit button" > </button> <label for="folder_simple_search_button" class="button" style="border: none; padding: 7.5px 12px;"><i class="fa fa-search" ></i> </label></div>  <span class="actionMenu"><button style="padding: 8px 12px; margin-left: -1px;" title="更多条件" id="advanced_button" class="button cancelBubble"  onclick="showMenu(this, '#drop-menu-8612', '');return false;"> <i class="fa fa-caret-down"></i></button><div class="actionMenuContent KSSActionMenuContent hidden" id="drop-menu-8612"><ul id="" class="kss-com"><li><a href="#" class="kss-com link kss KSSLoad" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_search?md%3Ajson=%7B%7D&switch%3Aboolean=1&advanced=file&update%3Aboolean=1&addon_option%3Ajson=%7B%22query_condition%22%3A%20%22%22%2C%20%22view_name%22%3A%20%22zopen.docs%3Aview_folder_listing%22%7D" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_search?md%3Ajson=%7B%7D&switch%3Aboolean=1&advanced=file&update%3Aboolean=1&addon_option%3Ajson=%7B%22query_condition%22%3A%20%22%22%2C%20%22view_name%22%3A%20%22zopen.docs%3Aview_folder_listing%22%7D">搜索文件</a></li><li><a href="#" class="kss-com link kss KSSLoad" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_search?md%3Ajson=%7B%7D&switch%3Aboolean=1&advanced=folder&update%3Aboolean=1&addon_option%3Ajson=%7B%22query_condition%22%3A%20%22%22%2C%20%22view_name%22%3A%20%22zopen.docs%3Aview_folder_listing%22%7D" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_search?md%3Ajson=%7B%7D&switch%3Aboolean=1&advanced=folder&update%3Aboolean=1&addon_option%3Ajson=%7B%22query_condition%22%3A%20%22%22%2C%20%22view_name%22%3A%20%22zopen.docs%3Aview_folder_listing%22%7D">搜索文件夹</a></li></ul></div></span><div></div></form><div style="position: relative;" class="kss-com" ><div style="border-radius: 2px; padding: 6px 3px; box-shadow:3px 4px 3px #afafaf; display:none; border: 1px solid #ccc; position: absolute; top: -1px; background-color: #fff; width: 78%; z-index: 2100;" id="live_search_result" class="kss-com" ></div></div><div style="margin-top: 10px;" id="advanced_panel" class="kss-com" ></div><input type="hidden" name="query_json" value="" form="folder_listing_form" /><input type="hidden" name="query_condition" value="" form="add_search_history_form" /><div class="kss-com" ><dl id="portal-tagsearch" class="portlet KSSShowHideArea" kssattr:formid="docs_simple_search_form">
                      <dt class="portletHeader deltaPortletHeader">
                          <div class="portletHeaderContent">
                              <span style="float: right;margin-top: 8px;color: #333;">
            <span class="KSSShowHideTarget hand actionMenu" title="设置">
                <a href="#" class="kss-com link cancelBubble"  onclick="showMenu(this, '#drop-menu-3134', '');return false;"><i class="fa fa-cog fa-small" style="color: #000;"></i></a>
                <div class="actionMenuContent KSSActionMenuContent hidden" id="drop-menu-3134">
                    <ul id="" class="kss-com">
                        <li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@setTagSearch" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@setTagSearch">设置</a></li>
                        <li><a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.views:change_tag" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.views:change_tag">标签改名</a></li>
                    </ul>
                </div>
            </span></span>
                              <span class="KSSShowHideAction">
                                  
                <span class="fa fa-angle-down expanded-icon KSSShowHideTarget"><!-- --></span>
                <span class="fa fa-angle-right collapsed-icon KSSShowHideTarget hidden"><!-- --></span>
             标签组
                              </span>
                          </div>
                      </dt>
                      <dd class="portletItem KSSShowHideTarget"><div id="nav_89ee29d139ada2a40cc26631d02f8ca4" class="navtree" kssattr:templ="templ_89ee29d139ada2a40cc26631d02f8ca4">
                  <script type="text/javascript">
                      var templ_89ee29d139ada2a40cc26631d02f8ca4 = Handlebars.compile('\n        {{#if category}}\n            <span class="toggleExpand">{{title}}{{#if required}}<i class="field-required"></i>{{/if}}</span>\n        {{else}}\n            <a href="javascript:;" style="color: #333;"\n                class="{{#if selected}}submitTag selected{{else}}submitTag{{/if}}" tags="{{sub_tags}}">{{title}}</a>\n        {{/if}}');
                      $('#nav_89ee29d139ada2a40cc26631d02f8ca4').html(render_navtree("%5B%7B%22category%22%3A%20true%2C%20%22expanded%22%3A%20false%2C%20%22title%22%3A%20%22%5Cu90e8%5Cu95e8%22%2C%20%22selected%22%3A%20false%2C%20%22required%22%3A%20false%2C%20%22radio%22%3A%20false%2C%20%22sub_tags%22%3A%20%22%5Cu90e8%5Cu95e8_%5Cu603b%5Cu88c1%5Cu529e_%5Cu4f53%5Cu7cfb%5Cu529e_%5Cu884c%5Cu653f%5Cu90e8_%5Cu4eba%5Cu529b%5Cu8d44%5Cu6e90%5Cu90e8_%5Cu4e1a%5Cu52a1%5Cu53d1%5Cu5c55%5Cu90e8_%5Cu91c7%5Cu8d2d%5Cu90e8_%5Cu5ba1%5Cu8ba1%5Cu5ba4_%5Cu8d22%5Cu52a1%5Cu90e8_%5Cu4fe1%5Cu606f%5Cu4e2d%5Cu5fc3_%5Cu6280%5Cu672f%5Cu4e2d%5Cu5fc3_%5Cu4f01%5Cu4e1a%5Cu6587%5Cu5316%5Cu90e8_%5Cu54c1%5Cu8d28%5Cu7ba1%5Cu7406%5Cu90e8_%5Cu8fdb%5Cu51fa%5Cu53e3%5Cu90e8_%5Cu4e8b%5Cu4e1a%5Cu4e00%5Cu90e8_%5Cu4e8b%5Cu4e1a%5Cu4e8c%5Cu90e8_%5Cu4e8b%5Cu4e1a%5Cu4e09%5Cu90e8_%5Cu4e8b%5Cu4e1a%5Cu56db%5Cu90e8_%5Cu7535%5Cu5668%5Cu516c%5Cu53f8_%5Cu5e7f%5Cu5dde%5Cu516c%5Cu53f8_%5Cu9999%5Cu6e2f%5Cu73af%5Cu7403_%5Cu667a%5Cu80fd%5Cu5bb6%5Cu5c45%5Cu516c%5Cu53f8%22%2C%20%22attributes%22%3A%20%22class%3D%5C%22tagParentNode%20kssattr-tagcategory-input.tags0%5C%22%22%2C%20%22children%22%3A%20%5B%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu603b%5Cu88c1%5Cu529e%22%2C%20%22title%22%3A%20%22%5Cu603b%5Cu88c1%5Cu529e%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4f53%5Cu7cfb%5Cu529e%22%2C%20%22title%22%3A%20%22%5Cu4f53%5Cu7cfb%5Cu529e%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu884c%5Cu653f%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu884c%5Cu653f%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4eba%5Cu529b%5Cu8d44%5Cu6e90%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu4eba%5Cu529b%5Cu8d44%5Cu6e90%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4e1a%5Cu52a1%5Cu53d1%5Cu5c55%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu4e1a%5Cu52a1%5Cu53d1%5Cu5c55%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu91c7%5Cu8d2d%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu91c7%5Cu8d2d%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu5ba1%5Cu8ba1%5Cu5ba4%22%2C%20%22title%22%3A%20%22%5Cu5ba1%5Cu8ba1%5Cu5ba4%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu8d22%5Cu52a1%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu8d22%5Cu52a1%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4fe1%5Cu606f%5Cu4e2d%5Cu5fc3%22%2C%20%22title%22%3A%20%22%5Cu4fe1%5Cu606f%5Cu4e2d%5Cu5fc3%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu6280%5Cu672f%5Cu4e2d%5Cu5fc3%22%2C%20%22title%22%3A%20%22%5Cu6280%5Cu672f%5Cu4e2d%5Cu5fc3%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4f01%5Cu4e1a%5Cu6587%5Cu5316%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu4f01%5Cu4e1a%5Cu6587%5Cu5316%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu54c1%5Cu8d28%5Cu7ba1%5Cu7406%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu54c1%5Cu8d28%5Cu7ba1%5Cu7406%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu8fdb%5Cu51fa%5Cu53e3%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu8fdb%5Cu51fa%5Cu53e3%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu4e00%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu4e00%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu4e8c%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu4e8c%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu4e09%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu4e09%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu56db%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu4e8b%5Cu4e1a%5Cu56db%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu7535%5Cu5668%5Cu516c%5Cu53f8%22%2C%20%22title%22%3A%20%22%5Cu7535%5Cu5668%5Cu516c%5Cu53f8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu5e7f%5Cu5dde%5Cu516c%5Cu53f8%22%2C%20%22title%22%3A%20%22%5Cu5e7f%5Cu5dde%5Cu516c%5Cu53f8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu9999%5Cu6e2f%5Cu73af%5Cu7403%22%2C%20%22title%22%3A%20%22%5Cu9999%5Cu6e2f%5Cu73af%5Cu7403%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu667a%5Cu80fd%5Cu5bb6%5Cu5c45%5Cu516c%5Cu53f8%22%2C%20%22title%22%3A%20%22%5Cu667a%5Cu80fd%5Cu5bb6%5Cu5c45%5Cu516c%5Cu53f8%22%7D%5D%2C%20%22icon%22%3A%20null%7D%2C%20%7B%22category%22%3A%20true%2C%20%22expanded%22%3A%20false%2C%20%22title%22%3A%20%22%5Cu5bc6%5Cu7ea7%22%2C%20%22selected%22%3A%20false%2C%20%22required%22%3A%20false%2C%20%22radio%22%3A%20false%2C%20%22sub_tags%22%3A%20%22%5Cu5bc6%5Cu7ea7_%5Cu79d8%5Cu5bc6_%5Cu5185%5Cu90e8_%5Cu516c%5Cu5f00%22%2C%20%22attributes%22%3A%20%22class%3D%5C%22tagParentNode%20kssattr-tagcategory-input.tags1%5C%22%22%2C%20%22children%22%3A%20%5B%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu79d8%5Cu5bc6%22%2C%20%22title%22%3A%20%22%5Cu79d8%5Cu5bc6%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu5185%5Cu90e8%22%2C%20%22title%22%3A%20%22%5Cu5185%5Cu90e8%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu516c%5Cu5f00%22%2C%20%22title%22%3A%20%22%5Cu516c%5Cu5f00%22%7D%5D%2C%20%22icon%22%3A%20null%7D%2C%20%7B%22category%22%3A%20true%2C%20%22expanded%22%3A%20false%2C%20%22title%22%3A%20%22%5Cu4fdd%5Cu5b58%5Cu671f%5Cu9650%22%2C%20%22selected%22%3A%20false%2C%20%22required%22%3A%20false%2C%20%22radio%22%3A%20false%2C%20%22sub_tags%22%3A%20%22%5Cu4fdd%5Cu5b58%5Cu671f%5Cu9650_%5Cu6c38%5Cu4e45_%5Cu957f%5Cu671f_%5Cu77ed%5Cu671f%22%2C%20%22attributes%22%3A%20%22class%3D%5C%22tagParentNode%20kssattr-tagcategory-input.tags2%5C%22%22%2C%20%22children%22%3A%20%5B%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu6c38%5Cu4e45%22%2C%20%22title%22%3A%20%22%5Cu6c38%5Cu4e45%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu957f%5Cu671f%22%2C%20%22title%22%3A%20%22%5Cu957f%5Cu671f%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu77ed%5Cu671f%22%2C%20%22title%22%3A%20%22%5Cu77ed%5Cu671f%22%7D%5D%2C%20%22icon%22%3A%20null%7D%2C%20%7B%22category%22%3A%20true%2C%20%22expanded%22%3A%20false%2C%20%22title%22%3A%20%22%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22selected%22%3A%20false%2C%20%22required%22%3A%20false%2C%20%22radio%22%3A%20false%2C%20%22sub_tags%22%3A%20%22%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu4f53%5Cu7cfb%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu9500%5Cu552e%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu6280%5Cu672f%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu91c7%5Cu8d2d%5Cu53ca%5Cu5916%5Cu5305%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu751f%5Cu4ea7%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu8d22%5Cu52a1%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_EHS%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu8d28%5Cu91cf%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu8bbe%5Cu5907%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu4eba%5Cu529b%5Cu8d44%5Cu6e90%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu884c%5Cu653f%5Cu53ca%5Cu540e%5Cu52e4%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu4fe1%5Cu606f%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu4ed3%5Cu50a8%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu6c9f%5Cu901a%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757_%5Cu6587%5Cu4ef6%5Cu8d44%5Cu6599%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22attributes%22%3A%20%22class%3D%5C%22tagParentNode%20kssattr-tagcategory-input.tags3%5C%22%22%2C%20%22children%22%3A%20%5B%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4f53%5Cu7cfb%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu4f53%5Cu7cfb%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu9500%5Cu552e%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu9500%5Cu552e%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu6280%5Cu672f%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu6280%5Cu672f%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu91c7%5Cu8d2d%5Cu53ca%5Cu5916%5Cu5305%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu91c7%5Cu8d2d%5Cu53ca%5Cu5916%5Cu5305%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu751f%5Cu4ea7%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu751f%5Cu4ea7%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu8d22%5Cu52a1%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu8d22%5Cu52a1%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22EHS%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22EHS%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu8d28%5Cu91cf%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu8d28%5Cu91cf%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu8bbe%5Cu5907%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu8bbe%5Cu5907%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4eba%5Cu529b%5Cu8d44%5Cu6e90%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu4eba%5Cu529b%5Cu8d44%5Cu6e90%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu884c%5Cu653f%5Cu53ca%5Cu540e%5Cu52e4%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu884c%5Cu653f%5Cu53ca%5Cu540e%5Cu52e4%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4fe1%5Cu606f%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu4fe1%5Cu606f%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu4ed3%5Cu50a8%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu4ed3%5Cu50a8%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu6c9f%5Cu901a%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu6c9f%5Cu901a%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%2C%20%7B%22icon%22%3A%20null%2C%20%22selected%22%3A%20false%2C%20%22children%22%3A%20null%2C%20%22sub_tags%22%3A%20%22%5Cu6587%5Cu4ef6%5Cu8d44%5Cu6599%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%2C%20%22title%22%3A%20%22%5Cu6587%5Cu4ef6%5Cu8d44%5Cu6599%5Cu7ba1%5Cu7406%5Cu677f%5Cu5757%22%7D%5D%2C%20%22icon%22%3A%20null%7D%2C%20%7B%22category%22%3A%20true%2C%20%22attributes%22%3A%20%22class%3D%5C%22tagParentNode%20kssattr-tagcategory-input.tags5%5C%22%20data-expand%3D%5C%22http%3A//192.168.0.38%3A7089/default/isodoc/files/%25E6%25B5%258B%25E8%25AF%2595/%40%40custom_tags%5C%22%22%2C%20%22title%22%3A%20%22%5Cu81ea%5Cu5b9a%5Cu4e49%5Cu6807%5Cu7b7e%22%7D%5D", templ_89ee29d139ada2a40cc26631d02f8ca4, false));
                  </script>
              </div>
           </dd>
                  </dl>
               </div><div class="kss-com html" ><script>
    var search_panels = $("[id='docs_search_panel']:gt(0)");
    if(search_panels){
        $.each(search_panels, function(index, panel){
            $(panel).text('搜索面板在同个界面中只能存在一个，请移除该面板。');
        })
    };
    $('#docs_simple_search_form input[name="text"]').on('keyup', function(){
        $(this).kss('http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:folder_live_search', {'text': $(this).val(), 'result_id': 'live_search_result'});
    });
    $('#docs_simple_search_form input[name="text"]').on('focus', function(){
        if(!$(this).val()){
            return false;
        }
        $(this).keyup();
    });
    $(document).on('click', function(e) {
        var e = e || window.event;
        var elem = e.target || e.srcElement;
        while (elem) {
            if (elem.id && elem.id == 'live_search_result') {
                return;
            }
            elem = elem.parentNode;
        }
        $('#live_search_result').css('display', 'none');
    });
</script></div><style type="text/css" >
        #docs_advanced_search_form tr:hover{background-color: #f6f8fa;}
        #docs_advanced_search_form .field-required{background-color: #f6f8fa;}
        #docs_advanced_search_form{
            background-color: #f6f8fa;
            margin-top: -4px;
            border-radius: 3px;
            padding-bottom: 13px;
            padding-top: 1px;
            padding-left: 5px;
        }
        #docs_advanced_search_form input[type="text"]{
            width: 94%;
        }
        #docs_advanced_search_form select{
            width: 94%;
        }
    </style></div></div><div class="layout-block" >
            <div id="" class="panel kss-com viewlet-folder-info KSSShowHideArea"  data-expand="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_info?expand%3Aboolean=1">
                <div class="panel-heading">
                    <div class="panel-toolbox" ></div>
                    
                   <div class="panel-heading-content KSSShowHideAction KSSShowHideTarget hidden">
                       <span class="fa fa-angle-down expanded-icon"></span>
                       <span class="panel-header">
                           文件夹信息
                       </span>
                   </div>
                   <div class="panel-heading-content KSSShowHideAction KSSShowHideTarget kss KSSAjaxLoad" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_info?expand%3Aboolean=1">
                       <span class="fa fa-angle-right collapsed-icon"></span>
                       <span class="panel-header" >
                           文件夹信息
                       </span>
                   </div>
                </div>
                <div class="panel-body KSSShowHideTarget hidden kss-com viewlet-folder-info" style="" data-expand="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:viewlet_folder_info?expand%3Aboolean=1">
                    
                </div>
                
            </div>
            
<style type="text/css" >
    .viewlet-folder-info p{
        margin: 0;
    }
    </style>
</div><div class="layout-block" >
            <span class="button-group minor-group unity-hight mini subscribe-186395102">
                <button class="kss button" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@subscribeAuthenticatedMember"><i class="fa fa-eye"></i> 关注</button>
                <button class="kss button" style="float: none;padding: 0 5px;" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@subscribeMember">0</button>
            </span>
        <button title="收藏这个文件夹" id="fav-186395102" class="button mini kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.favorites:add_fav"><i class="fa fa-star-o" ></i> 收藏</button></div><div class="layout-block" ><div class="panel kss-com" style="overflow: auto;" ><div style="" class="panel-body"><div style="margin:10px 0;font-size:12px;" class="tags-186395102 setTags KSSSetTags">
    <span style="float:left;padding:7px 2px;" class="discreet"><i class="fa fa-tags"></i></span>
    <span>

<span class="contenttags">
</span>
</span>
    <span class="kss KSSLoad hand discreet" style="float:left;padding:5px 0;" data-action="tag" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@targetContents">+ 标签</span>
</div>
</div></div></div></div></div>
<style type="text/css" >
    .side-button-group button{
        width: 36px;
        height: 26px;
        line-height: 10px;
    }
    .side-edit-button{
        visibility: hidden;
        position: relative;
    }
    #_portlets_docs_folder_right:hover .side-edit-button{
        visibility: visible;
    }
    #right .custom-view{
        margin-left: 2px;
    }
</style>
</div></div></div>
              </td>
            </tr>
          </tbody>
        </table>
        <div id="bottom"></div>
      </div>
      <div id="side"></div>
    </div>
    <div id="xmpp-chat-area">
      <div id="chatpanel" class="hidden"></div>
    </div>
    <iframe name="print_frame" width="0" height="0" frameborder="0" src="about:blank"></iframe>
    <script charset="utf-8" src="/__cache__/workonline/1585376646//zopen.js"></script>
    <script type="text/javascript">
        if ('True' == 'False (Google is dead)') {
            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-24758627-1']);
            _gaq.push(['_setDomainName', 'easydo.cn']);
            _gaq.push(['_setAllowHash', 'false']);
            _gaq.push(['_trackPageview']);
            (function() {
              var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
              var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
        }
    </script>
    <script type="text/javascript">load(['model.js']);</script>
    <script type="text/javascript">$('link[rel="cache-url"]').attr('href', '/__cache__/workonline/1585376646/');load(['{packages_cache_url}/zopen.assistant/resources/js/assistant.js?v=1.2.11', 'filerepos.js'], function(){
$(document).ready(function(){
    function pin_announcement(msg){
        var data = msg;
        if(data.channel_name.split('<>')[0] == 'announcement'){
            // 公告已经置顶，不要重复插入（可能出现在消息断线重连、公告保持未读的场景）
            if($('.pinned-announcement-item[data-msg-id="'+data.id+'"]').length > 0){
                return;
            }

            // 悬浮显示公告
            var announcement_html = Handlebars.compile('<div style="cursor: pointer;" class="floating-announcement" data-msg-id="{{id}}">{{title}}</div>')({
                title: data.subject || data.body.substr(0, 17)+'...',
                id: data.id
            });
            message_float(announcement_html, '公告', true);
        }
    };

    function get_notify_module(){
        return (window.message && message.notify_box) ? message.notify_box : message.notify;
    };

    $(document.body).on('click', '.floating-announcement', function(){ // 查看悬浮公告详情
        var msgid = $(this).data('msg-id');

        get_notify_module().show_msg_detail('announcement', msgid);
        $(this).closest('.jquery-message-content').find('a.close.cancelBubble').click();
        setTimeout(function(){
            if($('.floating-announcement').length == 0){
                if(window.message && message.notify_box){
                    message.notify_box._mark_read('announcement');
                }else{
                    message.utils.mark_read('announcement', 'notify', new Date() / 1000.0);
                }
            }
        }, 1000);
        return false;
    });

    $(document).on('message:update_unreads', function(e, data){ // 页面加载后查询到未读数时，如果有未读公告，也应该置顶显示
        if(data.channel_type == 'notify'){
            $.each(data.unreads, function(_index, unread){
                if(unread.channel_name.split('<>')[0] == 'announcement'){
                    message.client.query({
                        time_start: unread.time_start,
                        limit: unread.count,
                        channel_type: data.channel_type,
                        channel_name: unread.channel_name.replace('<>', ','),
                        event_name: 'notify'
                    }, function(unread_msgs){
                        $.each(unread_msgs, function(_i, msg){
                            pin_announcement(msg);
                        });
                    });
                }
            });
        }
    }).on('notify', function(e, data){ // 收到公告消息时，在置顶公告容器里插入一个公告
        pin_announcement(data);
    });
});

;
$('#bottom').css('min-height', '70px');
EDO.resource_version["zopen.message"]="7.4.11";
if('undefined'=== typeof EDO){EDO = {}; }
EDO.msg_options = {"account": "zopen", "enable_chat": true, "token": "62242b52b7bd7c037329ef23e51865a2", "user": {"id": "users.11608", "name": "\u7b80\u4e1c\u5174"}, "debug": false, "expand": true};
EDO.msg_instance = 'default';
EDO.chat_groups = [];
EDO.notify_channels = [{"name": "workflow", "title": "\u6d41\u7a0b"}, {"name": "sendme", "title": "\u53d1\u9001\u7ed9\u6211\u7684"}, {"name": "mentioned", "title": "\u63d0\u5230\u6211\u7684"}, {"name": "announcement", "title": "\u516c\u544a"}, {"name": "comment", "title": "\u8bc4\u8bba"}, {"name": "subscribe", "title": "\u8ba2\u9605"}, {"name": "default", "title": "\u5176\u4ed6"}];
EDO.servers = {"viewer": "http://192.168.0.38:7089/_viewer", "org": "http://192.168.0.38:7089/org_api", "message": "http://192.168.0.38:7089/_message"};


if(EDO.isMobile || EDO.template_type === 'basic'){
    $(document).ready(function() {
      load('zopen.message:i18n/{lang}.i18n.json', function() {
        // Ensure namespace existence
        if (typeof window.EDO === 'undefined') {
          window.EDO = {};
        }

        // Actual execution
        var requirements = ['rtc.js', 'msgclient.js', 'zopen.message:i18n.js'],
          msg_options = EDO.msg_options;
        if ('WebSocket' in window) {
          requirements.push('mqtt.js');
        } else {
          requirements.push('socketio.js');
        }
        if (msg_options.enable_chat) {
          requirements = requirements.concat(['js/jquery.simplemodal.js', 'js/jquery.edo.selectfile.js',
            EDO.servers.viewer + '/static/core.js',
            EDO.servers.viewer + '/static/viewer.js',
            'paste_image.i18n.js'
          ]);
        }
        load(requirements, function() {
          load(['zopen.message:init.js'], function(){
            if (window.EDO && !EDO.isMobile) {
              // 初始化桌面版
              $(document).on('message:inited', function() {
                load([
                  'zopen.message:notify.js',
                  'zopen.message:unread_counter.js'
                ], function() {
                  message.load_templates(function() {
                    message.notify.init(EDO.notify_channels);
                    message.counter.init('#current_site .site_msg_count');
                    if (EDO.msg_options.enable_chat) {
                      message.chat.init();
                    }
                  });
                });
              });
            } else if (window.EDO && EDO.isMobile) {
              // 移动端已经有专门的通知入口，隐藏桌面版的通知入口
              $('#notify-center').hide();
            }
          });
        });
      });
    });
}
;
EDO.idle=3000;EDO.idleTimeout=0;
onIdle('@zopen.idle_timeout:logout');
assistant_options = {"account": "zopen", "oc_server": "http://192.168.0.38:7089/oc_api", "min_builds": {"windows": 1712, "win64": 1712, "mac": 1712, "linux": 1712}, "site": {"url": "http://192.168.0.38:7089/default/", "name": "\u6587\u6863\u7ba1\u7406"}, "lan_p2p": false, "instance": "default", "upload_server": "http://192.168.0.38:7089/_upload", "version": 5, "user": {"id": "users.11608", "name": "\u7b80\u4e1c\u5174"}, "resumable": true, "download": {}, "server": "http://192.168.0.38:7089/wo_api", "token": "62242b52b7bd7c037329ef23e51865a2", "message_server": "http://192.168.0.38:7089/_message"};
"use load";

            var pageData = JSON.parse(window.localStorage.getItem('folder-186395102'));
            if(pageData && pageData.page > 1 && pageData.page <= 1){
                var text = '上次查看到第 ${page} 页'.replace('${page}', pageData.page);
                var link = '<a href="#" class="kss-com link kss" data-kss="http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:folder_bookmark?bookmark=folder-186395102&form_id=folder_listing_form">继续查看</a>';
                $().message(text + ' ' + link, 'info');
            }else{
                window.localStorage.removeItem('folder-186395102');
            };
"use load";
$('#batchActions').remove();
$('#content .icon-chbactions .fa-check').addClass('hidden');
$('#content .chbactions:hidden').attr('checked', false);
$(document).ksson('rtc:refused', {"delay": 0, "kss": "http://192.168.0.38:7089/default/@zopen.message:login_refused"}, {});
$(document).ksson('rtc:killed', {"delay": 0, "kss": "http://192.168.0.38:7089/default/@zopen.user_setting:login_again"}, {});
$('#folder_listing_form').ksson('refresh-folder', {"delay": 0, "kss": "http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:view_folder_listing?b_start=0"}, {}, true);
$('#folder_listing_form').ksson('content-removed', {"delay": 0, "kss": "http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.docs:view_folder_listing?b_start=0"}, {}, true);
$('#_portlets_docs_folder_right').ksson('customize', {"delay": 0, "kss": "http://192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@zopen.portlet:render?store_key=_portlets_docs_folder_right&store_obj=&id=&store_obj_uid%3Aint=186395102&defaults%3Ajson=%5B%22zopen.docs%3Aviewlet_folder_add_item%22%2C%20%22zopen.docs%3Aviewlet_folder_search%22%2C%20%22zopen.docs%3Aviewlet_folder_info%22%2C%20%22zopen.datacontainer%3Aviewlet_all_sub_fav_button%22%2C%20%22zopen.docs%3Aviewlet_all_tag%22%5D&config_entry%3Aboolean=&action=edit&viewlets%3Ajson=%5B%22zopen.datacontainer%3Aviewlet_all_sub_fav_button%22%2C%20%22zopen.docs%3Aviewlet_all_tag%22%2C%20%22zopen.docs%3Aviewlet_all_tag_groups%22%2C%20%22zopen.docs%3Aviewlet_folder_add_item%22%2C%20%22zopen.docs%3Aviewlet_folder_info%22%2C%20%22zopen.docs%3Aviewlet_folder_search%22%2C%20%22zopen.docs%3Aviewlet_folder_share%22%2C%20%22zopen.views%3Aviewlet_all_site_comment%22%2C%20%22zopen.pages%3Aviewlet_folder_nav_tree%22%5D"}, {});})</script>
  </body>
</html>

"""
from urllib.parse import  quote,unquote
from bs4 import BeautifulSoup
import re
html_doc='''192.168.0.38:7089/default/isodoc/files/%E6%B5%8B%E8%AF%95/@@kss_obj_delete_pulldown'''
print(unquote(html_doc)) #quote url编码 unquote url解码
# html_doc1=html_doc.encode().decode()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.select('span'))