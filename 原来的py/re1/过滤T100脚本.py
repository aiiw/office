import re
sql='''
SELECT UNIQUE 'N',pmdlstus,pmdlsite,pmdldocno,pmdnua001,pmdnua002,xmda033,pmdldocdt,pmdl004, ",  #add pmdnua001,pmdnua002,xmda033 20180529 wujhb  #add pmdlsite by zyh20210203
               "(SELECT pmaal004 FROM pmaal_t WHERE pmaalent=pmdlent AND pmaal001=pmdl004 AND pmaal002='"||g_dlang||"') pmaal004,",
               "               pmdl002, ",
               "(SELECT ooag011 FROM ooag_t WHERE ooagent=pmdlent AND ooag001=pmdl002) ooag011,",
               "               pmdl003, ",
               "(SELECT ooefl003 FROM ooefl_t WHERE ooeflent=pmdlent AND ooefl001=pmdl003 AND ooefl002='"||g_dlang||"') ooefl003,",
               "               pmdn045,pmdoseq,pmdoseq1,pmdoseq2,pmdo003,pmdo001,",
               #" imaal003,imaal004,",  #160510-00019#8 mark
               #160510-00019#8----s
               "(SELECT imaal003 FROM imaal_t WHERE imaalent=pmdoent AND imaal001=pmdo001 AND imaal002='"||g_dlang||"') imaal003,",
               "(SELECT imaal004 FROM imaal_t WHERE imaalent=pmdoent AND imaal001=pmdo001 AND imaal002='"||g_dlang||"') imaal004,",
               #160510-00019#8----e
               " pmdo002,pmdo011, ",
               "(SELECT inaml004 FROM inaml_t WHERE inamlent=pmdoent AND inaml001=pmdo001 AND inaml002=pmdo002 AND inaml003='"||g_dlang||"') inaml004,",
               #ming 20150915 modify ------------------------------------------------------(S) 
               #"               pmdo006,pmdo004,'',pmdo013,pmdo015,pmdo019,pmdo017,pmdn050 ",
               "               pmdo006,pmdo004, ",
               "(SELECT oocal003 FROM oocal_t WHERE oocalent=pmdoent AND oocal001=pmdo004 AND oocal002='"||g_dlang||"') oocal003,",
               "               pmdo013,pmdo015,",
               "(SELECT SUM(QCBA023) QCBA023 FROM QCBA_T WHERE QCBAENT = PMDL_T.PMDLENT AND QCBASITE = PMDL_T.PMDLSITE AND QCBA003 = PMDL_T.PMDLDOCNO AND QCBA004 = PMDO_T.PMDOSEQ) qcba023,",
               "pmdo019,pmdo040,pmdo016, ",
               "               (pmdo006-pmdo015+pmdo016+pmdo017),pmdn050,pmdacnfdt,pmdnud001,pmdnud014 ",  # #20191104 modify
               #ming 20150915 modify ------------------------------------------------------(E) 
               "   FROM pmdl_t,pmdn_t",  #20191104 modify
               "  LEFT JOIN pmdp_t on pmdnent=pmdpent AND pmdnsite=pmdpsite AND pmdndocno=pmdpdocno AND pmdnseq=pmdpseq ",
               "  LEFT JOIN pmda_t on pmdpent=pmdaent AND pmdpsite=pmdasite AND pmdp003=pmdadocno ",
               "   LEFT JOIN xmda_t ",  #add 20180529 wujhb
               "     ON xmdaent = pmdnent AND xmdadocno = pmdnua001 ",
               "  ,pmdo_t ",
               #160510-00019#8----s
               #"   LEFT JOIN (SELECT imaaent,imaa001,imaa009,imaal003,imaal004 FROM imaa_t ",
               #"   LEFT JOIN imaal_t ON imaalent = imaaent AND imaal001=imaa001) ",
               "   LEFT JOIN imaa_t ",  
               #160510-00019#8----e
               "     ON imaaent = pmdoent AND imaa001 = pmdo001 ",
               "  LEFT JOIN imaal_t ON imaaent = imaalent AND imaa001 = imaal001 AND imaal002 = '"||g_dlang||"' ",
               "  WHERE pmdlent   = ? ",
               #"    AND (pmdlsite = '",g_site,"' OR pmdnunit = '",g_site,"') ", #180227-00049#1 mod  OR pmdnunit = g_site #mark by zyh20210309
               "    AND pmdlent   = pmdoent ",
               "    AND pmdldocno = pmdodocno ", 
               "    AND pmdnent   = pmdoent ",
               "    AND pmdndocno = pmdodocno ", 
               "    AND pmdnseq   = pmdoseq ",
               #"    AND xmdaent = pmdnent AND xmdadocno = pmdnua001 ",
               
               "    AND ",ls_wc,
               "    AND ",l_input01 
'''
pv=re.compile(r'(",)|(")|#.+|g_dlang|\|')
print(pv.sub("", sql))
# 在上面，我们已将一个正则表达式编译成 Pattern 对象，接下来，我们就可以利用 pattern 的一系列方法对文本进行匹配查找了。Pattern 对象的一些常用方法主要有：

# match 方法
# search 方法
# findall 方法
# finditer 方法
# split 方法
# sub 方法
# subn 方法
