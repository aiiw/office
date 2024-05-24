from bs4 import BeautifulSoup
import re
import html
import requests,json
from urllib.parse import  quote,unquote
import xlwings as xw
# 192.168.10.250
html_doc='''<tbody>
    <tr style="display: table-row;">
        <td colspan="6" class="tdTitle"></td>
    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="Code">工号：</label>
        </td>
        <td class="tdInput">
            <input class="sepInput ui-widget ui-widget-content ui-input ui-field-readonly" type="text" id="Code"
                name="Code" ui-type="text" readonly="readonly" maxlength="20" style="width: 158px;"
                data-bind="value: mst.Code" val-options="{&quot;required&quot;:true}" autofocus="autofocus"
                onblur="SetFPCode()" title="11669">
        </td>
        <td class="tdLabel">
            <label class="form-field-label " for="Name">姓名：</label>
        </td>
        <td colspan="2" class="tdInput">
            <input type="text" class="sepInput ui-widget ui-widget-content ui-input ui-field-required" id="Name"
                name="Name" ui-type="text" onblur="ConvertName()" maxlength="100" style="width: 132px;"
                data-bind="value: mst.Name" val-options="{&quot;required&quot;:true}" title="麦燕霞">
            <input type="text" id="MnemonicCode" name="MnemonicCode" ui-type="text" maxlength="100"
                style="width: 100px;" readonly="readonly" data-bind="value: mst.MnemonicCode"
                val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="MYX">
        </td>
        <td rowspan="5" style="text-align:center">
            <input type="hidden" id="readPhoto" name="readPhoto">
            <img id="EmpPhoto" name="EmpPhoto" title="照片" style="width: 120px; height: 160px;"
                src="data:image/jpg;base64,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"
                data-bind="src: mst.EmpPhoto">
        </td>
    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="DepartmentName">部门：</label>
        </td>
        <td class="tdInput">
            <input type="hidden" id="DeptID" name="DeptID" data-bind="value: mst.DeptID" value="22">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text"
                    class="sepInput ui-buttonEdit-input ui-field-readonly" id="DepartmentCode" name="DepartmentCode"
                    readonly="readonly" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.DepartmentCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;callback&quot;:&quot;DeptChange&quot;,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/SelectDept/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;SelectMode&quot;:&quot;1&quot;, &quot;ExpandAll&quot;:&quot;0&quot;,&quot;RtnFillField&quot;:&quot;DeptID=key,DepartmentName=title,DepartmentCode=DepartmentCode&quot;,&quot;FormId&quot;:&quot;#mstForm&quot;,&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;DepartmentCode&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"><button
                    type="button" class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false" disabled="disabled"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="DepartmentName" name="DepartmentName" ui-type="text" maxlength="10"
                readonly="readonly" style="width: 80px; margin-left: -3px;" data-bind="value: mst.DepartmentName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="财务会计部">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="PostName">岗位：</label>
        </td>
        <td colspan="3" class="tdInput">
            <input type="hidden" id="PostID" name="PostID" data-bind="value: mst.PostID" value="1548">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text"
                    class="sepInput ui-buttonEdit-input ui-field-required" id="PostCode" name="PostCode"
                    ui-type="buttonEdit" maxlength="10" style="width:80px;" data-bind="value: mst.PostCode"
                    val-options="{&quot;required&quot;:true}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;PostCode&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;,&quot;WhereField&quot;:&quot;DeptID&quot;}},&quot;beforeRequest&quot;:&quot;onChangePostData&quot;}}"><button
                    type="button" class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="PostName" name="PostName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 138px; margin-left: -3px;" data-bind="value: mst.PostName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="应收账款会计">
        </td>
    </tr>
    <tr style="display: table-row;">

        <td class="tdLabel">
            <label class="form-field-label" for="IdentityNumber">身份证号:</label>
        </td>
        <td class="tdInput">

            <input type="text" id="IdentityNumber" name="IdentityNumber" onblur="idDecode()" ui-type="text"
                maxlength="20" style="width: 158px;" data-bind="value:mst.IdentityNumber"
                val-options="{&quot;required&quot;:false}" class="ui-widget ui-widget-content ui-input"
                title="445321199111135289">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="Sex">性别：</label>
        </td>
        <td class="tdInput">
            <select id="Sex" name="Sex" ui-type="dropdownlist" val-options="{&quot;required&quot;:false}"
                style="width: 155px;" data-bind="value: mst.Sex"
                ui-options="{&quot;url&quot;:&quot;/Common/GetDropDownListItems&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;DataSource&quot;:&quot;gender&quot;}}"
                class="ui-widget ui-widget-content ui-dropdownlist">
                <option value=""></option>
                <option value="1">男</option>
                <option value="2">女</option>
            </select>
        </td>

    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="IdentityNumber">职务：</label>
        </td>
        <td class="tdInput">
            <input type="hidden" id="JobID" name="JobID" data-bind="value: mst.JobID" value="0">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="JobCode"
                    name="JobCode" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.JobCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;JobCode&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="JobName" name="JobName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.JobName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="JobRankName">职级：</label>
        </td>

        <td class="tdInput">
            <input type="hidden" id="JobRankID" name="JobRankID" data-bind="value: mst.JobRankID" value="8">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text"
                    class="sepInput ui-buttonEdit-input ui-field-readonly" id="JobRankCode" name="JobRankCode"
                    readonly="readonly" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.JobRankCode" val-options="{&quot;required&quot;:true}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;JobRankCode&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"><button
                    type="button" class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false" disabled="disabled"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="JobRankName" name="JobRankName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.JobRankName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="08主办、主任助理、中级技工、班长">
        </td>


    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="PayTypeName">计薪方式：</label>
        </td>
        <td class="tdInput">

            <input type="hidden" id="PayTypeID" name="PayTypeID" data-bind="value: mst.PayTypeID" value="1">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text"
                    class="sepInput ui-buttonEdit-input ui-field-required" id="PayTypeCode" name="PayTypeCode"
                    ui-type="buttonEdit" maxlength="10" style="width:58px;" data-bind="value: mst.PayTypeCode"
                    val-options="{&quot;required&quot;:true}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;PayTypeName&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"><button
                    type="button" class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="PayTypeName" name="PayTypeName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.PayTypeName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="计时">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="JobLevelID">职等：</label>
        </td>
        <td class="tdInput">

            <input type="hidden" id="JobLevelID" name="JobLevelID" data-bind="value: mst.JobLevelID" value="0">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="JobLevelCode"
                    name="JobLevelCode" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.JobLevelCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;JobLevelName&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="JobLevelName" name="JobLevelName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.JobLevelName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="">

        </td>

    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="HireDate">入职日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input
                    class="sepInput ui-datepicker-input hasDatepicker ui-field-required" type="text" id="HireDate"
                    name="HireDate" ui-type="date" maxlength="10" style="width: 140px;" value="2023-04-21"
                    data-format="d:Y-M-d" data-bind="value: mst.HireDate"
                    val-options="{&quot;required&quot;:true}"><button type="button" name="btn_date_HireDate"
                    class="ui-widget ui-state-default"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="ProbationPeriod">试用期：</label>
        </td>
        <td class="tdInput" nowrap="nowrap">
            <input type="text" id="ProbationPeriod" name="ProbationPeriod" ui-type="text" maxlength="100" value="3"
                style="width: 130px;" onchange="timeChange();" data-bind="value: mst.ProbationPeriod"
                val-options="{&quot;required&quot;:false}" class="ui-widget ui-widget-content ui-input" title="">
            <label class="form-field-label" for="">月</label>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="DimissionDate">离职日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="DimissionDate"
                    name="DimissionDate" ui-type="date" maxlength="10" readonly="readonly" style="width: 140px;"
                    data-format="d:Y-M-d" data-bind="value: mst.DimissionDate"
                    val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker ui-field-readonly" disabled="disabled"><button
                    type="button" name="btn_date_DimissionDate" class="ui-widget ui-state-default" disabled="disabled"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" style="width: 85px!important" for="PlanTurnDate">预转正日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="PlanTurnDate"
                    name="PlanTurnDate" ui-type="date" maxlength="10" style="width: 140px;" value="2023-07-21"
                    data-format="d:Y-M-d" data-bind="value: mst.PlanTurnDate" val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker"><button type="button" name="btn_date_PlanTurnDate"
                    class="ui-widget ui-state-default"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="TurnDate">转正日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="TurnDate"
                    name="TurnDate" ui-type="date" maxlength="10" style="width: 140px;" readonly="readonly"
                    data-format="d:Y-M-d" data-bind="value: mst.TurnDate" val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker ui-field-readonly" disabled="disabled"><button
                    type="button" name="btn_date_TurnDate" class="ui-widget ui-state-default" disabled="disabled"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="TurnStatus">转正状态：</label>
        </td>
        <td class="tdInput">
            <select id="TurnStatus" name="TurnStatus" ui-type="dropdownlist" val-options="{&quot;required&quot;:false}"
                readonly="readonly" style="width: 160px;" data-bind="value: mst.TurnStatus"
                ui-options="{&quot;url&quot;:&quot;/Common/GetDropDownListItems&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;DataSource&quot;:&quot;TurnStatus&quot;}}"
                class="ui-widget ui-widget-content ui-dropdownlist ui-field-readonly" disabled="disabled">
                <option value=""></option>
                <option value="1">试用期</option>
                <option value="2">正式员工</option>
            </select>
        </td>
    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="NationName">民族：</label>
        </td>
        <td class="tdInput border_c">
            <input type="hidden" id="NationID" name="NationID" data-bind="value: mst.NationID" value="1">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="NationCode"
                    name="NationCode" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.NationCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;NationName&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="NationName" name="NationName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.NationName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="汉族">

        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="HomeName">籍贯：</label>
        </td>
        <td class="tdInput">
            <input type="hidden" id="HomeID" name="HomeID" data-bind="value: mst.HomeID" value="278">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="HomeCode"
                    name="HomeCode" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.HomeCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;HomeName&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="HomeName" name="HomeName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.HomeName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="广东省云浮市">

        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="marriage">婚姻状况：</label>
        </td>
        <td class="tdInput">
            <select id="marriage" name="marriage" ui-type="dropdownlist" style="width: 160px;"
                data-bind="value: mst.marriage" val-options="{&quot;required&quot;:false}"
                ui-options="{&quot;url&quot;:&quot;/Common/GetDropDownListItems&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;DataSource&quot;:&quot;MarriedSts&quot;}}"
                class="ui-widget ui-widget-content ui-dropdownlist">
                <option value=""></option>
                <option value="0">未婚</option>
                <option value="1">已婚</option>
                <option value="2">离婚</option>
                <option value="3">丧偶</option>
                <option value="4">其它</option>
            </select>
        </td>
    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="DegreeName">学历：</label>
        </td>
        <td class="tdInput">

            <input type="hidden" id="DegreeID" name="DegreeID" data-bind="value: mst.DegreeID" value="16">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text"
                    class="sepInput ui-buttonEdit-input ui-field-required" id="DegreeCode" name="DegreeCode"
                    ui-type="buttonEdit" maxlength="10" style="width:58px;" data-bind="value: mst.DegreeCode"
                    val-options="{&quot;required&quot;:true}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;DegreeName&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"><button
                    type="button" class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="DegreeName" name="DegreeName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.DegreeName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="大专">

        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="EmpNatureID">员工性质：</label>
        </td>
        <td class="tdInput">

            <input type="hidden" id="EmpNatureID" name="EmpNatureID" data-bind="value: mst.EmpNatureID" value="1">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="NatureCode"
                    name="NatureCode" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.NatureCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;NatureName&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="NatureName" name="NatureName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst.NatureName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="正式工">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="IsDirect">直/间接：</label>
        </td>
        <td class="tdInput">
            <select id="IsDirect" name="IsDirect" ui-type="dropdownlist" style="width: 160px;"
                data-bind="value: mst.IsDirect" val-options="{&quot;required&quot;:false}"
                ui-options="{&quot;url&quot;:&quot;/Common/GetDropDownListItems&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;DataSource&quot;:&quot;DL_IDLSts&quot;}}"
                class="ui-widget ui-widget-content ui-dropdownlist">
                <option value=""></option>
                <option value="0">直接</option>
                <option value="1">间接</option>
            </select>
        </td>
    </tr>
    <tr style="display: table-row;">
        <td class="tdLabel">
            <label class="form-field-label" for="DirectSuperiorID">直接上级：</label>
        </td>
        <td class="tdInput">

            <input type="hidden" id="DirectSuperiorID" name="DirectSuperiorID" data-bind="value: mst.DirectSuperiorID"
                value="0">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="DirectSuperiorCode"
                    name="DirectSuperiorCode" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst.DirectSuperiorCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;DirectSuperiorID&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="DirectSuperiorName" name="DirectSuperiorName" ui-type="text" maxlength="10"
                readonly="readonly" style="width: 80px; margin-left: -3px;" data-bind="value: mst.DirectSuperiorName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="">

        </td>
        <td class="tdLabel"><label class="form-field-label" for="DirectSuperiorJobName">上级职务：</label> </td>
        <td class="tdInput">
            <input type="text" id="DirectSuperiorJobName" name="DirectSuperiorJobName" ui-type="text" maxlength="100"
                style="width: 156px;" readonly="readonly" data-bind="value: mst.DirectSuperiorJobName"
                val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="">
        </td>
        <td class="tdLabel"><label class="form-field-label" for="DirectSuperiorPostName">上级岗位：</label> </td>
        <td class="tdInput">
            <input type="text" id="DirectSuperiorPostName" name="DirectSuperiorPostName" ui-type="text" maxlength="100"
                style="width: 156px;" readonly="readonly" data-bind="value: mst.DirectSuperiorPostName"
                val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="">
        </td>
    </tr>

    <tr>
        <td class="tdLabel">
            <label class="form-field-label" for="_state">员工状态：</label></td>
        <td class="tdInput">
            <input type="text" id="_state" name="_state" ui-type="text" maxlength="40" style="width: 140px;"
                readonly="readonly" data-bind="value: mst._state" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="在职">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="_htqsr">合同起始：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="_htqsr" name="_htqsr"
                    ui-type="date" maxlength="100" style="width: 140px;" readonly="readonly" data-format="d:Y-M-d"
                    data-bind="value: mst._htqsr" val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker ui-field-readonly" disabled="disabled"><button
                    type="button" name="btn_date__htqsr" class="ui-widget ui-state-default" disabled="disabled"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>

        <td class="tdLabel">
            <label class="form-field-label" for="_htzzr">合同终止：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="_htzzr" name="_htzzr"
                    ui-type="date" maxlength="100" style="width: 140px;" readonly="readonly" data-format="d:Y-M-d"
                    data-bind="value: mst._htzzr" val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker ui-field-readonly" disabled="disabled"><button
                    type="button" name="btn_date__htzzr" class="ui-widget ui-state-default" disabled="disabled"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>


    </tr>

    <tr>
        <td class="tdLabel">
            <label class="form-field-label" for="_isjjr">享有节假日：</label>
        </td>
        <td class="tdInput">
            <select id="_isjjr" name="_isjjr"
                class="sepInput ui-widget ui-widget-content ui-dropdownlist ui-field-required" ui-type="dropdownlist"
                style="width: 140px;" data-bind="value: mst._isjjr" val-options="{&quot;required&quot;:true}"
                ui-options="{&quot;url&quot;:&quot;/Common/GetDropDownListItems&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;DataSource&quot;:&quot;jblx&quot;}}">
                <option value=""></option>
                <option value="否">否</option>
                <option value="是">是</option>
            </select>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="_gongl">工龄(年)：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="_gongl" name="_gongl" ui-type="text" maxlength="50" style="width: 156px;"
                readonly="readonly" data-bind="value: mst._gongl" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="3">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="_bName">默认班制：</label>
        </td>
        <td class="tdInput">
            <input type="hidden" id="_bID" name="_bID" data-bind="value: mst._bID" value="21">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="_bCode" name="_bCode"
                    ui-type="buttonEdit" maxlength="10" style="width:58px;" data-bind="value: mst._bCode"
                    val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;_bCode&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="_bName" name="_bName" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst._bName"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="集团办公室               ">
        </td>

    </tr>
    <tr>
        <td class="tdLabel">
            <label class="form-field-label" for="_lsgl">历史工龄：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="_lsgl" name="_lsgl" ui-type="text" maxlength="50" style="width: 140px;"
                data-bind="value: mst._lsgl" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input" title="">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="_CardNo">卡号：</label>
        </td>
        <td class="tdInput">
            <input type="text" class="sepInput ui-widget ui-widget-content ui-input ui-field-required" id="_CardNo"
                name="_CardNo" ui-type="text" maxlength="50" style="width: 140px;" data-bind="value: mst._CardNo"
                val-options="{&quot;required&quot;:true}" title="0128428556">
        </td>

        <td class="tdLabel">
            <label class="form-field-label" for="_jsr">介绍人：</label>
        </td>
        <td class="tdInput">
            <input type="text" class="sepInput ui-widget ui-widget-content ui-input" id="_jsr" name="_jsr"
                ui-type="text" maxlength="50" style="width: 140px;" data-bind="value: mst._jsr"
                val-options="{&quot;required&quot;:false}" title="">
        </td>

    </tr>

    <tr class="baseSubBlock">
        <td colspan="6" class="tdTitle">联系信息</td>
    </tr>
    <tr class="baseSubBlock">
        <td class="tdLabel">
            <label class="form-field-label" for="phone">联系电话：</label>
        </td>
        <td class="tdInput">
            <input type="text" class="sepInput ui-widget ui-widget-content ui-input ui-field-required" id="phone"
                name="phone" ui-type="text" placeholder="请入输手机号码" maxlength="100" style="width: 158px;"
                data-bind="value: mst.phone" val-options="{&quot;required&quot;:true}" title="13826469561">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="WorkPhoneNumber">工作号码：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="WorkPhoneNumber" name="WorkPhoneNumber" placeholder="请输手机、电话或分机号码等" ui-type="text"
                maxlength="100" style="width: 158px;" data-bind="value: mst.WorkPhoneNumber"
                val-options="{&quot;required&quot;:false}" class="ui-widget ui-widget-content ui-input" title="">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="email">E-Mail：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="email" name="email" ui-type="text" maxlength="100" style="width: 158px;"
                data-bind="value: mst.email" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input" title="">
        </td>

    </tr>
    <tr class="baseSubBlock">
        <td class="tdLabel">
            <label class="form-field-label" for="Address">住址：</label>
        </td>
        <td colspan="3" class="tdInput">
            <input type="text" id="Address" name="Address" ui-type="text" maxlength="400" style="width: 418px;"
                data-bind="value: mst.Address" class="ui-widget ui-widget-content ui-input" title="">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="qq">QQ/MSN：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="qq" name="qq" ui-type="text" maxlength="100" style="width: 158px;"
                data-bind="value: mst.qq" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input" title="">
        </td>
    </tr>
    <tr class="baseSubBlock">
        <td class="tdLabel">
            <label class="form-field-label" for="EmergencyContact">紧急联系人：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="EmergencyContact" name="EmergencyContact" ui-type="text" maxlength="100"
                style="width: 158px;" data-bind="value: mst.EmergencyContact" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input" title="">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="ContactRelationship">联系人关系：</label>
        </td>
        <td class="tdInput">
            <select id="ContactRelationship" name="ContactRelationship" ui-type="dropdownlist"
                val-options="{&quot;required&quot;:false}" style="width: 158px;"
                data-bind="value: mst.ContactRelationship"
                ui-options="{&quot;url&quot;:&quot;/Common/GetDropDownListItems&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;DataSource&quot;:&quot;ContactRelationship&quot;}}"
                class="ui-widget ui-widget-content ui-dropdownlist">
                <option value=""></option>
                <option value="0">父亲</option>
                <option value="1">母亲</option>
                <option value="2">夫妻</option>
                <option value="3">儿子</option>
                <option value="4">女儿</option>
                <option value="5">兄妹</option>
                <option value="6">其他</option>
            </select>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="EmergencyCall" style="width:85px;">紧急联系电话：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="EmergencyCall"
                class="sepInput ui-widget ui-widget-content ui-input ui-field-required" name="EmergencyCall"
                ui-type="text" maxlength="100" style="width: 158px;" data-bind="value: mst.EmergencyCall"
                val-options="{&quot;required&quot;:true}" title="13672505875">
        </td>
    </tr>
    <tr class="baseSubBlock">
        <td colspan="6" class="tdTitle">身份证信息</td>
    </tr>
    <tr class="baseSubBlock">
        <td class="tdLabel">
            <label class="form-field-label" for="IssuingBody">发证机关：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="IssuingBody" name="IssuingBody" ui-type="text" maxlength="400" style="width: 158px;"
                data-bind="value: mst.IssuingBody" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input" title="新兴县公安局">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="IssuingDate">生效日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="IssuingDate"
                    name="IssuingDate" ui-type="date" maxlength="10" style="width: 140px;" data-format="d:Y-M-d"
                    data-bind="value: mst.IssuingDate" class="ui-datepicker-input hasDatepicker"><button type="button"
                    name="btn_date_IssuingDate" class="ui-widget ui-state-default"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="IssuingDate">失效日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="DueDate"
                    name="DueDate" ui-type="date" maxlength="10" style="width: 140px;" data-format="d:Y-M-d"
                    data-bind="value: mst.DueDate" class="ui-datepicker-input hasDatepicker"><button type="button"
                    name="btn_date_DueDate" class="ui-widget ui-state-default"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>

    </tr>
    <tr class="baseSubBlock">
        <td class="tdLabel">
            <label class="form-field-label" for="Birthday">出生日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="Birthday"
                    name="Birthday" ui-type="date" maxlength="10" style="width: 140px;" data-format="d:Y-M-d"
                    data-bind="value: mst.Birthday" val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker"><button type="button" name="btn_date_Birthday"
                    class="ui-widget ui-state-default"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="HomeAddress">户籍地址：</label>
        </td>
        <td colspan="3" class="tdInput">
            <input type="text" id="HomeAddress" name="HomeAddress" ui-type="text" maxlength="400" style="width: 475px;"
                data-bind="value: mst.HomeAddress" class="ui-widget ui-widget-content ui-input"
                title="广东省云浮市新兴县新城镇城南居委竹围洞17幢301号">
        </td>
    </tr>

    <tr class="baseSubBlock">
        <td colspan="6" class="tdTitle">其它信息</td>
    </tr>
    <tr class="baseSubBlock">
    </tr>
    <tr class="baseSubBlock">

        <td class="tdLabel">
            <label class="form-field-label" for="_tobb">是否验厂人员：</label>
        </td>
        <td class="tdInput">
            <select id="_tobb" name="_tobb"
                class="sepInput ui-widget ui-widget-content ui-dropdownlist ui-field-required" ui-type="dropdownlist"
                style="width: 140px;" data-bind="value: mst._tobb" val-options="{&quot;required&quot;:true}"
                ui-options="{&quot;url&quot;:&quot;/Common/GetDropDownListItems&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;DataSource&quot;:&quot;tob&quot;}}">
                <option value=""></option>
                <option value="1">否</option>
                <option value="2">是</option>
            </select>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="OldHireDate" style="width: 72px!important;">登记号：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="FpCode" name="FpCode" ui-type="text" maxlength="100" style="width: 158px;"
                placeholder="请输入指纹或人脸号" data-bind="value: mst.FpCode" val-options="{&quot;required&quot;:false}"
                class="ui-widget ui-widget-content ui-input" readonly="readonly" title="11669">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="FreeSign">非考勤人员：</label>
        </td>
        <td class="tdInput">
            <input type="checkbox" id="FreeSign" name="FreeSign" ui-type="checkbox" ui-value="1|0"
                data-bind="checkbox:mst.FreeSign" value="0">
        </td>
    </tr>
    <tr class="baseSubBlock">
        <td class="tdLabel">
            <label class="form-field-label" for="OldCode">原工号：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="OldCode" name="OldCode" ui-type="text" maxlength="400" style="width: 158px;"
                data-bind="value:mst.OldCode" readonly="readonly"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="OldHireDate" style="width: 72px!important;">原入职日期：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="OldHireDate"
                    name="OldHireDate" style="width: 140px;" ui-type="date" data-format="d:Y-M-d"
                    data-bind="value:mst.OldHireDate" readonly="readonly"
                    class="ui-datepicker-input hasDatepicker ui-field-readonly" disabled="disabled"><button
                    type="button" name="btn_date_OldHireDate" class="ui-widget ui-state-default" disabled="disabled"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="Remark">备注：</label>
        </td>
        <td class="tdInput">
            <input type="text" id="Remark" name="Remark" ui-type="text" maxlength="400" style="width: 158px;"
                data-bind="value:mst.Remark" class="ui-widget ui-widget-content ui-input" title="">
        </td>
    </tr>

    <tr>
        <td class="tdLabel">
            <label class="form-field-label" for="_AtnDeptname">验厂部门：</label>
        </td>
        <td class="tdInput">

            <input type="hidden" id="_AtnDeptID" name="_AtnDeptID" data-bind="value: mst._AtnDeptID" value="">
            <span class="ui-widget ui-widget-content ui-buttonEdit-wrapper"><input type="text" id="_AtnDeptCode"
                    name="_AtnDeptCode" ui-type="buttonEdit" maxlength="10" style="width:58px;"
                    data-bind="value: mst._AtnDeptCode" val-options="{&quot;required&quot;:false}"
                    ui-options="{&quot;windowOptions&quot;:{&quot;title&quot;:&quot;查找数据&quot;,&quot;height&quot;:&quot;395&quot;,&quot;width&quot;:&quot;550&quot;,&quot;modal&quot;:true,&quot;ajaxOptions&quot;:{&quot;url&quot;:&quot;/OpenWindow/Index&quot;,&quot;type&quot;:&quot;POST&quot;,&quot;data&quot;:{&quot;AppCode&quot;:&quot;PSN01&quot;,&quot;InterCode&quot;:&quot;Mst&quot;,&quot;FieldCode&quot;:&quot;_AtnDeptCode&quot;,&quot;OpenType&quot;:&quot;1&quot;,&quot;PageSize&quot;:&quot;1000&quot;}}}}"
                    class="ui-buttonEdit-input"><button type="button"
                    class="ui-button ui-widget ui-state-default ui-button-text-only" role="button"
                    aria-disabled="false"><span class="ui-button-text">...</span></button></span>
            <input type="text" id="_AtnDeptname" name="_AtnDeptname" ui-type="text" maxlength="10" readonly="readonly"
                style="width: 80px; margin-left: -3px;" data-bind="value: mst._AtnDeptname"
                class="ui-widget ui-widget-content ui-input ui-field-readonly" title="">

        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="_AtBHireDate">验厂开始：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="_AtBHireDate"
                    name="_AtBHireDate" ui-type="date" maxlength="10" style="width: 140px;" data-format="d:Y-M-d"
                    data-bind="value: mst._AtBHireDate" val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker"><button type="button" name="btn_date__AtBHireDate"
                    class="ui-widget ui-state-default"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="_AtBDimDate">验厂结束：</label>
        </td>
        <td class="tdInput">
            <span class="ui-widget ui-widget-content ui-datepicker-wrapper"><input type="text" id="_AtBDimDate"
                    name="_AtBDimDate" ui-type="date" maxlength="10" style="width: 140px;" data-format="d:Y-M-d"
                    data-bind="value: mst._AtBDimDate" val-options="{&quot;required&quot;:false}"
                    class="ui-datepicker-input hasDatepicker"><button type="button" name="btn_date__AtBDimDate"
                    class="ui-widget ui-state-default"
                    style="display: inline-block; border-top: none; border-right: none; border-bottom: none; cursor: pointer; height: 21px; padding: 0px; margin: 0px;"><span
                        class="ui-icon ui-icon-calendar"
                        style="display: inline-block; position: relative; top: 2px;"></span></button></span>
        </td>
    </tr>

    <tr class="baseSubBlock">
        <td class="tdLabel">
            <label class="form-field-label" for="">厂服数量:</label>
        </td>
        <td class="tdInput">
            <input data-bind="value:mst._cfsl" id="_cfsl" name="_cfsl" style="width:158px;" type="text" ui-type="text"
                value="" class="ui-widget ui-widget-content ui-input" title="">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="">入职体检:</label>
        </td>
        <td class="tdInput">
            <input data-bind="value:mst._rztj" id="_rztj" name="_rztj" style="width:158px;" type="text" ui-type="text"
                value="" class="ui-widget ui-widget-content ui-input" title="常规体检报告">
        </td>
        <td class="tdLabel">
            <label class="form-field-label" for="">在职体检:</label>
        </td>
        <td class="tdInput">
            <input data-bind="value:mst._zztj" id="_zztj" name="_zztj" style="width:158px;" type="text" ui-type="text"
                value="" class="ui-widget ui-widget-content ui-input" title="">
        </td>
    </tr>
</tbody>
'''


