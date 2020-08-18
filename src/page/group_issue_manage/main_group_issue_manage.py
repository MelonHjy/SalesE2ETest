#  -*- coding:utf-8 -*-
# @Time : 2020/8/14 1:54
# @Author: fyl

import allure
import requests

from config.global_var import sleep, g
from src.page.table_page import TablePage
import xml.etree.ElementTree as Etree

from src.utils.common_util import BusinessType
from src.utils.log import info


class MainGroupIssueManage(TablePage):
    input_btn = "//input[@value='{}']"  # 按钮
    group_name = "//*[@id='groupName']"  # 团队名称
    status = "//input[@id='state1{}']"  # 任务状态
    pk_deptdoc = "//*[@id='pk_deptdoc']"  # 团队代码

    xml = '''<?xml version="1.0" encoding="GBK"?>
        <requestXml>
            <requesthead>
                <uuid>f55b5c5f-bda4-4b63-b5a4-415d2aa7b47e</uuid>
                <flowintime>2020-08-14 14:47:00</flowintime>
                <user>0306</user>
                <request_type>05220020</request_type>
                <password>9b5ef3d5-64d0-4dad-a754-bc4930db3913</password>
                <server_version>00000000</server_version>
                <sender>0306</sender>
            </requesthead>
            <requestbody>
                <hrGroupInFo>
                    <msgId>%s</msgId>
                    <businessType>{0}</businessType>
                    <groupCode>%s</groupCode>
                    <pkDeptdoc>%s</pkDeptdoc>
                    <groupName>%s</groupName>
                    <groupType>%s</groupType>
                    <comCode>%s</comCode>
                    <licenseFlag>N</licenseFlag>
                    <optTime>2020-07-27 17:13:38</optTime>
                    <optUser>%s</optUser>
                    <state>2</state>
                    <reaSon>批准！</reaSon>
                    <auditTime>2020-08-14 14:47:00</auditTime>
                    <auditUser>销管系统测试账号</auditUser>
                </hrGroupInFo>
            </requestbody>
        </requestXml>'''

    def into_page(self):
        self.to_main_page("经营机构", "销售团队", "团队出单权管理")

    @allure.step("点击{btn_text}")
    def click_btn(self, btn_text):
        self.click(self.wait_until_el_xpath(self.input_btn.format(btn_text)))
        sleep(2)

    @allure.step("根据团队->查询")
    def query(self, group_name=None, pk_deptdoc=None, status="100"):
        """
        group_name:团队名称
        status：任务提交：0->未选定）,1->被选定，未提交，已提交，被打回
        """
        if group_name:
            self.click(self.wait_until_el_xpath(self.group_name))
            self.send_keys(self.wait_until_el_xpath(self.group_name), group_name)
        if pk_deptdoc:
            self.click(self.wait_until_el_xpath(self.pk_deptdoc))
            self.send_keys(self.wait_until_el_xpath(self.pk_deptdoc), pk_deptdoc)
        j = 0
        for i in status:
            el = self.wait_until_el_xpath(self.status.format(j))
            if (el.is_selected() == False and i == "1") or (el.is_selected() and i == "0"):
                self.click(el)
            j = j + 1
        self.click(self.wait_until_el_xpath(self.input_btn.format("查询")))
        sleep(3)

    def select_data(self, column_name, column_value, row_ope):
        """
        根据指定列中指定的值获取该行数据，并对该行数据进行操作
        column_name：列名
        column_value：该列所指定的值
        row_ope：对该行进行点击的列名
        """
        status_list = self.get_cell_text_by_head(column_name)
        index = status_list.index(column_value)
        self.click(self.get_a_by_head(index, row_ope))

    def switch_max_window(self):
        self.switch_to_window()
        self.maximize_window()

    def hr_send_create(self, group_name, pk_deptdoc, group_code):
        '''
        pk_deptdoc:8位数字  32999999
        group_code：CHAR(20) 1130B810000000UITEST
        '''
        sql = "select msgid,'%s','%s',groupName,groupType,comCode,optUser from saugroupbackmsg where groupid in " \
              "(select groupid from saugroup where groupname='%s' and businessType='%s' and state='1');" % (
                  pk_deptdoc, group_code, group_name, BusinessType.create.value)
        self.__hr_send_msg(sql, group_name, self.xml.format(BusinessType.create.value))

    def hr_send_change(self, group_name):
        sql = "select msgid,pk_deptdoc,groupCode,groupName,groupType,comCode,optUser from saugroupbackmsg where groupid in " \
              "(select groupid from saugroup where groupname='%s' and businessType='%s' and state='1');" % (
                  group_name, BusinessType.change.value)
        self.__hr_send_msg(sql, group_name, self.xml.format(BusinessType.change.value))

    def hr_send_logout(self, group_name):
        sql = "select msgid,pk_deptdoc,groupCode,groupName,groupType,comCode,optUser from saugroupbackmsg where groupid in " \
              "(select groupid from saugroup where groupname='%s' and businessType='%s' and state='1');" % (
                  group_name, BusinessType.logout.value)
        self.__hr_send_msg(sql, group_name, self.xml.format(BusinessType.logout.value))

    def __hr_send_msg(self, sql, group_name, xml):
        '''
        group_name:团队名称
        business_type：业务类型
        '''
        sql_data = g.db.select(sql)
        if len(sql_data) < 1:
            info("团队反馈表没有此团队：%s" % group_name)
            return
        url = g.config['DEFAULT']['url'].replace('main.jsp', 'HRMsgService')
        data = xml % sql_data[0].encode('GBK')
        res = requests.post(url=url, data=data)
        print(res.text)
        response_head = Etree.fromstring(res.text).find('responseHead')
        response_code = response_head.find('response_code').text
        if response_code == '1':
            info("模拟hr推送信息成功")
        else:
            info("模拟hr推送信息失败，错误信息：%s" % response_head.find('error_message').text)
