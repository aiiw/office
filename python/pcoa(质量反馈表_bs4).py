import requests
from urllib.parse import  quote,unquote
from bs4 import BeautifulSoup
import re




html_doc='''


<p style="TEXT-ALIGN: left">
    <meta name="ProgId" content="Word.Document"/>
    <meta name="Generator" content="Microsoft Word 12"/>
    <meta name="Originator" content="Microsoft Word 12"/>
    <link rel="File-List" href="质量信息反馈表.files/filelist.xml"/>
    <link rel="dataStoreItem" href="质量信息反馈表.files/item0007.xml" target="质量信息反馈表.files/props0008.xml"/>
    <link rel="themeData" href="质量信息反馈表.files/themedata.thmx"/>
    <link rel="colorSchemeMapping" href="质量信息反馈表.files/colorschememapping.xml"/>
</p>
<div class="Section1" align="center">
    <p class="MsoNormal">
        <br/>
    </p>
    <table style="BORDER-BOTTOM: rgb(0,0,0) 0px solid; BORDER-LEFT: rgb(0,0,0) 0px solid; WIDTH: 735px; BORDER-COLLAPSE: collapse; TABLE-LAYOUT: fixed; MARGIN-LEFT: 6.75pt; BORDER-TOP: rgb(0,0,0) 0px solid; MARGIN-RIGHT: 6.75pt; BORDER-RIGHT: rgb(0,0,0) 0px solid" class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="703" align="center" data-sort="sortDisabled">
        <colgroup class="ue-tableresize-colgroup">
            <col style="WIDTH: 80px"/>
            <col style="WIDTH: 151px"/>
            <col style="WIDTH: 80px"/>
            <col style="WIDTH: 116px"/>
            <col style="WIDTH: 103px"/>
            <col style="WIDTH: 205px"/>
        </colgroup>
        <tbody>
            <tr class="firstRow">
                <th style="BORDER-BOTTOM-COLOR: rgb(255,255,255); BACKGROUND-COLOR: rgb(255,255,255); BORDER-TOP-COLOR: rgb(255,255,255); BORDER-RIGHT-COLOR: rgb(255,255,255); BORDER-LEFT-COLOR: rgb(255,255,255); WORD-BREAK: break-all" height="36" valign="center" rowspan="1" colspan="6" align="middle">
                    <p style="text-align: center;">
                        <span style="TEXT-ALIGN: center; FONT-FAMILY: 宋体; FONT-SIZE: 16px">广东万事泰集团有限公司</span>
                    </p>
                    <p style="text-align: center;">
                        <span style="TEXT-ALIGN: center; FONT-FAMILY: 宋体; FONT-SIZE: 16px"><strong style="TEXT-ALIGN: center; WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体; FONT-SIZE: 16pt">质 量 信 息 反 馈 表</span></strong></span>
                    </p>
                </th>
            </tr>
            <tr style="HEIGHT: 21.6pt; mso-yfti-irow: 1">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 21.6pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">部门/车间</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"></span>
                    </p>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 21.6pt; WORD-BREAK: break-all; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <input style="TEXT-ALIGN: left; WIDTH: 100px; HEIGHT: 20px; FONT-SIZE: 14px" title="部门/车间" align="left" type="text" name="DATA_6" hidden="0"/><img style="CURSOR: pointer" class="USER" title="部门人员控件:部门/车间" border="0" name="OTHER_1" alt="" align="absMiddle" src="/static/images/form/orgselect.png" type="1" value="部门/车间"/>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 21.6pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">数量</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"></span>
                    </p>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 21.6pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <input style="TEXT-ALIGN: left; WIDTH: 80px; HEIGHT: 20px; FONT-SIZE: 14px" title="数量" align="left" type="text" name="DATA_2" hidden="0"/>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 21.6pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"></span>
                    </p>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 21.6pt; WORD-BREAK: break-all; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期" align="left" type="text" name="DATA_4" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期" border="0" name="OTHER_2" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期" classname="DATE" date_format="yyyy-MM-dd"/>
                </td>
            </tr>
            <tr style="HEIGHT: 20.9pt; mso-yfti-irow: 2">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 20.9pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">生产单号</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"></span>
                    </p>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 20.9pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="生产单号" align="left" type="text" name="DATA_7" hidden="0"/>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 20.9pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">客户代号</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"></span>
                    </p>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 20.9pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <input style="TEXT-ALIGN: left; WIDTH: 80px; HEIGHT: 20px; FONT-SIZE: 14px" title="客户代号" align="left" type="text" name="DATA_3" hidden="0"/>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 20.9pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">产品规格名称</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"></span>
                    </p>
                </td>
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; BACKGROUND-COLOR: rgb(255,255,255); PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 20.9pt; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm">
                    <input style="TEXT-ALIGN: left; WIDTH: 160px; HEIGHT: 20px; FONT-SIZE: 14px" title="产品规格名称" align="left" type="text" name="DATA_5" hidden="0"/>
                </td>
            </tr>
            <tr style="HEIGHT: 17.6pt; mso-yfti-irow: 3">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 17.6pt; WORD-BREAK: break-all; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" valign="top" colspan="6">
                    <p style="TEXT-ALIGN: left; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 168.0pt 330.75pt" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">站别：</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt; mso-bidi-font-weight: bold"><select style="WIDTH: 120px" title="站别:" name="DATA_1"><option value="制程检验">
                            制程检验
                        </option>
                        <option value="成品检验">
                            成品检验
                        </option>
                        <option value="来料检验">
                            来料检验
                        </option>
                        <option value="" selected="selected"></option></select></span>
                    </p>
                </td>
            </tr>
            <tr>
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid" height="19" valign="top" rowspan="1" colspan="6" align="left">
                    <strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">&nbsp;反馈内容</span></strong><span style="FONT-FAMILY: 宋体">（反馈描述需简洁明了、突出问题重点）：</span>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 53pt; mso-yfti-irow: 4">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; HEIGHT: 53pt; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" valign="top" colspan="6">
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 42.0pt" class="MsoNormal">
                        <textarea style="WIDTH: 690px; HEIGHT: 70px; FONT-SIZE: 14px" title="反馈内容" name="DATA_8" rich="0"></textarea><br/>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 13.3pt; mso-yfti-irow: 5">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="-8" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">发出反馈部门：</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="发出反馈部门" align="left" type="text" name="DATA_44" hidden="0"/><span lang="EN-US">&nbsp;<img style="CURSOR: pointer" class="USER" title="部门人员控件:发出反馈部门" border="0" name="OTHER_3" alt="" align="absMiddle" src="/static/images/form/orgselect.png" type="1" value="发出反馈部门"/>&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="TEXT-ALIGN: left; WIDTH: 110px; HEIGHT: 20px; FONT-SIZE: 14px" title="签名:" align="left" type="text" name="DATA_11" hidden="0"/><span lang="EN-US">&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期:" align="left" type="text" name="DATA_12" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期:" border="0" name="OTHER_4" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期:" classname="DATE" date_format="yyyy-MM-dd"/><strong><span lang="EN-US"></span></strong></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 46.5pt; mso-yfti-irow: 6">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; HEIGHT: 46.5pt; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" valign="top" colspan="6">
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-SIZE: 14px"><strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">总检处理意见:</span></strong></span>
                    </p>
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt; mso-bidi-font-weight: bold" lang="EN-US"><textarea style="WIDTH: 690px; HEIGHT: 40px; FONT-SIZE: 14px" title="总检处理意见:" name="DATA_13" rich="0"></textarea></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 14.25pt; mso-yfti-irow: 7">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="5" valign="top" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt">&nbsp;<span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="WIDTH: 100px; FONT-SIZE: 14px" class="AUTO" title="签名:1" datafld="SYS_USERNAME" value="{MACRO}" type="text" name="DATA_16" hidden="0"/><span lang="EN-US">&nbsp; </span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期：1" align="left" type="text" name="DATA_22" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期：1" border="0" name="OTHER_5" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期：1" classname="DATE" date_format="yyyy-MM-dd"/></span>
                    </p>
                </td>
            </tr>
            <tr>
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid" height="17" valign="top" rowspan="1" colspan="6" align="left">
                    <strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">&nbsp;<span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">反馈单位处理意见：</span></span></strong>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 47.8pt; mso-yfti-irow: 8">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="48" valign="top" colspan="6">
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"></span><strong><span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><textarea style="MARGIN: 0px; WIDTH: 694px; HEIGHT: 40px; FONT-SIZE: 14px" title="反馈单位处理意见：" name="DATA_19" rich="0"></textarea></span></strong><br/>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 15.8pt; mso-yfti-irow: 9">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="12" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="WIDTH: 100px; FONT-SIZE: 14px" class="AUTO" title="签名：2" datafld="SYS_USERNAME" value="{MACRO}" type="text" name="DATA_20" hidden="0"/><span lang="EN-US">&nbsp;&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期：2" align="left" type="text" name="DATA_21" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期：2" border="0" name="OTHER_6" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期：2" classname="DATE" date_format="yyyy-MM-dd"/></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 46.6pt; mso-yfti-irow: 10">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="66" valign="top" colspan="6">
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-SIZE: 14px"><strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">质检科处理意见：</span></strong></span>
                    </p>
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px"><textarea style="WIDTH: 690px; HEIGHT: 40px; FONT-SIZE: 14px" title="质检科处理意见" name="DATA_38" rich="0"></textarea></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 17.6pt; mso-yfti-irow: 11">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="12" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 171.75pt" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="WIDTH: 100px; FONT-SIZE: 14px" class="AUTO" title="签名：3" datafld="SYS_USERNAME" value="{MACRO}" type="text" name="DATA_23" hidden="0"/><span lang="EN-US">&nbsp;&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期：3" align="left" type="text" name="DATA_24" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期：3" border="0" name="OTHER_7" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期：3" classname="DATE" date_format="yyyy-MM-dd"/><strong><span lang="EN-US"></span></strong></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 45.45pt; mso-yfti-irow: 12">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; HEIGHT: 45.45pt; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" valign="top" colspan="6">
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 171.75pt" class="MsoNormal">
                        <span style="FONT-SIZE: 14px"><strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">责任单位一处理意见：</span></strong></span>
                    </p>
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 171.75pt" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px"><textarea style="WIDTH: 690px; HEIGHT: 40px; FONT-SIZE: 14px" title="责任单位处理一意见" name="DATA_39" rich="0"></textarea></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 14.45pt; mso-yfti-irow: 13">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="8" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 171.75pt" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="WIDTH: 100px; FONT-SIZE: 14px" class="AUTO" title="签名：4" datafld="SYS_USERNAME" value="{MACRO}" type="text" name="DATA_25" hidden="0"/><span lang="EN-US">&nbsp;&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期：4" align="left" type="text" name="DATA_26" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期：4" border="0" name="OTHER_8" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期：4" classname="DATE" date_format="yyyy-MM-dd"/><strong><span lang="EN-US"></span></strong></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 36pt; mso-yfti-irow: 14">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; HEIGHT: 36pt; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" valign="top" colspan="6" align="left">
                    <span style="FONT-SIZE: 14px"><strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">责任单位二处理意见:</span></strong></span>
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 171.75pt" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px"><textarea style="WIDTH: 691px; HEIGHT: 40px; MARGIN-LEFT: 0px; FONT-SIZE: 14px; MARGIN-RIGHT: 0px" title="责任单位二处理意见" name="DATA_40" rich="0"></textarea></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 10.3pt; mso-yfti-irow: 15">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; HEIGHT: 10.3pt; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" valign="top" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 171.75pt" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="WIDTH: 100px; FONT-SIZE: 14px" class="AUTO" title="签名：5" datafld="SYS_USERNAME" value="{MACRO}" type="text" name="DATA_27" hidden="0"/><span lang="EN-US">&nbsp;&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期：5" align="left" type="text" name="DATA_28" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期：5" border="0" name="OTHER_9" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期：5" classname="DATE" date_format="yyyy-MM-dd"/><strong><span lang="EN-US"></span></strong></span>
                    </p>
                </td>
            </tr>
            <tr>
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid" valign="top" rowspan="1" colspan="6" align="left">
                    <strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">&nbsp;<span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">生产部经理处理意见：</span></span></strong>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 47.05pt; mso-yfti-irow: 16">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="48" valign="top" colspan="6">
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly; tab-stops: 171.75pt" class="MsoNormal">
                        <textarea style="WIDTH: 695px; HEIGHT: 40px; MARGIN-LEFT: 0px; FONT-SIZE: 14px; MARGIN-RIGHT: 0px" title="事业部经理处理意见" name="DATA_41" rich="0"></textarea><br/>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 14.15pt; mso-yfti-irow: 17">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="10" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="WIDTH: 100px; FONT-SIZE: 14px" class="AUTO" title="签名：6" datafld="SYS_USERNAME" value="{MACRO}" type="text" name="DATA_29" hidden="0"/><span lang="EN-US">&nbsp;&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期：6" align="left" type="text" name="DATA_30" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期：6" border="0" name="OTHER_10" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期：6" classname="DATE" date_format="yyyy-MM-dd"/><strong><span lang="EN-US"></span></strong></span>
                    </p>
                </td>
            </tr>
            <tr>
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-TOP: rgb(0,0,0) 1px solid; BORDER-RIGHT: rgb(0,0,0) 1px solid" height="18" valign="top" rowspan="1" colspan="6" align="left">
                    <span style="FONT-SIZE: 14px"><strong style="WHITE-SPACE: normal"><span style="FONT-FAMILY: 宋体">&nbsp;最终处理（品检中心经理）：</span></strong></span>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 46.85pt; mso-yfti-irow: 18">
                <td style="BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="31" valign="top" colspan="6">
                    <p style="mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <textarea style="WIDTH: 690px; HEIGHT: 40px; FONT-SIZE: 14px" title="最终处理(品质部经理)" name="DATA_42" rich="0"></textarea><br/>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 11.9pt; mso-yfti-irow: 19">
                <td style="BORDER-BOTTOM: rgb(0,0,0) 1px solid; BORDER-LEFT: rgb(0,0,0) 1px solid; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; BORDER-TOP-WIDTH: 0px; WORD-BREAK: break-all; BORDER-RIGHT: rgb(0,0,0) 1px solid; PADDING-TOP: 0cm" height="6" colspan="6">
                    <p style="TEXT-ALIGN: center; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 12pt"><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">签名：</span><input style="WIDTH: 100px; FONT-SIZE: 14px" class="AUTO" title="签名：7" datafld="SYS_USERNAME" value="{MACRO}" type="text" name="DATA_31" hidden="0"/><span lang="EN-US">&nbsp;&nbsp;</span><span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">日期：</span><input style="TEXT-ALIGN: left; WIDTH: 120px; HEIGHT: 20px; FONT-SIZE: 14px" title="日期：7" align="left" type="text" name="DATA_32" hidden="0"/><img style="WIDTH: 18px; HEIGHT: 18px; CURSOR: pointer" class="DATE" title="日期控件:日期：7" border="0" name="OTHER_11" alt="" align="absMiddle" src="/static/images/form/calendar.png" value="日期：7" classname="DATE" date_format="yyyy-MM-dd"/><strong style="mso-bidi-font-weight: normal"><span lang="EN-US"></span></strong></span>
                    </p>
                </td>
            </tr>
            <tr style="PAGE-BREAK-INSIDE: avoid; HEIGHT: 15.1pt; mso-yfti-irow: 22; mso-yfti-lastrow: yes">
                <td style="BORDER-BOTTOM: 0px; TEXT-ALIGN: left; BORDER-LEFT: 0px; PADDING-BOTTOM: 0cm; PADDING-LEFT: 5.4pt; PADDING-RIGHT: 5.4pt; HEIGHT: 15.1pt; WORD-BREAK: break-all; BORDER-TOP: 1px solid; BORDER-RIGHT: 0px; PADDING-TOP: 0cm" valign="center" colspan="6" align="middle">
                    <p style="TEXT-ALIGN: right; MARGIN-RIGHT: 28pt; mso-element: frame; mso-element-frame-hspace: 9.0pt; mso-element-wrap: around; mso-element-anchor-vertical: page; mso-element-anchor-horizontal: margin; mso-element-top: 46.55pt; mso-height-rule: exactly" class="MsoNormal">
                        <span style="FONT-FAMILY: 宋体; FONT-SIZE: 14px">&nbsp;&nbsp;&nbsp; F.PZB.0077.02</span>
                    </p>
                </td>
            </tr>
        </tbody>
    </table>
    <p style="MARGIN-RIGHT: 28pt" class="MsoNormal">
        <span lang="EN-US">&nbsp;</span>
    </p>
</div>
'''

soup = BeautifulSoup(html_doc, 'html.parser')
ls = soup.find_all(['textarea', 'input'],attrs={"name":re.compile(r'DATA')})

for item in ls:
	print(item.attrs['name'],"\"",item.attrs['title'],"\"",",",end="")

# 直接检索id属性和不确定值，正则表达式
#           soup.find_all(id=re.compile("link"))