soup = BeautifulSoup(html_doc, 'lxml')
#print(soup.prettify())#整个DOM 加上prettify 格式化
#ls = soup.find_all(['textarea', 'input'],attrs={"name":re.compile(r'DATA')})
# form1=soup.find(['label'],attrs={"name":"form1"})
ds=soup.find_all(['label'])

# token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(appid,sceret) # 创建获取token的url



listobj=[]

# 如果您的文本中有多个占位符 %s，则可以在格式化字符串时传递多个参数。例如：

# text = "{The %s set contains {%s} elements}" % ("empty", "x")
n1=806738
n2=801303
n5=5
for item in ds:
	n1=n1+1
	n2=n2+1
	n3=str(n1)
	n4=str(n2)

	n5=n5+1
	n6=str(n5)
	obj='''{
        "$id": "%s",
        "ID": %s,
        "Name": "%s",
        "FieldName": "%s",
        "DataType": 2,
        "FieldLength": 50,
        "AllowDuplicate": true,
        "AllowNull": true,
        "FieldOrder": 3,
        "EntityID": %s,
        "IsContainer": false,
        "IsKeyCol": false,
        "ThirdPK": false,
        "AutoFillSearchCol": false,
        "Entity": {
          "$ref": "1"
        }
      },'''%(n6,n3,item['for'],item.text,n4)
	# print(obj)
	print(item.text,'  ',item['for'],)
