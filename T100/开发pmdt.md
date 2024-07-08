![image-20240626095544429](https://gitee.com/aiiw/images/raw/master/img/image-20240626095544429.png)

![image-20240626101444570](https://gitee.com/aiiw/images/raw/master/img/image-20240626101444570.png)

![image-20240626102644381](https://gitee.com/aiiw/images/raw/master/img/image-20240626102644381.png)

項次加1





 \#add-point:AFTER FIELD xmwtucdocno name="input.a.xmwtucdocno"
       \#應用 a05 樣板自動產生(Version:3)
       \#確認資料無重複
       **IF** **NOT** cl_null**(**g_xmwtuc_m.xmwtucdocno**)** **THEN** 
        **IF** p_cmd **=** 'a' **OR** **(** p_cmd **=** 'u' **AND** **(**g_xmwtuc_m.xmwtucdocno **!=** g_xmwtucdocno_t **))** **THEN** 
          **IF** **NOT** ap_chk_notDup**(**""**,**"SELECT COUNT(*) FROM xmwtuc_t WHERE "**||**"xmwtucent = " **||**g_enterprise**||** " AND "**||**"xmwtucdocno = '"**||**g_xmwtuc_m.xmwtucdocno **||**"'"**,**'std-00004'**,**0**)** **THEN** 
           **NEXT** **FIELD** **CURRENT**
          **END** **IF**
        **END** **IF**
       **END** **IF**