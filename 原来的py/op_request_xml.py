import requests
xml='''
<request type="sync" key="a688c42975ab8d72661008adfd303bca">
  <host prod="testhrm" ver="1.0" ip="192.168.4.253" id="testhrm" lang="zh_CN" timezone="+8" timestamp="20211115112201263"></host>
  <service prod="HR" name="GetEmp" srvver="1.0" ip="192.168.0.7" ></service>
  <datakey type="FOM">
    <key name="EntId">100</key>
    <key name="CompanyId">W</key>
  </datakey>
  <payload>
    <param key="std_data" type="XML">
      <data_request>
        <datainfo>
          <parameter key="wo_item_state_data" type="data">
            <data name="wo_item_state">
              <row seq="1">
                <field name="doc_no" type="string">WMT03-21111500001</field>
                <field name="create_date" type="date">20211115</field>
                <field name="status" type="string">3</field>
                <field name="remark" type="string"></field>
                <field name="applicant_no" type="string">61035W</field>
                <detail name="wo_item_detail">
                  <row>
                    <field name="seq" type="numeric">1</field>
                    <field name="wo_no" type="string">WLS41-21081300085</field>
                    <field name="item_no" type="string">100420000930</field>
                    <field name="qpa_molecular" type="string"></field>
                    <field name="qpa_denominator" type="string"></field>
                    <field name="std_qty" type="numeric">1</field>
                    <field name="qty" type="numeric">270</field>
                    <field name="unit_no" type="string">PCS</field>
                    <field name="item_type" type="string">1</field>
                    <field name="input_datetime" type="date">20211115</field>
                    <field name="warehouse_no" type="string">LS75</field>
                    <field name="location_no" type="string">A0001</field>
                    <field name="lot_no" type="string"></field>
                    <field name="item_feature_no" type="string"></field>
                    <field name="remark" type="string"></field>
                    <field name="positive_negative" type="numeric">1</field>
                    <field name="replaced_item_no" type="string">100420000916</field>
                    <field name="replaced_qty" type="numeric">1</field>
                    <field name="replaced_type" type="string">1</field>
                    <field name="issue_to_type" type="string">3</field>
                    <field name="op_no" type="string">LZ002</field>
                  </row>
                  <row>
                    <field name="seq" type="numeric">2</field>
                    <field name="wo_no" type="string">WLS41-21081300085</field>
                    <field name="item_no" type="string">401000000347</field>
                    <field name="qpa_molecular" type="string"></field>
                    <field name="qpa_denominator" type="string"></field>
                    <field name="std_qty" type="numeric">2</field>
                    <field name="qty" type="numeric">1000</field>
                    <field name="unit_no" type="string">PCS</field>
                    <field name="item_type" type="string">0</field>
                    <field name="input_datetime" type="date">20211115</field>
                    <field name="warehouse_no" type="string">LS75</field>
                    <field name="location_no" type="string">A0001</field>
                    <field name="lot_no" type="string"></field>
                    <field name="item_feature_no" type="string"></field>
                    <field name="remark" type="string"></field>
                    <field name="positive_negative" type="numeric">1</field>
                    <field name="replaced_item_no" type="string">401000000347</field>
                    <field name="replaced_qty" type="numeric">2</field>
                    <field name="replaced_type" type="string">0</field>
                    <field name="issue_to_type" type="string">3</field>
                    <field name="op_no" type="string">LZ002</field>
                  </row>
                  <row>
                    <field name="seq" type="numeric">3</field>
                    <field name="wo_no" type="string">WLS41-21081300085</field>
                    <field name="item_no" type="string">109910000313</field>
                    <field name="qpa_molecular" type="string"></field>
                    <field name="qpa_denominator" type="string"></field>
                    <field name="std_qty" type="numeric">2</field>
                    <field name="qty" type="numeric">1000</field>
                    <field name="unit_no" type="string">PCS</field>
                    <field name="item_type" type="string">1</field>
                    <field name="input_datetime" type="date">20211115</field>
                    <field name="warehouse_no" type="string">LS75</field>
                    <field name="location_no" type="string">A0001</field>
                    <field name="lot_no" type="string"></field>
                    <field name="item_feature_no" type="string"></field>
                    <field name="remark" type="string"></field>
                    <field name="positive_negative" type="numeric">1</field>
                    <field name="replaced_item_no" type="string">109910000313</field>
                    <field name="replaced_qty" type="numeric">2</field>
                    <field name="replaced_type" type="string">1</field>
                    <field name="issue_to_type" type="string">3</field>
                    <field name="op_no" type="string">LZ002</field>
                  </row>
                </detail>
              </row>
            </data>
          </parameter>
        </datainfo>
      </data_request>
    </param>
  </payload>
</request>

'''
url='http://192.168.0.51:9999/IntegrationEntry?wsdl'
r=requests.post(url,data=xml.encode('utf-8'))
print(r.text)